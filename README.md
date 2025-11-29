# 🎮 Trader Game Life

A cryptocurrency trading and mining simulation game for the terminal. Play solo or compete with friends using synchronized seeds - **no internet required!**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-AGPL--3.0-orange)

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Game Modes](#game-modes)
- [How to Play](#how-to-play)
- [Mining Pools](#mining-pools)
- [Game Mechanics](#game-mechanics)
- [Multiplayer (Offline)](#multiplayer-offline)
- [File Structure](#file-structure)
- [Tips & Strategies](#tips--strategies)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**Trader Game Life** is a terminal-based game where you:
- Trade cryptocurrency ("@" arobase) against dollars ("$")
- Mine using graphics cards (RTX 2080, 3070, 3090)
- Join mining pools for strategic advantages
- Manage random events (bills, accidents, opportunities)
- Compete with friends using synchronized market seeds

**Key Feature**: The market course is deterministically generated from a seed, allowing multiple players to experience the **exact same market conditions** without any network connection!

---

## ✨ Features

### 🎲 Game Modes
- **Unlimited**: Play without time or turn constraints
- **Time Limited**: 7-day challenge mode
- **Competitive**: 3-day competitive mode with friends
- **Tutorial**: Learn the game mechanics

### 💰 Trading System
- Real-time market with deterministic course generation
- Buy and sell arobase (@) with transaction taxes
- Gradual sale system (70-100% sells per turn)
- Market statistics and trend analysis

### ⛏️ Mining System
- 3 graphics cards with different power levels
- 7 unique mining pools with special bonuses
- Mining power affects arobase generation
- Secret pool with special code

### 🎪 Special Features
- **26 random events**: bills, accidents, opportunities
- **Pepe the Frog quiz**: Test your knowledge for x1.5 or ÷2 your money
- **Player exchanges**: Transfer currency using time-limited QR codes
- **Collectibles**: Unlock trophies and achievements
- **ASCII charts**: Visualize market trends in terminal

### 💾 Save System
- Auto-save every 30 seconds
- Multiple save slots
- Encoded saves for basic protection
- Resume from most recent game

---

## 📥 Installation

### Prerequisites
- Python 3.7 or higher
- Terminal with UTF-8 support

### Install

1. **Clone or download the repository**
```bash
git clone <repository-url>
cd TraderGameLife
```

2. **No dependencies required!** The game uses only Python standard library.

3. **Run the game**
```bash
python main_game_loop.py
```

---

## 🚀 Quick Start

### First Launch

```bash
python main_game_loop.py
```

You'll see:
```
============================================================
                    TRADER GAME LIFE
============================================================

A cryptocurrency trading and mining simulation game

No saved games found. Starting new game...
```

### Choose Your Mode

```
============================================================
                     SELECT GAME MODE
============================================================

  [1] Unlimited
      Play without time or turn limits

  [2] Time Limited
      7-day challenge mode

  [3] Competitive
      3-day competitive mode with friends

  [4] Tutorial
      Learn the game basics
============================================================
```

### Set Your Seed

For **multiplayer with friends**, share the same seed:
```
Seed options:
  [1] Random seed
  [2] Enter custom seed
  [3] Quick start (seed: 35042)

Choice: 2
Enter seed: 42069
```

**Everyone using seed `42069` will have the same market!**

---

## 🎮 Game Modes

### 🔄 Unlimited Mode
- **Duration**: Unlimited
- **Turns**: Unlimited
- **Best for**: Learning and experimentation
- **Features**: All features enabled

### ⏱️ Time Limited Mode
- **Duration**: 7 days (real-time)
- **Turns**: Unlimited (30 min per turn)
- **Best for**: Week-long personal challenge
- **Features**: Real-time progression

### 🏆 Competitive Mode
- **Duration**: 3 days
- **Turn limit**: 100 turns
- **Best for**: Competing with friends
- **Features**: Shared seed, leaderboard-ready
- **Strategy**: Optimize every decision!

### 📚 Tutorial Mode
- **Duration**: 20 turns
- **Starting money**: $1,000 (instead of $250)
- **Best for**: New players
- **Features**: No random events, hints enabled

---

## 🎯 How to Play

### Main Interface

```
============================================================
@ Course: $125.75 [+5.50] 📈
Power: 12 | Turn: 15

You have: 25.12345@ and $5,234.56
============================================================

ACTIONS:
  [V] Sell @                [A] Buy @
  [E] Cancel sale           [M] Mine
  
  [C] Shop                  [P] Mining Pools
  [Z] Exchange              [L] Market Chart
  
  [I] Info/Save             [Q] Quit

Action: _
```

### Core Actions

#### 🔴 **[V] Sell Arobase**
Put your @ up for sale. Will gradually sell over next turns (70-100% each turn).
- Requires paying transaction tax
- Instant sale with FBG pool

#### 🟢 **[A] Buy Arobase**
Purchase @ at current market price.
- Transaction tax applies
- Price changes every turn

#### ⛏️ **[M] Mine**
Advance one turn and mine arobase based on your power.
- Market updates
- Sales process
- Random events may occur
- Pool bonuses apply

#### 🛒 **[C] Shop**
Purchase graphics cards, collectibles, and victory!

**Graphics Cards:**
- RTX 2080: $6,000 (Power: 2) - Max 5
- RTX 3070: $50,000 (Power: 5) - Max 6
- RTX 3090: $100,000 (Power: 10) - Max 5

**Collectibles:**
- `#` Trophy: $1,000,000
- `!` Pro Trader Trophy: $50,000,000
- `?` 99.99% Mining Trophy: Achievement only

**Victory Condition:**
- Cost: $500,000,000 + 600@
- Instant win!

#### 🏊 **[P] Mining Pools**
Join pools for strategic advantages. See [Mining Pools](#mining-pools) section.

#### 🔄 **[Z] Exchange**
Send or receive currency with other players using time-limited codes (60s).

#### 📊 **[L] Market Chart**
View ASCII chart of market history with statistics.

#### 💾 **[I] Info/Save**
- Manual save
- View game status
- Check statistics

---

## 🏊 Mining Pools

Each pool offers unique strategic advantages. **Cooldown: 10 turns** between switches.

### 🎯 C53 Pool
```
💵 +$75 per turn
```
**Strategy**: Steady dollar income, great for beginners

### 🅱️ BTC Pool
```
@ +0.25@ per turn
```
**Strategy**: Extra arobase generation

### ⚡ FBG Pool
```
🏃 Instant arobase sales
```
**Strategy**: All @ for sale sells immediately (100%)

### 📢 HELLO Pool
```
📊 Market alerts + analysis tools
```
**Strategy**: Get notified of market highs/lows
- Alerts when course hits extremes
- Access to extended chart features

### 🔐 ITS Pool
```
🛡️ Reduced random event probability
```
**Strategy**: Protection from malus events
- **Secret**: Enter code `3667` to unlock ITS+
- ITS+ gives welcome bonus: +$250

### 💸 +=+ Pool
```
⚠️ -$1,000 per turn
```
**Strategy**: High risk, high reward?
- Costs money each turn
- Best avoided unless you have a strategy

### 🏴 Solo Mining
Not in a pool:
- 1/200 chance for jackpot each turn
- No pool benefits

---

## 🎲 Game Mechanics

### 📈 Market System

The market course is **deterministically generated** from the seed:
```python
seed = 42069  # Same seed = Same market for everyone
```

**Market Properties:**
- Starts at $70
- Variations based on seed
- Decay after turn 35 (prevents infinite growth)
- Min value: $1

**Course Change Formula:**
```
if course > 100:
    course += variation - decay
else:
    course += variation / 10
```

### 💰 Transaction Tax

Tax increases with your wealth:
```python
tax = max_dollar_ever / 1000
```

**Example:**
- Max wealth was $50,000
- Tax = $50 per transaction

### 🎰 Random Events (Malus)

**Probability:**
```python
malus_level = seed // 10000
chance = malus_level / 10
```

**26 Different Events:**
- Bills (gas, electricity, water, phone)
- Accidents (hospital, car)
- Misfortunes (robbery, scam)
- Unexpected costs (fridge, roof repair)
- And more...

**Cost Range:**
- Base: $10-20
- Plus: 0.5% to 30% of your dollar balance

**Protection:**
- ITS/ITS+ pools reduce malus chance
- No malus until you have $1,000

### 🐸 Pepe the Frog Event

**Appearance:** 1/20 chance per turn

**Quiz Questions:**
- Card prices
- Pool bonuses  
- Last course value
- Collectible costs

**Rewards:**
- ✓ Correct: Money × 1.5
- ✗ Wrong: Money ÷ 2
- Decline: No change

### 🏆 Score System

```python
total_wealth = dollar + (arobase × course) + card_values + collectibles
score = int(total_wealth × 0.8 × 0.001) - 17
```

---

## 👥 Multiplayer (Offline)

### How It Works

1. **All players use the same seed**
```bash
Player 1: python main_game_loop.py
Seed: 42069

Player 2: python main_game_loop.py  
Seed: 42069  # Same seed!
```

2. **Market is synchronized**
   - Turn 1: @ = $70 for everyone
   - Turn 10: @ = $125.50 for everyone
   - Same opportunities, same challenges!

3. **Trade Between Players**
   - Use [Z] Exchange to create transfer codes
   - Codes valid for 60 seconds
   - Send dollars or arobase

### Competitive Play

**Setup:**
1. Choose **Competitive Mode** (3 days, 100 turns)
2. All players use **same seed**
3. Set deadline: "We compare scores on Sunday at 8 PM"

**Compare Results:**
```
Player 1 Final Score: 1,234
Player 2 Final Score: 1,567  ← Winner!
Player 3 Final Score: 891
```

**Fair Play:**
- Same market conditions
- Same random events (seed-based)
- Same opportunities
- Pure strategy competition!

### Exchange System

**Sending:**
```
[Z] Exchange → [1] Send → [1] Dollar
Amount: 100

╔═══════════════════════════════╗
║      EXCHANGE CODE            ║
╠═══════════════════════════════╣
║  j5m2e8j1                     ║
║  4e7m9j6e                     ║
╠═══════════════════════════════╣
║  Scan or enter manually       ║
╚═══════════════════════════════╝

Code: j5m2e8j14e7m9j6e
Expires in: 60 seconds
```

**Receiving:**
```
[Z] Exchange → [2] Receive
Code: j5m2e8j14e7m9j6e

✓ Received 100 DOLLAR!
```

---

## 📁 File Structure

```
TraderGameLife/
├── function/
│   ├── main_game_loop.py       # Main game loop and menu
│   ├── game_config.py          # Game modes and configuration
│   ├── market_system.py        # Market and course generation
│   ├── wallet_system.py        # Wallet and assets management
│   ├── mining_pools.py         # Mining pools system
│   ├── random_events.py        # Random events and Pepe
│   ├── save_system.py          # Save/load with encoding
│   ├── exchange_qrcode.py      # P2P exchange system
│   └── terminal_ui.py          # Terminal interface utilities
├── README.md               # This file
├── LICENSE                 # AGPL-3.0 License
├── Run.py                  # Run the game
└── Game_data/
    └── Parties/            # Save files directory
        ├── game1/
        │   └── game_save.json
        └── game2/
            └── game_save.json
```

### Module Dependencies

```
main_game_loop.py
    ├── game_config.py
    ├── market_system.py
    ├── wallet_system.py
    ├── mining_pools.py
    ├── random_events.py
    ├── save_system.py
    ├── exchange_qrcode.py
    └── terminal_ui.py
```

All modules are **independent** and use only Python standard library.

---

## 💡 Tips & Strategies

### 🎯 Beginner Strategy

1. **Start with C53 pool** (+$75/turn)
2. **Buy RTX 2080 first** (cheap, good start)
3. **Don't over-trade** (taxes add up!)
4. **Save often** (manual save recommended)
5. **Watch for Pepe** (know your prices!)

### 🏆 Advanced Strategy

**Early Game (Turns 1-20):**
- Join C53 for steady income
- Buy 2-3 RTX 2080 cards
- Trade conservatively (tax management)

**Mid Game (Turns 21-50):**
- Switch to BTC pool (+0.25@/turn)
- Upgrade to RTX 3070 cards
- Start trading more actively
- Use HELLO pool to catch market extremes

**Late Game (Turns 51+):**
- Max out RTX 3090 cards
- Use FBG pool for instant sales
- Buy collectibles if wealthy enough
- Go for victory condition

### 📊 Market Timing

**Buy When:**
- Course is near all-time low
- Downward trend shows signs of reversal
- You have spare cash after tax

**Sell When:**
- Course is near all-time high  
- Upward trend slowing down
- You need cash for cards/events

**HELLO Pool Strategy:**
```
📉 ALERT: Course at ALL-TIME LOW!
→ Perfect time to buy!

📈 ALERT: Course at ALL-TIME HIGH!
→ Perfect time to sell!
```

### 💰 Wealth Management

**Tax Management:**
```
Your max wealth: $100,000
Current tax: $100 per trade
→ Each trade costs $100!
```

**Strategy:**
- Keep some cash reserve for taxes
- Don't let $ go negative (game over!)
- Collectibles don't increase tax

### 🎯 Pool Rotation Strategy

**Optimal Rotation:**
1. **Turns 1-10**: C53 (build capital)
2. **Turns 11-30**: BTC (accumulate @)
3. **Turns 31-50**: HELLO (trade at extremes)
4. **Turns 51+**: FBG (instant sales)

**Remember:** 10-turn cooldown between switches!

### 🏆 Competitive Mode Tips

**Time Management:**
- 3 days = 72 hours
- 100 turns max
- Plan your playing sessions

**Optimal Play:**
- Check every 2-4 hours
- Use HELLO pool for market alerts
- Trade at extremes only
- Avoid random event costs

**Final Push:**
- Last 20 turns are critical
- Max out your power
- All-in on market timing
- Consider victory purchase

---

## 🤝 Contributing

Contributions are welcome! Here are ways to help:

### 🐛 Bug Reports
Open an issue with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Game version and Python version

### 💡 Feature Requests
Suggest new features:
- Mining strategies
- New pools
- Additional collectibles
- UI improvements

### 🔧 Code Contributions
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Follow code style (English, no emojis in code)
4. Add tests if applicable
5. Commit changes (`git commit -m 'Add AmazingFeature'`)
6. Push to branch (`git push origin feature/AmazingFeature`)
7. Open Pull Request

### 📝 Code Style

```python
# English function and variable names
def calculate_tax(player_dollar):
    """Calculate transaction tax based on max wealth"""
    tax = max_dollar / 1000
    return int(tax)

# Clear comments
# Good: "Process arobase sales"
# Bad: "faire la vente"
```

---

## 📜 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

**Key Points:**
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ Must disclose source
- ⚠️ Must use same license
- ⚠️ Network use = distribution

See [LICENSE](LICENSE) file for full details.

---

## 📞 Support

**Need help?**
- 📖 Read this README
- 🐛 Check existing issues
- 💬 Open new issue
- 📧 Contact maintainers

---

## 🎮 Happy Trading!

```
    ╔═══════════════════════════════╗
    ║   Trade Smart, Mine Hard!     ║
    ║   May the markets be with you ║
    ╚═══════════════════════════════╝
```

**Remember:** The best strategy is the one you develop through experience. Start playing, learn the mechanics, and create your own winning approach!

---

**Version:** 2.0  
**Last Updated:** 2025

---

## 📚 Additional Resources

### Quick Reference Card

```
┌─────────────────────────────────────────────┐
│           TRADER GAME LIFE                  │
│              QUICK REFERENCE                │
├─────────────────────────────────────────────┤
│ ACTIONS                                     │
│   V - Sell @        M - Mine                │
│   A - Buy @         C - Shop                │
│   E - Cancel sale   P - Pools               │
│   Z - Exchange      L - Chart               │
│   I - Info/Save     Q - Quit                │
├─────────────────────────────────────────────┤
│ CARDS                                       │
│   RTX 2080: $6K     Power: 2    Max: 5     │
│   RTX 3070: $50K    Power: 5    Max: 6     │
│   RTX 3090: $100K   Power: 10   Max: 5     │
├─────────────────────────────────────────────┤
│ POOLS                                       │
│   C53:    +$75/turn                         │
│   BTC:    +0.25@/turn                       │
│   FBG:    Instant sales                     │
│   HELLO:  Market alerts                     │
│   ITS:    Less malus (secret: 3667)        │
│   +=+:    -$1000/turn                       │
├─────────────────────────────────────────────┤
│ FORMULAS                                    │
│   Tax = max_dollar / 1000                   │
│   Malus chance = seed / 100000              │
│   Score = wealth × 0.8 × 0.001 - 17        │
└─────────────────────────────────────────────┘
```

### Seed Recommendations

```
Quick Start:   35042  (Recommended for beginners)
Easy Mode:     44066  (Gentle learning curve)
Normal Mode:   42069  (Balanced gameplay)
Hard Mode:     66021  (Challenge accepted!)
Random:        [1-99999]
```

### Command Line Cheatsheet

```bash
# Start game
python main_game_loop.py

# Quick actions (in-game)
v          # Sell @
a          # Buy @
m          # Mine (advance turn)
c → 1      # Buy RTX 2080
p → 1      # Join C53 pool
i → 1      # Save game
q          # Quit

# Advanced
pepe       # Trigger Pepe quiz (when available)
```

---

*End of README*
