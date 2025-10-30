# Binance - Spot Trading

**Pages:** 45

---

## Authentication requests

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/authentication-requests

**Contents:**
- Authentication requests
  - Log in with API key (SIGNED)​
  - Query session status​
  - Log out of the session​

Note: Only Ed25519 keys are supported for this feature.

Authenticate WebSocket connection using the provided API key.

After calling session.logon, you can omit apiKey and signature parameters for future requests that require them.

Note that only one API key can be authenticated. Calling session.logon multiple times changes the current authenticated API key.

Query the status of the WebSocket connection, inspecting which API key (if any) is used to authorize requests.

Forget the API key previously authenticated. If the connection is not authenticated, this request does nothing.

Note that the WebSocket connection stays open after session.logout request. You can continue using the connection, but now you will have to explicitly provide the apiKey and signature parameters where needed.

**Examples:**

Example 1 (javascript):
```javascript
{  "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  "method": "session.logon",  "params": {    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "signature": "1cf54395b336b0a9727ef27d5d98987962bc47aca6e13fe978612d0adee066ed",    "timestamp": 1649729878532  }}
```

Example 2 (javascript):
```javascript
{  "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",  "status": 200,  "result": {    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "authorizedSince": 1649729878532,    "connectedSince": 1649729873021,    "returnRateLimits": false,    "serverTime": 1649729878630,    "userDataStream": false // is User Data Stream subscription active?  }}
```

Example 3 (javascript):
```javascript
{  "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",  "method": "session.status"}
```

Example 4 (javascript):
```javascript
{  "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",  "status": 200,  "result": {    // if the connection is not authenticated, "apiKey" and "authorizedSince" will be shown as null    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "authorizedSince": 1649729878532,    "connectedSince": 1649729873021,    "returnRateLimits": false,    "serverTime": 1649730611671,    "userDataStream": true // is User Data Stream subscription active?  }}
```

---

## (deprecated)Start Margin User Data Stream (USER_STREAM)

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Start-Margin-User-Data-Stream

**Contents:**
- (deprecated)Start Margin User Data Stream (USER_STREAM)
- API Description​
- HTTP Request​
- Request Weight(UID)​
- Request Parameters​
- Response Example​

Start a new margin user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

POST /sapi/v1/userDataStream

The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

**Examples:**

Example 1 (javascript):
```javascript
{  "listenKey": "T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhdmjifQ2tRbuKkTHhr"}
```

---

## General API Information

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information

**Contents:**
- General API Information

---

## User Data Stream requests

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests

**Contents:**
- User Data Stream requests
  - User Data Stream subscription​
    - Subscribe to User Data Stream (USER_STREAM)​
    - Unsubscribe from User Data Stream​
    - Listing all subscriptions​
    - Subscribe to User Data Stream through signature subscription (USER_STREAM)​

Subscribe to the User Data Stream in the current WebSocket connection.

Stop listening to the User Data Stream in the current WebSocket connection.

Note that session.logout will only close the subscription created with userdataStream.subscribe but not subscriptions opened with userDataStream.subscribe.signature.

**Examples:**

Example 1 (javascript):
```javascript
{  "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  "method": "userDataStream.subscribe"}
```

Example 2 (javascript):
```javascript
{  "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  "status": 200,  "result": {    "subscriptionId": 0  }}
```

Example 3 (javascript):
```javascript
{  "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  "method": "userDataStream.unsubscribe"}
```

Example 4 (javascript):
```javascript
{  "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",  "status": 200,  "result": {}}
```

---

## General requests

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-requests

**Contents:**
- General requests
  - Test connectivity​
  - Check server time​
  - Exchange information​

Test connectivity to the WebSocket API.

Note: You can use regular WebSocket ping frames to test connectivity as well, WebSocket API will respond with pong frames as soon as possible. ping request along with time is a safe way to test request-response handling in your application.

Test connectivity to the WebSocket API and get the current server time.

Query current exchange trading rules, rate limits, and symbol information.

Only one of symbol, symbols, permissions parameters can be specified.

Without parameters, exchangeInfo displays all symbols with ["SPOT, "MARGIN", "LEVERAGED"] permissions.

permissions accepts either a list of permissions, or a single permission name. E.g. "SPOT".

Available Permissions

Examples of Symbol Permissions Interpretation from the Response:

**Examples:**

Example 1 (javascript):
```javascript
{  "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",  "method": "ping"}
```

Example 2 (javascript):
```javascript
{  "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",  "status": 200,  "result": {},  "rateLimits": [    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 1    }  ]}
```

Example 3 (javascript):
```javascript
{  "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",  "method": "time"}
```

Example 4 (javascript):
```javascript
{  "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",  "status": 200,  "result": {    "serverTime": 1656400526260  },  "rateLimits": [    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 1    }  ]}
```

---

## General API Information

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-api-information

**Contents:**
- General API Information

---

## Request security

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/request-security

**Contents:**
- Request security
  - SIGNED request security​
  - Timing security​
  - SIGNED request example (HMAC)​
  - SIGNED request example (RSA)​
  - SIGNED Request Example (Ed25519)​

Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It is recommended to use a small recvWindow of 5000 or less!

Here is a step-by-step guide on how to sign requests using HMAC secret key.

Example API key and secret key:

WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.

The example keys are provided here only for illustrative purposes.

As you can see, the signature parameter is currently missing.

Step 1. Construct the signature payload

Take all request params except for the signature, sort them by name in alphabetical order:

Format parameters as parameter=value pairs separated by &.

Resulting signature payload:

Step 2. Compute the signature

Note that apiKey, secretKey, and the payload are case-sensitive, while resulting signature value is case-insensitive.

You can cross-check your signature algorithm implementation with OpenSSL:

Step 3. Add signature to request params

Finally, complete the request by adding the signature parameter with the signature string.

Here is a step-by-step guide on how to sign requests using your RSA private key.

In this example, we assume the private key is stored in the test-prv-key.pem file.

WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.

The example keys are provided here only for illustrative purposes.

Step 1. Construct the signature payload

Take all request params except for the signature, sort them by name in alphabetical order:

Format parameters as parameter=value pairs separated by &.

Resulting signature payload:

Step 2. Compute the signature

Note that apiKey, the payload, and the resulting signature are case-sensitive.

You can cross-check your signature algorithm implementation with OpenSSL:

Step 3. Add signature to request params

Finally, complete the request by adding the signature parameter with the signature string.

Note: It is highly recommended to use Ed25519 API keys as it should provide the best performance and security out of all supported key types.

This is a sample code in Python to show how to sign the payload with an Ed25519 key.

**Examples:**

Example 1 (javascript):
```javascript
serverTime = getCurrentTime()if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {  // begin processing request  serverTime = getCurrentTime()  if (serverTime - timestamp) <= recvWindow {    // forward request to Matching Engine  } else {    // reject request  }  // finish processing request} else {  // reject request}
```

Example 2 (json):
```json
{  "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",  "method": "order.place",  "params": {    "symbol":           "BTCUSDT",    "side":             "SELL",    "type":             "LIMIT",    "timeInForce":      "GTC",    "quantity":         "0.01000000",    "price":            "52000.00",    "newOrderRespType": "ACK",    "recvWindow":       100,    "timestamp":        1645423376532,    "apiKey":           "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "signature":        "------ FILL ME ------"  }}
```

Example 3 (text):
```text
apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&newOrderRespType=ACK&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

Example 4 (console):
```console
$ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&newOrderRespType=ACK&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \  | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'cc15477742bd704c29492d96c7ead9414dfd8e0ec4a00f947bb5bb454ddbd08a
```

---

## General API Information

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api

**Contents:**
- General API Information

---

## Market Data Only URLs

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/market_data_only

**Contents:**
- Market Data Only URLs
  - RESTful API​
  - Websocket Streams​

These URLs do not require any authentication (i.e. The API key is not necessary) and serve only public market data.

On the RESTful API, these are the endpoints you can request on data-api.binance.vision:

Public market data can also be retrieved through the websocket market data using the URL data-stream.binance.vision. The streams available through this domain are the same that can be found in the Websocket Market Streams documentation.

Note that User Data Streams cannot be accessed through this URL.

**Examples:**

Example 1 (text):
```text
curl -sX GET "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"
```

Example 2 (text):
```text
wss://data-stream.binance.vision:443/ws/btcusdt@kline_1m
```

---

## (deprecated)Close Margin User Data Stream (USER_STREAM)

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Close-Margin-User-Data-Stream

**Contents:**
- (deprecated)Close Margin User Data Stream (USER_STREAM)
- API Description​
- HTTP Request​
- Request Weight(UID)​
- Request Parameters​
- Response Example​

Close out a Margin user data stream.

DELETE /sapi/v1/userDataStream

---

## Trading requests

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests

**Contents:**
- Trading requests
  - Place new order (TRADE)​
  - Test new order (TRADE)​
  - Cancel order (TRADE)​
  - Cancel and replace order (TRADE)​
  - Order Amend Keep Priority (TRADE)​
  - Cancel open orders (TRADE)​
  - Order lists​
    - Place new OCO - Deprecated (TRADE)​
    - Place new Order list - OCO (TRADE)​

This adds 1 order to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Unfilled Order Count: 1

Select response format: ACK, RESULT, FULL.

MARKET and LIMIT orders use FULL by default, other order types default to ACK.

Arbitrary numeric value identifying the order strategy.

Values smaller than 1000000 are reserved and cannot be used.

Certain parameters (*) become mandatory based on the order type:

Supported order types:

Buy or sell quantity at the specified price or better.

LIMIT order that will be rejected if it immediately matches and trades as a taker.

This order type is also known as a POST-ONLY order.

Buy or sell at the best available market price.

MARKET order with quantity parameter specifies the amount of the base asset you want to buy or sell. Actually executed quantity of the quote asset will be determined by available market liquidity.

E.g., a MARKET BUY order on BTCUSDT for "quantity": "0.1000" specifies that you want to buy 0.1 BTC at the best available price. If there is not enough BTC at the best price, keep buying at the next best price, until either your order is filled, or you run out of USDT, or market runs out of BTC.

MARKET order with quoteOrderQty parameter specifies the amount of the quote asset you want to spend (when buying) or receive (when selling). Actually executed quantity of the base asset will be determined by available market liquidity.

E.g., a MARKET BUY on BTCUSDT for "quoteOrderQty": "100.00" specifies that you want to buy as much BTC as you can for 100 USDT at the best available price. Similarly, a SELL order will sell as much available BTC as needed for you to receive 100 USDT (before commission).

Execute a MARKET order for given quantity when specified conditions are met.

I.e., when stopPrice is reached, or when trailingDelta is activated.

Place a LIMIT order with given parameters when specified conditions are met.

Like STOP_LOSS but activates when market price moves in the favorable direction.

Like STOP_LOSS_LIMIT but activates when market price moves in the favorable direction.

Notes on using parameters for Pegged Orders:

Available timeInForce options, setting how long the order should be active before expiration:

newClientOrderId specifies clientOrderId value for the order.

A new order with the same clientOrderId is accepted only when the previous one is filled or expired.

Any LIMIT or LIMIT_MAKER order can be made into an iceberg order by specifying the icebergQty.

An order with an icebergQty must have timeInForce set to GTC.

Trigger order price rules for STOP_LOSS/TAKE_PROFIT orders:

MARKET orders using quoteOrderQty follow LOT_SIZE filter rules.

The order will execute a quantity that has notional value as close as possible to requested quoteOrderQty.

Data Source: Matching Engine

Response format is selected by using the newOrderRespType parameter.

RESULT response type:

Conditional fields in Order Responses

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to Order lists.

The fields are listed below:

Test order placement.

Validates new order parameters and verifies your signature but does not send the order into the matching engine.

In addition to all parameters accepted by order.place, the following optional parameters are also accepted:

Without computeCommissionRates:

With computeCommissionRates:

Cancel an active order.

If both orderId and origClientOrderId parameters are provided, the orderId is searched first, then the origClientOrderId from that result is checked against that order. If both conditions are not met the request will be rejected.

newClientOrderId will replace clientOrderId of the canceled order, freeing it up for new orders.

If you cancel an order that is a part of an order list, the entire order list is canceled.

The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only orderId is sent. Sending origClientOrderId or both orderId + origClientOrderId will be slower.

Data Source: Matching Engine

When an individual order is canceled:

When an order list is canceled:

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Regarding cancelRestrictions

Cancel an existing order and immediately place a new order instead of the canceled one.

A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the unfilled order count by 1.

Unfilled Order Count: 1

Select response format: ACK, RESULT, FULL.

MARKET and LIMIT orders produce FULL response by default, other order types default to ACK.

Arbitrary numeric value identifying the order strategy.

Values smaller than 1000000 are reserved and cannot be used.

The allowed enums is dependent on what is configured on the symbol.

Supported values: STP Modes.

Similar to the order.place request, additional mandatory parameters (*) are determined by the new order type.

Available cancelReplaceMode options:

If both cancelOrderId and cancelOrigClientOrderId parameters are provided, the cancelOrderId is searched first, then the cancelOrigClientOrderId from that result is checked against that order. If both conditions are not met the request will be rejected.

cancelNewClientOrderId will replace clientOrderId of the canceled order, freeing it up for new orders.

newClientOrderId specifies clientOrderId value for the placed order.

A new order with the same clientOrderId is accepted only when the previous one is filled or expired.

The new order can reuse old clientOrderId of the canceled order.

This cancel-replace operation is not transactional.

If one operation succeeds but the other one fails, the successful operation is still executed.

For example, in STOP_ON_FAILURE mode, if the new order placement fails, the old order is still canceled.

Filters and order count limits are evaluated before cancellation and order placement occurs.

If new order placement is not attempted, your order count is still incremented.

Like order.cancel, if you cancel an individual order from an order list, the entire order list is canceled.

The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only orderId is sent. Sending origClientOrderId or both orderId + origClientOrderId will be slower.

Data Source: Matching Engine

If both cancel and placement succeed, you get the following response with "status": 200:

In STOP_ON_FAILURE mode, failed order cancellation prevents new order from being placed and returns the following response with "status": 400:

If cancel-replace mode allows failure and one of the operations fails, you get a response with "status": 409, and the "data" field detailing which operation succeeded, which failed, and why:

If both operations fail, response will have "status": 400:

If orderRateLimitExceededMode is DO_NOTHING regardless of cancelReplaceMode, and you have exceeded your unfilled order count, you will get status 429 with the following error:

If orderRateLimitExceededMode is CANCEL_ONLY regardless of cancelReplaceMode, and you have exceeded your unfilled order count, you will get status 409 with the following error:

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Reduce the quantity of an existing open order.

This adds 0 orders to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Read Order Amend Keep Priority FAQ to learn more.

Unfilled Order Count: 0

Data Source: Matching Engine

Response for a single order:

Response for an order which is part of an Order list:

Note: The payloads above do not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Cancel all open orders on a symbol. This includes orders that are part of an order list.

Data Source: Matching Engine

Cancellation reports for orders and order lists have the same format as in order.cancel.

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Send in a new one-cancels-the-other (OCO) pair: LIMIT_MAKER + STOP_LOSS/STOP_LOSS_LIMIT orders (called legs), where activation of one order immediately cancels the other.

This adds 1 order to EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter

Unfilled Order Count: 1

Arbitrary numeric value identifying the limit order strategy.

Values smaller than 1000000 are reserved and cannot be used.

Arbitrary numeric value identifying the stop order strategy.

Values smaller than 1000000 are reserved and cannot be used.

listClientOrderId parameter specifies listClientOrderId for the OCO pair.

A new OCO with the same listClientOrderId is accepted only when the previous one is filled or completely expired.

listClientOrderId is distinct from clientOrderId of individual orders.

limitClientOrderId and stopClientOrderId specify clientOrderId values for both legs of the OCO.

A new order with the same clientOrderId is accepted only when the previous one is filled or expired.

Price restrictions on the legs:

Both legs have the same quantity.

However, you can set different iceberg quantity for individual legs.

If stopIcebergQty is used, stopLimitTimeInForce must be GTC.

trailingDelta applies only to the STOP_LOSS/STOP_LOSS_LIMIT leg of the OCO.

Data Source: Matching Engine

Response format for orderReports is selected using the newOrderRespType parameter. The following example is for RESULT response type. See order.place for more examples.

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

Unfilled Order Count: 2

Data Source: Matching Engine

Response format for orderReports is selected using the newOrderRespType parameter. The following example is for RESULT response type. See order.place for more examples.

Unfilled Order Count: 2

Mandatory parameters based on pendingType or workingType

Depending on the pendingType or workingType, some optional parameters will become mandatory.

Data Source: Matching Engine

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Unfilled Order Count: 3

Mandatory parameters based on pendingAboveType, pendingBelowType or workingType

Depending on the pendingAboveType/pendingBelowType or workingType, some optional parameters will become mandatory.

Data Source: Matching Engine

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Cancel an active order list.

If both orderListId and listClientOrderId parameters are provided, the orderListId is searched first, then the listClientOrderId from that result is checked against that order. If both conditions are not met the request will be rejected.

Canceling an individual order with order.cancel will cancel the entire order list as well.

Data Source: Matching Engine

Places an order using smart order routing (SOR).

This adds 1 order to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Read SOR FAQ to learn more.

Unfilled Order Count: 1

Select response format: ACK, RESULT, FULL.

MARKET and LIMIT orders use FULL by default.

Arbitrary numeric value identifying the order strategy.

Values smaller than 1000000 are reserved and cannot be used.

Note: sor.order.place only supports LIMIT and MARKET orders. quoteOrderQty is not supported.

Data Source: Matching Engine

Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new order but does not send it into the matching engine.

In addition to all parameters accepted by sor.order.place, the following optional parameters are also accepted:

Without computeCommissionRates:

With computeCommissionRates:

**Examples:**

Example 1 (javascript):
```javascript
{  "id": "56374a46-3061-486b-a311-99ee972eb648",  "method": "order.place",  "params": {    "symbol": "BTCUSDT",    "side": "SELL",    "type": "LIMIT",    "timeInForce": "GTC",    "price": "23416.10000000",    "quantity": "0.00847000",    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",    "timestamp": 1660801715431  }}
```

Example 2 (javascript):
```javascript
{  "id": "56374a46-3061-486b-a311-99ee972eb648",  "status": 200,  "result": {    "symbol": "BTCUSDT",    "orderId": 12569099453,    "orderListId": -1, // always -1 for singular orders    "clientOrderId": "4d96324ff9d44481926157ec08158a40",    "transactTime": 1660801715639  },  "rateLimits": [    {      "rateLimitType": "ORDERS",      "interval": "SECOND",      "intervalNum": 10,      "limit": 50,      "count": 1    },    {      "rateLimitType": "ORDERS",      "interval": "DAY",      "intervalNum": 1,      "limit": 160000,      "count": 1    },    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 1    }  ]}
```

Example 3 (javascript):
```javascript
{  "id": "56374a46-3061-486b-a311-99ee972eb648",  "status": 200,  "result": {    "symbol": "BTCUSDT",    "orderId": 12569099453,    "orderListId": -1, // always -1 for singular orders    "clientOrderId": "4d96324ff9d44481926157ec08158a40",    "transactTime": 1660801715639,    "price": "23416.10000000",    "origQty": "0.00847000",    "executedQty": "0.00000000",    "origQuoteOrderQty": "0.000000",    "cummulativeQuoteQty": "0.00000000",    "status": "NEW",    "timeInForce": "GTC",    "type": "LIMIT",    "side": "SELL",    "workingTime": 1660801715639,    "selfTradePreventionMode": "NONE"  },  "rateLimits": [    {      "rateLimitType": "ORDERS",      "interval": "SECOND",      "intervalNum": 10,      "limit": 50,      "count": 1    },    {      "rateLimitType": "ORDERS",      "interval": "DAY",      "intervalNum": 1,      "limit": 160000,      "count": 1    },    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 1    }  ]}
```

Example 4 (javascript):
```javascript
{  "id": "56374a46-3061-486b-a311-99ee972eb648",  "status": 200,  "result": {    "symbol": "BTCUSDT",    "orderId": 12569099453,    "orderListId": -1,    "clientOrderId": "4d96324ff9d44481926157ec08158a40",    "transactTime": 1660801715793,    "price": "23416.10000000",    "origQty": "0.00847000",    "executedQty": "0.00847000",    "origQuoteOrderQty": "0.000000",    "cummulativeQuoteQty": "198.33521500",    "status": "FILLED",    "timeInForce": "GTC",    "type": "LIMIT",    "side": "SELL",    "workingTime": 1660801715793,    // FULL response is identical to RESULT response, with the same optional fields    // based on the order type and parameters. FULL response additionally includes    // the list of trades which immediately filled the order.    "fills": [      {        "price": "23416.10000000",        "qty": "0.00635000",        "commission": "0.000000",        "commissionAsset": "BNB",        "tradeId": 1650422481      },      {        "price": "23416.50000000",        "qty": "0.00212000",        "commission": "0.000000",        "commissionAsset": "BNB",        "tradeId": 1650422482      }    ]  },  "rateLimits": [    {      "rateLimitType": "ORDERS",      "interval": "SECOND",      "intervalNum": 10,      "limit": 50,      "count": 1    },    {      "rateLimitType": "ORDERS",      "interval": "DAY",      "intervalNum": 1,      "limit": 160000,      "count": 1    },    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 1    }  ]}
```

---

## Request Security

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/request-security

**Contents:**
- Request Security
  - SIGNED Endpoint security​
  - Timing security​
  - SIGNED Endpoint Examples for POST /api/v3/order​
    - HMAC Keys​
    - RSA Keys​
    - Ed25519 Keys​

Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It is recommended to use a small recvWindow of 5000 or less! The max cannot go beyond 60,000!

Here is a step-by-step example of how to send a valid signed payload from the Linux command line using echo, openssl, and curl.

Example 1: As a request body

requestBody: symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

HMAC SHA256 signature:

Example 2: As a query string

queryString: symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

HMAC SHA256 signature:

Example 3: Mixed query string and request body

queryString: symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC

requestBody: quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559

HMAC SHA256 signature:

Note that the signature is different in example 3. There is no & between "GTC" and "quantity=1".

This will be a step by step process how to create the signature payload to send a valid signed payload.

We support PKCS#8 currently.

To get your API key, you need to upload your RSA Public Key to your account and a corresponding API key will be provided for you.

For this example, the private key will be referenced as ./test-prv-key.pem

Step 1: Construct the payload

Arrange the list of parameters into a string. Separate each parameter with a &.

For the parameters above, the signature payload would look like this:

Step 2: Compute the signature:

A sample Bash script below does the similar steps said above.

Note: It is highly recommended to use Ed25519 API keys as it should provide the best performance and security out of all supported key types.

This is a sample code in Python to show how to sign the payload with an Ed25519 key.

**Examples:**

Example 1 (javascript):
```javascript
serverTime = getCurrentTime()if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {  // begin processing request  serverTime = getCurrentTime()  if (serverTime - timestamp) <= recvWindow {    // forward request to Matching Engine  } else {    // reject request  }  // finish processing request} else {  // reject request}
```

Example 2 (text):
```text
[linux]$ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"(stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71
```

Example 3 (text):
```text
(HMAC SHA256)[linux]$ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order' -d 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
```

Example 4 (text):
```text
[linux]$ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"(stdin)= c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71
```

---

## API Key Types

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/api_key_types

**Contents:**
- API Key Types
  - Ed25519​
  - HMAC​
  - RSA​

Binance APIs require an API key to access authenticated endpoints for trading, account history, etc.

We support several types of API keys:

This document provides an overview of supported API keys.

We recommend to use Ed25519 API keys as it should provide the best performance and security out of all supported key types.

Read REST API or WebSocket API documentation to learn how to use different API keys.

Ed25519 keys use asymmetric cryptography. You share your public key with Binance and use the private key to sign API requests. Binance API uses the public key to verify your signature.

Ed25519 keys provide security comparable to 3072-bit RSA keys, but with considerably smaller key, smaller signature size, and faster signature computation.

We recommend to use Ed25519 API keys.

Sample Ed25519 signature:

HMAC keys use symmetric cryptography. Binance generates and shares with you a secret key which you use to sign API requests. Binance API uses the same shared secret key to verify your signature.

HMAC signatures are quick to compute and compact. However, the shared secret must be shared between multiple parties which is less secure than asymmetric cryptography used by Ed25519 or RSA keys.

HMAC keys are deprecated. We recommend to migrate to asymmetric API keys, such as Ed25519 or RSA.

Sample HMAC signature:

RSA keys use asymmetric cryptography. You share your public key with Binance and use the private key to sign API requests. Binance API uses the public key to verify your signature.

We support 2048 and 4096 bit RSA keys.

While RSA keys are more secure than HMAC keys, RSA signatures are much larger than HMAC and Ed25519 which can lead to a degradation to performance.

Sample RSA key (2048 bits):

Sample RSA signature (2048 bits):

**Examples:**

Example 1 (text):
```text
-----BEGIN PUBLIC KEY-----MCowBQYDK2VwAyEAgmDRTtj2FA+wzJUIlAL9ly1eovjLBu7uXUFR+jFULmg=-----END PUBLIC KEY-----
```

Example 2 (text):
```text
E7luAubOlcRxL10iQszvNCff+xJjwJrfajEHj1hOncmsgaSB4NE+A/BbQhCWwit/usNJ32/LeTwDYPoA7Qz4BA==
```

Example 3 (text):
```text
Fhs4lGae2qAi6VNjbJjebUAwXrIChb7mlf372UOICMwdKaNdNBGKtfdeUff2TTTT
```

Example 4 (text):
```text
7f3fc79c57d7a70d2b644ad4589672f4a5d55a62af2a336a0af7d4896f8d48b8
```

---

## Filters

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/filters

**Contents:**
- Filters
- Symbol filters​
  - PRICE_FILTER​
  - PERCENT_PRICE​
  - PERCENT_PRICE_BY_SIDE​
  - LOT_SIZE​
  - MIN_NOTIONAL​
  - NOTIONAL​
  - ICEBERG_PARTS​
  - MARKET_LOT_SIZE​

Filters define trading rules on a symbol or an exchange. Filters come in three forms: symbol filters, exchange filters and asset filters.

The PRICE_FILTER defines the price rules for a symbol. There are 3 parts:

Any of the above variables can be set to 0, which disables that rule in the price filter. In order to pass the price filter, the following must be true for price/stopPrice of the enabled rules:

/exchangeInfo format:

The PERCENT_PRICE filter defines the valid range for the price based on the average of the previous trades. avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.

In order to pass the percent price, the following must be true for price:

/exchangeInfo format:

The PERCENT_PRICE_BY_SIDE filter defines the valid range for the price based on the average of the previous trades. avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used. There is a different range depending on whether the order is placed on the BUY side or the SELL side.

Buy orders will succeed on this filter if:

Sell orders will succeed on this filter if:

/exchangeInfo format:

The LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

In order to pass the lot size, the following must be true for quantity/icebergQty:

/exchangeInfo format:

The MIN_NOTIONAL filter defines the minimum notional value allowed for an order on a symbol. An order's notional value is the price * quantity. applyToMarket determines whether or not the MIN_NOTIONAL filter will also be applied to MARKET orders. Since MARKET orders have no price, the average price is used over the last avgPriceMins minutes. avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.

/exchangeInfo format:

The NOTIONAL filter defines the acceptable notional range allowed for an order on a symbol. applyMinToMarket determines whether the minNotional will be applied to MARKET orders. applyMaxToMarket determines whether the maxNotional will be applied to MARKET orders.

In order to pass this filter, the notional (price * quantity) has to pass the following conditions:

For MARKET orders, the average price used over the last avgPriceMins minutes will be used for calculation. If the avgPriceMins is 0, then the last price will be used.

/exchangeInfo format:

The ICEBERG_PARTS filter defines the maximum parts an iceberg order can have. The number of ICEBERG_PARTS is defined as CEIL(qty / icebergQty).

/exchangeInfo format:

The MARKET_LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for MARKET orders on a symbol. There are 3 parts:

In order to pass the market lot size, the following must be true for quantity:

/exchangeInfo format:

The MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to have open on a symbol. Note that both "algo" orders and normal orders are counted for this filter.

/exchangeInfo format:

The MAX_NUM_ALGO_ORDERS filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol. "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.

/exchangeInfo format:

The MAX_NUM_ICEBERG_ORDERS filter defines the maximum number of ICEBERG orders an account is allowed to have open on a symbol. An ICEBERG order is any order where the icebergQty is > 0.

/exchangeInfo format:

The MAX_POSITION filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

BUY orders will be rejected if the account's position is greater than the maximum position allowed.

If an order's quantity can cause the position to overflow, this will also fail the MAX_POSITION filter.

/exchangeInfo format:

The TRAILING_DELTA filter defines the minimum and maximum value for the parameter trailingDelta.

In order for a trailing stop order to pass this filter, the following must be true:

For STOP_LOSS BUY, STOP_LOSS_LIMIT_BUY,TAKE_PROFIT SELL and TAKE_PROFIT_LIMIT SELL orders:

For STOP_LOSS SELL, STOP_LOSS_LIMIT SELL, TAKE_PROFIT BUY, and TAKE_PROFIT_LIMIT BUY orders:

/exchangeInfo format:

The MAX_NUM_ORDER_AMENDS filter defines the maximum number of times an order can be amended on the given symbol.

If there are too many order amendments made on a single order, you will receive the -2038 error code.

/exchangeInfo format:

The MAX_NUM_ORDER_LISTS filter defines the maximum number of open order lists an account can have on a symbol. Note that OTOCOs count as one order list.

/exchangeInfo format:

The EXCHANGE_MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to have open on the exchange. Note that both "algo" orders and normal orders are counted for this filter.

/exchangeInfo format:

The EXCHANGE_MAX_NUM_ALGO_ORDERS filter defines the maximum number of "algo" orders an account is allowed to have open on the exchange. "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.

/exchangeInfo format:

The EXCHANGE_MAX_NUM_ICEBERG_ORDERS filter defines the maximum number of iceberg orders an account is allowed to have open on the exchange.

/exchangeInfo format:

The EXCHANGE_MAX_NUM_ORDERS filter defines the maximum number of order lists an account is allowed to have open on the exchange. Note that OTOCOs count as one order list.

/exchangeInfo format:

The MAX_ASSET filter defines the maximum quantity of an asset that an account is allowed to transact in a single order.

**Examples:**

Example 1 (javascript):
```javascript
{  "filterType": "PRICE_FILTER",  "minPrice": "0.00000100",  "maxPrice": "100000.00000000",  "tickSize": "0.00000100"}
```

Example 2 (javascript):
```javascript
{  "filterType": "PERCENT_PRICE",  "multiplierUp": "1.3000",  "multiplierDown": "0.7000",  "avgPriceMins": 5}
```

Example 3 (javascript):
```javascript
{    "filterType": "PERCENT_PRICE_BY_SIDE",    "bidMultiplierUp": "1.2",    "bidMultiplierDown": "0.2",    "askMultiplierUp": "5",    "askMultiplierDown": "0.8",    "avgPriceMins": 1  }
```

Example 4 (javascript):
```javascript
{  "filterType": "LOT_SIZE",  "minQty": "0.00100000",  "maxQty": "100000.00000000",  "stepSize": "0.00100000"}
```

---

## Rate limits

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/rate-limits

**Contents:**
- Rate limits
  - Connection limits​
  - General information on rate limits​
    - How to interpret rate limits​
    - How to show/hide rate limit information​
  - IP limits​
  - Unfilled Order Count​

There is a limit of 300 connections per attempt every 5 minutes.

The connection is per IP address.

A response with rate limit status may look like this:

The rateLimits array describes all currently active rate limits affected by the request.

Rate limits are accounted by intervals.

For example, a 1 MINUTE interval starts every minute. Request submitted at 00:01:23.456 counts towards the 00:01:00 minute's limit. Once the 00:02:00 minute starts, the count will reset to zero again.

Other intervals behave in a similar manner. For example, 1 DAY rate limit resets at 00:00 UTC every day, and 10 SECOND interval resets at 00, 10, 20... seconds of each minute.

APIs have multiple rate-limiting intervals. If you exhaust a shorter interval but the longer interval still allows requests, you will have to wait for the shorter interval to expire and reset. If you exhaust a longer interval, you will have to wait for that interval to reset, even if shorter rate limit count is zero.

rateLimits field is included with every response by default.

However, rate limit information can be quite bulky. If you are not interested in detailed rate limit status of every request, the rateLimits field can be omitted from responses to reduce their size.

Optional returnRateLimits boolean parameter in request.

Use returnRateLimits parameter to control whether to include rateLimits fields in response to individual requests.

Default request and response:

Request and response without rate limit status:

Optional returnRateLimits boolean parameter in connection URL.

If you wish to omit rateLimits from all responses by default, use returnRateLimits parameter in the query string instead:

This will make all requests made through this connection behave as if you have passed "returnRateLimits": false.

If you want to see rate limits for a particular request, you need to explicitly pass the "returnRateLimits": true parameter.

Note: Your requests are still rate limited if you hide the rateLimits field in responses.

Successful response indicating that in 1 minute you have used 70 weight out of your 6000 limit:

Failed response indicating that you are banned and the ban will last until epoch 1659146400000:

Successful response indicating that you have placed 12 orders in 10 seconds, and 4043 orders in the past 24 hours:

**Examples:**

Example 1 (json):
```json
{  "id": "7069b743-f477-4ae3-81db-db9b8df085d2",  "status": 200,  "result": {    "serverTime": 1656400526260  },  "rateLimits": [    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 70    }  ]}
```

Example 2 (json):
```json
{"id":1,"method":"time"}
```

Example 3 (json):
```json
{"id":1,"status":200,"result":{"serverTime":1656400526260},"rateLimits":[{"rateLimitType":"REQUEST_WEIGHT","interval":"MINUTE","intervalNum":1,"limit":6000,"count":70}]}
```

Example 4 (json):
```json
{"id":2,"method":"time","params":{"returnRateLimits":false}}
```

---

## (deprecated)Keepalive Isolated Margin User Data Stream (USER_STREAM)

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Keepalive-Isolated-Margin-User-Data-Stream

**Contents:**
- (deprecated)Keepalive Isolated Margin User Data Stream (USER_STREAM)
- API Description​
- HTTP Request​
- Request Weight(UID)​
- Request Parameters​
- Response Example​

Keepalive an isolated margin user data stream to prevent a time out.

PUT /sapi/v1/userDataStream/isolated

The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

---

## Simple Binary Encoding (SBE) FAQ

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/sbe_faq

**Contents:**
- Simple Binary Encoding (SBE) FAQ
  - How to get an SBE response​
    - REST API​
    - WebSocket API​
  - Supported APIs​
  - SBE Schema​
  - Regarding Legacy support​
  - Generate SBE decoders:​
    - Decimal field encoding​
    - Timestamp field encoding​

The goal of this document is to explain:

SBE is a serialization format used for low-latency.

This implementation is based on the FIX SBE specification.

Sample request (REST):

Sample request (WebSocket):

REST API and WebSocket API for SPOT support SBE.

Unlike the FIX SBE specification, decimal fields have their mantissa and exponent fields encoded separately as primitive fields in order to minimize payload size and the number of encoded fields within messages.

Timestamps in SBE responses are in microseconds. This differs from JSON responses, which contain millisecond timestamps by default.

A few field attributes prefixed with mbx: were added to the schema file for documentation purposes:

**Examples:**

Example 1 (text):
```text
curl -sX GET -H "Accept: application/sbe" -H "X-MBX-SBE: 1:0" 'https://api.binance.com/api/v3/exchangeInfo?symbol=BTCUSDT'
```

Example 2 (bash):
```bash
id=$(date +%s%3N)method="exchangeInfo"params='{"symbol":"BTCUSDT"}'request=$( jq -n \        --arg id "$id" \        --arg method "$method" \        --argjson params "$params" \        '{id: $id, method: $method, params: $params}' )response=$(echo $request | websocat -n1 'wss://ws-api.binance.com:443/ws-api/v3?responseFormat=sbe&sbeSchemaId=1&sbeSchemaVersion=0')
```

Example 3 (json):
```json
{    "environment": "PROD",    "latestSchema": {        "id": 2,        "version": 1,        "releaseDate": "3025-02-01"    },    "deprecatedSchemas": [        {            "id": 2,            "version": 0,            "releaseDate": "3024-08-01",            "deprecatedDate": "3025-02-01"        }    ],    "retiredSchemas": [        {            "id": 1,            "version": 1,            "releaseDate": "3024-03-01",            "deprecatedDate": "3024-08-01",            "retiredDate": "3025-02-01",        },        {            "id": 1,            "version": 0,            "releaseDate": "3024-01-01",            "deprecatedDate": "3024-03-01",            "retiredDate": "3024-09-01",        }    ]}
```

Example 4 (shell):
```shell
$ git clone https://github.com/real-logic/simple-binary-encoding.git $ cd simple-binary-encoding $ ./gradlew
```

---

## SBE Market Data Streams

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/sbe-market-data-streams

**Contents:**
- SBE Market Data Streams
- General Information​
- WebSocket Limits​
- Available Streams​
  - Trades Streams​
  - Best Bid/Ask Streams​
  - Diff. Depth Streams​
  - Partial Book Depth Streams​

Raw trade information, pushed in real-time.

SBE Message Name: TradesStreamEvent

Stream Name: <symbol>@trade

Update Speed: Real time

The best bid and ask price and quantity, pushed in real-time when the order book changes.

[!NOTE] Best bid/ask streams in SBE are the equivalent of bookTicker streams in JSON, except they support auto-culling, and also include the eventTime field.

SBE Message Name: BestBidAskStreamEvent

Stream Name: <symbol>@bestBidAsk

Update Speed: Real time

SBE best bid/ask streams use auto-culling: when our system is under high load, we may drop outdated events instead of queuing all events and delivering them with a delay.

For example, if a best bid/ask event is generated at time T2 when we still have an undelivered event queued at time T1 (where T1 < T2), the event for T1 is dropped, and we will deliver only the event for T2. This is done on a per-symbol basis.

Incremental updates to the order book, pushed at regular intervals. Use this stream to maintain a local order book.

How to manage a local order book.

SBE Message Name: DepthDiffStreamEvent

Stream Name: <symbol>@depth

Snapshots of the top 20 levels of the order book, pushed at regular intervals.

SBE Message Name: DepthSnapshotStreamEvent

Stream Name: <symbol>@depth20

---

## User Data Streams for Binance

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/user-data-stream

**Contents:**
- User Data Streams for Binance
- General information​
- User Data Stream Events​
  - Account Update​
  - Balance Update​
  - Order Update​
    - Conditional Fields in Execution Report​
    - Order Reject Reason​
- Event Stream Terminated​
- External Lock Update​

Last Updated: 2025-10-24

outboundAccountPosition is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.

Balance Update occurs during the following:

Orders are updated with the executionReport event.

Note: Average price can be found by doing Z divided by z.

These are fields that appear in the payload only if certain conditions are met.

For additional information on these parameters, please refer to the Spot Glossary.

For additional details, look up the Error Message in the Errors documentation.

If the order is an order list, an event named ListStatus will be sent in addition to the executionReport event.

Check the Enums page for more relevant enum definitions.

eventStreamTerminated is sent when the User Data Stream is stopped. For example, after you send a userDataStream.unsubscribe request, or a session.logout request.

externalLockUpdate is sent when part of your spot wallet balance is locked/unlocked by an external system, for example when used as margin collateral.

**Examples:**

Example 1 (javascript):
```javascript
{  "subscriptionId": 0,  "event": {    "e": "outboundAccountPosition", // Event type    "E": 1564034571105,             // Event Time    "u": 1564034571073,             // Time of last account update    "B":                            // Balances Array    [      {        "a": "ETH",                 // Asset        "f": "10000.000000",        // Free        "l": "0.000000"             // Locked      }    ]  }}
```

Example 2 (javascript):
```javascript
{  "subscriptionId": 0,  "event": {    "e": "balanceUpdate",         // Event Type    "E": 1573200697110,           // Event Time    "a": "BTC",                   // Asset    "d": "100.00000000",          // Balance Delta    "T": 1573200697068            // Clear Time  }}
```

Example 3 (javascript):
```javascript
{  "subscriptionId": 0,  "event": {    "e": "executionReport",         // Event type    "E": 1499405658658,             // Event time    "s": "ETHBTC",                  // Symbol    "c": "mUvoqJxFIILMdfAW5iGSOW",  // Client order ID    "S": "BUY",                     // Side    "o": "LIMIT",                   // Order type    "f": "GTC",                     // Time in force    "q": "1.00000000",              // Order quantity    "p": "0.10264410",              // Order price    "P": "0.00000000",              // Stop price    "F": "0.00000000",              // Iceberg quantity    "g": -1,                        // OrderListId    "C": "",                        // Original client order ID; This is the ID of the order being canceled    "x": "NEW",                     // Current execution type    "X": "NEW",                     // Current order status    "r": "NONE",                    // Order reject reason; Please see Order Reject Reason (below) for more information.    "i": 4293153,                   // Order ID    "l": "0.00000000",              // Last executed quantity    "z": "0.00000000",              // Cumulative filled quantity    "L": "0.00000000",              // Last executed price    "n": "0",                       // Commission amount    "N": null,                      // Commission asset    "T": 1499405658657,             // Transaction time    "t": -1,                        // Trade ID    "v": 3,                         // Prevented Match Id; This is only visible if the order expired due to STP    "I": 8641984,                   // Execution Id    "w": true,                      // Is the order on the book?    "m": false,                     // Is this trade the maker side?    "M": false,                     // Ignore    "O": 1499405658657,             // Order creation time    "Z": "0.00000000",              // Cumulative quote asset transacted quantity    "Y": "0.00000000",              // Last quote asset transacted quantity (i.e. lastPrice * lastQty)    "Q": "0.00000000",              // Quote Order Quantity    "W": 1499405658657,             // Working Time; This is only visible if the order has been placed on the book.    "V": "NONE"                     // SelfTradePreventionMode  }}
```

Example 4 (javascript):
```javascript
{  "subscriptionId": 0,  "event": {    "e": "listStatus",                 // Event Type    "E": 1564035303637,                // Event Time    "s": "ETHBTC",                     // Symbol    "g": 2,                            // OrderListId    "c": "OCO",                        // Contingency Type    "l": "EXEC_STARTED",               // List Status Type    "L": "EXECUTING",                  // List Order Status    "r": "NONE",                       // List Reject Reason    "C": "F4QN4G8DlFATFlIUQ0cjdD",     // List Client Order ID    "T": 1564035303625,                // Transaction Time    "O":                               // An array of objects    [      {        "s": "ETHBTC",                 // Symbol        "i": 17,                       // OrderId        "c": "AJYsMjErWJesZvqlJCTUgL"  // ClientOrderId      },      {        "s": "ETHBTC",        "i": 18,        "c": "bfYPSQdLoqAJeNrOr9adzq"      }    ]  }}
```

---

## (deprecated)Keepalive Margin User Data Stream (USER_STREAM)

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Keepalive-Margin-User-Data-Stream

**Contents:**
- (deprecated)Keepalive Margin User Data Stream (USER_STREAM)
- API Description​
- HTTP Request​
- Request Weight(UID)​
- Request Parameters​
- Response Example​

Keepalive a margin user data stream to prevent a time out.

PUT /sapi/v1/userDataStream

The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

---

## General API Information

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api

**Contents:**
- General API Information

---

## ENUM Definitions

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/enums

**Contents:**
- ENUM Definitions
- Symbol status (status)​
- Account and Symbol Permissions (permissions)​
- Order status (status)​
- Order List Status (listStatusType)​
- Order List Order Status (listOrderStatus)​
- ContingencyType​
- AllocationType​
- Order types (orderTypes, type)​
- Order Response Type (newOrderRespType)​

This will apply for both REST API and WebSocket API.

This sets how long an order will be active before expiration.

Read Self Trade Prevention (STP) FAQ to learn more.

**Examples:**

Example 1 (json):
```json
{      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000    }
```

Example 2 (json):
```json
{      "rateLimitType": "ORDERS",      "interval": "SECOND",      "intervalNum": 1,      "limit": 10    }
```

Example 3 (json):
```json
{      "rateLimitType": "RAW_REQUESTS",      "interval": "MINUTE",      "intervalNum": 5,      "limit": 61000    }
```

---

## FIX API

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/fix-api

**Contents:**
- FIX API
- General API Information​
  - FIX API Order Entry sessions​
  - FIX API Drop Copy sessions​
  - FIX API Market Data sessions​
  - FIX Connection Lifecycle​
  - API Key Permissions​
  - On message processing order​
  - Response Mode​
  - Timing Security​

[!NOTE] This API can only be used with the SPOT Exchange.

FIX sessions only support Ed25519 keys.

Please refer to this tutorial on how to set up an Ed25519 key pair.

To access the FIX API order entry sessions, your API key must be configured with the FIX_API permission.

To access the FIX Drop Copy sessions, your API key must be configured with either FIX_API_READ_ONLY or FIX_API permission.

To access the FIX Market Data sessions, your API key must be configured with either FIX_API or FIX_API_READ_ONLY permission.

FIX sessions only support Ed25519 keys.

Please refer to this tutorial on how to set up an Ed25519 key pair.

The MessageHandling (25035) field required in the initial Logon<A> message controls whether messages from the client may be reordered before they are processed by the Matching Engine.

In all modes, the client's MsgSeqNum (34) must increase monotonically, with each subsequent message having a sequence number that is exactly 1 greater than the previous message.

[!TIP] UNORDERED(1) should offer better performance when there are multiple messages in flight from the client to the server.

By default, all concurrent order entry sessions receive all of the account's successful ExecutionReport<8> and ListStatus<N> messages, including those in response to orders placed from other FIX sessions and via non-FIX APIs.

Use the ResponseMode (25036) field in the initial Logon<A> message to change this behavior.

The Logon<A> message authenticates your connection to the FIX API. This must be the first message sent by the client.

The signature payload is a text string constructed by concatenating the values of the following fields in this exact order, separated by the SOH character:

Sign the payload using your private key. Encode the signature with base64. The resulting text string is the value of the RawData (96) field.

Here is a sample Python code implementing the signature algorithm:

The values presented below can be used to validate the correctness of the signature computation implementation:

The Ed25519 private key used in the example computation is shown below:

[!CAUTION] The following secret key is provided solely for illustrative purposes. Do not use this key in any real-world application as it is not secure and may compromise your cryptographic implementation. Always generate your own unique and secure keys for actual use.

Resulting Logon <A> message:

Client messages that contain syntax errors, missing required fields, or refer to unknown symbols will be rejected by the server with a Reject <3> message.

If a valid message cannot be processed and is rejected, an appropriate reject response will be sent. Please refer to the individual message documentation for possible responses.

Please refer to the Text (58) and ErrorCode (25016) fields in responses for the reject reason.

The list of error codes can be found on the Error codes page.

Only printable ASCII characters and SOH are supported.

Supported UTCTIMESTAMP formats:

Client order ID fields must conform to the regex ^[a-zA-Z0-9-_]{1,36}$:

[!NOTE] In example messages, the | character is used to represent SOH character:

Appears at the start of every message.

Appears at the end of every message.

Sent by the server if there is no outgoing traffic during the heartbeat interval (HeartBtInt (108) in Logon<A>).

Sent by the client to indicate that the session is healthy.

Sent by the client or the server in response to a TestRequest<1> message.

Sent by the server if there is no incoming traffic during the heartbeat interval (HeartBtInt (108) in Logon<A>).

Sent by the client to request a Heartbeat<0> response.

[!NOTE] If the client does not respond to TestRequest<1> with Heartbeat<0> with a correct TestReqID (112) within timeout, the connection will be dropped.

Sent by the server in response to an invalid message that cannot be processed.

Sent by the server if a new connection cannot be accepted. Please refer to Connection Limits.

Please refer to the Text (58) and ErrorCode (25016) fields for the reject reason.

Sent by the client to authenticate the connection. Logon<A> must be the first message sent by the client.

Sent by the server in response to a successful logon.

[!NOTE] Logon<A> can only be sent once for the entirety of the session.

Sent to initiate the process of closing the connection, and also when responding to Logout.

When the server enters maintenance, a News message will be sent to clients every 10 seconds for 10 minutes. After this period, clients will be logged out and their sessions will be closed.

Upon receiving this message, clients are expected to establish a new session and close the old one.

The countdown message sent will be:

When there are 10 seconds remaining, the following message will be sent:

If the client does not close the old session within 10 seconds of receiving the above message, the server will log it out and close the session.

Resend requests are currently not supported.

[!NOTE] The messages below can only be used for the FIX Order Entry and FIX Drop Copy Sessions.

Sent by the client to submit a new order for execution.

This adds 1 order to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Unfilled Order Count: 1

Please refer to Supported Order Types for supported field combinations.

[!NOTE] Many fields become required based on the order type. Please refer to Supported Order Types.

Required fields based on Binance OrderType:

Sent by the server whenever an order state changes.

Sent by the client to cancel an order or an order list.

If the canceled order is part of an order list, the entire list will be canceled.

Sent by the server when OrderCancelRequest<F> has failed.

Sent by the client to cancel an order and submit a new one for execution.

Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the unfilled order count by 1.

Unfilled Order Count: 1

Please refer to Supported Order Types for supported field combinations when describing the new order.

[!NOTE] Cancel is always processed first. Then immediately after that the new order is submitted.

Sent by the client to cancel all open orders on a symbol.

[!NOTE] All orders of the account will be canceled, including those placed in different connections.

Sent by the server in response to OrderMassCancelRequest<q>.

Sent by the client to submit a list of orders for execution.

Unfilled Order Count:

Orders in an order list are contingent on one another. Please refer to Supported Order List Types for supported order types and triggering instructions.

[!NOTE] Orders must be specified in the sequence indicated in the Order Names column in the table below.

Sent by the server whenever an order list state changes.

[!NOTE] By default, ListStatus<N> is sent for all order lists of an account, including those submitted in different connections. Please see Response Mode for other behavior options.

Sent by the client to reduce the original quantity of their order.

This adds 0 orders to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Unfilled Order Count: 0

Read Order Amend Keep Priority FAQ to learn more.

Sent by the server when the OrderAmendKeepPriorityRequest <XAK> has failed.

Sent by the client to query current limits.

Sent by the server in response to LimitQuery<XLQ>.

[!NOTE] The messages below can only be used for the FIX Market Data.

Sent by the client to query information about active instruments (i.e., those that have the TRADING status). If used for an inactive instrument, it will be responded to with a Reject<3>.

Sent by the server in a response to the InstrumentListRequest<x>.

[!NOTE] More detailed symbol information is available through the exchangeInfo endpoint.

Sent by the client to subscribe to or unsubscribe from market data stream.

The Trade Streams push raw trade information; each trade has a unique buyer and seller.

Fields required to subscribe:

Update Speed: Real-time

Individual Symbol Book Ticker Stream

Pushes any update to the best bid or offers price or quantity in real-time for a specified symbol.

Fields required to subscribe:

Update Speed: Real-time

[!NOTE] In the Individual Symbol Book Ticker Stream, when MDUpdateAction is set to CHANGE(1) in a MarketDataIncrementalRefresh<X> message sent from the server, it replaces the previous best quote.

Order book price and quantity depth updates used to locally manage an order book.

Fields required to subscribe:

[!NOTE] Since the MarketDataSnapshot<W> have a limit on the number of price levels (5000 on each side maximum), you won't learn the quantities for the levels outside of the initial snapshot unless they change. So be careful when using the information for those levels, since they might not reflect the full view of the order book. However, for most use cases, seeing 5000 levels on each side is enough to understand the market and trade effectively.

Sent by the server in a response to an invalid MarketDataRequest <V>.

Sent by the server in response to a MarketDataRequest<V>, activating Individual Symbol Book Ticker Stream or Diff. Depth Stream subscriptions.

Sent by the server when there is a change in a subscribed stream.

Sample fragmented messages:

[!NOTE] Below are example messages, with NoMDEntry limited to 2, In the real streams, the NoMDEntry is limited to 10000.

**Examples:**

Example 1 (javascript):
```javascript
serverTime = getCurrentTime()if (SendingTime < (serverTime + 1 second) && (serverTime - SendingTime) <= RecvWindow) {  // begin processing request  serverTime = getCurrentTime()  if (serverTime - SendingTime) <= RecvWindow {    // forward request to Matching Engine  } else {    // reject request  }  // finish processing request} else {  // reject request}
```

Example 2 (python):
```python
import base64from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKeyfrom cryptography.hazmat.primitives.serialization import load_pem_private_keydef logon_raw_data(private_key: Ed25519PrivateKey,                   sender_comp_id: str,                   target_comp_id: str,                   msg_seq_num: str,                   sending_time: str):    """    Computes the value of RawData (96) field in Logon<A> message.    """    payload = chr(1).join([        'A',        sender_comp_id,        target_comp_id,        msg_seq_num,        sending_time,    ])    signature = private_key.sign(payload.encode('ASCII'))    return base64.b64encode(signature).decode('ASCII')with open('private_key.pem', 'rb') as f:    private_key = load_pem_private_key(data=f.read(),                                       password=None)raw_data = logon_raw_data(private_key,                          sender_comp_id='5JQmUOsm',                          target_comp_id='SPOT',                          msg_seq_num='1',                          sending_time='20240612-08:52:21.613')
```

Example 3 (text):
```text
-----BEGIN PRIVATE KEY-----MC4CAQAwBQYDK2VwBCIEIIJEYWtGBrhACmb9Dvy+qa8WEf0lQOl1s4CLIAB9m89u-----END PRIVATE KEY-----
```

Example 4 (text):
```text
4MHXelVVcpkdwuLbl6n73HQUXUf1dse2PCgT1DYqW9w8AVZ1RACFGM+5UdlGPrQHrgtS3CvsRURC1oj73j8gCA==
```

---

## (deprecated)Start Isolated Margin User Data Stream (USER_STREAM)

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Start-Isolated-Margin-User-Data-Stream

**Contents:**
- (deprecated)Start Isolated Margin User Data Stream (USER_STREAM)
- API Description​
- HTTP Request​
- Request Weight(UID)​
- Request Parameters​
- Response Example​

Start a new isolated margin user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

POST /sapi/v1/userDataStream/isolated

The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

**Examples:**

Example 1 (javascript):
```javascript
{  "listenKey": "T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhdmjifQ2tRbuKkTHhr"}
```

---

## Order Amend Keep Priority

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/order_amend_keep_priority

**Contents:**
- Order Amend Keep Priority
- What is Order Amend Keep Priority?​
- How can I amend the quantity of my order?​
- What is the difference between "Cancel an Existing Order and Send a New Order" (cancel-replace) and "Order Amend Keep Priority"?​
- Does Order Amend Keep Priority affect unfilled order count (rate limits)?​
- How do I know if my order has been amended?​
- What happens if my amend request does not succeed?​
- Is it possible to reuse the current clientOrderId for my amended order?​
- Can Iceberg Orders be amended?​
- Can Order lists be amended?​

Order Amend Keep Priority request is used to modify (amend) an existing order without losing order book priority.

The following order modifications are allowed:

Use the following requests:

Cancel an Existing Order and Send a New Order request cancels the old order and places a new order. Time priority is lost. The new order executes after existing orders at the same price.

Order Amend Keep Priority request modifies an existing order in-place. The amended order keeps its time priority among existing orders at the same price.

For example, consider the following order book:

Your order 15 is the second one in the queue based on price and time.

You want to reduce the quantity from 5.50 down to 5.00.

If you use cancel-replace to cancel orderId=15 and place a new order with qty=5.00, the order book will look like this:

Note that the new order gets a new order ID and you lose time priority: order 22 will trade after the order 20.

If instead you use Order Amend Keep Priority to reduce the quantity of orderId=15 down to qty=5.00, the order book will look like this:

Note that the order ID stays the same and the order keeps its priority in the queue. Only the quantity of the order changes.

Currently, Order Amend Keep Priority requests charge 0 for unfilled order count.

If the order was amended successfully, the API response contains your order with the updated quantity.

On User Data Stream, you will receive an "executionReport" event with execution type "x": "REPLACED".

If the amended order belongs to an order list and the client order ID has changed, you will also receive a "listStatus" event with list status type "l": "UPDATED".

You can also use the following requests to query order modification history:

If the request fails for any reason (e.g. fails the filters, permissions, account restrictions, etc), then the order amend request is rejected and the order remains unchanged.

By default, amended orders get a random new client order ID, but you can pass the current client order ID in the newClientOrderId parameter if you wish to keep it.

Note that an iceberg order's visible quantity will only change if newQty is below the pre-amended visible quantity.

Orders in an order list can be amended.

Note that OCO order pairs must have the same quantity, since only one of the orders can ever be executed. This means that amending either order affects both orders.

For OTO orders, the working and pending orders can be amended individually.

This information is available in Exchange Information. Symbols that allow Order Amend Keep Priority requests have amendAllowed set to true.

---

## Smart Order Routing (SOR)

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/sor_faq

**Contents:**
- Smart Order Routing (SOR)
  - What is Smart Order Routing (SOR)?​
  - What symbols support SOR?​
  - How do I place an order using SOR?​
  - In the API response, there's a field called workingFloor. What does that field mean?​
  - In the API response, fills contain fields matchType and allocId. What do they mean?​
  - What are allocations?​
  - How do I query orders that used SOR?​
  - How do I get details of my fills for orders that used SOR?​

Smart Order Routing (SOR) allows you to potentially get better liquidity by filling an order with liquidity from other order books with the same base asset and interchangeable quote assets. Interchangeable quote assets are quote assets with fixed 1 to 1 exchange rate, such as stablecoins pegged to the same fiat currency.

Note that even though the quote assets are interchangeable, when selling the base asset you will always receive the quote asset of the symbol in your order.

When you place an order using SOR, it goes through the eligible order books, looks for best price levels for each order book in that SOR configuration, and takes from those books if possible.

Note: If the order using SOR cannot fully fill based on the eligible order books' liquidity, LIMIT IOC or MARKET orders will immediately expire, while LIMIT GTC orders will place the remaining quantity on the order book you originally submitted the order to.

Let's consider a SOR configuration containing the symbols BTCUSDT, BTCUSDC and BTCUSDP, and the following ASK (SELL side) order books for those symbols:

If you send a LIMIT GTC BUY order for BTCUSDT with quantity=0.5 and price=31000, you would match with the best SELL price on the BTCUSDT book at 30,500. You would spend 15,250 USDT and receive 0.5 BTC.

If you send a LIMIT GTC BUY order using SOR for BTCUSDT with quantity=0.5 and price=31000, you would match with the best SELL price across all symbols in the SOR, which is BTCUSDC at price 28,000. You would spend 14,000 USDT (not USDC!) and receive 0.5 BTC.

Using the same order book as Example 1:

If you send a LIMIT GTC BUY order for BTCUSDT with quantity=5 and price=31000, you would:

In total, you spend 153,100 USDT and receive 5 BTC.

If you send the same LIMIT GTC BUY order using SOR for BTCUSDT with quantity=5 and price=31000, you would:

In total, you spend 148,000 USDT and receive 5 BTC.

Using the same order book as Example 1 and 2:

If you send a MARKET BUY order for BTCUSDT using SOR with quantity=11, there is only 10 BTC in total available across all eligible order books. Once all the order books in SOR configuration have been exhausted, the remaining quantity of 1 expires.

Let's consider a SOR configuration containing the symbols BTCUSDT, BTCUSDC and BTCUSDP and the following BID (BUY side) order book for those symbols:

If you send a LIMIT GTC SELL order for BTCUSDT with price=29000 and quantity=10, you would sell 5 BTC and receive 147,500 USDT. Since there is no better price available on the BTCUSDT book, the remaining (unfilled) quantity of the order will rest there at the price of 29,000.

If you send a LIMIT GTC SELL order using SOR for BTCUSDT, you would:

In total, you sell 10 BTC and receive 325,000 USDT.

Summary: The goal of SOR is to potentially access better liquidity across order books with interchangeable quote assets. Better liquidity access can fill orders more fully and at better prices during an order's taker phase.

You can find the current SOR configuration in Exchange Information (GET /api/v3/exchangeInfo for Rest, and exchangeInfo on Websocket API).

The sors field is optional. It is omitted in responses if SOR is not available.

On the Rest API, the request is POST /api/v3/sor/order.

On the WebSocket API, the request is sor.order.place.

This is a term used to determine where the order's last activity occurred (filling, expiring, or being placed as new, etc.).

If the workingFloor is SOR, this means your order interacted with other eligible order books in the SOR configuration.

If the workingFloor is EXCHANGE, this means your order interacted on the order book that you sent that order to.

matchType field indicates a non-standard order fill.

When your order is filled by SOR, you will see matchType: ONE_PARTY_TRADE_REPORT, indicating that you did not trade directly on the exchange (tradeId: -1). Instead your order is filled by allocations.

allocId field identifies the allocation so that you can query it later.

An allocation is a transfer of an asset from the exchange to your account. For example, when SOR takes liquidity from eligible order books, your order is filled by allocations. In this case you don't trade directly, but rather receive allocations from SOR corresponding to the trades made by SOR on your behalf.

You can find them the same way you query any other order. The main difference is that in the response for an order that used SOR there are two extra fields: usedSor and workingFloor.

When SOR orders trade against order books other than the symbol submitted with the order, the order is filled with an allocation and not a trade. Orders placed with SOR can potentially have both allocations and trades.

In the API response, you can review the fills fields. Allocations have an allocId and "matchType": "ONE_PARTY_TRADE_REPORT", while trades will have a non-negative tradeId.

Allocations can be queried using GET /api/v3/myAllocations (Rest API) or myAllocations (WebSocket API).

Trades can be queried using GET /api/v3/myTrades (Rest API) or myTrades (WebSocket API).

**Examples:**

Example 1 (text):
```text
BTCUSDT quantity 3 price 30,800BTCUSDT quantity 3 price 30,500BTCUSDC quantity 1 price 30,000BTCUSDC quantity 1 price 28,000BTCUSDP quantity 1 price 35,000BTCUSDP quantity 1 price 29,000
```

Example 2 (javascript):
```javascript
{  "symbol": "BTCUSDT",  "orderId": 2,  "orderListId": -1,  "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",  "transactTime": 1689149087774,  "price": "31000.00000000",  "origQty": "0.50000000",  "executedQty": "0.50000000",  "cummulativeQuoteQty": "14000.00000000",  "status": "FILLED",  "timeInForce": "GTC",  "type": "LIMIT",  "side": "BUY",  "workingTime": 1689149087774,  "fills": [    {      "matchType": "ONE_PARTY_TRADE_REPORT",      "price": "28000.00000000",      "qty": "0.50000000",      "commission": "0.00000000",      "commissionAsset": "BTC",      "tradeId": -1,      "allocId": 0    }  ],  "workingFloor": "SOR",  "selfTradePreventionMode": "NONE",  "usedSor": true}
```

Example 3 (text):
```text
BTCUSDT quantity 3 price 30,800BTCUSDT quantity 3 price 30,500BTCUSDC quantity 1 price 30,000BTCUSDC quantity 1 price 28,000BTCUSDP quantity 1 price 35,000BTCUSDP quantity 1 price 29,000
```

Example 4 (javascript):
```javascript
{  "symbol": "BTCUSDT",  "orderId": 2,  "orderListId": -1,  "clientOrderId": "tHonoNjWfOSaKiTygN3bfY",  "transactTime": 1689146154686,  "price": "31000.00000000",  "origQty": "5.00000000",  "executedQty": "5.00000000",  "cummulativeQuoteQty": "148000.00000000",  "status": "FILLED",  "timeInForce": "GTC",  "type": "LIMIT",  "side": "BUY",  "workingTime": 1689146154686,  "fills": [    {      "matchType": "ONE_PARTY_TRADE_REPORT",      "price": "28000.00000000",      "qty": "1.00000000",      "commission": "0.00000000",      "commissionAsset": "BTC",      "tradeId": -1,      "allocId": 0    },    {      "matchType": "ONE_PARTY_TRADE_REPORT",      "price": "29000.00000000",      "qty": "1.00000000",      "commission": "0.00000000",      "commissionAsset": "BTC",      "tradeId": -1,      "allocId": 1    },    {      "matchType": "ONE_PARTY_TRADE_REPORT",      "price": "30000.00000000",      "qty": "1.00000000",      "commission": "0.00000000",      "commissionAsset": "BTC",      "tradeId": -1,      "allocId": 2    },    {      "matchType": "ONE_PARTY_TRADE_REPORT",      "price": "30500.00000000",      "qty": "2.00000000",      "commission": "0.00000000",      "commissionAsset": "BTC",      "tradeId": -1,      "allocId": 3    }  ],  "workingFloor": "SOR",  "selfTradePreventionMode": "NONE",  "usedSor": true}
```

---

## SPOT API Glossary

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/spot_glossary

**Contents:**
- SPOT API Glossary
  - A​
  - B​
  - C​
  - D​
  - E​
  - F​
  - G​
  - H​
  - I​

Disclaimer: This glossary refers only to the SPOT API Implementation. The definition for these terms may differ with regards to Futures, Options, and other APIs by Binance.

aggTrade/Aggregate trade

baseCommissionPrecision

GTC/ Good Til Canceled

IOC / Immediate or Canceled

Last Prevented Quantity

Order Amend Keep Priority

Prevented execution price

Prevented execution quantity

Prevented execution quote quantity

quoteCommissionPrecision

Self Trade Prevention (STP)

selfTradePreventionMode

Smart Order Routing (SOR)

specialCommissionForOrder/specialCommission

standardCommissionForOrder/standardCommission

taxCommissionForOrder/taxCommission

---

## Account Endpoints

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints

**Contents:**
- Account Endpoints
  - Account information (USER_DATA)​
  - Query order (USER_DATA)​
  - Current open orders (USER_DATA)​
  - All orders (USER_DATA)​
  - Query Order list (USER_DATA)​
  - Query all Order lists (USER_DATA)​
  - Query Open Order lists (USER_DATA)​
  - Account trade list (USER_DATA)​
  - Query Unfilled Order Count (USER_DATA)​

Get current account information.

Data Source: Memory => Database

Check an order's status.

Data Source: Memory => Database

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Get all open orders on a symbol. Careful when accessing this with no symbol.

Weight: 6 for a single symbol; 80 when the symbol parameter is omitted

Data Source: Memory => Database

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Get all account orders; active, canceled, or filled.

Data Source: Database

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Retrieves a specific order list based on provided optional parameters.

Data Source: Database

Retrieves all order lists based on provided optional parameters.

Note that the time between startTime and endTime can't be longer than 24 hours.

Data Source: Database

Data Source: Database

Get trades for a specific account and symbol.

Data Source: Memory => Database

Displays the user's unfilled order count for all intervals.

Displays the list of orders that were expired due to STP.

These are the combinations supported:

Retrieves allocations resulting from SOR order placement.

Supported parameter combinations:

Note: The time between startTime and endTime can't be longer than 24 hours.

Data Source: Database

Get current account commission rates.

Data Source: Database

Queries all amendments of a single order.

Retrieves the list of filters relevant to an account on a given symbol. This is the only endpoint that shows if an account has MAX_ASSET filters applied to it.

**Examples:**

Example 1 (text):
```text
GET /api/v3/account
```

Example 2 (javascript):
```javascript
{  "makerCommission": 15,  "takerCommission": 15,  "buyerCommission": 0,  "sellerCommission": 0,  "commissionRates": {    "maker": "0.00150000",    "taker": "0.00150000",    "buyer": "0.00000000",    "seller": "0.00000000"  },  "canTrade": true,  "canWithdraw": true,  "canDeposit": true,  "brokered": false,  "requireSelfTradePrevention": false,  "preventSor": false,  "updateTime": 123456789,  "accountType": "SPOT",  "balances": [    {      "asset": "BTC",      "free": "4723846.89208129",      "locked": "0.00000000"    },    {      "asset": "LTC",      "free": "4763368.68006011",      "locked": "0.00000000"    }  ],  "permissions": [    "SPOT"  ],  "uid": 354937868}
```

Example 3 (text):
```text
GET /api/v3/order
```

Example 4 (javascript):
```javascript
{  "symbol": "LTCBTC",  "orderId": 1,  "orderListId": -1,                 // This field will always have a value of -1 if not an order list.  "clientOrderId": "myOrder1",  "price": "0.1",  "origQty": "1.0",  "executedQty": "0.0",  "cummulativeQuoteQty": "0.0",  "status": "NEW",  "timeInForce": "GTC",  "type": "LIMIT",  "side": "BUY",  "stopPrice": "0.0",  "icebergQty": "0.0",  "time": 1499827319559,  "updateTime": 1499827319559,  "isWorking": true,  "workingTime":1499827319559,  "origQuoteOrderQty": "0.000000",  "selfTradePreventionMode": "NONE"}
```

---

## (deprecated)Close Isolated Margin User Data Stream (USER_STREAM)

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Close-Isolated-Margin-User-Data-Stream

**Contents:**
- (deprecated)Close Isolated Margin User Data Stream (USER_STREAM)
- API Description​
- HTTP Request​
- Request Weight(UID)​
- Request Parameters​
- Response Example​

Close out a isolated margin user data stream.

DELETE /sapi/v1/userDataStream/isolated

---

## Pegged orders

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/pegged_orders

**Contents:**
- Pegged orders
- What are pegged orders?​
- How can I send a pegged order?​
- What order types support pegged orders?​
  - Limit orders​
  - Stop-limit orders​
  - OCO​
  - OTO and OTOCO​
- Which symbols allow pegged orders?​
- Which Filters are applicable to pegged orders?​

Pegged orders are essentially limit orders with the price derived from the order book.

For example, instead of using a specific price (e.g. SELL 1 BTC for at least 100,000 USDC) you can send orders like “SELL 1 BTC at the best asking price” to queue your order after the orders on the book at the highest price, or “BUY 1 BTC for 100,000 USDT or best offer, IOC” to cherry-pick the sellers at the lowest price, and only that price.

Pegged orders offer a way for market makers to match the best price with minimal latency, while retail users can get quick fills at the best price with minimal slippage.

Pegged orders are also known as “best bid-offer” or BBO orders.

Please refer to the following table:

pegOffsetType and pegOffsetValue PRICE_LEVEL — offset by existing price levels, deeper into the order book

For order lists: (Please see the API documentation for more details.)

Currently, Smart Order Routing (SOR) does not support pegged orders.

This sample REST API response shows that for pegged orders, peggedPrice reflects the selected price, while price is the original order price (zero if not set).

All order types, with the exception of MARKET orders, are supported by this feature.

Since both STOP_LOSS and TAKE_PROFIT orders place a MARKET order once the stop condition is met, these order types cannot be pegged.

Pegged limit orders immediately enter the market at the current best price:

Pegged stop-limit orders enter the market at the best price when price movement triggers the stop order (via stop price or trailing stop):

That is, stop orders use the best price at the time when they are triggered, which is different from the price when the stop order is placed. Only the limit price can be pegged, not the stop price.

OCO order lists may use peg instructions.

OTO order lists may use peg instructions as well.

OTOCO order lists may contain pegged orders as well, similar to OTO and OCO.

Please refer to Exchange Information requests and look for the field pegInstructionsAllowed. If set to true, pegged orders can be used with the symbol.

Pegged orders are required to pass all applicable filters with the selected price:

If a pegged order specifies price, it must pass validation at both price and peggedPrice.

Contingent pegged orders as well as pegged pending orders of OTO order lists are (re)validated at the trigger time and may be rejected later.

**Examples:**

Example 1 (json):
```json
{  "symbol": "BTCUSDT",  "orderId": 18,  "orderListId": -1,  "clientOrderId": "q1fKs4Y7wgE61WSFMYRFKo",  "transactTime": 1750313780050,  "price": "0.00000000",  "pegPriceType": "PRIMARY_PEG",  "peggedPrice": "0.04000000",  "origQty": "1.00000000",  "executedQty": "0.00000000",  "origQuoteOrderQty": "0.00000000",  "cummulativeQuoteQty": "0.00000000",  "status": "NEW",  "timeInForce": "GTC",  "type": "LIMIT",  "side": "BUY",  "workingTime": 1750313780050,  "fills": [],  "selfTradePreventionMode": "NONE"}
```

---

## listenToken Subscription Methods

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream/Listen-Token-Websocket-API

**Contents:**
- listenToken Subscription Methods
- Create Margin Account listenToken (USER_STREAM)​
  - Description​
  - HTTP Request​
  - Request Parameters​
  - Notes​
  - Response Example​
- Subscribe to User Data Stream using listenToken (USER_STREAM)​
  - Description​
  - method​

There are currently two ways to subscribe to the User Data Stream:

Both sources will push all account-related events to you in real time.

Create a listenToken that authorizes the user to access the User Data Stream of the current account for a limited amout of time. The stream's validity is specified by the validity parameter (milliseconds), default 24 hours, maximum 24 hours. The response includes the listenToken and the corresponding expirationTime (in milliseconds).

POST /sapi/v1/userListenToken

Request weight (UID): 1

Subscribe to the user data stream using listenToken.

This method must be called on the WebSocket API. For more information about how to use the WebSocket API, see : WebSocket API documentation

userDataStream.subscribe.listenToken

**Examples:**

Example 1 (json):
```json
{  "token": "6xXxePXwZRjVSHKhzUCCGnmN3fkvMTXru+pYJS8RwijXk9Vcyr3rkwfVOTcP2OkONqciYA",  "expirationTime": 1758792204196}
```

Example 2 (json):
```json
{  "id": "f3a8f7a29f2e54df796db582f3d",  "method": "userDataStream.subscribe.listenToken",  "params": {    "listenToken": "5DbylArkmImhyHkpG6s9tbiFy5uAMTFwzx9vwsFjDv9dC3GkKxSuoTCj0HvcJC0WYi8fA"  }}
```

Example 3 (json):
```json
{  "subscriptionId": 1,  "expirationTime": 1749094553955907}
```

Example 4 (json):
```json
{  "subscriptionId": 0,  "event": {    "e": "eventStreamTerminated",    "E": 1759089357377  }}
```

---

## Account requests

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/account-requests

**Contents:**
- Account requests
  - Account information (USER_DATA)​
  - Query order (USER_DATA)​
  - Current open orders (USER_DATA)​
  - Account order history (USER_DATA)​
  - Query Order list (USER_DATA)​
  - Current open Order lists (USER_DATA)​
  - Account order list history (USER_DATA)​
  - Account trade history (USER_DATA)​
  - Unfilled Order Count (USER_DATA)​

Query information about your account.

Data Source: Memory => Database

Check execution status of an order.

If both orderId and origClientOrderId are provided, the orderId is searched first, then the origClientOrderId from that result is checked against that order. If both conditions are not met the request will be rejected.

For some historical orders the cummulativeQuoteQty response field may be negative, meaning the data is not available at this time.

Data Source: Memory => Database

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Query execution status of all open orders.

If you need to continuously monitor order status updates, please consider using WebSocket Streams:

Weight: Adjusted based on the number of requested symbols:

Data Source: Memory => Database

Status reports for open orders are identical to order.status.

Note that some fields are optional and included only for orders that set them.

Open orders are always returned as a flat list. If all symbols are requested, use the symbol field to tell which symbol the orders belong to.

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Query information about all your orders – active, canceled, filled – filtered by time range.

If startTime and/or endTime are specified, orderId is ignored.

Orders are filtered by time of the last execution status update.

If orderId is specified, return orders with order ID >= orderId.

If no condition is specified, the most recent orders are returned.

For some historical orders the cummulativeQuoteQty response field may be negative, meaning the data is not available at this time.

The time between startTime and endTime can't be longer than 24 hours.

Data Source: Database

Status reports for orders are identical to order.status.

Note that some fields are optional and included only for orders that set them.

Check execution status of an Order list.

For execution status of individual orders, use order.status.

origClientOrderId refers to listClientOrderId of the order list itself.

If both origClientOrderId and orderListId parameters are specified, only origClientOrderId is used and orderListId is ignored.

Data Source: Database

Query execution status of all open order lists.

If you need to continuously monitor order status updates, please consider using WebSocket Streams:

Data Source: Database

Query information about all your order lists, filtered by time range.

If startTime and/or endTime are specified, fromId is ignored.

Order lists are filtered by transactionTime of the last order list execution status update.

If fromId is specified, return order lists with order list ID >= fromId.

If no condition is specified, the most recent order lists are returned.

The time between startTime and endTime can't be longer than 24 hours.

Data Source: Database

Status reports for order lists are identical to orderList.status.

Query information about all your trades, filtered by time range.

If fromId is specified, return trades with trade ID >= fromId.

If startTime and/or endTime are specified, trades are filtered by execution time (time).

fromId cannot be used together with startTime and endTime.

If orderId is specified, only trades related to that order are returned.

startTime and endTime cannot be used together with orderId.

If no condition is specified, the most recent trades are returned.

The time between startTime and endTime can't be longer than 24 hours.

Data Source: Memory => Database

Query your current unfilled order count for all intervals.

Displays the list of orders that were expired due to STP.

These are the combinations supported:

Data Source: Database

Retrieves allocations resulting from SOR order placement.

Supported parameter combinations:

Note: The time between startTime and endTime can't be longer than 24 hours.

Data Source: Database

Get current account commission rates.

Data Source: Database

Queries all amendments of a single order.

Data Source: Database

Retrieves the list of filters relevant to an account on a given symbol. This is the only endpoint that shows if an account has MAX_ASSET filters applied to it.

**Examples:**

Example 1 (javascript):
```javascript
{  "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  "method": "account.status",  "params": {    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "signature": "83303b4a136ac1371795f465808367242685a9e3a42b22edb4d977d0696eb45c",    "timestamp": 1660801839480  }}
```

Example 2 (javascript):
```javascript
{  "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  "status": 200,  "result": {    "makerCommission": 15,    "takerCommission": 15,    "buyerCommission": 0,    "sellerCommission": 0,    "canTrade": true,    "canWithdraw": true,    "canDeposit": true,    "commissionRates": {      "maker": "0.00150000",      "taker": "0.00150000",      "buyer": "0.00000000",      "seller": "0.00000000"    },    "brokered": false,    "requireSelfTradePrevention": false,    "preventSor": false,    "updateTime": 1660801833000,    "accountType": "SPOT",    "balances": [      {        "asset": "BNB",        "free": "0.00000000",        "locked": "0.00000000"      },      {        "asset": "BTC",        "free": "1.3447112",        "locked": "0.08600000"      },      {        "asset": "USDT",        "free": "1021.21000000",        "locked": "0.00000000"      }    ],    "permissions": [      "SPOT"    ],    "uid": 354937868  },  "rateLimits": [    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 20    }  ]}
```

Example 3 (javascript):
```javascript
{  "id": "aa62318a-5a97-4f3b-bdc7-640bbe33b291",  "method": "order.status",  "params": {    "symbol": "BTCUSDT",    "orderId": 12569099453,    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",    "signature": "2c3aab5a078ee4ea465ecd95523b77289f61476c2f238ec10c55ea6cb11a6f35",    "timestamp": 1660801720951  }}
```

Example 4 (javascript):
```javascript
{  "id": "aa62318a-5a97-4f3b-bdc7-640bbe33b291",  "status": 200,  "result": {    "symbol": "BTCUSDT",    "orderId": 12569099453,    "orderListId": -1,                  // set only for orders of an order list    "clientOrderId": "4d96324ff9d44481926157",    "price": "23416.10000000",    "origQty": "0.00847000",    "executedQty": "0.00847000",    "cummulativeQuoteQty": "198.33521500",    "status": "FILLED",    "timeInForce": "GTC",    "type": "LIMIT",    "side": "SELL",    "stopPrice": "0.00000000",          // always present, zero if order type does not use stopPrice    "trailingDelta": 10,                // present only if trailingDelta set for the order    "trailingTime": -1,                 // present only if trailingDelta set for the order    "icebergQty": "0.00000000",         // always present, zero for non-iceberg orders    "time": 1660801715639,              // time when the order was placed    "updateTime": 1660801717945,        // time of the last update to the order    "isWorking": true,    "workingTime": 1660801715639,    "origQuoteOrderQty": "0.00000000",   // always present, zero if order type does not use quoteOrderQty    "strategyId": 37463720,             // present only if strategyId set for the order    "strategyType": 1000000,            // present only if strategyType set for the order    "selfTradePreventionMode": "NONE",    "preventedMatchId": 0,              // present only if the order expired due to STP    "preventedQuantity": "1.200000"     // present only if the order expired due to STP  },  "rateLimits": [    {      "rateLimitType": "REQUEST_WEIGHT",      "interval": "MINUTE",      "intervalNum": 1,      "limit": 6000,      "count": 4    }  ]}
```

---

## listenToken Subscription Methods

**URL:** https://developers.binance.com/docs/margin_trading/trade-data-stream

**Contents:**
- listenToken Subscription Methods
- Create Margin Account listenToken (USER_STREAM)​
  - Description​
  - HTTP Request​
  - Request Parameters​
  - Notes​
  - Response Example​
- Subscribe to User Data Stream using listenToken (USER_STREAM)​
  - Description​
  - method​

There are currently two ways to subscribe to the User Data Stream:

Both sources will push all account-related events to you in real time.

Create a listenToken that authorizes the user to access the User Data Stream of the current account for a limited amout of time. The stream's validity is specified by the validity parameter (milliseconds), default 24 hours, maximum 24 hours. The response includes the listenToken and the corresponding expirationTime (in milliseconds).

POST /sapi/v1/userListenToken

Request weight (UID): 1

Subscribe to the user data stream using listenToken.

This method must be called on the WebSocket API. For more information about how to use the WebSocket API, see : WebSocket API documentation

userDataStream.subscribe.listenToken

**Examples:**

Example 1 (json):
```json
{  "token": "6xXxePXwZRjVSHKhzUCCGnmN3fkvMTXru+pYJS8RwijXk9Vcyr3rkwfVOTcP2OkONqciYA",  "expirationTime": 1758792204196}
```

Example 2 (json):
```json
{  "id": "f3a8f7a29f2e54df796db582f3d",  "method": "userDataStream.subscribe.listenToken",  "params": {    "listenToken": "5DbylArkmImhyHkpG6s9tbiFy5uAMTFwzx9vwsFjDv9dC3GkKxSuoTCj0HvcJC0WYi8fA"  }}
```

Example 3 (json):
```json
{  "subscriptionId": 1,  "expirationTime": 1749094553955907}
```

Example 4 (json):
```json
{  "subscriptionId": 0,  "event": {    "e": "eventStreamTerminated",    "E": 1759089357377  }}
```

---

## Market Data endpoints

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints

**Contents:**
- Market Data endpoints
  - Order book​
  - Recent trades list​
  - Old trade lookup​
  - Compressed/Aggregate trades list​
  - Kline/Candlestick data​
  - UIKlines​
  - Current average price​
  - 24hr ticker price change statistics​
  - Trading Day Ticker​

Weight: Adjusted based on the limit:

Data Source: Database

Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price will have the quantity aggregated.

Data Source: Database

Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

Supported kline intervals (case-sensitive):

Data Source: Database

The request is similar to klines having the same parameters and response.

uiKlines return modified kline data, optimized for presentation of candlestick charts.

Data Source: Database

Current average price for a symbol.

24 hour rolling window price change statistics. Careful when accessing this with no symbol.

Price change statistics for a trading day.

4 for each requested symbol. The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

Data Source: Database

Latest price for a symbol or symbols.

Best price/qty on the order book for a symbol or symbols.

Note: This endpoint is different from the GET /api/v3/ticker/24hr endpoint.

The window used to compute statistics will be no more than 59999ms from the requested windowSize.

openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request. As such, the effective window will be up to 59999ms wider than windowSize.

E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the openTime will be: 1641201420000 (January 3, 2022, 09:17:00)

4 for each requested symbol regardless of windowSize. The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

Data Source: Database

**Examples:**

Example 1 (text):
```text
GET /api/v3/depth
```

Example 2 (javascript):
```javascript
{  "lastUpdateId": 1027024,  "bids": [    [      "4.00000000",     // PRICE      "431.00000000"    // QTY    ]  ],  "asks": [    [      "4.00000200",      "12.00000000"    ]  ]}
```

Example 3 (text):
```text
GET /api/v3/trades
```

Example 4 (javascript):
```javascript
[  {    "id": 28457,    "price": "4.00000100",    "qty": "12.00000000",    "quoteQty": "48.000012",    "time": 1499865549590,    "isBuyerMaker": true,    "isBestMatch": true  }]
```

---

## Self Trade Prevention (STP) FAQ

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/stp_faq

**Contents:**
- Self Trade Prevention (STP) FAQ
  - What is Self Trade Prevention?​
  - What defines a self-trade?​
  - What happens when STP is triggered?​
  - What is a Trade Group Id?​
  - What is a Prevented Match?​
  - What is "prevented quantity?"​
  - How do I know which symbol uses STP?​
  - How do I know if an order expired due to STP?​
  - STP Examples​

Self Trade Prevention (or STP) prevents orders of users, or the user's tradeGroupId to match against their own.

A self-trade can occur in either scenario:

There are five possible modes for what the system does when an order would create a self-trade.

NONE - This mode exempts the order from self-trade prevention. Accounts or Trade group IDs will not be compared, no orders will be expired, and the trade will occur.

EXPIRE_TAKER - This mode prevents a trade by immediately expiring the taker order's remaining quantity.

EXPIRE_MAKER - This mode prevents a trade by immediately expiring the potential maker order's remaining quantity.

EXPIRE_BOTH - This mode prevents a trade by immediately expiring both the taker and the potential maker orders' remaining quantities.

DECREMENT - This mode increases the prevented quantity of both orders by the amount of the prevented match. The smaller of the two orders will expire, or both if they have the same quantity.

The STP event will occur depending on the STP mode of the taker order. Thus, the STP mode of an order that goes on the book is no longer relevant and will be ignored for all future order processing.

Different accounts with the same tradeGroupId are considered part of the same "trade group". Orders submitted by members of a trade group are eligible for STP according to the taker-order's STP mode.

A user can confirm if their accounts are under the same tradeGroupId from the API either from GET /api/v3/account (REST API) or account.status (WebSocket API) for each account.

The field is also present in the response for GET /api/v3/preventedMatches (REST API) or myPreventedMatches (WebSocket API).

If the value is -1, then the tradeGroupId has not been set for that account, so the STP may only take place between orders of the same account.

When a self-trade is prevented, a prevented match is created. The orders in the prevented match have their prevented quantities increased and one or more orders expire.

This is not to be confused with a trade, as no orders will match.

This is a record of what orders could have self-traded.

This can be queried through the endpoint GET /api/v3/preventedMatches on the REST API or myPreventedMatches on the WebSocket API.

This is a sample of the output request for reference:

STP events expire quantity from open orders. The STP modes EXPIRE_TAKER, EXPIRE_MAKER, and EXPIRE_BOTH expire all remaining quantity on the affected orders, resulting in the entire open order being expired.

Prevented quantity is the amount of quantity that is expired due to STP events for a particular order. User stream execution reports for orders involved in STP may have these fields:

B is present for execution type TRADE_PREVENTION, and is the quantity expired due to that individual STP event.

A is the cumulative quantity expired due to STP over the lifetime of the order. For EXPIRE_TAKER, EXPIRE_MAKER, and EXPIRE_BOTH modes this will always be the same value as B.

API responses for orders which expired due to STP will also have a preventedQuantity field, indicating the cumulative quantity expired due to STP over the lifetime of the order.

While an order is open, the following equation holds true:

When an order's available quantity goes to zero, the order will be removed from the order book and the status will be one of EXPIRED_IN_MATCH, FILLED, or EXPIRED.

Symbols may be configured to allow different sets of STP modes and take different default STP modes.

defaultSelfTradePreventionMode - Orders will use this STP mode if the user does not provide one on order placement.

allowedSelfTradePreventionModes - Defines the allowed set of STP modes for order placement on that symbol.

For example, if a symbol has the following configuration:

Then that means if a user sends an order with no selfTradePreventionMode provided, then the order sent will have the value of NONE.

If a user wants to explicitly specify the mode they can pass the enum NONE, EXPIRE_TAKER, or EXPIRE_BOTH.

If a user tries to specify EXPIRE_MAKER for orders on this symbol, they will receive an error:

The order will have the status EXPIRED_IN_MATCH.

For all these cases, assume that all orders for these examples are made on the same account.

Scenario A- A user sends a new order with selfTradePreventionMode:NONE that will match with another order of theirs that is already on the book.

Result: No STP is triggered and the orders will match.

Order Status of the Maker Order

Order Status of the Taker Order

Scenario B- A user sends an order with EXPIRE_MAKER that would match with their orders that are already on the book.

Result: The orders that were on the book will expire due to STP, and the taker order will go on the book.

Output of the Taker Order

Scenario C - A user sends an order with EXPIRE_TAKER that would match with their orders already on the book.

Result: The orders already on the book will remain, while the taker order will expire.

Output of the Taker order

Scenario D- A user has an order on the book, and then sends an order with EXPIRE_BOTH that would match with the existing order.

Result: Both orders will expire.

Scenario E - A user has an order on the book with EXPIRE_MAKER, and then sends a new order with EXPIRE_TAKER which would match with the existing order.

Result: The taker order's STP mode will be used, so the taker order will be expired.

Scenario F - A user sends a market order with EXPIRE_MAKER which would match with an existing order.

Result: The existing order expires with the status EXPIRED_IN_MATCH, due to STP. The new order also expires but with status EXPIRED, due to low liquidity on the order book.

Scenario G- A user sends a limit order with DECREMENT which would match with an existing order.

Result: Both orders have a preventedQuantity of 2. Since this is the taker order’s full quantity, it expires due to STP.

**Examples:**

Example 1 (javascript):
```javascript
[  {    "symbol": "BTCDUSDT",                       //Symbol of the orders    "preventedMatchId": 8,                      //Identifies the prevented match of the expired order(s) for the symbol.    "takerOrderId": 12,                         //Order Id of the Taker Order    "makerOrderId": 10,                         //Order Id of the Maker Order    "tradeGroupId": 1,                          //Identifies the Trade Group Id. (If the account is not part of a trade group, this will be -1.)    "selfTradePreventionMode": "EXPIRE_BOTH",   //STP mode that expired the order(s).    "price": "50.00000000",                     //Price at which the match occurred.    "takerPreventedQuantity": "1.00000000",     //Taker's remaining quantity before the STP. Only appears if the STP mode is EXPIRE_TAKER, EXPIRE_BOTH or DECREMENT.    "makerPreventedQuantity": "10.00000000",    //Maker's remaining quantity before the STP. Only appears if the STP mode is EXPIRE_MAKER, EXPIRE_BOTH, or DECREMENT.    "transactTime": 1663190634060               //Time the order(s) expired due to STP.  }]
```

Example 2 (javascript):
```javascript
{  "A":"3.000000", // Prevented Quantity  "B":"3.000000"  // Last Prevented Quantity}
```

Example 3 (text):
```text
original order quantity - executed quantity - prevented quantity = quantity available for further execution
```

Example 4 (json):
```json
"defaultSelfTradePreventionMode": "NONE","allowedSelfTradePreventionModes": [    "NONE",    "EXPIRE_TAKER",    "EXPIRE_BOTH"  ]
```

---

## Spot Unfilled Order Count Rules

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/order_count_decrement

**Contents:**
- Spot Unfilled Order Count Rules
  - What are the current rate limits?​
  - How does the unfilled ORDERS rate limit work?​
  - Is the unfilled order count tracked by IP address?​
  - How do filled orders affect the unfilled order count?​
  - How do canceled or expired orders affect the unfilled order count?​
  - Which time zone does "interval":"DAY" use?​
  - What happens if I placed an order yesterday but it is filled the next day?​

To ensure a fair and orderly Spot market, we limit the rate at which new orders may be placed.

The rate limit applies to the number of new, unfilled orders placed within a time interval. That is, orders which are partially or fully filled do not count against the rate limit.

[!NOTE] Unfilled order rate limit rewards efficient traders.

So long as your orders trade, you can keep trading.

More information: How do filled orders affect the rate limit?

You can query current rate limits using the "exchange information" request.

The "rateLimitType": "ORDERS" indicates the current unfilled order rate limit.

Please refer to the API documentation:

[!IMPORTANT] Order placement requests are also affected by the general request rate limits on REST and WebSocket API and the message limits on FIX API.

If you send too many requests at a high rate, you will be blocked by the API.

Every successful request to place an order adds to the unfilled order count for the current time interval. If too many unfilled orders accumulate during the interval, subsequent requests will be rejected.

For example, if the unfilled order rate limit is 100 per 10 seconds:

then you can place at most 100 new orders between 12:34:00 and 12:34:10, then 100 more from 12:34:10 to 12:34:20, and so on.

[!TIP] If the newly placed orders receive fills, your unfilled order count decreases and you may place more orders during the time interval.

More information: How do filled orders affect the rate limit?

When an order is rejected by the system due to the unfilled order rate limit, the HTTP status code is set to 429 Too Many Requests and the error code is -1015 "Too many new orders".

If you encounter these errors, please stop sending orders until the affected rate limit interval expires.

Please refer to the API documentation:

Unfilled order count is tracked by (sub)account.

Unfilled order count is shared across all IP addresses, all API keys, and all APIs.

When an order is filled for the first time (partially or fully), your unfilled order count is decremented by one order for all intervals of the ORDERS rate limit. Effectively, orders that trade do not count towards the rate limit, allowing efficient traders to keep placing new orders.

Certain orders provide additional incentive:

In these cases the unfilled order count may be decremented by more than one order for each order that starts trading.

Note how for every taker order that immediately trades, the unfilled order count is decremented later, allowing you to keep placing orders.

Note how for every maker order that is filled later, the unfilled order count is decremented by a higher amount, allowing you to place more orders.

Canceling an order does not change the unfilled order count.

Expired orders also do not change the unfilled order count.

New order fills decrease your current unfilled order count regardless of when the orders were placed.

Note: You do not get credit for order fills. That is, once the unfilled order count is down to zero, additional fills will not decrease it further. New orders will increase the count as usual.

**Examples:**

Example 1 (javascript):
```javascript
{  "rateLimitType": "ORDERS",  "interval": "SECOND",  "intervalNum": 10,  "limit": 100}
```

---

## LIMITS

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/limits

**Contents:**
- LIMITS
  - General Info on Limits​
  - IP Limits​
  - Unfilled Order Count​

---

## WebSocket Streams for Binance (2025-01-28)

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams

**Contents:**
- WebSocket Streams for Binance (2025-01-28)
- General WSS information​
- WebSocket Limits​
- Live Subscribing/Unsubscribing to streams​
  - Subscribe to a stream​
  - Unsubscribe to a stream​
  - Listing Subscriptions​
  - Setting Properties​
  - Retrieving Properties​
  - Error Messages​

Currently, the only property that can be set is whether combined stream payloads are enabled or not. The combined property is set to false when connecting using /ws/ ("raw streams") and true when connecting using /stream/.

The Aggregate Trade Streams push trade information that is aggregated for a single taker order.

Stream Name: <symbol>@aggTrade

Update Speed: Real-time

The Trade Streams push raw trade information; each trade has a unique buyer and seller.

Stream Name: <symbol>@trade

Update Speed: Real-time

The Kline/Candlestick Stream push updates to the current klines/candlestick every second in UTC+0 timezone

Kline/Candlestick chart intervals:

s-> seconds; m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

Stream Name: <symbol>@kline_<interval>

Update Speed: 1000ms for 1s, 2000ms for the other intervals

The Kline/Candlestick Stream push updates to the current klines/candlestick every second in UTC+8 timezone

Kline/Candlestick chart intervals:

Supported intervals: See Kline/Candlestick chart intervals

UTC+8 timezone offset:

Stream Name: <symbol>@kline_<interval>@+08:00

Update Speed: 1000ms for 1s, 2000ms for the other intervals

24hr rolling window mini-ticker statistics. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

Stream Name: <symbol>@miniTicker

24hr rolling window mini-ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

Stream Name: !miniTicker@arr

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

Stream Name: <symbol>@ticker

24hr rolling window ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

Stream Name: !ticker@arr

Rolling window ticker statistics for a single symbol, computed over multiple windows.

Stream Name: <symbol>@ticker_<window_size>

Window Sizes: 1h,4h,1d

Note: This stream is different from the <symbol>@ticker stream. The open time "O" always starts on a minute, while the closing time "C" is the current time of the update. As such, the effective window might be up to 59999ms wider than <window_size>.

Rolling window ticker statistics for all market symbols, computed over multiple windows. Note that only tickers that have changed will be present in the array.

Stream Name: !ticker_<window-size>@arr

Window Size: 1h,4h,1d

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol. Multiple <symbol>@bookTicker streams can be subscribed to over one connection.

Stream Name: <symbol>@bookTicker

Update Speed: Real-time

Average price streams push changes in the average price over a fixed time interval.

Stream Name: <symbol>@avgPrice

Top <levels> bids and asks, pushed every second. Valid <levels> are 5, 10, or 20.

Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms

Update Speed: 1000ms or 100ms

Order book price and quantity depth updates used to locally manage an order book.

Stream Name: <symbol>@depth OR <symbol>@depth@100ms

Update Speed: 1000ms or 100ms

To apply an event to your local order book, follow this update procedure:

[!NOTE] Since depth snapshots retrieved from the API have a limit on the number of price levels (5000 on each side maximum), you won't learn the quantities for the levels outside of the initial snapshot unless they change. So be careful when using the information for those levels, since they might not reflect the full view of the order book. However, for most use cases, seeing 5000 levels on each side is enough to understand the market and trade effectively.

**Examples:**

Example 1 (javascript):
```javascript
{  "method": "SUBSCRIBE",  "params": [    "btcusdt@aggTrade",    "btcusdt@depth"  ],  "id": 1}
```

Example 2 (javascript):
```javascript
{  "result": null,  "id": 1}
```

Example 3 (javascript):
```javascript
{  "method": "UNSUBSCRIBE",  "params": [    "btcusdt@depth"  ],  "id": 312}
```

Example 4 (javascript):
```javascript
{  "result": null,  "id": 312}
```

---

## Error codes for Binance

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/errors

**Contents:**
- Error codes for Binance
- 10xx - General Server or Network issues​
  - -1000 UNKNOWN​
  - -1001 DISCONNECTED​
  - -1002 UNAUTHORIZED​
  - -1003 TOO_MANY_REQUESTS​
  - -1006 UNEXPECTED_RESP​
  - -1007 TIMEOUT​
  - -1008 SERVER_BUSY​
  - -1013 INVALID_MESSAGE​

Last Updated: 2025-10-28

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:

This code is sent when an error has been returned by the matching engine. The following messages which will indicate the specific error:

**Examples:**

Example 1 (javascript):
```javascript
{  "code":-1121,  "msg":"Invalid symbol."}
```

---

## General endpoints

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints

**Contents:**
- General endpoints
  - Test connectivity​
  - Check server time​
  - Exchange information​

Test connectivity to the Rest API.

Test connectivity to the Rest API and get the current server time.

Current exchange trading rules and symbol information

Examples of Symbol Permissions Interpretation from the Response:

**Examples:**

Example 1 (text):
```text
GET /api/v3/ping
```

Example 2 (text):
```text
GET /api/v3/time
```

Example 3 (javascript):
```javascript
{  "serverTime": 1499827319559}
```

Example 4 (text):
```text
GET /api/v3/exchangeInfo
```

---

## CHANGELOG for Binance's API

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG

**Contents:**
- CHANGELOG for Binance's API
  - 2025-10-28​
  - 2025-10-24​
    - SBE​
    - REST and WebSocket API​
  - 2025-10-21​
  - 2025-10-08​
    - FIX API​
  - 2025-09-29​
  - 2025-09-18​

Last Updated: 2025-10-28

Notice: The following changes will be deployed on 2025-10-28, starting at 04:00 UTC and may take several hours to complete:

Following the announcement from 2025-04-07, all documentation related with listenKey for use on wss://stream.binance.com has been removed.

Please refer to the list of requests and methods below for more information.

The features will remain available until a future retirement announcement is made.

REST and WebSocket API:

Notice: The following changes will be deployed on 2025-09-29, starting at 10:00 UTC and may take several hours to complete.

Notice: The changes in this section will be gradually rolled out, and will take approximately up to two weeks to complete.

The following changes will be available on 2025-08-27 starting at 07:00 UTC:

The following changes will be available on 2025-08-28 starting at 07:00 UTC:

REST and WebSocket API:

Notice: The following changes will happen at 2025-06-06 7:00 UTC.

Clarification on the release of Order Amend Keep Priority and STP Decrement:

Notice: The changes in this section will be gradually rolled out, and will take a week to complete.

Notice: The changes in this section will be gradually rolled out, and will take a week to complete.

Notice: The following changes will occur during April 21, 2025.

The following changes will occur at April 24, 2025, 07:00 UTC:

The system now supports microseconds in all related time and/or timestamp fields. Microsecond support is opt-in, by default the requests and responses still use milliseconds. Examples in documentation are also using milliseconds for the foreseeable future.

Notice: The changes below will be rolled out starting at 2024-12-12 and may take approximately a week to complete.

The following changes will occur between 2024-12-16 to 2024-12-20:

REST and WebSocket API:

Changes to Exchange Information (i.e. GET /api/v3/exchangeInfo from REST and exchangeInfo for WebSocket API).

Notice: The changes below are being rolled out gradually, and may take approximately a week to complete.

This will be available by June 6, 11:59 UTC.

The following changes have been postponed to take effect on April 25, 05:00 UTC

Notice: The changes below are being rolled out gradually, and will take approximately a week to complete.

The following will take effect approximately a week after the release date:

This will take effect on March 5, 2024.

Simple Binary Encoding (SBE) will be added to the live exchange, both for the Rest API and WebSocket API.

For more information on SBE, please refer to the FAQ

The SPOT WebSocket API can now support SBE on SPOT Testnet.

The SBE schema has been updated with WebSocket API metadata without incrementing either schemaId or version.

Users using SBE only on the REST API may continue to use the SBE schema with git commit hash 128b94b2591944a536ae427626b795000100cf1d or update to the newly-published SBE schema.

Users who want to use SBE on the WebSocket API must use the newly-published SBE schema.

The FAQ for SBE has been updated.

Simple Binary Encoding (SBE) has been added to SPOT Testnet.

This will be added to the live exchange at a later date.

For more information on what SBE is, please refer to the FAQ

Notice: The changes below are being rolled out gradually, and will take approximately a week to complete.

The following will take effect approximately a week after the release date:

Effective on 2023-10-19 00:00 UTC

The following changes will be effective from 2023-08-25 at UTC 00:00.

Please refer to the table for more details:

Smart Order Routing (SOR) has been added to the APIs. For more information please refer to our FAQ. Please wait for future announcements on when the feature will be enabled.

Notice: The change below are being rolled out, and will take approximately a week to complete.

The following changes will take effect approximately a week from the release date::

Notice: The change below are being rolled out, and will take approximately a week to complete.

Notice: All changes are being rolled out gradually to all our servers, and may take a week to complete.

The following changes will take effect approximately a week from the release date, but the rest of the documentation has been updated to reflect the future changes:

Changes to Websocket Limits

The WS-API and Websocket Stream now only allows 300 connections requests every 5 minutes.

This limit is per IP address.

Please be careful when trying to open multiple connections or reconnecting to the Websocket API.

As per the announcement, Self Trade Prevention will be enabled at 2023-01-26 08:00 UTC.

Please refer to GET /api/v3/exchangeInfo from the Rest API or exchangeInfo from the Websocket API on the default and allowed modes.

New API cluster has been added. Note that all endpoints are functionally equal, but may vary in performance.

ACTUAL RELEASE DATE TBD

New Feature: Self-Trade Prevention (aka STP) will be added to the system at a later date. This will prevent orders from matching with orders from the same account, or accounts under the same tradeGroupId.

Please refer to GET /api/v3/exchangeInfo from the Rest API or exchangeInfo from the Websocket API on the status.

Additional details on the functionality of STP is explained in the STP FAQ document.

WEBSOCKET API WILL BE AVAILABLE ON THE LIVE EXCHANGE AT A LATER DATE.

Some error messages on error code -1003 have changed.

Notice: These changes are being rolled out gradually to all our servers, and will take approximately a week to complete.

Fixed a bug where symbol + orderId combination would return all trades even if the number of trades went beyond the 500 default limit.

Previous behavior: The API would send specific error messages depending on the combination of parameters sent. E.g:

New behavior: If the combinations of optional parameters to the endpoint were not supported, then the endpoint will respond with the generic error:

Added a new combination of supported parameters: symbol + orderId + fromId.

The following combinations of parameters were previously supported but no longer accepted, as these combinations were only taking fromId into consideration, ignoring startTime and endTime:

Thus, these are the supported combinations of parameters:

Note: These new fields will appear approximately a week from the release date.

Scheduled changes to the removal of !bookTicker around November 2022.

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

Changes to GET /api/v3/ticker

Note: The update is being rolled out over the next few days, so these changes may not be visible right away.

Changes to Order Book Depth Levels

What does this affect?

Updates to MAX_POSITION

Note: The changes are being rolled out during the next few days, so these will not appear right away.

On April 28, 2021 00:00 UTC the weights to the following endpoints will be adjusted:

New API clusters have been added in order to improve performance.

Users can access any of the following API clusters, in addition to api.binance.com

If there are any performance issues with accessing api.binance.com please try any of the following instead:

This filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

BUY orders will be rejected if the account's position is greater than the maximum position allowed.

Deprecation of v1 endpoints:

By end of Q1 2020, the following endpoints will be removed from the API. The documentation has been updated to use the v3 versions of these endpoints.

These endpoints however, will NOT be migrated to v3. Please use the following endpoints instead moving forward.

Changes toexecutionReport event

balanceUpdate event type added

In Q4 2017, the following endpoints were deprecated and removed from the API documentation. They have been permanently removed from the API as of this version. We apologize for the omission from the original changelog:

Streams, endpoints, parameters, payloads, etc. described in the documents in this repository are considered official and supported. The use of any other streams, endpoints, parameters, or payloads, etc. is not supported; use them at your own risk and with no guarantees.

New order type: OCO ("One Cancels the Other")

An OCO has 2 orders: (also known as legs in financial terms)

Quantity Restrictions:

recvWindow cannot exceed 60000.

New intervalLetter values for headers:

New Headers X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter) will give your current used request weight for the (intervalNum)(intervalLetter) rate limiter. For example, if there is a one minute request rate weight limiter set, you will get a X-MBX-USED-WEIGHT-1M header in the response. The legacy header X-MBX-USED-WEIGHT will still be returned and will represent the current used weight for the one minute request rate weight limit.

New Header X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)that is updated on any valid order placement and tracks your current order count for the interval; rejected/unsuccessful orders are not guaranteed to have X-MBX-ORDER-COUNT-** headers in the response.

GET api/v1/depth now supports limit 5000 and 10000; weights are 50 and 100 respectively.

GET api/v1/exchangeInfo has a new parameter ocoAllowed.

(qty * price) of all trades / sum of qty of all trades over previous 5 minutes.

If there is no trade in the last 5 minutes, it takes the first trade that happened outside of the 5min window. For example if the last trade was 20 minutes ago, that trade's price is the 5 min average.

If there is no trade on the symbol, there is no average price and market orders cannot be placed. On a new symbol with applyToMarket enabled on the MIN_NOTIONAL filter, market orders cannot be placed until there is at least 1 trade.

The current average price can be checked here: https://api.binance.com/api/v3/avgPrice?symbol=<symbol> For example: https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT

**Examples:**

Example 1 (json):
```json
{"code": -1169, "msg": "Invalid tag number."}
```

Example 2 (json):
```json
{"code": -1177, "msg": "Tag specified without a value."}
```

Example 3 (json):
```json
{"code": -1102, "msg": "Field value was empty or malformed."}
```

Example 4 (json):
```json
{    "code": -2013,    "msg": "Order does not exist."}
```

---

## Trading endpoints

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints

**Contents:**
- Trading endpoints
  - New order (TRADE)​
  - Test new order (TRADE)​
  - Cancel order (TRADE)​
  - Cancel All Open Orders on a Symbol (TRADE)​
  - Cancel an Existing Order and Send a New Order (TRADE)​
  - Order Amend Keep Priority (TRADE)​
  - Order lists​
    - New OCO - Deprecated (TRADE)​
    - New Order list - OCO (TRADE)​

This adds 1 order to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Unfilled Order Count: 1

Some additional mandatory parameters based on order type:

Notes on using parameters for Pegged Orders:

Any LIMIT or LIMIT_MAKER type order can be made an iceberg order by sending an icebergQty.

Any order with an icebergQty MUST have timeInForce set to GTC.

For STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT_LIMIT and TAKE_PROFIT orders, trailingDelta can be combined with stopPrice.

MARKET orders using quoteOrderQty will not break LOT_SIZE filter rules; the order will execute a quantity that will have the notional value as close as possible to quoteOrderQty. Trigger order price rules against market price for both MARKET and LIMIT versions:

Price above market price: STOP_LOSS BUY, TAKE_PROFIT SELL

Price below market price: STOP_LOSS SELL, TAKE_PROFIT BUY

Data Source: Matching Engine

Conditional fields in Order Responses

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to order lists.

The fields are listed below:

Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.

In addition to all parameters accepted by POST /api/v3/order, the following optional parameters are also accepted:

Without computeCommissionRates

With computeCommissionRates

Cancel an active order.

Data Source: Matching Engine

Regarding cancelRestrictions

Cancels all active orders on a symbol. This includes orders that are part of an order list.

Data Source: Matching Engine

Cancels an existing order and places a new order on the same symbol.

Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the unfilled order count by 1.

Unfilled Order Count: 1

Similar to POST /api/v3/order, additional mandatory parameters are determined by type.

Response format varies depending on whether the processing of the message succeeded, partially succeeded, or failed.

Data Source: Matching Engine

Response SUCCESS and account has not exceeded the unfilled order count:

Response when Cancel Order Fails with STOP_ON FAILURE and account has not exceeded their unfilled order count:

Response when Cancel Order Succeeds but New Order Placement Fails and account has not exceeded their unfilled order count:

Response when Cancel Order fails with ALLOW_FAILURE and account has not exceeded their unfilled order count:

Response when both Cancel Order and New Order Placement fail using cancelReplaceMode=ALLOW_FAILURE and account has not exceeded their unfilled order count:

Response when using orderRateLimitExceededMode=DO_NOTHING and account's unfilled order count has been exceeded:

Response when using orderRateLimitExceededMode=CANCEL_ONLY and account's unfilled order count has been exceeded:

Reduce the quantity of an existing open order.

This adds 0 orders to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Read Order Amend Keep Priority FAQ to learn more.

Unfilled Order Count: 0

Data Source: Matching Engine

Response: Response for a single order:

Response for an order that is part of an Order list:

Note: The payloads above do not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Unfilled Order Count: 2

Data Source: Matching Engine

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

Unfilled Order Count: 2

Data Source: Matching Engine

Response format for orderReports is selected using the newOrderRespType parameter. The following example is for the RESULT response type. See POST /api/v3/order for more examples.

Unfilled Order Count: 2

Mandatory parameters based on pendingType or workingType

Depending on the pendingType or workingType, some optional parameters will become mandatory.

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Unfilled Order Count: 3

Mandatory parameters based on pendingAboveType, pendingBelowType or workingType

Depending on the pendingAboveType/pendingBelowType or workingType, some optional parameters will become mandatory.

Note: The payload above does not show all fields that can appear. Please refer to Conditional fields in Order Responses.

Cancel an entire Order list

Data Source: Matching Engine

Places an order using smart order routing (SOR).

This adds 1 order to the EXCHANGE_MAX_ORDERS filter and the MAX_NUM_ORDERS filter.

Read SOR FAQ to learn more.

Unfilled Order Count: 1

Note: POST /api/v3/sor/order only supports LIMIT and MARKET orders. quoteOrderQty is not supported.

Data Source: Matching Engine

Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new order but does not send it into the matching engine.

In addition to all parameters accepted by POST /api/v3/sor/order, the following optional parameters are also accepted:

Without computeCommissionRates

With computeCommissionRates

**Examples:**

Example 1 (text):
```text
POST /api/v3/order
```

Example 2 (javascript):
```javascript
{  "symbol": "BTCUSDT",  "orderId": 28,  "orderListId": -1, // Unless it's part of an order list, value will be -1  "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  "transactTime": 1507725176595}
```

Example 3 (javascript):
```javascript
{  "symbol": "BTCUSDT",  "orderId": 28,  "orderListId": -1, // Unless it's part of an order list, value will be -1  "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  "transactTime": 1507725176595,  "price": "0.00000000",  "origQty": "10.00000000",  "executedQty": "10.00000000",  "origQuoteOrderQty": "0.000000",  "cummulativeQuoteQty": "10.00000000",  "status": "FILLED",  "timeInForce": "GTC",  "type": "MARKET",  "side": "SELL",  "workingTime": 1507725176595,  "selfTradePreventionMode": "NONE"}
```

Example 4 (javascript):
```javascript
{  "symbol": "BTCUSDT",  "orderId": 28,  "orderListId": -1, // Unless it's part of an order list, value will be -1  "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  "transactTime": 1507725176595,  "price": "0.00000000",  "origQty": "10.00000000",  "executedQty": "10.00000000",  "origQuoteOrderQty": "0.000000",  "cummulativeQuoteQty": "10.00000000",  "status": "FILLED",  "timeInForce": "GTC",  "type": "MARKET",  "side": "SELL",  "workingTime": 1507725176595,  "selfTradePreventionMode": "NONE",  "fills": [    {      "price": "4000.00000000",      "qty": "1.00000000",      "commission": "4.00000000",      "commissionAsset": "USDT",      "tradeId": 56    },    {      "price": "3999.00000000",      "qty": "5.00000000",      "commission": "19.99500000",      "commissionAsset": "USDT",      "tradeId": 57    },    {      "price": "3998.00000000",      "qty": "2.00000000",      "commission": "7.99600000",      "commissionAsset": "USDT",      "tradeId": 58    },    {      "price": "3997.00000000",      "qty": "1.00000000",      "commission": "3.99700000",      "commissionAsset": "USDT",      "tradeId": 59    },    {      "price": "3995.00000000",      "qty": "1.00000000",      "commission": "3.99500000",      "commissionAsset": "USDT",      "tradeId": 60    }  ]}
```

---

## Commission Rates

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/commission_faq

**Contents:**
- Commission Rates
  - What are Commission Rates?​
  - What are the different types of rates?​
  - How do I know what the commission rates are?​
  - What is the difference between the response sending a test order with computeCommissionRates vs the response from querying commission rates?​
  - How is the commission calculated?​

These are the rates that determine the commission to be paid on trades when your order fills for any amount.

Standard commission rate may be reduced, depending on promotions for specific trading pairs, applicable discounts, etc.

You can find them using the following requests:

REST API: GET /api/v3/account/commission

WebSocket API: account.commission

You can also find out the commission rates to a trade from an order using the test order requests with computeCommissionRates.

A test order with computeCommissionRates returns detailed commission rates for that specific order:

Note: It does not show buyer/seller commissions separately, as these are already taken into account based on the order side.

In contrast, querying commission rates returns your current commission rates for the symbol on your account.

Using an example commission configuration:

If you placed an order with the following parameters which took immediately and fully filled in a single trade:

Since you sold BTC for USDT, the commission will be paid either in USDT or BNB.

When standard commission is calculated, the received amount is multiplied with the sum of the rates.

Since this order is on the SELL side, the received amount is the notional value. (For orders on the BUY side, the received amount would be quantity.) The order type was MARKET, making this the taker order for the trade.

Tax commission (if applicable) is calculated similarly:

Special commission (if applicable) is calculated as:

If not paying in BNB, the total commission are summed up and deducted from your received amount of USDT.

Since enabledforAccount and enabledForSymbol under discount is set to true, this means the commission will be paid in BNB assuming you have a sufficient balance.

If paying with BNB, then the standard commission will be reduced based on the discount.

First the standard commission and tax commission will be converted into BNB based on the exchange rate. For this example, assume that 1 BNB = 260 USDT.

Note that the discount does not apply to tax commissions or special commissions.

If you do not have enough BNB to pay the discounted commission, the full commission will be taken out of your received amount of USDT instead.

**Examples:**

Example 1 (json):
```json
{  "standardCommissionForOrder": {    "maker": "0.00000050",    "taker": "0.00000060"  },  "specialCommissionForOrder": {    "maker": "0.05000000",    "taker": "0.06000000"  },  "taxCommissionForOrder": {    "maker": "0.00000228",    "taker": "0.00000230"  },  "discount": {    "enabledForAccount": true,    "enabledForSymbol": true,    "discountAsset": "BNB",    "discount": "0.25000000"  }}
```

Example 2 (json):
```json
{  "symbol": "BTCUSDT",  "standardCommission": {    "maker": "0.00000040",    "taker": "0.00000050",    "buyer": "0.00000010",    "seller": "0.00000010"  },  "specialCommission": {    "maker": "0.04000000",    "taker": "0.05000000",    "buyer": "0.01000000",    "seller": "0.01000000"  },  "taxCommission": {    "maker": "0.00000128",    "taker": "0.00000130",    "buyer": "0.00000100",    "seller": "0.00000100"  },  "discount": {    "enabledForAccount": true,    "enabledForSymbol": true,    "discountAsset": "BNB",    "discount": "0.25000000"  }}
```

Example 3 (json):
```json
{  "symbol": "BTCUSDT",  "standardCommission": {    "maker": "0.00000010",    "taker": "0.00000020",    "buyer": "0.00000030",    "seller": "0.00000040"  },  "specialCommission": {    "maker": "0.01000000",    "taker": "0.02000000",    "buyer": "0.03000000",    "seller": "0.04000000"  },  "taxCommission": {    "maker": "0.00000112",    "taker": "0.00000114",    "buyer": "0.00000118",    "seller": "0.00000116"  },  "discount": {    "enabledForAccount": true,    "enabledForSymbol": true,    "discountAsset": "BNB",    "discount": "0.25000000"  }}
```

Example 4 (text):
```text
Standard Commission = Notional value * (taker + seller)                    = (35000 * 0.49975) * (0.00000020 + 0.00000040)                    = 17491.25000000 * 0.00000060                    = 0.01049475 USDT
```

---

## Spot Trailing Stop order FAQ

**URL:** https://developers.binance.com/docs/binance-spot-api-docs/faqs/trailing-stop-faq

**Contents:**
- Spot Trailing Stop order FAQ
  - What is a trailing stop order?​
  - What are BIPs?​
  - What order types can be trailing stop orders?​
  - How do I place a trailing stop order?​
  - What kind of price changes will trigger my trailing stop order?​
  - How do I pass the TRAILING_DELTA filter?​
  - Trailing Stop Order Scenarios​
    - Scenario A - Trailing Stop Loss Limit Buy Order​
    - Scenario B - Trailing Stop Loss Limit Sell Order​

Trailing stop is a type of contingent order with a dynamic trigger price influenced by price changes in the market. For the SPOT API, the change required to trigger order entry is specified in the trailingDelta parameter, and is defined in BIPS.

Intuitively, trailing stop orders allow unlimited price movement in a direction that is beneficial for the order, and limited movement in a detrimental direction.

Buy orders: low prices are good. Unlimited price decreases are allowed but the order will trigger after a price increase of the supplied delta, relative to the lowest trade price since submission.

Sell orders: high prices are good. Unlimited price increases are allowed but the order will trigger after a price decrease of the supplied delta, relative to the highest trade price since submission.

Basis Points, also known as BIP or BIPS, are used to indicate a percentage change.

BIPS conversion reference:

For example, a STOP_LOSS SELL order with a trailingDelta of 100 is a trailing stop order which will be triggered after a price decrease of 1% from the highest price after placing the order.

Trailing stop orders are supported for contingent orders such as STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT.

OCO orders also support trailing stop orders in the contingent leg. In this scenario if the trailing stop condition is triggered, the limit leg of the OCO order will be canceled.

Trailing stop orders are entered the same way as regular STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, or TAKE_PROFIT_LIMIT orders, but with an additional trailingDelta parameter. This parameter must be within the range of the TRAILING_DELTA filter for that symbol.

Unlike regular contingent orders, the stopPrice parameter is optional for trailing stop orders. If it is provided then the order will only start tracking price changes after the stopPrice condition is met. If the stopPrice parameter is omitted then the order starts tracking price changes from the next trade.

For STOP_LOSS BUY, STOP_LOSS_LIMIT BUY, TAKE_PROFIT SELL, and TAKE_PROFIT_LIMIT SELL orders:

For STOP_LOSS SELL, STOP_LOSS_LIMIT SELL, TAKE_PROFIT BUY, and TAKE_PROFIT_LIMIT BUY orders:

At 12:01:00 there is a trade at a price of 40,000 and a STOP_LOSS_LIMIT order is placed on the BUY side of the exchange. The order has of a stopPrice of 44,000, a trailingDelta of 500 (5%), and a limit price of 45,000.

Between 12:01:00 and 12:02:00 a series of linear trades lead to a decrease in last price, ending at 37,000. This is a price decrease of 7.5% or 750 BIPS, well exceeding the order's trailingDelta. However since the order has not started price tracking, the price movement is ignored and the order remains contingent.

Between 12:02:00 and 12:03:00 a series of linear trades lead to an increase in last price. When a trade is equal to, or surpasses, the stopPrice the order starts tracking price changes immediately; the first trade that meets this condition sets the "lowest price". In this case, the lowest price is 44,000 and if there is a 500 BIPS increase from 44,000 then the order will trigger. The series of linear trades continue to increase the last price, ending at 45,000.

Between 12:03:00 and 12:04:00 a series of linear trades lead to an increase in last price, ending at 46,000. This is an increase of ~454 BIPS from the order's previously noted lowest price, but it's not large enough to trigger the order.

Between 12:04:00 and 12:05:00 a series of linear trades lead to a decrease in last price, ending at 42,000. This is a decrease from the order's previously noted lowest price. If there is a 500 BIPS increase from 42,000 then the order will trigger.

Between 12:05:00 and 12:05:30 a series of linear trades lead to an increase in last price to 44,100. This trade is equal to, or surpasses, the order's requirement of 500 BIPS, as 44,100 = 42,000 * 1.05. This causes the order to trigger and start working against the order book at its limit price of 45,000.

At 12:01:00 there is a trade at a price of 40,000 and a STOP_LOSS_LIMIT order is placed on the SELL side of the exchange. The order has of a stopPrice of 39,000, a trailingDelta of 1000 (10%), and a limit price of 38,000.

Between 12:01:00 and 12:02:00 a series of linear trades lead to an increase in last price, ending at 41,500.

Between 12:02:00 and 12:03:00 a series of linear trades lead to a decrease in last price. When a trade is equal to, or surpasses, the stopPrice the order starts tracking price changes immediately; the first trade that meets this condition sets the "highest price". In this case, the highest price is 39,000 and if there is a 1000 BIPS decrease from 39,000 then the order will trigger.

Between 12:03:00 and 12:04:00 a series of linear trades lead to a decrease in last price, ending at 37,000. This is a decrease of ~512 BIPS from the order's previously noted highest price, but it's not large enough to trigger the order.

Between 12:04:00 and 12:05:00 a series of linear trades lead to an increase in last price, ending at 41,000. This is an increase from the order's previously noted highest price. If there is a 1000 BIPS decrease from 41,000 then the order will trigger.

Between 12:05:00 and 12:05:30 a series of linear trades lead to a decrease in last price to 36,900. This trade is equal to, or surpasses, the order's requirement of 1000 BIPS, as 36,900 = 41,000 * 0.90. This causes the order to trigger and start working against the order book at its limit price of 38,000.

At 12:01:00 there is a trade at a price of 40,000 and a TAKE_PROFIT_LIMIT order is placed on the BUY side of the exchange. The order has of a stopPrice of 38,000, a trailingDelta of 850 (8.5%), and a limit price of 38,500.

Between 12:01:00 and 12:02:00 a series of linear trades lead to an increase in last price, ending at 42,000.

Between 12:02:00 and 12:03:00 a series of linear trades lead to a decrease in last price. When a trade is equal to, or surpasses, the stopPrice the order starts tracking price changes immediately; the first trade that meets this condition sets the "lowest price". In this case, the lowest price is 38,000 and if there is a 850 BIPS increase from 38,000 then the order will trigger.

The series of linear trades continues to decrease the last price, ending at 37,000. If there is a 850 BIPS increase from 37,000 then the order will trigger.

Between 12:03:00 and 12:04:00 a series of linear trades lead to an increase in last price, ending at 39,000. This is an increase of ~540 BIPS from the order's previously noted lowest price, but it's not large enough to trigger the order.

Between 12:04:00 and 12:05:00 a series of linear trades lead to a decrease in last price, ending at 38,000. It does not surpass the order's previously noted lowest price, resulting in no change to the order's trigger price.

Between 12:05:00 and 12:05:30 a series of linear trades lead to an increase in last price to 40,145. This trade is equal to, or surpasses, the order's requirement of 850 BIPS, as 40,145 = 37,000 * 1.085. This causes the order to trigger and start working against the order book at its limit price of 38,500.

At 12:01:00 there is a trade at a price of 40,000 and a TAKE_PROFIT_LIMIT order is placed on the SELL side of the exchange. The order has of a stopPrice of 42,000, a trailingDelta of 750 (7.5%), and a limit price of 41,000.

Between 12:01:00 and 12:02:00 a series of linear trades lead to an increase in last price, ending at 41,500.

Between 12:02:00 and 12:03:00 a series of linear trades lead to a decrease in last price, ending at 39,000.

Between 12:03:00 and 12:04:00 a series of linear trades lead to an increase in last price. When a trade is equal to, or surpasses, the stopPrice the order starts tracking price changes immediately; the first trade that meets this condition sets the "highest price". In this case, the highest price is 42,000 and if there is a 750 BIPS decrease from 42,000 then the order will trigger.

The series of linear trades continues to increase the last price, ending at 45,000. If there is a 750 BIPS decrease from 45,000 then the order will trigger.

Between 12:04:00 and 12:05:00 a series of linear trades lead to a decrease in last price, ending at 44,000. This is a decrease of ~222 BIPS from the order's previously noted highest price, but it's not large enough to trigger the order.

Between 12:05:00 and 12:06:00 a series of linear trades lead to an increase in last price, ending at 46,500. This is an increase from the order's previously noted highest price. If there is a 750 BIPS decrease from 46,500 then the order will trigger.

Between 12:06:00 and 12:06:50 a series of linear trades lead to a decrease in last price to 43,012.5. This trade is equal to, or surpasses, the order's requirement of 750 BIPS, as 43,012.5 = 46,500 * 0.925. This causes the order to trigger and start working against the order book at its limit price of 41,000.

At 12:01:00 there is a trade at a price of 40,000 and a STOP_LOSS_LIMIT order is placed on the SELL side of the exchange. The order has a trailingDelta of 700 (7%), a limit price of 39,000 and no stopPrice. The order starts tracking price changes once placed. If there is a 700 BIPS decrease from 40,000 then the order will trigger.

Between 12:01:00 and 12:02:00 a series of linear trades lead to an increase in last price, ending at 42,000. This is an increase from the order's previously noted highest price. If there is a 700 BIPS decrease from 42,000 then the order will trigger.

Between 12:02:00 and 12:03:00 a series of linear trades lead to a decrease in last price, ending at 39,500. This is a decrease of ~595 BIPS from the order's previously noted highest price, but it's not large enough to trigger the order.

Between 12:03:00 and 12:04:00 a series of linear trades lead to an increase in last price, ending at 45,500. This is an increase from the order's previously noted highest price. If there is a 700 BIPS decrease from 45,500 then the order will trigger.

Between 12:04:00 and 12:04:45 a series of linear trades lead to a decrease in last price to 42,315. This trade is equal to, or surpasses, the order's requirement of 700 BIPS, as 42,315 = 45,500 * 0.93. This causes the order to trigger and start working against the order book at its limit price of 39,000.

Assuming a last price of 40,000.

Placing a trailing stop STOP_LOSS_LIMIT BUY order, with a price of 42,000.0 and a trailing stop of 5%.

Placing a trailing stop STOP_LOSS_LIMIT SELL order, with a price of 37,500.0 and a trailing stop of 2.5%.

Placing a trailing stop TAKE_PROFIT_LIMIT BUY order, with a price of 38,000.0 and a trailing stop of 5%.

Placing a trailing stop TAKE_PROFIT_LIMIT SELL order, with a price of 41,500.0 and a trailing stop of 1.75%.

**Examples:**

Example 1 (bash):
```bash
# Excluding stop pricePOST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=STOP_LOSS_LIMIT&timeInForce=GTC&quantity=0.01&price=42000&trailingDelta=500&timestamp=<timestamp>&signature=<signature>'# Including stop price of 43,000POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=STOP_LOSS_LIMIT&timeInForce=GTC&quantity=0.01&price=42000&stopPrice=43000&trailingDelta=500&timestamp=<timestamp>&signature=<signature>'
```

Example 2 (bash):
```bash
# Excluding stop pricePOST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=STOP_LOSS_LIMIT&timeInForce=GTC&quantity=0.01&price=37500&trailingDelta=250&timestamp=<timestamp>&signature=<signature>'# Including stop price of 39,000POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=STOP_LOSS_LIMIT&timeInForce=GTC&quantity=0.01&price=37500&stopPrice=39000&trailingDelta=250&timestamp=<timestamp>&signature=<signature>'
```

Example 3 (bash):
```bash
# Excluding stop pricePOST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=TAKE_PROFIT_LIMIT&timeInForce=GTC&quantity=0.01&price=38000&trailingDelta=500&timestamp=<timestamp>&signature=<signature>'# Including stop price of 36,000POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=TAKE_PROFIT_LIMIT&timeInForce=GTC&quantity=0.01&price=38000&stopPrice=36000&trailingDelta=500&timestamp=<timestamp>&signature=<signature>'
```

Example 4 (bash):
```bash
# Excluding stop pricePOST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=TAKE_PROFIT_LIMIT&timeInForce=GTC&quantity=0.01&price=41500&trailingDelta=175&timestamp=<timestamp>&signature=<signature>'# Including stop price of 42,500POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=TAKE_PROFIT_LIMIT&timeInForce=GTC&quantity=0.01&price=41500&stopPrice=42500&trailingDelta=175&timestamp=<timestamp>&signature=<signature>'
```

---

## CHANGELOG for Binance's API

**URL:** https://developers.binance.com/docs/binance-spot-api-docs

**Contents:**
- CHANGELOG for Binance's API
  - 2025-10-28​
  - 2025-10-24​
    - SBE​
    - REST and WebSocket API​
  - 2025-10-21​
  - 2025-10-08​
    - FIX API​
  - 2025-09-29​
  - 2025-09-18​

Last Updated: 2025-10-28

Notice: The following changes will be deployed on 2025-10-28, starting at 04:00 UTC and may take several hours to complete:

Following the announcement from 2025-04-07, all documentation related with listenKey for use on wss://stream.binance.com has been removed.

Please refer to the list of requests and methods below for more information.

The features will remain available until a future retirement announcement is made.

REST and WebSocket API:

Notice: The following changes will be deployed on 2025-09-29, starting at 10:00 UTC and may take several hours to complete.

Notice: The changes in this section will be gradually rolled out, and will take approximately up to two weeks to complete.

The following changes will be available on 2025-08-27 starting at 07:00 UTC:

The following changes will be available on 2025-08-28 starting at 07:00 UTC:

REST and WebSocket API:

Notice: The following changes will happen at 2025-06-06 7:00 UTC.

Clarification on the release of Order Amend Keep Priority and STP Decrement:

Notice: The changes in this section will be gradually rolled out, and will take a week to complete.

Notice: The changes in this section will be gradually rolled out, and will take a week to complete.

Notice: The following changes will occur during April 21, 2025.

The following changes will occur at April 24, 2025, 07:00 UTC:

The system now supports microseconds in all related time and/or timestamp fields. Microsecond support is opt-in, by default the requests and responses still use milliseconds. Examples in documentation are also using milliseconds for the foreseeable future.

Notice: The changes below will be rolled out starting at 2024-12-12 and may take approximately a week to complete.

The following changes will occur between 2024-12-16 to 2024-12-20:

REST and WebSocket API:

Changes to Exchange Information (i.e. GET /api/v3/exchangeInfo from REST and exchangeInfo for WebSocket API).

Notice: The changes below are being rolled out gradually, and may take approximately a week to complete.

This will be available by June 6, 11:59 UTC.

The following changes have been postponed to take effect on April 25, 05:00 UTC

Notice: The changes below are being rolled out gradually, and will take approximately a week to complete.

The following will take effect approximately a week after the release date:

This will take effect on March 5, 2024.

Simple Binary Encoding (SBE) will be added to the live exchange, both for the Rest API and WebSocket API.

For more information on SBE, please refer to the FAQ

The SPOT WebSocket API can now support SBE on SPOT Testnet.

The SBE schema has been updated with WebSocket API metadata without incrementing either schemaId or version.

Users using SBE only on the REST API may continue to use the SBE schema with git commit hash 128b94b2591944a536ae427626b795000100cf1d or update to the newly-published SBE schema.

Users who want to use SBE on the WebSocket API must use the newly-published SBE schema.

The FAQ for SBE has been updated.

Simple Binary Encoding (SBE) has been added to SPOT Testnet.

This will be added to the live exchange at a later date.

For more information on what SBE is, please refer to the FAQ

Notice: The changes below are being rolled out gradually, and will take approximately a week to complete.

The following will take effect approximately a week after the release date:

Effective on 2023-10-19 00:00 UTC

The following changes will be effective from 2023-08-25 at UTC 00:00.

Please refer to the table for more details:

Smart Order Routing (SOR) has been added to the APIs. For more information please refer to our FAQ. Please wait for future announcements on when the feature will be enabled.

Notice: The change below are being rolled out, and will take approximately a week to complete.

The following changes will take effect approximately a week from the release date::

Notice: The change below are being rolled out, and will take approximately a week to complete.

Notice: All changes are being rolled out gradually to all our servers, and may take a week to complete.

The following changes will take effect approximately a week from the release date, but the rest of the documentation has been updated to reflect the future changes:

Changes to Websocket Limits

The WS-API and Websocket Stream now only allows 300 connections requests every 5 minutes.

This limit is per IP address.

Please be careful when trying to open multiple connections or reconnecting to the Websocket API.

As per the announcement, Self Trade Prevention will be enabled at 2023-01-26 08:00 UTC.

Please refer to GET /api/v3/exchangeInfo from the Rest API or exchangeInfo from the Websocket API on the default and allowed modes.

New API cluster has been added. Note that all endpoints are functionally equal, but may vary in performance.

ACTUAL RELEASE DATE TBD

New Feature: Self-Trade Prevention (aka STP) will be added to the system at a later date. This will prevent orders from matching with orders from the same account, or accounts under the same tradeGroupId.

Please refer to GET /api/v3/exchangeInfo from the Rest API or exchangeInfo from the Websocket API on the status.

Additional details on the functionality of STP is explained in the STP FAQ document.

WEBSOCKET API WILL BE AVAILABLE ON THE LIVE EXCHANGE AT A LATER DATE.

Some error messages on error code -1003 have changed.

Notice: These changes are being rolled out gradually to all our servers, and will take approximately a week to complete.

Fixed a bug where symbol + orderId combination would return all trades even if the number of trades went beyond the 500 default limit.

Previous behavior: The API would send specific error messages depending on the combination of parameters sent. E.g:

New behavior: If the combinations of optional parameters to the endpoint were not supported, then the endpoint will respond with the generic error:

Added a new combination of supported parameters: symbol + orderId + fromId.

The following combinations of parameters were previously supported but no longer accepted, as these combinations were only taking fromId into consideration, ignoring startTime and endTime:

Thus, these are the supported combinations of parameters:

Note: These new fields will appear approximately a week from the release date.

Scheduled changes to the removal of !bookTicker around November 2022.

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

Changes to GET /api/v3/ticker

Note: The update is being rolled out over the next few days, so these changes may not be visible right away.

Changes to Order Book Depth Levels

What does this affect?

Updates to MAX_POSITION

Note: The changes are being rolled out during the next few days, so these will not appear right away.

On April 28, 2021 00:00 UTC the weights to the following endpoints will be adjusted:

New API clusters have been added in order to improve performance.

Users can access any of the following API clusters, in addition to api.binance.com

If there are any performance issues with accessing api.binance.com please try any of the following instead:

This filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

BUY orders will be rejected if the account's position is greater than the maximum position allowed.

Deprecation of v1 endpoints:

By end of Q1 2020, the following endpoints will be removed from the API. The documentation has been updated to use the v3 versions of these endpoints.

These endpoints however, will NOT be migrated to v3. Please use the following endpoints instead moving forward.

Changes toexecutionReport event

balanceUpdate event type added

In Q4 2017, the following endpoints were deprecated and removed from the API documentation. They have been permanently removed from the API as of this version. We apologize for the omission from the original changelog:

Streams, endpoints, parameters, payloads, etc. described in the documents in this repository are considered official and supported. The use of any other streams, endpoints, parameters, or payloads, etc. is not supported; use them at your own risk and with no guarantees.

New order type: OCO ("One Cancels the Other")

An OCO has 2 orders: (also known as legs in financial terms)

Quantity Restrictions:

recvWindow cannot exceed 60000.

New intervalLetter values for headers:

New Headers X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter) will give your current used request weight for the (intervalNum)(intervalLetter) rate limiter. For example, if there is a one minute request rate weight limiter set, you will get a X-MBX-USED-WEIGHT-1M header in the response. The legacy header X-MBX-USED-WEIGHT will still be returned and will represent the current used weight for the one minute request rate weight limit.

New Header X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)that is updated on any valid order placement and tracks your current order count for the interval; rejected/unsuccessful orders are not guaranteed to have X-MBX-ORDER-COUNT-** headers in the response.

GET api/v1/depth now supports limit 5000 and 10000; weights are 50 and 100 respectively.

GET api/v1/exchangeInfo has a new parameter ocoAllowed.

(qty * price) of all trades / sum of qty of all trades over previous 5 minutes.

If there is no trade in the last 5 minutes, it takes the first trade that happened outside of the 5min window. For example if the last trade was 20 minutes ago, that trade's price is the 5 min average.

If there is no trade on the symbol, there is no average price and market orders cannot be placed. On a new symbol with applyToMarket enabled on the MIN_NOTIONAL filter, market orders cannot be placed until there is at least 1 trade.

The current average price can be checked here: https://api.binance.com/api/v3/avgPrice?symbol=<symbol> For example: https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT

**Examples:**

Example 1 (json):
```json
{"code": -1169, "msg": "Invalid tag number."}
```

Example 2 (json):
```json
{"code": -1177, "msg": "Tag specified without a value."}
```

Example 3 (json):
```json
{"code": -1102, "msg": "Field value was empty or malformed."}
```

Example 4 (json):
```json
{    "code": -2013,    "msg": "Order does not exist."}
```

---
