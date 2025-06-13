# http header
API_URL = 'https://www.okx.com'

CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'

ACEEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'Locale='

APPLICATION_JSON = 'application/json'

GET = "GET"
POST = "POST"

SERVER_TIMESTAMP_URL = '/api/v5/public/time'

# account
POSITION_RISK='/api/v5/account/account-position-risk'
ACCOUNT_INFO = '/api/v5/account/balance'
POSITION_INFO = '/api/v5/account/positions'
BILLS_DETAIL = '/api/v5/account/bills'
BILLS_ARCHIVE = '/api/v5/account/bills-archive'
ACCOUNT_CONFIG = '/api/v5/account/config'
POSITION_MODE = '/api/v5/account/set-position-mode'
SET_LEVERAGE = '/api/v5/account/set-leverage'
MAX_TRADE_SIZE = '/api/v5/account/max-size'
MAX_AVAIL_SIZE = '/api/v5/account/max-avail-size'
ADJUSTMENT_MARGIN = '/api/v5/account/position/margin-balance'
GET_LEVERAGE = '/api/v5/account/leverage-info'
MAX_LOAN = '/api/v5/account/max-loan'
FEE_RATES = '/api/v5/account/trade-fee'
INTEREST_ACCRUED = '/api/v5/account/interest-accrued'
INTEREST_RATE = '/api/v5/account/interest-rate'
SET_GREEKS = '/api/v5/account/set-greeks'
ISOLATED_MODE = '/api/v5/account/set-isolated-mode'
MAX_WITHDRAWAL = '/api/v5/account/max-withdrawal'
ACCOUNT_RISK = '/api/v5/account/risk-state'
BORROW_REPAY = '/api/v5/account/borrow-repay'
BORROW_REPAY_HISTORY = '/api/v5/account/borrow-repay-history'
INTEREST_LIMITS = '/api/v5/account/interest-limits'
SIMULATED_MARGIN = '/api/v5/account/simulated_margin'
GREEKS = '/api/v5/account/greeks'
POSITIONS_HISTORY = '/api/v5/account/positions-history'
POSITION_TIRES = '/api/v5/account/position-tiers'
ACTIVATE_OPTION = '/api/v5/account/activate-option'
QUICK_MARGIN_BRROW_REPAY = '/api/v5/account/quick-margin-borrow-repay'
QUICK_MARGIN_BORROW_REPAY_HISTORY = '/api/v5/account/quick-margin-borrow-repay-history'
VIP_INTEREST_ACCRUED = '/api/v5/account/vip-interest-accrued'
VIP_INTEREST_DEDUCTED = '/api/v5/account/vip-interest-deducted'
VIP_LOAN_ORDER_LIST = '/api/v5/account/vip-loan-order-list'
VIP_LOAN_ORDER_DETAIL = '/api/v5/account/vip-loan-order-detail'
SET_LOAN_ALLOCATION = '/api/v5/account/subaccount/set-loan-allocation'
INTEREST_LIMITS = '/api/v5/account/subaccount/interest-limits'
SET_RISKOFFSET_TYPE = '/api/v5/account/set-riskOffset-type'
SET_AUTO_LOAN = '/api/v5/account/set-auto-loan'
MMP_RESET = '/api/v5/account/mmp-reset'
SET_RISKOFFSET_AMT = '/api/v5/account/set-riskOffset-amt'
GET_FIXED_LOAN_BORROWING_LIMIT = '/api/v5/account/fixed-loan/borrowing-limit'
GET_FIXED_LOAN_BORROWING_QUOTE = '/api/v5/account/fixed-loan/borrowing-quote'
FIXED_LOAN_BORROWING_ORDER = '/api/v5/account/fixed-loan/borrowing-order'
FIXED_LOAN_AMEND_BORROWING_ORDER = '/api/v5/account/fixed-loan/amend-borrowing-order'
FIXED_LOAN_MANUAL_BORROWING = '/api/v5/account/fixed-loan/manual-reborrow'
FIXED_LOAN_REPAY_BORROWING_ORDER = '/api/v5/account/fixed-loan/repay-borrowing-order'
GET_FIXED_LOAN_BORROWING_ORDERS_LIST = '/api/v5/account/fixed-loan/borrowing-orders-list'
GET_ACCOUNT_INSTRUMENTS = '/api/v5/account/instruments'
SPOT_MANUAL_BORROW_REPAY = '/api/v5/account/spot-manual-borrow-repay'
SET_AUTO_REPAY = '/api/v5/account/set-auto-repay'
GET_SPOT_BORROW_REPAY_HISTORY = '/api/v5/account/spot-borrow-repay-history'
CONVERT_TO_MARKET_LOAN = '/api/v5/account/fixed-loan/convert-to-market-loan'
REDYCE_LIABILITIES = '/api/v5/account/fixed-loan/reduce-liabilities'
ACC_RATE_LIMIT = '/api/v5/trade/account-rate-limit'
BILLS_HISTORY_ARCHIVE = '/api/v5/account/bills-history-archive'
GET_BILLS_HISTORY_ARCHIVE = '/api/v5/account/bills-history-archive'

# funding
DEPOSIT_ADDRESS = '/api/v5/asset/deposit-address'
GET_BALANCES = '/api/v5/asset/balances'
FUNDS_TRANSFER = '/api/v5/asset/transfer'
TRANSFER_STATE = '/api/v5/asset/transfer-state'
WITHDRAWAL_COIN = '/api/v5/asset/withdrawal'
DEPOSIT_HISTORIY = '/api/v5/asset/deposit-history'
CURRENCY_INFO = '/api/v5/asset/currencies'
PURCHASE_REDEMPT = '/api/v5/finance/savings/purchase-redempt'
BILLS_INFO = '/api/v5/asset/bills'
PIGGY_BALANCE = '/api/v5/finance/savings/balance'
DEPOSIT_LIGHTNING = '/api/v5/asset/deposit-lightning'
WITHDRAWAL_LIGHTNING = '/api/v5/asset/withdrawal-lightning'
CANCEL_WITHDRAWAL = '/api/v5/asset/cancel-withdrawal'
WITHDRAWAL_HISTORIY = '/api/v5/asset/withdrawal-history'
CONVERT_DUST_ASSETS = '/api/v5/asset/convert-dust-assets'
ASSET_VALUATION = '/api/v5/asset/asset-valuation'
SET_LENDING_RATE = '/api/v5/finance/savings/set-lending-rate'
LENDING_HISTORY = '/api/v5/finance/savings/lending-history'
LENDING_RATE_HISTORY = '/api/v5/asset/lending-rate-history'
LENDING_RATE_SUMMARY = '/api/v5/asset/lending-rate-summary'
DEPOSIT_WITHDRAW_STATUS = '/api/v5/asset/deposit-withdraw-status'
EXCHANGE_LIST = '/api/v5/asset/exchange-list'
MONTHLY_STATEMENT = '/api/v5/asset/monthly-statement'
MONTHLY_STATEMENTS = '/api/v5/asset/monthly-statement'

# Market Data
TICKERS_INFO = '/api/v5/market/tickers'
TICKER_INFO = '/api/v5/market/ticker'
INDEX_TICKERS = '/api/v5/market/index-tickers'
ORDER_BOOKS = '/api/v5/market/books'
MARKET_CANDLES = '/api/v5/market/candles'
HISTORY_CANDLES = '/api/v5/market/history-candles'
INDEX_CANSLES = '/api/v5/market/index-candles'
MARKPRICE_CANDLES = '/api/v5/market/mark-price-candles'
MARKET_TRADES = '/api/v5/market/trades'
VOLUMNE = '/api/v5/market/platform-24-volume'
ORACLE = '/api/v5/market/oracle'
Components = '/api/v5/market/index-components'
EXCHANGE_RATE = '/api/v5/market/exchange-rate'
HISTORY_TRADES = '/api/v5/market/history-trades'
BLOCK_TICKERS = '/api/v5/market/block-tickers'
BLOCK_TICKER = '/api/v5/market/block-ticker'
BLOCK_TRADES = '/api/v5/market/trades'
HISTORY_INDEX_CANDLES = '/api/v5/market/history-index-candles'
HISTORY_MARK_PRICE_CANDLES = '/api/v5/market/history-mark-price-candles'
INSTRUMENT_FAMILY_TRADES = '/api/v5/market/option/instrument-family-trades'
GET_BOOKS_LITE = '/api/v5/market/books-lite'
BOOKS_FULL = '/api/v5/market/books-full'
GET_CALL_AUCTION_DETAILS = '/api/v5/market/call-auction-details'

# Public Data
INSTRUMENT_INFO = '/api/v5/public/instruments'
DELIVERY_EXERCISE = '/api/v5/public/delivery-exercise-history'
OPEN_INTEREST = '/api/v5/public/open-interest'
FUNDING_RATE = '/api/v5/public/funding-rate'
FUNDING_RATE_HISTORY = '/api/v5/public/funding-rate-history'
PRICE_LIMIT = '/api/v5/public/price-limit'
OPT_SUMMARY = '/api/v5/public/opt-summary'
ESTIMATED_PRICE = '/api/v5/public/estimated-price'
DICCOUNT_INTETEST_INFO = '/api/v5/public/discount-rate-interest-free-quota'
SYSTEM_TIME = '/api/v5/public/time'
LIQUIDATION_ORDERS = '/api/v5/public/liquidation-orders'
MARK_PRICE = '/api/v5/public/mark-price'
TIER = '/api/v5/public/position-tiers'
INTEREST_LOAN = '/api/v5/public/interest-rate-loan-quota'
UNDERLYING = '/api/v5/public/underlying'
VIP_INTEREST_RATE_LOAN_QUOTA = '/api/v5/public/vip-interest-rate-loan-quota'
INSURANCE_FUND = '/api/v5/public/insurance-fund'
CONVERT_CONTRACT_COIN = '/api/v5/public/convert-contract-coin'
INSTRUMENT_TICK_BANDS = '/api/v5/public/instrument-tick-bands'
OPTION_TRADES = '/api/v5/public/option-trades'

# TRADING DATA
SUPPORT_COIN = '/api/v5/rubik/stat/trading-data/support-coin'
TAKER_VOLUME = '/api/v5/rubik/stat/taker-volume'
MARGIN_LENDING_RATIO = '/api/v5/rubik/stat/margin/loan-ratio'
LONG_SHORT_RATIO = '/api/v5/rubik/stat/contracts/long-short-account-ratio'
CONTRACTS_INTEREST_VOLUME = '/api/v5/rubik/stat/contracts/open-interest-volume'
OPTIONS_INTEREST_VOLUME = '/api/v5/rubik/stat/option/open-interest-volume'
PUT_CALL_RATIO = '/api/v5/rubik/stat/option/open-interest-volume-ratio'
OPEN_INTEREST_VOLUME_EXPIRY = '/api/v5/rubik/stat/option/open-interest-volume-expiry'
INTEREST_VOLUME_STRIKE = '/api/v5/rubik/stat/option/open-interest-volume-strike'
TAKER_FLOW = '/api/v5/rubik/stat/option/taker-block-volume'
GET_OPEN_INTEREST_HISTORY = '/api/v5/rubik/stat/contracts/open-interest-history'
GET_TAKER_VOLUME_CONTRACT = '/api/v5/rubik/stat/taker-volume-contract'
GET_LONG_SHORT_ACCOUNT_RADIO_CONTRACT_TOP_TRADER = '/api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader'
GET_LONG_SHORT_POSTION_RADIO_CONTRACT_TOP_TRADER = '/api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader'
GET_LONG_SHORT_ACCOUNT_RADIO_CONTRACT = '/api/v5/rubik/stat/contracts/long-short-account-ratio-contract'

# TRADE
PLACR_ORDER = '/api/v5/trade/order'
BATCH_ORDERS = '/api/v5/trade/batch-orders'
CANAEL_ORDER = '/api/v5/trade/cancel-order'
CANAEL_BATCH_ORDERS = '/api/v5/trade/cancel-batch-orders'
AMEND_ORDER = '/api/v5/trade/amend-order'
AMEND_BATCH_ORDER = '/api/v5/trade/amend-batch-orders'
CLOSE_POSITION = '/api/v5/trade/close-position'
ORDER_INFO = '/api/v5/trade/order'
ORDERS_PENDING = '/api/v5/trade/orders-pending'
ORDERS_HISTORY = '/api/v5/trade/orders-history'
ORDERS_HISTORY_ARCHIVE = '/api/v5/trade/orders-history-archive'
ORDER_FILLS = '/api/v5/trade/fills'
ORDERS_FILLS_HISTORY = '/api/v5/trade/fills-history'
PLACE_ALGO_ORDER = '/api/v5/trade/order-algo'
CANCEL_ALGOS = '/api/v5/trade/cancel-algos'
AMEND_ALGOS = '/api/v5/trade/amend-algos'
Cancel_Advance_Algos = '/api/v5/trade/cancel-advance-algos'
ORDERS_ALGO_OENDING = '/api/v5/trade/orders-algo-pending'
ORDERS_ALGO_HISTORY = '/api/v5/trade/orders-algo-history'
EASY_CONVERT_CURRENCY_LIST = '/api/v5/trade/easy-convert-currency-list'
EASY_CONVERT = '/api/v5/trade/easy-convert'
EASY_CONVERT_HISTORY = '/api/v5/trade/easy-convert-history'
ONE_CLICK_REPAY_CURRENCY_LIST = '/api/v5/trade/one-click-repay-currency-list'
ONE_CLICK_REPAY = '/api/v5/trade/one-click-repay'
ONE_CLICK_REPAY_HISTORY = '/api/v5/trade/one-click-repay-history'
GET_ORDER_ALGO = '/api/v5/trade/order-algo'
MASS_CANCEL = '/api/v5/trade/mass-cancel'
CANCEL_ALL_AFTER = '/api/v5/trade/cancel-all-after'
FILLS_ARCHIVE = '/api/v5/trade/fills-archive'
FILLS_ARCHIVES = '/api/v5/trade/fills-archive'
ORDER_PRECHECK = '/api/v5/trade/order-precheck'

#Sprd
SPRD_PLACE_ORDER = '/api/v5/sprd/order'
SPRD_CANCEL_ORDER = '/api/v5/sprd/cancel-order'
SPRD_MASS_CANCELS = '/api/v5/sprd/mass-cancel'
SPRD_AMEND_CANCELS = '/api/v5/sprd/amend-order'
SPRD_ORDER = '/api/v5/sprd/order'
SPRD_ORDERS_PENDING = '/api/v5/sprd/orders-pending'
SPRD_ORDERS_HISTORY = '/api/v5/sprd/orders-history'
SPRD_ORDERS_HISTORY_ARCHIVE = '/api/v5/sprd/orders-history-archive'
SPRD_TRADES = '/api/v5/sprd/trades'
SPRD_SPREADS = '/api/v5/sprd/spreads'
SPRD_BOOKS = '/api/v5/sprd/books'
SPRD_TICKER = '/api/v5/market/sprd-ticker'
SPRD_PUBLIC_TRADES = '/api/v5/sprd/public-trades'
SPRD_CANCEL_ALL_AFTER = '/api/v5/sprd/cancel-all-after'
GET_SPRD_CANDLES = '/api/v5/market/sprd-candles'
GET_SPRD_HISTORY_CANDLES = '/api/v5/market/sprd-history-candles'


# SubAccount
BALANCE = '/api/v5/account/subaccount/balances'
BILLs = '/api/v5/asset/subaccount/bills'
DELETE = '/api/v5/users/subaccount/delete-apikey' # 移除此接口
RESET = '/api/v5/users/subaccount/modify-apikey' # 移除此接口
CREATE = '/api/v5/users/subaccount/apikey' # 移除此接口
WATCH = '/api/v5/users/subaccount/apikey'  # 移除此接口
VIEW_LIST = '/api/v5/users/subaccount/list'
SUBACCOUNT_TRANSFER = '/api/v5/asset/subaccount/transfer'
ENTRUST_SUBACCOUNT_LIST = '/api/v5/users/entrust-subaccount-list'
MODIFY_APIKEY = '/api/v5/users/subaccount/modify-apikey'
ASSET_BALANCES = '/api/v5/asset/subaccount/balances'
PARTNER_IF_REBATE = '/api/v5/users/partner/if-rebate'
MAX_WITHDRAW = '/api/v5/account/subaccount/max-withdrawal'
SUB_BILLS = '/api/v5/asset/subaccount/managed-subaccount-bills'

# Broker
BROKER_INFO = '/api/v5/broker/nd/info'
CREATE_SUBACCOUNT = '/api/v5/broker/nd/create-subaccount'
DELETE_SUBACCOUNT = '/api/v5/broker/nd/delete-subaccount'
SUBACCOUNT_INFO = '/api/v5/broker/nd/subaccount-info'
SET_SUBACCOUNT_LEVEL = '/api/v5/broker/nd/set-subaccount-level'
SET_SUBACCOUNT_FEE_REAT = '/api/v5/broker/nd/set-subaccount-fee-rate'
SUBACCOUNT_DEPOSIT_ADDRESS = '/api/v5/asset/broker/nd/subaccount-deposit-address'
SUBACCOUNT_DEPOSIT_HISTORY = '/api/v5/asset/broker/nd/subaccount-deposit-history'
REBATE_DAILY = '/api/v5/broker/nd/rebate-daily'
# BROKER_INFO = '/api/v5/broker/nd/info' Broker 获取充值地址文档无法打开，预留位置
ND_CREAET_APIKEY = '/api/v5/broker/nd/subaccount/apikey'
ND_SELECT_APIKEY = '/api/v5/broker/nd/subaccount/apikey'
ND_MODIFY_APIKEY = '/api/v5/broker/nd/subaccount/modify-apikey'
ND_DELETE_APIKEY = '/api/v5/broker/nd/subaccount/delete-apikey'
GET_REBATE_PER_ORDERS = '/api/v5/broker/nd/rebate-per-orders'
REBATE_PER_ORDERS = '/api/v5/broker/nd/rebate-per-orders'
MODIFY_SUBACCOUNT_DEPOSIT_ADDRESS = '/api/v5/asset/broker/nd/modify-subaccount-deposit-address'
ND_SUBACCOUNT_WITHDRAWAL_HISTORY = '/api/v5/asset/broker/nd/subaccount-withdrawal-history'
SET_SUBACCOUNT_ASSETS = '/api/v5/broker/nd/set-subaccount-assets'
R_SACCOUNT_IP = '/api/v5/broker/nd/report-subaccount-ip'
IF_REBATE = '/api/v5/broker/nd/if-rebate'

# Convert
GET_CURRENCIES = '/api/v5/asset/convert/currencies'
GET_CURRENCY_PAIR = '/api/v5/asset/convert/currency-pair'
ESTIMATE_QUOTE = '/api/v5/asset/convert/estimate-quote'
CONVERT_TRADE = '/api/v5/asset/convert/trade'
CONVERT_HISTORY = '/api/v5/asset/convert/history'

# FDBroker
FD_GET_REBATE_PER_ORDERS = '/api/v5/broker/fd/rebate-per-orders'
FD_REBATE_PER_ORDERS = '/api/v5/broker/fd/rebate-per-orders'
FD_IF_REBATE = '/api/v5/broker/fd/if-rebate'

# Rfq
COUNTERPARTIES = '/api/v5/rfq/counterparties'
CREATE_RFQ = '/api/v5/rfq/create-rfq'
CANCEL_RFQ = '/api/v5/rfq/cancel-rfq'
CANCEL_BATCH_RFQS = '/api/v5/rfq/cancel-batch-rfqs'
CANCEL_ALL_RSQS = '/api/v5/rfq/cancel-all-rfqs'
EXECUTE_QUOTE = '/api/v5/rfq/execute-quote'
CREATE_QUOTE = '/api/v5/rfq/create-quote'
CANCEL_QUOTE = '/api/v5/rfq/cancel-quote'
CANCEL_BATCH_QUOTES = '/api/v5/rfq/cancel-batch-quotes'
CANCEL_ALL_QUOTES = '/api/v5/rfq/cancel-all-quotes'
GET_RFQS = '/api/v5/rfq/rfqs'
GET_QUOTES = '/api/v5/rfq/quotes'
GET_RFQ_TRADES = '/api/v5/rfq/trades'
GET_PUBLIC_TRADES = '/api/v5/rfq/public-trades'
RFQ_CANCEL_ALL_AFTER = '/api/v5/rfq/cancel-all-after'
MARKET_INSTRUMENT_SETTINGS = '/api/v5/rfq/maker-instrument-settings'
MMP_RESET = '/api/v5/rfq/mmp-reset'
MMP_CONFIG = '/api/v5/rfq/mmp-config'
MMP_CONF = '/api/v5/rfq/mmp-config'
MMP_CONFIG = '/api/v5/account/mmp-config'
MMP = '/api/v5/account/mmp-config'
SET_ACCOUNT_LEVEL = '/api/v5/account/set-account-level'
GET_MAKER_INSTRUMENT_SETTINGS = '/api/v5/rfq/maker-instrument-settings'
POSITION_BUILDER = '/api/v5/account/position-builder'

# tradingBot
GRID_ORDER_ALGO = '/api/v5/tradingBot/grid/order-algo'
GRID_AMEND_ORDER_ALGO = '/api/v5/tradingBot/grid/amend-order-algo'
GRID_STOP_ORDER_ALGO = '/api/v5/tradingBot/grid/stop-order-algo'
GRID_ORDERS_ALGO_PENDING = '/api/v5/tradingBot/grid/orders-algo-pending'
GRID_ORDERS_ALGO_HISTORY = '/api/v5/tradingBot/grid/orders-algo-history'
GRID_ORDERS_ALGO_DETAILS = '/api/v5/tradingBot/grid/orders-algo-details'
GRID_SUB_ORDERS = '/api/v5/tradingBot/grid/sub-orders'
GRID_POSITIONS = '/api/v5/tradingBot/grid/positions'
GRID_WITHDRAW_INCOME = '/api/v5/tradingBot/grid/withdraw-income'
GRID_COMPUTE_MARGIN_BALANCE = '/api/v5/tradingBot/grid/compute-margin-balance'
GRID_MARGIN_BALANCE = '/api/v5/tradingBot/grid/margin-balance'
GRID_AI_PARAM = '/api/v5/tradingBot/grid/ai-param'
GRID_ADJUST_INVESTMETN = '/api/v5/tradingBot/grid/adjust-investment'
GRID_QUANTITY = '/api/v5/tradingBot/grid/grid-quantity'
SIGNAL_ORDERS_ALGO_PENDING = '/api/v5/tradingBot/signal/orders-algo-pending'
SIGNAL_CLOSE_POSITION = '/api/v5/tradingBot/signal/close-position'

# finance
STAKING_DEFI_OFFERS = '/api/v5/finance/staking-defi/offers'
STAKING_DEFI_PURCHASE = '/api/v5/finance/staking-defi/purchase'
STAKING_DEFI_REDEEM = '/api/v5/finance/staking-defi/redeem'
STAKING_DEFI_CANCEL = '/api/v5/finance/staking-defi/cancel'
STAKING_DEFI_ORDERS_ACTIVE = '/api/v5/finance/staking-defi/orders-active'
STAKING_DEFI_ORDERS_HISTORY = '/api/v5/finance/staking-defi/orders-history'
STAKING_DEFI_ETH_PURCASE = '/api/v5/finance/staking-defi/eth/purchase'
STAKING_DEFI_ETH_REDEEM = '/api/v5/finance/staking-defi/eth/redeem'
STAKING_DEFI_ETH_BALANCE ='/api/v5/finance/staking-defi/eth/balance'
STAKING_DEFI_ETH_P_R_HISTORY= '/api/v5/finance/staking-defi/eth/purchase-redeem-history'
STAKING_DEFI_ETH_APY_HISTORY = '/api/v5/finance/staking-defi/eth/apy-history'
SAVINGS_LENDING_RATE_SUM = '/api/v5/finance/savings/lending-rate-summary'
SAVINGS_LENDING_RATE_HIS = '/api/v5/finance/savings/lending-rate-history'
FIXED_LOAN_LENDING_OFFERS = '/api/v5/finance/fixed-loan/lending-offers'
FIXED_LOAN_LENDING_APY_HIS = '/api/v5/finance/fixed-loan/lending-apy-history'
FIXED_LOAN_PENDING_LENDING_VOL = '/api/v5/finance/fixed-loan/pending-lending-volume'
FIXED_LOAN_LENDING_ORDER = '/api/v5/finance/fixed-loan/lending-order'
FIXED_LOAN_AMEND_LENDING_ORDER = '/api/v5/finance/fixed-loan/amend-lending-order'
FIXED_LOAN_LENDING_ORDERS_LIST = '/api/v5/finance/fixed-loan/lending-orders-list'
FIXED_LOAN_LENDING_SUB_ORDERS = '/api/v5/finance/fixed-loan/lending-sub-orders'
STAKING_DEFI_ETH_PRODUCT_INFO = '/api/v5/finance/staking-defi/eth/product-info'




# copytrading
CURRENT_SUBPOSITIONS = '/api/v5/copytrading/current-subpositions'
SUBPOSITIONS_HISTORY = '/api/v5/copytrading/subpositions-history'
COPYTRADING_ALGO_ORDER = '/api/v5/copytrading/algo-order'
COPYTRADING_CLOSE_POS = '/api/v5/copytrading/close-subposition'
COPYTRADING_INSTRUMENTS = '/api/v5/copytrading/instruments'
COPYTRADING_SET_INSTRUMENTS = '/api/v5/copytrading/set-instruments'
PROFIT_SHARING_DETAILS = '/api/v5/copytrading/profit-sharing-details'
TOTAL_PROFIT_SHARING = '/api/v5/copytrading/total-profit-sharing'
UNREALIZED_PROFIT_SHARING_DETAILS = '/api/v5/copytrading/unrealized-profit-sharing-details'
FIRST_COPY_SETTINGS = '/api/v5/copytrading/first-copy-settings'
AMEND_COPY_SETTINGS = '/api/v5/copytrading/amend-copy-settings'
STOP_COPY_SETTINGS = 'api/v5/copytrading/stop-copy-trading'
COPY_SETTINGS = 'api/v5/copytrading/copy-trading'
BATCH_LEVERAGE_INF = '/api/v5/copytrading/batch-leverage-info'
BATCH_SET_LEVERAGE = '/api/v5/copytrading/batch-set-leverage'
CURRENT_LEAD_TRADERS = '/api/v5/copytrading/current-lead-traders'
LEAD_TRADERS_HISTORY = '/api/v5/copytrading/lead-traders-history'
PUBLIC_LEAD_TRADERS = '/api/v5/copytrading/public-lead-traders'
PUBLIC_WEEKLY_PNL = '/api/v5/copytrading/public-weekly-pnl'
PUBLIC_PNL = '/api/v5/copytrading/public-pnl'
PUBLIC_STATS = '/api/v5/copytrading/public-stats'
PUBLIC_PRE_CURR = '/api/v5/copytrading/public-preference-currency'
PUBLIC_CURR_SUBPOS = '/api/v5/copytrading/public-current-subpositions'
PUBLIC_SUBPOS_HIS = '/api/v5/copytrading/public-subpositions-history'
APP_LEA_TRAD = '/api/v5/copytrading/apply-lead-trading'
STOP_LEA_TRAD = '/api/v5/copytrading/stop-lead-trading'
AMEDN_PRO_SHAR_RATIO = '/api/v5/copytrading/amend-profit-sharing-ratio'
LEAD_TRADERS = '/api/v5/copytrading/lead-traders'
WEEKLY_PNL = '/api/v5/copytrading/weekly-pnl'
PNL = '/api/v5/copytrading/pnl'
STATS = '/api/v5/copytrading/stats'
PRE_CURR = '/api/v5/copytrading/preference-currency'
PRE_CURR_SUNPOSITION = '/api/v5/copytrading/performance-current-subpositions'
PRE_SUNPOSITION_HISTORY = '/api/v5/copytrading/performance-subpositions-history'
COPY_TRADERS = '/api/v5/copytrading/copy-traders'
PUB_COPY_TRADERS = '/api/v5/copytrading/public-copy-traders'
CONFIG = '/api/v5/copytrading/config'
TOTAL_UNREA_PRO_SHAR = '/api/v5/copytrading/total-unrealized-profit-sharing'


# recurring
RECURRING_ORDER_ALGO = '/api/v5/tradingBot/recurring/order-algo'
RECURRING_AMEND_ORDER_ALGO = '/api/v5/tradingBot/recurring/amend-order-algo'
RECURRING_STOP_ORDER_ALGO = '/api/v5/tradingBot/recurring/stop-order-algo'
RECURRING_ORDER_ALGO_PENDING = '/api/v5/tradingBot/recurring/orders-algo-pending'
RECURRING_ORDER_ALGO_HISTORY = '/api/v5/tradingBot/recurring/orders-algo-history'
RECURRING_ORDER_ALGO_DETAILS = '/api/v5/tradingBot/recurring/orders-algo-details'
RECURRING_SUB_ORDERS = '/api/v5/tradingBot/recurring/sub-orders'

# status
STATUS = '/api/v5/system/status'
GET_ANNOUNCEMENTS = '/api/v5/support/announcements'
GET_ANNOUNCEMENTS_TYPES = '/api/v5/support/announcement-types'
