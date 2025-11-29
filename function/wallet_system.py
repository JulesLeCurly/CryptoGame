"""
Wallet System - Manages player's portfolio and assets
Handles dollars, arobase, graphics cards, and collectibles
"""

import json


class GraphicsCard:
    """Graphics card for mining"""
    
    CARDS = {
        "RTX_2080": {"name": "RTX 2080", "power": 2, "price": 6000, "max": 5},
        "RTX_3070": {"name": "RTX 3070", "power": 5, "price": 50000, "max": 6},
        "RTX_3090": {"name": "RTX 3090", "power": 10, "price": 100000, "max": 5},
    }
    
    @classmethod
    def get_card_info(cls, card_type):
        """Get information about a card type"""
        return cls.CARDS.get(card_type, None)
    
    @classmethod
    def get_sell_price(cls, card_type):
        """Get resell price (75% of original)"""
        info = cls.get_card_info(card_type)
        if info:
            return int(info["price"] * 0.75)
        return 0


class Collectible:
    """Collectible items/trophies"""
    
    ITEMS = {
        "hashtag": {"symbol": "#", "name": "Trophy", "price": 1000000, "max": 9},
        "exclamation": {"symbol": "!", "name": "Pro Trader Trophy", "price": 50000000, "max": 9},
        "question": {"symbol": "?", "name": "99.99% Mining Trophy", "price": None, "max": 9},
    }
    
    @classmethod
    def get_item_info(cls, item_type):
        """Get information about an item type"""
        return cls.ITEMS.get(item_type, None)


class Wallet:
    """Player's wallet managing all assets"""
    
    def __init__(self, starting_dollar=250, starting_arobase=0):
        # Currencies
        self.dollar = starting_dollar
        self.arobase = starting_arobase
        self.arobase_for_sale = 0
        
        # Graphics cards
        self.cards = {
            "RTX_2080": 0,
            "RTX_3070": 0,
            "RTX_3090": 0,
        }
        
        # Collectibles
        self.collectibles = {
            "hashtag": 0,
            "exclamation": 0,
            "question": 0,
        }
        
        # Statistics
        self.max_dollar = starting_dollar
        self.min_dollar = starting_dollar
        self.max_arobase = starting_arobase
        self.min_arobase = starting_arobase
        
        # Victory flag
        self.victory_purchased = False
    
    def get_total_power(self):
        """Calculate total mining power"""
        power = 0
        for card_type, count in self.cards.items():
            card_info = GraphicsCard.get_card_info(card_type)
            if card_info:
                power += count * card_info["power"]
        return power
    
    def can_afford(self, cost):
        """Check if player can afford something"""
        return self.dollar >= cost
    
    def add_dollar(self, amount):
        """Add dollars to wallet"""
        self.dollar += amount
        self._update_stats()
    
    def remove_dollar(self, amount):
        """Remove dollars from wallet"""
        if amount > self.dollar:
            return False
        self.dollar -= amount
        self._update_stats()
        return True
    
    def add_arobase(self, amount):
        """Add arobase to wallet"""
        self.arobase += amount
        self._update_stats()
    
    def remove_arobase(self, amount):
        """Remove arobase from wallet"""
        if amount > self.arobase:
            return False
        self.arobase -= amount
        self._update_stats()
        return True
    
    def put_arobase_for_sale(self, amount):
        """Put arobase up for sale"""
        if amount > self.arobase:
            return False
        self.arobase -= amount
        self.arobase_for_sale += amount
        return True
    
    def cancel_sale(self):
        """Cancel arobase sale and return to wallet"""
        self.arobase += self.arobase_for_sale
        self.arobase_for_sale = 0
    
    def process_sale(self, sold_amount, dollar_received):
        """Process partial or complete sale"""
        if sold_amount > self.arobase_for_sale:
            sold_amount = self.arobase_for_sale
        
        self.arobase_for_sale -= sold_amount
        self.dollar += dollar_received
        self._update_stats()
        return sold_amount
    
    def buy_card(self, card_type):
        """Buy a graphics card"""
        card_info = GraphicsCard.get_card_info(card_type)
        if not card_info:
            return {"success": False, "error": "Invalid card type"}
        
        if self.cards[card_type] >= card_info["max"]:
            return {"success": False, "error": f"Maximum {card_info['max']} cards reached"}
        
        if not self.can_afford(card_info["price"]):
            return {"success": False, "error": "Insufficient funds"}
        
        self.dollar -= card_info["price"]
        self.cards[card_type] += 1
        self._update_stats()
        
        return {"success": True, "power": self.get_total_power()}
    
    def sell_card(self, card_type):
        """Sell a graphics card"""
        if self.cards.get(card_type, 0) == 0:
            return {"success": False, "error": "No cards to sell"}
        
        sell_price = GraphicsCard.get_sell_price(card_type)
        self.cards[card_type] -= 1
        self.dollar += sell_price
        self._update_stats()
        
        return {"success": True, "amount": sell_price}
    
    def buy_collectible(self, item_type):
        """Buy a collectible item"""
        item_info = Collectible.get_item_info(item_type)
        if not item_info:
            return {"success": False, "error": "Invalid item"}
        
        if item_info["price"] is None:
            return {"success": False, "error": "Cannot purchase this item"}
        
        if self.collectibles[item_type] >= item_info["max"]:
            return {"success": False, "error": f"Maximum {item_info['max']} items reached"}
        
        if not self.can_afford(item_info["price"]):
            return {"success": False, "error": "Insufficient funds"}
        
        self.dollar -= item_info["price"]
        self.collectibles[item_type] += 1
        self._update_stats()
        
        return {"success": True}
    
    def award_collectible(self, item_type):
        """Award a collectible (for achievements)"""
        item_info = Collectible.get_item_info(item_type)
        if not item_info:
            return False
        
        if self.collectibles[item_type] >= item_info["max"]:
            return False
        
        self.collectibles[item_type] += 1
        return True
    
    def buy_victory(self, cost_dollar=500000000, cost_arobase=600):
        """Purchase victory condition"""
        if self.victory_purchased:
            return {"success": False, "error": "Victory already purchased"}
        
        if self.dollar < cost_dollar:
            return {"success": False, "error": "Insufficient dollars"}
        
        if self.arobase < cost_arobase:
            return {"success": False, "error": "Insufficient arobase"}
        
        self.dollar -= cost_dollar
        self.arobase -= cost_arobase
        self.victory_purchased = True
        self._update_stats()
        
        return {"success": True}
    
    def calculate_score(self, current_course):
        """Calculate player's score"""
        # Total wealth in dollars
        total = self.dollar
        total += self.arobase * current_course
        total += self.arobase_for_sale * current_course
        
        # Add card values
        for card_type, count in self.cards.items():
            card_info = GraphicsCard.get_card_info(card_type)
            if card_info:
                total += count * card_info["price"]
        
        # Add collectible values
        for item_type, count in self.collectibles.items():
            item_info = Collectible.get_item_info(item_type)
            if item_info and item_info["price"]:
                total += count * item_info["price"]
        
        # Score formula from original game
        score = int(total * 0.8 * 0.001) - 17
        return max(0, score)
    
    def _update_stats(self):
        """Update min/max statistics"""
        if self.dollar > self.max_dollar:
            self.max_dollar = self.dollar
        if self.dollar < self.min_dollar:
            self.min_dollar = self.dollar
        
        if self.arobase > self.max_arobase:
            self.max_arobase = self.arobase
        if self.arobase < self.min_arobase:
            self.min_arobase = self.arobase
    
    def round_values(self):
        """Round currency values for cleaner display"""
        self.dollar = round(self.dollar, 2)
        self.arobase = round(self.arobase, 5)
        self.arobase_for_sale = round(self.arobase_for_sale, 5)
    
    def get_summary(self):
        """Get wallet summary"""
        return {
            "dollar": self.dollar,
            "arobase": self.arobase,
            "arobase_for_sale": self.arobase_for_sale,
            "total_power": self.get_total_power(),
            "cards": self.cards.copy(),
            "collectibles": self.collectibles.copy(),
            "victory": self.victory_purchased
        }
    
    def to_dict(self):
        """Convert wallet to dictionary"""
        return {
            "dollar": self.dollar,
            "arobase": self.arobase,
            "arobase_for_sale": self.arobase_for_sale,
            "cards": self.cards,
            "collectibles": self.collectibles,
            "max_dollar": self.max_dollar,
            "min_dollar": self.min_dollar,
            "max_arobase": self.max_arobase,
            "min_arobase": self.min_arobase,
            "victory_purchased": self.victory_purchased
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create wallet from dictionary"""
        wallet = cls(data.get("dollar", 250), data.get("arobase", 0))
        wallet.arobase_for_sale = data.get("arobase_for_sale", 0)
        wallet.cards = data.get("cards", wallet.cards)
        wallet.collectibles = data.get("collectibles", wallet.collectibles)
        wallet.max_dollar = data.get("max_dollar", wallet.dollar)
        wallet.min_dollar = data.get("min_dollar", wallet.dollar)
        wallet.max_arobase = data.get("max_arobase", wallet.arobase)
        wallet.min_arobase = data.get("min_arobase", wallet.arobase)
        wallet.victory_purchased = data.get("victory_purchased", False)
        return wallet


# Example usage
if __name__ == "__main__":
    wallet = Wallet()
    
    print("Initial Wallet:")
    print(f"Dollar: ${wallet.dollar}")
    print(f"Arobase: {wallet.arobase}@")
    print(f"Power: {wallet.get_total_power()}")
    
    # Buy a card
    print("\n--- Buying RTX 2080 ---")
    result = wallet.buy_card("RTX_2080")
    if result["success"]:
        print(f"✓ Card purchased! New power: {result['power']}")
        print(f"  Remaining: ${wallet.dollar}")
    
    # Add some arobase
    wallet.add_arobase(10.5)
    print(f"\n✓ Added 10.5@ -> Total: {wallet.arobase}@")
    
    # Put arobase for sale
    wallet.put_arobase_for_sale(5)
    print(f"\n✓ Put 5@ for sale")
    print(f"  Available: {wallet.arobase}@")
    print(f"  For sale: {wallet.arobase_for_sale}@")
    
    # Calculate score
    score = wallet.calculate_score(70)
    print(f"\nScore: {score}")
    
    # Show summary
    print("\nWallet Summary:")
    summary = wallet.get_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
