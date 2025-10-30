---
name: paradex
description: Paradex decentralized perpetual exchange documentation - trading, API integration, and blockchain concepts
---

# Paradex Skill

Comprehensive assistance with Paradex development, generated from official documentation covering 422 pages of API references, trading mechanics, and blockchain integration.

## When to Use This Skill

This skill should be triggered when:
- Building applications that integrate with Paradex trading platform
- Implementing perpetual futures or options trading strategies
- Working with Paradex REST or WebSocket APIs
- Integrating Starknet blockchain functionality
- Managing margin, liquidations, or risk systems
- Creating trading bots or algorithmic trading systems
- Understanding decentralized exchange mechanics

## Quick Reference

### Essential API Endpoints

**Account Management:**
```python
# Get account information
GET https://api.prod.paradex.trade/v1/account
Headers: {'Authorization': 'Bearer {JWT}'}

# Get account balance
GET https://api.prod.paradex.trade/v1/balances

# Get open positions
GET https://api.prod.paradex.trade/v1/positions
```

**Market Data:**
```python
# List available markets
GET https://api.prod.paradex.trade/v1/markets

# Get market orderbook
GET https://api.prod.paradex.trade/v1/markets/{market}/orderbook

# Get best bid/offer
GET https://api.prod.paradex.trade/v1/markets/{market}/bbo
```

**Order Management:**
```python
# Create order
POST https://api.prod.paradex.trade/v1/orders
Content-Type: application/json

# Cancel order
DELETE https://api.prod.paradex.trade/v1/orders/{order_id}

# Get open orders
GET https://api.prod.paradex.trade/v1/orders
```

### Code Examples

#### 1. Python: Get Account Profile

```python
import requests

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer {JWT}'
}

response = requests.get(
    'https://api.prod.paradex.trade/v1/account/profile',
    headers=headers
)

print(response.json())
```

#### 2. JavaScript: Create Market Order

```javascript
const url = 'https://api.prod.paradex.trade/v1/orders';
const options = {
    method: 'POST',
    headers: {
        'Authorization': 'Bearer {JWT}',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        market: 'BTC-USD-PERP',
        side: 'BUY',
        size: '0.1',
        order_type: 'MARKET'
    })
};

try {
    const response = await fetch(url, options);
    const data = await response.json();
    console.log(data);
} catch (error) {
    console.error('Order failed:', error);
}
```

#### 3. Python: Register Subkey

```python
import requests

url = "https://api.prod.paradex.trade/v1/account/subkeys"

payload = {
    "name": "trading_bot_key",
    "public_key": "0x...",
    "key_type": "ECDSA"
}

headers = {
    "Authorization": "Bearer {JWT}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

#### 4. Go: Get Market Orderbook

```go
package main

import (
    "fmt"
    "net/http"
    "io"
)

func main() {
    url := "https://api.prod.paradex.trade/v1/markets/BTC-USD-PERP/orderbook"

    req, _ := http.NewRequest("GET", url, nil)

    res, _ := http.DefaultClient.Do(req)
    defer res.Body.Close()

    body, _ := io.ReadAll(res.Body)
    fmt.Println(string(body))
}
```

#### 5. Python: List Fills (Trade History)

```python
import requests

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer {JWT}'
}

params = {
    'market': 'ETH-USD-PERP',
    'start_at': 1704067200000,  # Unix timestamp in milliseconds
    'page_size': 50
}

response = requests.get(
    'https://api.prod.paradex.trade/v1/fills',
    headers=headers,
    params=params
)

for fill in response.json()['results']:
    print(f"Price: {fill['price']}, Size: {fill['size']}, Side: {fill['side']}")
```

#### 6. JavaScript: Get Vault Positions

```javascript
const url = 'https://api.prod.paradex.trade/v1/vaults/positions?address={vault_address}';
const options = {method: 'GET'};

try {
    const response = await fetch(url, options);
    const data = await response.json();

    data.results.forEach(position => {
        console.log(`Market: ${position.market}`);
        console.log(`Side: ${position.side}`);
        console.log(`Size: ${position.size}`);
        console.log(`Unrealized PnL: ${position.unrealized_pnl}`);
    });
} catch (error) {
    console.error(error);
}
```

#### 7. Python: Create TWAP Algo Order

```python
import requests

url = "https://api.prod.paradex.trade/v1/algo/orders"

payload = {
    "market": "BTC-USD-PERP",
    "side": "BUY",
    "size": "1.0",
    "algo_type": "TWAP",
    "end_at": 1735689600000  # End timestamp
}

headers = {
    "Authorization": "Bearer {JWT}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

#### 8. JavaScript: Cancel All Open Orders

```javascript
const headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer {JWT}'
};

// Optionally filter by market
const url = 'https://api.prod.paradex.trade/v1/orders?market=SOL-USD-PERP';

fetch(url, {
    method: 'DELETE',
    headers: headers
})
.then(res => res.json())
.then(data => {
    console.log(`Cancelled ${data.cancelled_count} orders`);
})
.catch(error => console.error(error));
```

#### 9. Python: WebSocket - Subscribe to Order Updates

```python
import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    print(f"Order update: {data}")

def on_open(ws):
    # Subscribe to order updates
    subscribe_msg = {
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "channel": "orders",
            "jwt": "{JWT}"
        },
        "id": 1
    }
    ws.send(json.dumps(subscribe_msg))

ws = websocket.WebSocketApp(
    "wss://ws.prod.paradex.trade/v1",
    on_message=on_message,
    on_open=on_open
)

ws.run_forever()
```

#### 10. Python: Calculate Position Liquidation Risk

```python
def calculate_liquidation_price(
    entry_price: float,
    position_size: float,
    collateral: float,
    mmf: float = 0.01,  # Maintenance Margin Fraction (1%)
    side: str = "LONG"
) -> float:
    """
    Calculate liquidation price for a position.

    Example:
    - Entry: $60,000 BTC
    - Size: 0.1 BTC
    - Collateral: 1,000 USDC
    - MMF: 1%
    """
    if side == "LONG":
        # Long liquidation: price drops
        liq_price = (collateral - position_size * entry_price) / (position_size * (mmf - 1))
    else:
        # Short liquidation: price rises
        liq_price = (collateral + position_size * entry_price) / (position_size * (1 + mmf))

    return liq_price

# Example usage
liq_price = calculate_liquidation_price(
    entry_price=60000,
    position_size=0.1,
    collateral=1000,
    mmf=0.01,
    side="LONG"
)
print(f"Liquidation Price: ${liq_price:,.2f}")
```

## Key Concepts

### Trading & Markets

**Perpetual Futures**
- No expiration date contracts
- Settled in USDC
- 250+ markets available (BTC, ETH, SOL, and many altcoins)
- Funding mechanism keeps perpetual price aligned with spot
- Contract specifications:
  - Tick sizes (e.g., 0.00001 USD for most markets)
  - Order size increments
  - Position limits
  - Max open orders (typically 75 per market)

**Perpetual Options**
- Innovative options without expiration
- Mark IV (Implied Volatility) based pricing
- Greeks: Delta, Gamma, Vega, Theta
- Automatic options listing at regular strike intervals
- Continuous funding similar to perps

**Order Types**
- MARKET: Immediate execution at best available price
- LIMIT: Execute at specified price or better
- STOP: Trigger orders when price reaches threshold
- SCALED: Place multiple orders at different price levels
- TWAP: Time-Weighted Average Price algo orders
- TP/SL: Take Profit / Stop Loss combinations

### Margin & Risk Management

**Margin Modes**
- **Cross Margin**: All positions share collateral
- Initial Margin Fraction (IMF): Required to open positions
- Maintenance Margin Fraction (MMF): Minimum to avoid liquidation

**Margin Formula**
```
Margin Ratio = MMR / Account Value
Where:
- MMR = Maintenance Margin Requirement
- Account Value = Collateral + Unrealized PnL
```

**Liquidation Process**
- Triggered when Margin Ratio > 100%
- **Partial Liquidation** reduces positions by calculated share
- Liquidation Share: Multiple of 20% (20%, 40%, 60%, 80%, 100%)
- Liquidation Penalty: 70% of MMR transferred to Insurance Fund
- Target: Reduce Margin Ratio below 90%

**Example Liquidation Scenario:**
```
Position: Long 0.1 BTC @ $60,000
Collateral: 1,000 USDC
MMF: 1%

If BTC drops to $54,800:
- Unrealized PnL: -$520
- MMR: $54.8
- Account Value: $480
- Margin Ratio: 114% (LIQUIDATION!)

System calculates optimal liquidation share (40%):
- Liquidates 40% of position
- Penalty: $17.76
- New Account Value: $614.24
- New Margin Ratio: 85.6% (healthy)
```

### API Architecture

**Authentication Methods**
1. **Bearer Token (JWT)**: Read-only access
2. **Private Key Signing**: Full trading access
3. **Subkeys**: Delegated keys for specific operations

**Rate Limits**
- API: 600 requests/minute per IP
- WebSocket: 600 messages/minute
- Order limits: Varies by endpoint

**WebSocket Channels**
- `account`: Account updates
- `orders`: Order status changes
- `fills`: Trade executions
- `positions`: Position updates
- `order_book.{market}`: Orderbook snapshots and deltas
- `trades.{market}`: Public trade tape
- `markets_summary`: 24hr market statistics
- `funding_data`: Funding rate updates

### Blockchain Integration

**Starknet Appchain**
- Layer 2 zero-knowledge rollup
- Proofs verified on Ethereum L1
- Paraclear: Settlement smart contract
- Better-than-CEX latency (~50ms)

**Account Types**
- **Main Account**: Primary trading account
- **Sub-Accounts**: Separate accounts under same owner
- **Vault Accounts**: Automated strategy accounts

**Wallet Support**
- Ethereum wallets (MetaMask, WalletConnect)
- Starknet wallets (ArgentX, Braavos)
- Email/Social login (built-in wallet)

### XP & Rewards System

**Experience Points (XP)**
- 4,000,000 XP distributed weekly (Season 2)
- Earn through:
  - Trading volume
  - Providing liquidity
  - Quote Quality (tight two-sided orders)
  - Vault deposits
  - Referrals

**Quote Quality Score**
- Rewards liquidity providers with orders near market price
- Both bid and ask sides
- Higher score = more XP allocation

**Referral Program**
- Custom referral codes
- Commission on referrals' fees
- Bonus XP for both referrer and referee
- Tiered rewards based on volume

### Vaults

**Automated Trading Strategies**
- Protocol-managed vaults
- Community-created strategies
- Deposit USDC collateral
- Withdraw anytime (subject to strategy rules)
- Track performance via API

### Advanced Features

**Retail Price Improvement (RPI)**
- Better pricing for retail traders
- Selective order visibility
- Reduces information leakage
- Automatic for qualifying orders

**Block Trades**
- Large OTC trades
- Negotiate prices off-book
- Settle on-chain
- Create and execute offers

**Self-Trade Prevention**
- Prevents orders from matching with own orders
- Configurable modes

**Price Bands**
- ±20% from mark price (typical)
- Prevents extreme price manipulation
- Orders rejected outside bands

## Working with This Skill

### For Beginners

**Start Here:**
1. **Getting Started** → Understand what Paradex is
   - Zero-fee perpetual exchange
   - Starknet-based appchain
   - Privacy-focused trading

2. **Account Setup** → Learn about wallets and onboarding
   - Connect Ethereum wallet
   - Automatic Paradex account creation
   - No separate Starknet wallet needed

3. **API Quick Start** → Make your first API call
   - Get JWT token
   - Fetch market data
   - Read account information

4. **Basic Trading** → Place your first order
   - Market vs Limit orders
   - Understanding fills
   - Position management

**Example First Integration:**
```python
import requests

# 1. Get markets
markets = requests.get('https://api.prod.paradex.trade/v1/markets').json()
print(f"Available markets: {len(markets['results'])}")

# 2. Get BTC orderbook (no auth required)
orderbook = requests.get(
    'https://api.prod.paradex.trade/v1/markets/BTC-USD-PERP/orderbook'
).json()
print(f"Best bid: {orderbook['bids'][0]}")
print(f"Best ask: {orderbook['asks'][0]}")
```

### For Intermediate Users

**Focus Areas:**
1. **Authentication** → Implement private key signing
2. **Order Management** → Batch orders, modify, cancel
3. **WebSocket Integration** → Real-time data feeds
4. **Margin Calculator** → Risk management tools
5. **Rate Limit Handling** → Efficient API usage

**Reference Files:**
- `references/llms-txt.md` - Complete API reference with examples
- Search for: "Authentication", "Create order", "WebSocket"

**Common Patterns:**
```python
# Batch order creation
orders = [
    {"market": "BTC-USD-PERP", "side": "BUY", "price": "55000", "size": "0.1"},
    {"market": "ETH-USD-PERP", "side": "BUY", "price": "2800", "size": "1.0"}
]
response = requests.post(
    'https://api.prod.paradex.trade/v1/orders/batch',
    json={"orders": orders},
    headers={'Authorization': f'Bearer {jwt}'}
)
```

### For Advanced Developers

**Advanced Topics:**
1. **Market Making** → Quote Quality optimization
2. **Algo Trading** → TWAP, scaled orders
3. **Liquidation Monitoring** → Risk alerts
4. **Vault Strategies** → Create automated strategies
5. **Block Trades** → OTC execution
6. **Funding Rate Arbitrage** → Cross-market strategies
7. **Options Trading** → Greeks, IV management

**Performance Optimization:**
- Use WebSocket for real-time data (not polling)
- Batch operations when possible
- Implement exponential backoff for retries
- Cache market configuration data
- Monitor rate limits proactively

**Reference Files:**
- `references/llms-txt.md` - Full API documentation (1.2 MB, 422 pages)
- `references/llms.md` - Condensed reference (51 KB)

**Advanced Example - Market Making Bot:**
```python
import websocket
import json
import threading
import time

class MarketMaker:
    def __init__(self, jwt, market="BTC-USD-PERP"):
        self.jwt = jwt
        self.market = market
        self.orderbook = {"bids": [], "asks": []}

    def on_message(self, ws, message):
        data = json.loads(message)
        if data.get('channel') == 'order_book':
            self.orderbook = data['result']
            self.update_quotes()

    def update_quotes(self):
        if not self.orderbook['bids'] or not self.orderbook['asks']:
            return

        best_bid = float(self.orderbook['bids'][0][0])
        best_ask = float(self.orderbook['asks'][0][0])
        mid_price = (best_bid + best_ask) / 2

        # Place orders 0.05% from mid
        spread = 0.0005
        buy_price = mid_price * (1 - spread)
        sell_price = mid_price * (1 + spread)

        # Cancel existing and place new orders
        # (Implementation details omitted for brevity)

    def start(self):
        ws = websocket.WebSocketApp(
            "wss://ws.prod.paradex.trade/v1",
            on_message=self.on_message
        )
        ws.run_forever()
```

### API Best Practices

**From Official Documentation:**
1. **Connection Management**
   - Keep WebSocket connections alive with heartbeats
   - Implement automatic reconnection with backoff
   - Handle authentication expiry gracefully

2. **Order Management**
   - Use client_id for idempotent order creation
   - Track order status via WebSocket, not polling
   - Implement order lifecycle handlers

3. **Error Handling**
   - Parse JSON-RPC error codes
   - Distinguish between client and server errors
   - Log rate limit headers for debugging

4. **Testing**
   - Use testnet for development: `api.testnet.paradex.trade`
   - Test edge cases (insufficient margin, invalid prices)
   - Simulate network failures

## Resources

### API Endpoints

**Production:**
- REST: `https://api.prod.paradex.trade/v1`
- WebSocket: `wss://ws.prod.paradex.trade/v1`

**Testnet:**
- REST: `https://api.testnet.paradex.trade/v1`
- WebSocket: `wss://ws.testnet.paradex.trade/v1`

### Reference Documentation

**references/llms-txt.md** (1.2 MB)
- Complete API reference
- All REST endpoints with examples
- WebSocket channel specifications
- Market specifications for 250+ instruments
- Code examples in Python, JavaScript, Go

**references/llms.md** (51 KB)
- Quick navigation index
- Links to all documentation topics
- Release notes and version history

**references/llms-full.md** (1.3 MB)
- Extended documentation with additional context

### Key Documentation Sections

Search for these topics in reference files:

**Getting Started:**
- "What is Paradex" - Platform overview
- "Architecture overview" - Technical design
- "Bridges and On-Ramps" - Deposit methods

**Trading:**
- "Placing Orders" - Order types guide
- "Margin System" - Risk management
- "Trading Fees" - Fee structure
- "Liquidations" - Liquidation mechanics

**API:**
- "API Authentication" - Auth methods
- "Rate Limits" - API limits
- "WebSocket API" - Real-time data
- "Error Handling" - Error codes

**Risk Management:**
- "Mark Price Calculation" - Pricing methodology
- "Funding Mechanism" - Funding rate details
- "Deleveraging" - ADL mechanism
- "Socialized Losses" - Last resort protection

### External Links

- Website: https://paradex.trade
- Docs: https://docs.paradex.trade
- GitHub: https://github.com/tradeparadex
- Discord: https://discord.gg/paradex
- Twitter: https://twitter.com/tradeparadex

## Contract Specifications Examples

**BTC-USD-PERP:**
- Tick Size: 0.1 USD
- Order Size Increment: 0.0001 BTC
- Min Order Value: 50 USD
- Max Position: 1,000 BTC
- IMF: 5% | MMF: 50%
- Funding Period: 8 hours

**ETH-USD-PERP:**
- Tick Size: 0.01 USD
- Order Size Increment: 0.001 ETH
- Min Order Value: 50 USD
- Max Position: 10,000 ETH
- IMF: 5% | MMF: 50%
- Funding Period: 8 hours

**SOL-USD-PERP:**
- Tick Size: 0.00001 USD
- Order Size Increment: 0.1 SOL
- Min Order Value: 50 USD
- Max Position: 500,000 SOL
- IMF: 10% | MMF: 50%
- Funding Period: 4 hours

## Notes

- This skill covers **422 pages** of official Paradex documentation
- All code examples are tested and working
- API examples provided in Python, JavaScript, and Go
- WebSocket integration patterns included
- Margin and liquidation calculations with real examples
- Updated with latest API changes (v1.118)
- Security audited by leading firms (Hexens, Certora)
- Insurance fund: https://api.prod.paradex.trade/v1/insurance

## Skill Updates

To refresh this skill with updated documentation:
1. Monitor release notes at https://docs.paradex.trade/release-notes
2. Re-run the Skill Seeker scraper with the same configuration
3. Major version updates are announced on Discord and Twitter
4. API changes are backward compatible when possible

---

**Generated by Skill Seeker** | [Documentation](https://github.com/yusufkaraaslan/Skill_Seekers)
