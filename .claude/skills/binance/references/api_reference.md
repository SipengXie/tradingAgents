# Binance - Api Reference

**Pages:** 3

---

## Change Log

**URL:** https://developers.binance.com/docs/derivatives

**Contents:**
- Change Log
- 2025-10-21​
- 2025-10-20​
- 2025-10-14​
- 2025-10-09​
- 2025-08-11​
- 2025-07-25​
- 2025-07-02​
- 2025-04-23​
- 2025-04-15​

Effective 2025-10-23, the priceMatch enum values OPPONENT_10 and OPPONENT_20 are temporarily removed from place/amend flows, other enums are not impacted. Affected endpoints:

USDT-M Futures (/fapi)

COIN-M Futures (/dapi)

Portfolio Margin (/papi)

Portfolio Margin and Portfolio Margin Pro

USDⓈ-M Futures & COIN-M Futures

The following endpoints will be updated at 2024-01-14:

Changes to the request parameter limit:

Portfolio Margin Pro & Portfolio Margin

REST API: Added new endpoint GET /eapi/v1/blockTrades to get recent block trades

Websocket Market Streams: Add field X in streams <symbol>@trade and <underlyingAsset>@trade to show trade type

USDⓈ-M Futures & COIN-M Futures

USDⓈ-M Futures & COIN-M Futures

Portfolio Margin Pro(Release date 2024-10-18)

Self-Trade Prevention:

Self-Trade Prevention (aka STP) is added to the system. This prevents orders from matching with orders from the same account, or accounts under the same tradeGroupId(currently only support same account). For more detail, please check FAQ

User can set selfTradePreventionMode when placing new orders. All symbols support the following STP mode:

WEBSOCKET User Data Stream:

Coin margin future supports order price match function. This feature allows users' LIMIT/STOP/TAKE_PROFIT orders to be placed without entering a price. The price match function will automatically determine the order price in real-time based on the price match mode and the order book.

The following priceMatch modes are supported on order level:

Add optional parameter priceMatch in the endpoints below to set order's priceMatch mode:

Add new field priceMatch in response of the endpoints below to show order's priceMatch mode:

WEBSOCKET User Data Stream:

Binance will update the following endpoints, estimated to be in force on 2024-10-17 03:00 (UTC). After 2024-10-17 03:00 (UTC), the endpoints will support querying futures trade histories that are not older than one year:

Binance will update the following endpoints, estimated to be in force on 2024-10-16 03:00 (UTC). After 2024-10-16 03:00 (UTC), the endpoint will support querying future histories that are not older than 30 days:

The most recent 7-days data is returned by default when requesting the following endpoints. The query time period for these endpoints must be less than 7 days:

The following endpoints will be adjusted to keep only recent three month data:

Update endpoint for Portfolio Margin/Trade(Release date 2024-09-06):

Add new field priceMatch in response of the endpoints below to show order's priceMatch:

The following endpoints IP weight limit will be adjusted from 2024-09-03:

The following WebSocket User Data Requests will be deprecated from 2024-09-03

Please refer to annoucement for api replacement

GET /dapi/v1/pmExchangeInfo will be deprecated on August 6,2024 due to removing notionalLimit restriction.

New Endpoints to Query Account Information:

New Endpoints to Query Trade Information:

REST API & Websocket API

REST API & Websocket API

USDⓈ-M Futures/ COIN-M Futures / Portfolio Margin

Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：

Self-Trade Prevention(Released):

Self-Trade Prevention (aka STP) will be added to the system. This will prevent orders from matching with orders from the same account, or accounts under the same tradeGroupId. For more detail, please check FAQ

User can set selfTradePreventionMode when placing new orders. All symbols support the following STP mode:

New order status EXPIRED_IN_MATCH - This means that the order expired due to STP being triggered.

GET /papi/v1/um/account: Add new field tradeGroupId in response to show user's tradeGroupId

Add optional parameter selfTradePreventionMode in the endpoints below to set order's STP mode:

Add new field selfTradePreventionMode in response of the endpoints below to show order's STP mode:

POST /papi/v1/um/order

POST/papi/v1/um/conditional/order

GET /papi/v1/um/order

GET /papi/v1/um/openOrder

GET /papi/v1/um/openOrders

GET /papi/v1/um/allOrders

GET /papi/v1/um/conditional/openOrder

GET /papi/v1/um/conditional/openOrders

GET /papi/v1/um/conditional/orderHistory

GET /papi/v1/um/conditional/allOrders

DELETE /papi/v1/um/order

DELETE /papi/v1/um/conditional/order

DELETE /papi/v1/margin/order

DELETE /papi/v1/margin/allOpenOrders

DELETE /papi/v1/margin/orderList

GET /papi/v1/margin/order

GET /papi/v1/margin/allOrders

GET /papi/v1/margin/orderList

GET /papi/v1/margin/allOrderList

GET /papi/v1/margin/openOrderList

WEBSOCKET User Data Stream:

Good Till Date TIF(Released)

USDⓈ margin future will support Good To Date TIF. Orders with the TIF set to GTD will be automatically canceled by the goodTillDate time.

Add optional parameter goodTillDate in the endpoints below to set order's goodTillDate :

Add new field goodTillDate in response of the endpoints below to show order's goodTillDate:

WEBSOCKET User Data Stream:

Breakeven Price(Released)

Add new Market Data Endpoints:

Update on GET /fapi/v1/fundingRate:

Binance Option is doing Websocket Service upgrade and the upgrade impacts the following：

Websocket User Data Streams Update:

Update on GET /dapi/v1/ticker/bookTicker:

Update on GET /dapi/v1/account:

Expect 2023-09-07 Release

Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：

Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：

Websocket User Data Stream

Self-Trade Prevention(Release Date TBD):

Self-Trade Prevention (aka STP) will be added to the system. This will prevent orders from matching with orders from the same account, or accounts under the same tradeGroupId. For more detail, please check FAQ

User can set selfTradePreventionMode when placing new orders. All symbols support the following STP mode:

WEBSOCKET User Data Stream:

Websocket Market Streams

It is recommended to use standard HTTP request formats, non-standard request formats will not be supported in fapi, below are some examples for correct code practice:

Escaping (") with '\x22' is no longer supported, please use the standard '%22' instead. It is necessary to URL encode the square brackets [] and the double quotes（"）inside the square brackets.

[\x229151944646313025900\x22]

["9151944646313025900"]

DELETE /fapi/v1/batchOrders?origClientOrderIdList=%5B%229151944646313025900%22%5D

Non-standard nested JSON formats are not supported,

["{\"type\":\"LIMIT\",\"timeInForce\":\"GTC\"}"]

[{"type":"LIMIT","timeInForce":"GTC"}]

POST /fapi/v1/batchOrders?batchOrders=%5B%7B%22type%22%3A%22LIMIT%22%2C%22timeInForce%22%3A%22GTC%22%7D%5D

Using incorrect data type is not supported

["159856286502","159856313662"]

[159856286502,159856313662]

DELETE /fapi/v1/batchOrders?orderIdList=%5B159856286502%2C159856313662%5D

Invalid whitespace characters from the request parameters are not supported

POST symbol=BTCUSDT& price= 40000.0 & signature=2d24a314

POST symbol=BTCUSDT&&price=40000.0&signature=2d24a314

Passing empty values in request parameters is not supported

GET symbol=BTCUSDT&orderId=&signature=2d24a314

GET symbol=BTCUSDT&signature=2d24a314

General Information on Endpoints

The recvWindow check will also be performed when orders reach matching engine. The recvWindow will be checked more precisely on order placing endpoints.

recvWindow Logic Before Release:

recvWindow Logic After Release:

Add new recwWindow check: the order placing requests are valid if recvWindow + timestamp => matching engine timestamp

RELEASE DATE 2023-04-18

The recvWindow check will also be performed when orders reach matching engine. The recvWindow will be checked more precisely on order placing endpoints.

recvWindow Logic Before Release:

recvWindow Logic After Release:

Add new recwWindow check: the order placing requests are valid if recvWindow + timestamp => matching engine timestamp

Referal Rebate Logic Before Release

Referal Rebate Logic After Release

RELEASE DATE 2023-03-22

Order Logic Before Release:

Order Logic After Release:

WEB SOCKET USER DATA STREAM

WEB SOCKET USER DATA STREAM

Note: This change will be effictive on 2022-10-17

REST RATE LIMIT WEIGHT

Endpoint GET /dapi/v1/ticker/bookTicker

2 for a single symbol; 5 when the symbol parameter is omitted

Note: This change will be effictive on 2022-10-17

REST RATE LIMIT WEIGHT

Endpoint GET /fapi/v1/ticker/bookTicker

2 for a single symbol; 5 when the symbol parameter is omitted

REST RATE LIMIT WEIGHT

REST RATE LIMIT WEIGHT

WEB SOCKET USER DATA STREAM

New endpoint GET /fapi/v1/indexPriceKlines to get index price kline/candlestick data.

New endpoint GET /fapi/v1/markPriceKlines to get mark price kline/candlestick data.

REST RATE LIMIT WEIGHT

REST RATE LIMIT WEIGHT

REST RATE LIMIT WEIGHT

WEB SOCKET USER DATA STREAM

REST RATE LIMIT WEIGHT

The regular expression rule for newClientOrderId updated as ^[\.A-Z\:/a-z0-9_-]{1,36}$

The regular expression rule for newClientOrderId updated as ^[\.A-Z\:/a-z0-9_-]{1,36}$

REST RATE LIMIT WEIGHT

Following endpoints will use new weight rule based on the paremeter "LIMIT" in the request:

Following endpoints' weights will be updated to 20:

Following DAPI endpoints will use new weight rule based on the parameter "LIMIT" in the request:

Following DAPI endpoints' weights will be updated to 20:

New field "estimatedSettlePrice" in response to GET /fapi/v1/premiumIndex

New fields in response to GET /fapi/v1/exchangeInfo:

New endpoint GET /fapi/v1/continuousKlines to get continuous contract kline data

WEB SOCKET USER DATA STREAM

Please notice: new streamlined and optimized push rules on event ACCOUNT_UPDATE in USER-DATA-STREAM

When an asset of a user is changed:

When a position or the margin type of a symbol is changed:

In short, the full information of assets and positions should be obtained via the related RESTful endpoints(GET /fapi/v2/account and GET /fapi/v2/positionRisk), and the locally cached asset or position data can be updated via the event ACCOUNT_UPDATE in Websocket USER-DATA-STREAM with the information of changed asset or position.

Please visit here to get examples for helping to understand the upgrade.

COIN MARGINED PERPETUAL FUTURES

New contract type ("contractType") PERPETUAL for coin margined perpetual futures countract.

New fields in the reponse to endpoint GET /dapi/v1/premiumIndex:

New endpoint GET /dapi/v1/fundingRate to get funding rate history of perpetual futures

New fields in the payload of WSS <symbol>@markPrice, <symbol>@markPrice@1s, <pair>@markPrice, and <pair>@markPrice@1s:

WEB SOCKET USER DATA STREAM

New fields in USER DATA STREAM event ORDER_TRADE_UPDATE :

New USER DATA STREAM event MARGIN_CALL.

Please notice: event ACCOUNT_UPDATE in USER-DATA-STREAM will not be pushed without update of account balances or positions.

New endpoint POST /fapi/v1/positionSide/dual to change position mode: Hedge Mode or One-way Mode.

New parameter positionSide in the following endpoints：

New field positionSide in the responses to the following endpoints：

New field ps for "position side"in USER_DATA_STREAM events ACCOUNT_UPDATE and ORDER_TRADE_UPDATE.

New SDK and Code Demonstration on Java

Faster mark price websocket data with 1s updates: <symbol>@markPrice@1s and !markPrice@arr@1s

New endpoints related to isolated position：

New field in response to GET /fapi/v1/positionRisk related to isolated position:

New field in response to GET /fapi/v1/accountrelated to isolated position: isolated

New field in event ACCOUNT_UPDATE:

**Examples:**

Example 1 (javascript):
```javascript
{    "code": -1008,    "msg": "Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again."}
```

Example 2 (javascript):
```javascript
{    "listenKey": "3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg"}
```

Example 3 (javascript):
```javascript
{    "code": -1008,    "msg": "Server is currently overloaded with other requests. Please try again in a few minutes."}
```

Example 4 (text):
```text
DELETE /fapi/v1/batchOrders?origClientOrderIdList=Unsupported:
```

---

## Using OAuth to Access Binance API

**URL:** https://developers.binance.com/docs/

**Contents:**
- Using OAuth to Access Binance API
- 1. Authorization Code Flow​
  - Step 1. Redirect users to request Binance access and set authorization parameters.​
  - Step 2. Binance prompts user for consent​
  - Step 3. Binance redirects back to your application​
  - Step 4. Exchange authorization code for refresh and access tokens​
  - Step 5. Exchange refresh token for access tokens​
  - Step 6. Calling Binance APIs​
- 2. PKCE Flow​
  - Step 1. Redirect users to request Binance access and set authorization parameters.​

Binance APIs utilize the OAuth 2.0 protocol for authentication and authorization. Binance supports common OAuth 2.0 scenarios such as those for web server, single page (browser based), mobile and native applications. This document will guide you through how your application communicates with Binance's OAuth 2.0 server to secure a user's consent for performing an API request on his behalf.

To begin, your application must identify the necessary permissions, or scopes. Visit the Binance Developer Center, sign up for a Binance entity account, and from there, navigate to your console to create an OAuth application and get your own client ID and client secret. For now, Binance Login (Oauth2.0), is exclusively offered to close ecosystem partners. Please reach to our business team for further information.

Depending on your specific application type, you can select one of the two different authorization flows listed here:

⚠️ The carriage returns of the above example are only for readability and should be removed in real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to create the authorization request.

Here is an Example of an authorization URL:

In this step, the user decides whether to grant your application the requested access. At this stage, Binance displays a consent window that shows the name of your application and the Binance API services that it is requesting permission to access with the user's authorization credentials. The user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0 server to redirect back.

If the user approves your application, Binance's OAuth server will redirect back to your redirect_uri with a temporary authorization code parameter.

If you specified a state parameter in step 1, the parameter will be included as well. If you generate a random string or encode the hash of a cookie or another value that captures the client's state, you can validate the response to additionally ensure that the request and response originated in the same browser, providing protection against attacks such as cross-site request forgery.

Example of the redirection:

state is the same as the one in step 1

After your application receives the authorization code, it can exchange the authorization code for an access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

If your access token is expired, you can use refresh_token to get a new access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

After you have a valid access_token, you can make your first API call:

The PKCE extension prevents an attack where the authorization code is intercepted and exchanged for an access token by a malicious client, by providing the authorization server with a way to verify the same client instance that exchanges the authorization code is the same one that initiated the flow. For more details, refer to https://tools.ietf.org/html/rfc7636

⚠️ The carriage returns of the above example are only for readability and should be removed in real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to create the authorization request. You need create and store a new PKCE code_verifier, also will be used in STEP4

Here is an Example of javascript generate code_verifier

Here is an Example of javascript generate code_challenge

Here is an Example of an authorization URL:

In this step, the user decides whether to grant your application the requested access. At this stage, Binance displays a consent window that shows the name of your application and the Binance API services that it is requesting permission to access with the user's authorization credentials. The user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0 server to redirect back.

If the user approves your application, Binance's OAuth server will redirect back to your redirect_uri with a temporary authorization code parameter.

If you specified a state parameter in step 1, the parameter will be included as well. If you generate a random string or encode the hash of a cookie or another value that captures the client's state, you can validate the response to additionally ensure that the request and response originated in the same browser, providing protection against attacks such as cross-site request forgery.

Example of the redirection:

state is the same as the one in step 1

After your application receives the authorization code, it can exchange the authorization code for an access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

If your access token is expired, you can use refresh_token to get a new access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

After you have a valid access_token, you can make your first API call:

**Examples:**

Example 1 (text):
```text
GET https://accounts.binance.com/en/oauth/authorize?    response_type=code&    client_id=YOUR_CLIENT_ID&    redirect_uri=YOUR_REDIRECT_URI&    state=CSRF_TOKEN&    scope=SCOPES
```

Example 2 (text):
```text
GET https://accounts.binance.com/en/oauth/authorize?    response_type=code&    client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&    redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&    state=377f36a4557ab5935b36&    scope=user:openId,create:apikey
```

Example 3 (text):
```text
GET https://domain.com/oauth/callback?    code=cf6941ae8918b6a008f1377f36a4557ab5935b36&    state=377f36a4557ab5935b36
```

Example 4 (text):
```text
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
```

---

## Using OAuth to Access Binance API

**URL:** https://developers.binance.com/docs

**Contents:**
- Using OAuth to Access Binance API
- 1. Authorization Code Flow​
  - Step 1. Redirect users to request Binance access and set authorization parameters.​
  - Step 2. Binance prompts user for consent​
  - Step 3. Binance redirects back to your application​
  - Step 4. Exchange authorization code for refresh and access tokens​
  - Step 5. Exchange refresh token for access tokens​
  - Step 6. Calling Binance APIs​
- 2. PKCE Flow​
  - Step 1. Redirect users to request Binance access and set authorization parameters.​

Binance APIs utilize the OAuth 2.0 protocol for authentication and authorization. Binance supports common OAuth 2.0 scenarios such as those for web server, single page (browser based), mobile and native applications. This document will guide you through how your application communicates with Binance's OAuth 2.0 server to secure a user's consent for performing an API request on his behalf.

To begin, your application must identify the necessary permissions, or scopes. Visit the Binance Developer Center, sign up for a Binance entity account, and from there, navigate to your console to create an OAuth application and get your own client ID and client secret. For now, Binance Login (Oauth2.0), is exclusively offered to close ecosystem partners. Please reach to our business team for further information.

Depending on your specific application type, you can select one of the two different authorization flows listed here:

⚠️ The carriage returns of the above example are only for readability and should be removed in real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to create the authorization request.

Here is an Example of an authorization URL:

In this step, the user decides whether to grant your application the requested access. At this stage, Binance displays a consent window that shows the name of your application and the Binance API services that it is requesting permission to access with the user's authorization credentials. The user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0 server to redirect back.

If the user approves your application, Binance's OAuth server will redirect back to your redirect_uri with a temporary authorization code parameter.

If you specified a state parameter in step 1, the parameter will be included as well. If you generate a random string or encode the hash of a cookie or another value that captures the client's state, you can validate the response to additionally ensure that the request and response originated in the same browser, providing protection against attacks such as cross-site request forgery.

Example of the redirection:

state is the same as the one in step 1

After your application receives the authorization code, it can exchange the authorization code for an access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

If your access token is expired, you can use refresh_token to get a new access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

After you have a valid access_token, you can make your first API call:

The PKCE extension prevents an attack where the authorization code is intercepted and exchanged for an access token by a malicious client, by providing the authorization server with a way to verify the same client instance that exchanges the authorization code is the same one that initiated the flow. For more details, refer to https://tools.ietf.org/html/rfc7636

⚠️ The carriage returns of the above example are only for readability and should be removed in real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to create the authorization request. You need create and store a new PKCE code_verifier, also will be used in STEP4

Here is an Example of javascript generate code_verifier

Here is an Example of javascript generate code_challenge

Here is an Example of an authorization URL:

In this step, the user decides whether to grant your application the requested access. At this stage, Binance displays a consent window that shows the name of your application and the Binance API services that it is requesting permission to access with the user's authorization credentials. The user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0 server to redirect back.

If the user approves your application, Binance's OAuth server will redirect back to your redirect_uri with a temporary authorization code parameter.

If you specified a state parameter in step 1, the parameter will be included as well. If you generate a random string or encode the hash of a cookie or another value that captures the client's state, you can validate the response to additionally ensure that the request and response originated in the same browser, providing protection against attacks such as cross-site request forgery.

Example of the redirection:

state is the same as the one in step 1

After your application receives the authorization code, it can exchange the authorization code for an access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

If your access token is expired, you can use refresh_token to get a new access token, which can be done by make a POST call:

After a successful request, a valid access_token will be returned in the response and it will be invalid if it exceeds the expires_in time in the response, which is in seconds.

Here is an example response:

After you have a valid access_token, you can make your first API call:

**Examples:**

Example 1 (text):
```text
GET https://accounts.binance.com/en/oauth/authorize?    response_type=code&    client_id=YOUR_CLIENT_ID&    redirect_uri=YOUR_REDIRECT_URI&    state=CSRF_TOKEN&    scope=SCOPES
```

Example 2 (text):
```text
GET https://accounts.binance.com/en/oauth/authorize?    response_type=code&    client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&    redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&    state=377f36a4557ab5935b36&    scope=user:openId,create:apikey
```

Example 3 (text):
```text
GET https://domain.com/oauth/callback?    code=cf6941ae8918b6a008f1377f36a4557ab5935b36&    state=377f36a4557ab5935b36
```

Example 4 (text):
```text
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
```

---
