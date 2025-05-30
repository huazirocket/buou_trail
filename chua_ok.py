# -*- coding: utf-8 -*-
import time
import logging
import requests
import json
import okx.Trade as TradeAPI
import okx.Account as AccountAPI
import okx.PublicData as PublicDataAPI
from logging.handlers import TimedRotatingFileHandler

class MultiAssetTradingBot:
    def __init__(self, config, feishu_webhook=None, monitor_interval=4):
        self.leverage = float(config["leverage"])
        self.stop_loss_pct = config["stop_loss_pct"]
        self.low_trail_stop_loss_pct = config["low_trail_stop_loss_pct"]
        self.trail_stop_loss_pct = config["trail_stop_loss_pct"]
        self.higher_trail_stop_loss_pct = config["higher_trail_stop_loss_pct"]
        self.low_trail_profit_threshold = config["low_trail_profit_threshold"]
        self.first_trail_profit_threshold = config["first_trail_profit_threshold"]
        self.second_trail_profit_threshold = config["second_trail_profit_threshold"]
        self.feishu_webhook = feishu_webhook
        self.blacklist = set(config.get("blacklist", []))
        self.monitor_interval = monitor_interval  # 从配置文件读取的监控循环时间


        # 配置 OKX 官方 SDK
        # flag: '0' 表示实盘交易，'1' 表示模拟交易
        self.flag = '0'  # 实盘交易
        self.api_key = config["apiKey"]
        self.secret_key = config["secret"]
        self.passphrase = config["password"]
        
        # 初始化各个API模块
        self.trade_api = TradeAPI.TradeAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.account_api = AccountAPI.AccountAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.public_api = PublicDataAPI.PublicAPI(flag=self.flag)
        # 配置日志
        log_file = "log/okx.log"
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # 使用 TimedRotatingFileHandler 以天为单位进行日志分割
        file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7, encoding='utf-8')
        file_handler.suffix = "%Y-%m-%d"  # 设置日志文件名的后缀格式，例如 multi_asset_bot.log.2024-11-05
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        self.logger = logger

        # 用于记录每个持仓的最高盈利值和当前档位
        self.highest_profits = {}
        self.current_tiers = {}
        self.detected_positions = {}
        # 获取持仓模式
        self.position_mode = self.get_position_mode()

    def convert_inst_id_to_symbol(self, inst_id):
        """将OKX的instId转换为ccxt格式的symbol"""
        try:
            # 例如: BTC-USDT-SWAP -> BTC/USDT:USDT
            if '-SWAP' in inst_id:
                base_quote = inst_id.replace('-SWAP', '')
                parts = base_quote.split('-')
                if len(parts) == 2:
                    return f"{parts[0]}/{parts[1]}:{parts[1]}"
            # 例如: BTC-USDT -> BTC/USDT
            elif '-' in inst_id and 'SWAP' not in inst_id:
                parts = inst_id.split('-')
                if len(parts) == 2:
                    return f"{parts[0]}/{parts[1]}"
            return inst_id  # 如果无法转换，返回原值
        except Exception as e:
            self.logger.error(f"转换instId失败: {e}")
            return inst_id

    def convert_symbol_to_inst_id(self, symbol):
        """将ccxt格式的symbol转换为OKX的instId"""
        try:
            # 例如: BTC/USDT:USDT -> BTC-USDT-SWAP
            if ':' in symbol:
                base_part = symbol.split(':')[0]
                return base_part.replace('/', '-') + '-SWAP'
            # 例如: BTC/USDT -> BTC-USDT
            else:
                return symbol.replace('/', '-')
        except Exception as e:
            self.logger.error(f"转换symbol失败: {e}")
            return symbol

    def get_position_mode(self):
        try:
            # 使用OKX官方SDK获取账户配置
            response = self.account_api.get_account_config()
            if response['code'] == '0' and response.get('data'):
                data = response['data']
                if data and isinstance(data, list):
                    # 取列表的第一个元素（假设它是一个字典），然后获取 'posMode'
                    position_mode = data[0].get('posMode', 'single')  # 默认值为单向
                    self.logger.info(f"当前持仓模式: {position_mode}")
                    return position_mode
                else:
                    self.logger.error("无法检测持仓模式: 'data' 字段为空或格式不正确")
                    return 'single'  # 返回默认值
            else:
                self.logger.error(f"获取账户配置失败: {response}")
                return 'single'
        except Exception as e:
            self.logger.error(f"无法检测持仓模式: {e}")
            return 'single'

    def send_feishu_notification(self, message):
        if self.feishu_webhook:
            try:
                headers = {'Content-Type': 'application/json'}
                payload = {"msg_type": "text", "content": {"text": message}}
                response = requests.post(self.feishu_webhook, json=payload, headers=headers)
                if response.status_code == 200:
                    self.logger.info("飞书通知发送成功")
                else:
                    self.logger.error("飞书通知发送失败，状态码: %s", response.status_code)
            except Exception as e:
                self.logger.error("发送飞书通知时出现异常: %s", str(e))

    def schedule_task(self):
        self.logger.info("启动主循环，开始执行任务调度...")
        try:
            while True:
                self.monitor_positions()
                time.sleep(self.monitor_interval)
        except KeyboardInterrupt:
            self.logger.info("程序收到中断信号，开始退出...")
        except Exception as e:
            error_message = f"程序异常退出: {str(e)}"
            self.logger.error(error_message)
            self.send_feishu_notification(error_message)

    def fetch_positions(self):
        try:
            # 使用OKX官方SDK获取持仓信息
            response = self.account_api.get_positions()
            if response['code'] == '0':
                positions_data = response.get('data', [])
                # 转换为与原来ccxt格式兼容的数据结构
                positions = []
                for pos in positions_data:
                    if float(pos.get('pos', 0)) != 0:  # 只返回有持仓的数据
                        position = {
                            'symbol': self.convert_inst_id_to_symbol(pos['instId']),
                            'contracts': pos['pos'],  # 持仓数量
                            'entryPrice': pos['avgPx'],  # 开仓均价
                            'markPrice': pos['markPx'],  # 标记价格
                            'side': pos['posSide'],  # 持仓方向
                            'marginMode': pos['mgnMode'],  # 保证金模式
                            'instId': pos['instId'],  # 保留原始instId
                            'lever': pos['lever']
                        }
                        positions.append(position)
                return positions
            else:
                self.logger.error(f"获取持仓失败: {response}")
                return []
        except Exception as e:
            self.logger.error(f"Error fetching positions: {e}")
            return []

    def close_position(self, symbol, amount, side, td_mode):
        try:
            # 转换symbol为instId
            inst_id = self.convert_symbol_to_inst_id(symbol)

            # 根据 position_mode 选择平仓方向
            if self.position_mode == 'long_short_mode':
                # 在双向持仓模式下，确保指定平仓方向  posSide 指定方向
                # 注意：side参数是从fetch_positions中获取的，已经正确表示了仓位方向
                pos_side = side  # 直接使用传入的side值，它已经是'long'或'short'
            else:
                # 在 net_mode 模式下，不区分方向，系统会自动平仓
                pos_side = 'net'

            # 使用OKX官方SDK平仓
            order = self.trade_api.close_positions(instId=inst_id, mgnMode=td_mode, posSide=pos_side, autoCxl='true')

            if order['code'] == '0':
                self.logger.info(f"Closed position for {symbol} with size {amount}, side: {pos_side}")
                self.send_feishu_notification(f"Closed position for {symbol} with size {amount}, side: {side}")
                self.detected_positions.pop(symbol, None)
                self.highest_profits.pop(symbol, None)
                self.current_tiers.pop(symbol, None)
                return True
            else:
                self.logger.error(f"Failed to close position for {symbol}: {order}")
                return False
        except Exception as e:
            self.logger.error(f"Error closing position for {symbol}: {e}")
            return False

    def monitor_positions(self):
        positions = self.fetch_positions()
        current_symbols = set(position['symbol'] for position in positions if float(position['contracts']) != 0)

        closed_symbols = set(self.detected_positions.keys()) - current_symbols

        for symbol in closed_symbols:
            self.logger.info(f"手动平仓检测：{symbol} 已平仓，从监控中移除")
            self.send_feishu_notification(f"手动平仓检测：{symbol} 已平仓，从监控中移除")
            self.detected_positions.pop(symbol, None)

        for position in positions:
            symbol = position['symbol']
            # print(position)
            position_amt = float(position['contracts'])
            entry_price = float(position['entryPrice'])
            current_price = float(position['markPrice'])
            side = position['side']
            td_mode = position['marginMode']
            lever = float(position['lever'])

            if position_amt == 0:
                continue

            if symbol in self.blacklist:
                if symbol not in self.detected_positions:
                    self.send_feishu_notification(f"检测到黑名单品种：{symbol}，跳过监控")
                    self.detected_positions[symbol] = position_amt
                continue

            # 首次检测仓位
            if symbol not in self.detected_positions:
                self.detected_positions[symbol] = position_amt  # 存储仓位数量
                self.highest_profits[symbol] = 0
                self.current_tiers[symbol] = "无"
                self.logger.info(
                    f"首次检测到仓位：{symbol}, 仓位数量: {position_amt}, 开仓价格: {entry_price}, 方向: {side}")
                self.send_feishu_notification(
                    f"首次检测到仓位：{symbol}, 仓位数量: {position_amt}, 开仓价格: {entry_price}, 方向: {side}")

            # 检测是否有加仓
            elif position_amt > self.detected_positions[symbol]:
                self.highest_profits[symbol] = 0  # 重置最高盈利
                self.current_tiers[symbol] = "无"  # 重置档位
                self.detected_positions[symbol] = position_amt  # 更新持仓数量
                self.logger.info(f"{symbol} 检测到加仓，重置最高盈利和档位。")
                continue  # 跳出当前循环，进入下一个仓位检测

            # 计算盈亏（修正做多/做空方向逻辑并考虑杠杆倍数）
            if side == 'long':
                profit_pct = (current_price - entry_price) / entry_price * 100 * lever
            elif side == 'short':
                profit_pct = (entry_price - current_price) / entry_price * 100 * lever
            else:
                continue


            highest_profit = self.highest_profits.get(symbol, 0)
            if profit_pct > highest_profit:
                highest_profit = profit_pct
                self.highest_profits[symbol] = highest_profit

            current_tier = self.current_tiers.get(symbol, "无")
            if highest_profit >= self.second_trail_profit_threshold:
                current_tier = "第二档移动止盈"
            elif highest_profit >= self.first_trail_profit_threshold:
                current_tier = "第一档移动止盈"
            elif highest_profit >= self.low_trail_profit_threshold:
                current_tier = "低档保护止盈"
            else:
                current_tier = "无"

            self.current_tiers[symbol] = current_tier

            self.logger.info(
                f"监控 {symbol}，仓位: {position_amt}，方向: {side}，开仓价格: {entry_price}，当前价格: {current_price}，浮动盈亏: {profit_pct:.2f}%，最高盈亏: {highest_profit:.2f}%，当前档位: {current_tier}")

            if current_tier == "低档保护止盈":
                self.logger.info(f"回撤到{self.low_trail_stop_loss_pct:.2f}% 止盈")
                if profit_pct <= self.low_trail_stop_loss_pct:
                    self.logger.info(f"{symbol} 触发低档保护止盈，当前盈亏回撤到: {profit_pct:.2f}%，执行平仓")
                    self.close_position(symbol, abs(position_amt), side, td_mode)
                    continue

            elif current_tier == "第一档移动止盈":
                trail_stop_loss = highest_profit * (1 - self.trail_stop_loss_pct)
                self.logger.info(f"回撤到 {trail_stop_loss:.2f}% 止盈")
                if profit_pct <= trail_stop_loss:
                    self.logger.info(
                        f"{symbol} 达到利润回撤阈值，当前档位：第一档移动止盈，最高盈亏: {highest_profit:.2f}%，当前盈亏: {profit_pct:.2f}%，执行平仓")
                    self.close_position(symbol, abs(position_amt), side, td_mode)
                    continue

            elif current_tier == "第二档移动止盈":
                trail_stop_loss = highest_profit * (1 - self.higher_trail_stop_loss_pct)
                self.logger.info(f"回撤到 {trail_stop_loss:.2f}% 止盈")
                if profit_pct <= trail_stop_loss:
                    self.logger.info(
                        f"{symbol} 达到利润回撤阈值，当前档位：第二档移动止盈，最高盈亏: {highest_profit:.2f}%，当前盈亏: {profit_pct:.2f}%，执行平仓")
                    self.close_position(symbol, abs(position_amt), side, td_mode)
                    continue

            if profit_pct <= -self.stop_loss_pct:
                self.logger.info(f"{symbol} 触发止损，当前盈亏: {profit_pct:.2f}%，执行平仓")
                self.close_position(symbol, abs(position_amt), side, td_mode)


if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    # 选择交易平台，假设这里选择 OKX
    platform_config = config_data['okx']
    feishu_webhook_url = config_data['feishu_webhook']
    monitor_interval = config_data.get("monitor_interval", 4)  # 默认值为4秒

    bot = MultiAssetTradingBot(platform_config, feishu_webhook=feishu_webhook_url, monitor_interval=monitor_interval)
    bot.schedule_task()
