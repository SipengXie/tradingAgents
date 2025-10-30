---
name: binance
description: Binance API documentation for cryptocurrency trading. Use for Binance REST API, WebSocket streams, trading pairs, market data, and crypto exchange integration.
---

# Binance API Skill

Comprehensive assistance with Binance API development, covering REST API, WebSocket API, trading, authentication, and market data.

## When to Use This Skill

This skill should be triggered when:
- Working with Binance cryptocurrency exchange APIs
- Implementing spot trading, futures, or margin trading
- Building real-time market data streaming applications
- Authenticating with Binance API keys (Ed25519, HMAC, RSA)
- Debugging Binance API errors or rate limits
- Implementing order placement, cancellation, or modification
- Setting up OAuth 2.0 authentication for Binance

## Quick Reference

### Essential API Patterns

#### 1. REST API Authentication (HMAC SHA256)

```bash
# Example: Place a LIMIT order using HMAC signature
curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" \
  -X POST 'https://api.binance.com/api/v3/order' \
  -d 'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
```

**Signature Generation:**
```bash
echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" \
  | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
```

#### 2. WebSocket API - Place Order

```javascript
{
  "id": "56374a46-3061-486b-a311-99ee972eb648",
  "method": "order.place",
  "params": {
    "symbol": "BTCUSDT",
    "side": "SELL",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "23416.10000000",
    "quantity": "0.00847000",
    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
    "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",
    "timestamp": 1660801715431
  }
}
```

**Response (ACK format):**
```javascript
{
  "id": "56374a46-3061-486b-a311-99ee972eb648",
  "status": 200,
  "result": {
    "symbol": "BTCUSDT",
    "orderId": 12569099453,
    "orderListId": -1,
    "clientOrderId": "4d96324ff9d44481926157ec08158a40",
    "transactTime": 1660801715639
  },
  "rateLimits": [...]
}
```

#### 3. WebSocket API - Session Login (Ed25519)

```javascript
{
  "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
  "method": "session.logon",
  "params": {
    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
    "signature": "1cf54395b336b0a9727ef27d5d98987962bc47aca6e13fe978612d0adee066ed",
    "timestamp": 1649729878532
  }
}
```

#### 4. WebSocket API - Check Server Time

```javascript
{
  "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",
  "method": "time"
}
```

**Response:**
```javascript
{
  "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",
  "status": 200,
  "result": {
    "serverTime": 1656400526260
  }
}
```

#### 5. User Data Stream Subscription

```javascript
{
  "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
  "method": "userDataStream.subscribe"
}
```

#### 6. OAuth 2.0 Authorization Flow

```text
# Step 1: Authorization URL
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=YOUR_CLIENT_ID&
    redirect_uri=YOUR_REDIRECT_URI&
    state=CSRF_TOKEN&
    scope=SCOPES

# Step 2: Exchange code for token
POST https://accounts.binance.com/oauth/token?
    client_id=YOUR_CLIENT_ID&
    client_secret=YOUR_CLIENT_SECRET&
    grant_type=authorization_code&
    code=STEP3_CODE&
    redirect_uri=YOUR_REDIRECT_URI
```

#### 7. Market Data - Get Exchange Info

```javascript
{
  "id": "exchange-info-123",
  "method": "exchangeInfo",
  "params": {
    "symbol": "BTCUSDT"  // optional: filter by symbol
  }
}
```

#### 8. Cancel and Replace Order (Atomic Operation)

```javascript
{
  "id": "cancel-replace-456",
  "method": "order.cancelReplace",
  "params": {
    "cancelReplaceMode": "STOP_ON_FAILURE",
    "cancelOrderId": 12345,
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "price": "25000.00",
    "quantity": "0.5",
    "timestamp": 1660801715431,
    "apiKey": "YOUR_API_KEY",
    "signature": "YOUR_SIGNATURE"
  }
}
```

### Common Order Types

| Type | Description | Required Parameters |
|------|-------------|---------------------|
| `LIMIT` | Buy/sell at specified price or better | `price`, `quantity`, `timeInForce` |
| `MARKET` | Execute at best available price | `quantity` OR `quoteOrderQty` |
| `STOP_LOSS` | Market order triggered at stop price | `stopPrice`, `quantity` |
| `STOP_LOSS_LIMIT` | Limit order triggered at stop price | `stopPrice`, `price`, `quantity`, `timeInForce` |
| `TAKE_PROFIT` | Market order for profit-taking | `stopPrice`, `quantity` |
| `TAKE_PROFIT_LIMIT` | Limit order for profit-taking | `stopPrice`, `price`, `quantity`, `timeInForce` |
| `LIMIT_MAKER` | Post-only limit order (no taker) | `price`, `quantity` |

### Time In Force Options

- `GTC` - Good Till Cancel (remains active until filled or canceled)
- `IOC` - Immediate or Cancel (fill immediately or cancel)
- `FOK` - Fill or Kill (fill completely or cancel entirely)
- `GTX` - Good Till Crossing (post-only, like LIMIT_MAKER)
- `GTD` - Good Till Date (auto-cancel at specified time)

### API Key Types (Recommended: Ed25519)

| Type | Security | Performance | Use Case |
|------|----------|-------------|----------|
| **Ed25519** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **Recommended** - Best security & speed |
| HMAC | ⭐⭐⭐ | ⭐⭐⭐⭐ | Shared secret, simple implementation |
| RSA | ⭐⭐⭐⭐ | ⭐⭐⭐ | Asymmetric, larger signatures |

## Key Concepts

### 1. WebSocket vs REST API

- **REST API**: Request-response model, good for one-time operations (place order, cancel order)
- **WebSocket API**: Persistent connection, better for real-time data and high-frequency trading
- **WebSocket URL**: `wss://ws-api.binance.com/ws-api/v3`
- **REST Base URL**: `https://api.binance.com`

### 2. Authentication Flow

1. **Generate timestamp**: Current Unix timestamp in milliseconds
2. **Build signature payload**: Sort parameters alphabetically, format as `key=value&key2=value2`
3. **Sign payload**: Use HMAC-SHA256 (or Ed25519/RSA) with your secret key
4. **Add signature**: Append `signature` parameter to request
5. **Set API key header**: `X-MBX-APIKEY: your_api_key`

### 3. Rate Limits

Binance enforces multiple rate limit types:
- **REQUEST_WEIGHT**: Weight-based limit (varies by endpoint)
- **ORDERS**: Order placement limits (per second/day)
- **RAW_REQUESTS**: Raw request count limits

**Check your limits** in response `rateLimits` array.

### 4. recvWindow (Timing Security)

- Specifies max time (in ms) for request to be valid after timestamp
- **Recommended**: Use 5000ms or less
- **Max allowed**: 60,000ms
- Protects against replay attacks

### 5. Self-Trade Prevention (STP)

Prevents orders from matching with your own orders:
- `NONE`: No protection
- `EXPIRE_TAKER`: Cancel taker order
- `EXPIRE_MAKER`: Cancel maker order
- `EXPIRE_BOTH`: Cancel both orders

### 6. Order Response Types

- `ACK`: Minimal response (orderId, status)
- `RESULT`: Includes order details (price, quantity, status)
- `FULL`: Complete response including fills (trades executed)

### 7. Smart Order Routing (SOR)

- Automatically routes orders across multiple order books for best execution
- Use `sor.order.place` method
- Only supports `LIMIT` and `MARKET` orders

## Navigation Guide

### For Beginners

**Start here:**
1. Read `api_reference.md` - Understand API changelog and recent updates
2. Learn authentication - Focus on Ed25519 keys (best security)
3. Practice with `time` and `exchangeInfo` methods (no auth required)
4. Test order placement with `order.test` before real orders

**First integration checklist:**
- [ ] Create Binance API key (Ed25519 recommended)
- [ ] Implement signature generation
- [ ] Test connectivity with `ping` and `time`
- [ ] Query exchange info for trading pairs
- [ ] Place a test order with `order.test`
- [ ] Implement error handling for rate limits

### For Intermediate Users

**Focus on:**
- `spot_trading.md` - Complete trading operations guide
- Order types (LIMIT, MARKET, STOP_LOSS, OCO)
- WebSocket User Data Streams for real-time updates
- Order amendment and cancel-replace operations
- Handling conditional orders and order lists

**Advanced patterns:**
- Implement retry logic with exponential backoff
- Monitor rate limits and adjust request frequency
- Use WebSocket API for lower latency
- Implement STP to prevent self-trading

### For Advanced Users

**Optimize for:**
- WebSocket API for high-frequency trading
- Smart Order Routing (SOR) for best execution
- Order lists (OCO - One-Cancels-Other)
- Portfolio Margin and Futures trading
- OAuth 2.0 for third-party integrations

**Performance tips:**
- Prefer Ed25519 keys (fastest signature computation)
- Use WebSocket API to reduce latency
- Batch operations where possible
- Monitor `rateLimits` in responses
- Use `recvWindow` wisely (5000ms recommended)

## Error Handling

### Common Error Codes

```javascript
// Rate limit exceeded
{ "code": -1008, "msg": "Server is currently overloaded with other requests. Please try again in a few minutes." }

// Timing security
{ "code": -1021, "msg": "Timestamp for this request is outside of the recvWindow." }

// Order rate limit
{ "code": -1015, "msg": "Too many new orders; current limit is XX orders per XX." }
```

### Best Practices

1. **Always check response status**: Look for `"status": 200`
2. **Handle rate limits gracefully**: Implement exponential backoff
3. **Use recvWindow properly**: 5000ms is recommended
4. **Validate signatures**: Test with provided examples first
5. **Monitor rate limits**: Check `rateLimits` array in responses
6. **Use test endpoints**: Use `order.test` before real orders

## Market Data Only URLs (No Authentication)

For public market data without API keys:

**REST API:**
```bash
curl -sX GET "https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT"
```

**WebSocket:**
```text
wss://data-stream.binance.vision:443/ws/btcusdt@kline_1m
```

## Documentation Structure

This skill includes the following reference files:

- **`spot_trading.md`** (45 pages) - Complete spot trading guide including WebSocket API, order placement, authentication, market data, and user data streams
- **`api_reference.md`** (3 pages) - API changelog, updates, OAuth 2.0 authentication flows
- **`other.md`** (1 page) - Binance Login (OAuth2) for third-party applications

## Additional Resources

- **Official Docs**: https://developers.binance.com/docs/
- **WebSocket API**: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api
- **REST API**: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
- **Testnet**: Use testnet for development and testing
- **GitHub**: Official Binance API connectors available

## Recent Updates (2025)

- **2025-10-21**: Temporarily removed `OPPONENT_10` and `OPPONENT_20` from priceMatch enums
- **2025-10-09**: Futures now supports Chinese trading pair symbols (UTF-8 URL encoding required)
- **2025-08-11**: BFUSD migrated to Binance Earn
- **2025-07-25**: Added error code `-4109` for inactive accounts
- **2024-09**: Added TRADE_LITE event for lower latency user data streams

---

**Generated with Skill Seeker** - Enhanced with comprehensive examples and navigation guidance.
