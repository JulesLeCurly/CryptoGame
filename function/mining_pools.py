"""
Mining System - Pool management and mining mechanics
"""

import random
import time


class MiningPool:
    """Base class for mining pools"""
    
    def __init__(self, pool_id, name, description):
        self.pool_id = pool_id
        self.name = name
        self.description = description
        self.cooldown_turns = 10  # Turns before can switch
    
    def get_bonus(self, power, gain):
        """Get mining bonus for this pool"""
        return {"arobase": gain, "dollar": 0}
    
    def on_sale(self, arobase_amount, course):
        """Called when player sells arobase"""
        return arobase_amount  # Return amount actually sold
    
    def get_info(self):
        """Get pool information"""
        return {
            "id": self.pool_id,
            "name": self.name,
            "description": self.description
        }


class NoPool(MiningPool):
    """No pool - solo mining"""
    
    def __init__(self):
        super().__init__(
            "SOLO",
            "Solo Mining",
            "Mine independently without pool benefits"
        )
    
    def get_bonus(self, power, gain):
        # Rare chance to get big reward when solo
        if random.randint(1, 200) == 1:
            jackpot = round((1000000 / 70) * 1000) / 1000
            return {"arobase": jackpot, "dollar": 0, "message": "🎰 SOLO JACKPOT!"}
        return {"arobase": 0, "dollar": 0}


class C53Pool(MiningPool):
    """C53 Pool - Balanced sharing with dollar bonus"""
    
    def __init__(self):
        super().__init__(
            "C53",
            "C53 Pool",
            "Balanced pool with $75 bonus per mining turn"
        )
    
    def get_bonus(self, power, gain):
        return {"arobase": 0, "dollar": 75}


class BTCPool(MiningPool):
    """BTC Pool - Arobase gain bonus"""
    
    def __init__(self):
        super().__init__(
            "BTC",
            "BTC Pool",
            "Receive +0.25@ bonus per mining turn"
        )
    
    def get_bonus(self, power, gain):
        return {"arobase": 0.25, "dollar": 0}


class FBGPool(MiningPool):
    """FBG Pool - Instant arobase sales"""
    
    def __init__(self):
        super().__init__(
            "FBG",
            "FBG Pool",
            "All arobase for sale is sold instantly"
        )
    
    def on_sale(self, arobase_amount, course):
        # FBG instantly sells everything
        return 0  # Nothing left for sale


class HelloPool(MiningPool):
    """HELLO Pool - Market alerts and analysis"""
    
    def __init__(self):
        super().__init__(
            "HELLO",
            "HELLO Pool",
            "Receive market alerts and course analysis tools"
        )
        self.alerts_enabled = True
    
    def check_extremes(self, current_course, course_max, course_min):
        """Check if course hit extremes"""
        alerts = []
        if current_course >= course_max:
            alerts.append("📈 ALERT: Course at ALL-TIME HIGH!")
        if current_course <= course_min:
            alerts.append("📉 ALERT: Course at ALL-TIME LOW!")
        return alerts


class ITSPool(MiningPool):
    """ITS Pool - Special pool with reduced malus"""
    
    def __init__(self):
        super().__init__(
            "ITS",
            "ITS Pool",
            "Privacy-focused pool with reduced random events"
        )
        self.malus_reduction = True
        self.secret_code = "3667"
    
    def get_bonus(self, power, gain):
        return {"arobase": 0, "dollar": 0}


class ITSPlusPool(ITSPool):
    """ITS+ Pool - Secret enhanced version"""
    
    def __init__(self):
        super().__init__()
        self.pool_id = "ITS+"
        self.name = "ITS+ Pool"
        self.description = "Enhanced ITS with welcome bonus and reduced malus"
        self.welcome_bonus = 250
    
    def get_welcome_bonus(self):
        """Get one-time welcome bonus"""
        bonus = self.welcome_bonus
        self.welcome_bonus = 0
        return bonus


class PlusPlusPool(MiningPool):
    """+=+ Pool - Risky pool with costs"""
    
    def __init__(self):
        super().__init__(
            "+=+",
            "+=+ Pool",
            "Risky pool - charges $1000 per turn. High risk, high reward?"
        )
    
    def get_bonus(self, power, gain):
        return {"arobase": 0, "dollar": -1000}


class MiningManager:
    """Manages mining operations and pool membership"""
    
    def __init__(self):
        self.pools = {
            "SOLO": NoPool(),
            "C53": C53Pool(),
            "BTC": BTCPool(),
            "FBG": FBGPool(),
            "HELLO": HelloPool(),
            "ITS": ITSPool(),
            "ITS+": ITSPlusPool(),
            "+=+": PlusPlusPool(),
        }
        
        self.current_pool = None
        self.cooldown_remaining = 0
        self.its_plus_unlocked = False
    
    def get_available_pools(self):
        """Get list of available pools"""
        available = []
        for pool_id, pool in self.pools.items():
            if pool_id == "ITS+" and not self.its_plus_unlocked:
                continue  # Hidden until unlocked
            if pool_id == "SOLO":
                continue  # Not shown in list
            available.append(pool.get_info())
        return available
    
    def can_switch_pool(self):
        """Check if player can switch pools"""
        return self.cooldown_remaining == 0
    
    def join_pool(self, pool_id, secret_code=None):
        """Join a mining pool"""
        if not self.can_switch_pool():
            return {
                "success": False,
                "error": f"Cooldown: {self.cooldown_remaining} turns remaining"
            }
        
        # Handle ITS+ secret code
        if pool_id == "ITS" and secret_code == "3667":
            pool_id = "ITS+"
            self.its_plus_unlocked = True
        
        if pool_id not in self.pools:
            return {"success": False, "error": "Invalid pool"}
        
        # Special check for ITS+
        if pool_id == "ITS+" and not self.its_plus_unlocked:
            return {"success": False, "error": "Invalid pool"}
        
        old_pool = self.current_pool
        self.current_pool = pool_id
        self.cooldown_remaining = 10
        
        result = {"success": True, "pool": self.pools[pool_id].name}
        
        # ITS+ welcome bonus (only first time)
        if pool_id == "ITS+" and isinstance(self.pools[pool_id], ITSPlusPool):
            bonus = self.pools[pool_id].get_welcome_bonus()
            if bonus > 0:
                result["welcome_bonus"] = bonus
                result["message"] = f"Welcome to ITS+! Received ${bonus}"
        
        return result
    
    def leave_pool(self):
        """Leave current pool"""
        self.current_pool = None
    
    def mine(self, power, base_gain):
        """Perform mining and get rewards"""
        if self.cooldown_remaining > 0:
            self.cooldown_remaining -= 1
        
        results = {"arobase": 0, "dollar": 0, "messages": []}
        
        # Base mining gain
        if self.current_pool and self.current_pool != "SOLO":
            mining_gain = (power + 1) / 100
            if mining_gain < 0.2:
                mining_gain = 0.2
            results["arobase"] += mining_gain
            results["messages"].append(f"⛏️ Mined {mining_gain:.2f}@")
        
        # Pool bonus
        if self.current_pool:
            pool = self.pools[self.current_pool]
            bonus = pool.get_bonus(power, base_gain)
            
            if bonus.get("arobase", 0) > 0:
                results["arobase"] += bonus["arobase"]
                results["messages"].append(f"🎁 Pool bonus: +{bonus['arobase']}@")
            
            if bonus.get("dollar", 0) != 0:
                results["dollar"] += bonus["dollar"]
                if bonus["dollar"] > 0:
                    results["messages"].append(f"🎁 Pool bonus: +${bonus['dollar']}")
                else:
                    results["messages"].append(f"💸 Pool fee: ${bonus['dollar']}")
            
            if "message" in bonus:
                results["messages"].append(bonus["message"])
        
        return results
    
    def process_sale(self, arobase_for_sale, course):
        """Process arobase sale through pool"""
        if not self.current_pool:
            # Random sale 70-100%
            sold = random.randint(int(arobase_for_sale * 0.7), int(arobase_for_sale))
            return sold
        
        pool = self.pools[self.current_pool]
        remaining = pool.on_sale(arobase_for_sale, course)
        
        if isinstance(pool, FBGPool):
            return arobase_for_sale  # All sold instantly
        else:
            # Random sale 70-100%
            sold = random.randint(int(arobase_for_sale * 0.7), int(arobase_for_sale))
            return sold
    
    def get_market_alerts(self, current_course, course_max, course_min):
        """Get market alerts if in HELLO pool"""
        if self.current_pool == "HELLO":
            pool = self.pools["HELLO"]
            return pool.check_extremes(current_course, course_max, course_min)
        return []
    
    def reduces_malus(self):
        """Check if current pool reduces malus"""
        if self.current_pool in ["ITS", "ITS+"]:
            return True
        return False
    
    def get_current_pool_name(self):
        """Get current pool name"""
        if not self.current_pool:
            return "Solo Mining"
        return self.pools[self.current_pool].name
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "current_pool": self.current_pool,
            "cooldown_remaining": self.cooldown_remaining,
            "its_plus_unlocked": self.its_plus_unlocked
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary"""
        manager = cls()
        manager.current_pool = data.get("current_pool")
        manager.cooldown_remaining = data.get("cooldown_remaining", 0)
        manager.its_plus_unlocked = data.get("its_plus_unlocked", False)
        return manager


# Example usage
if __name__ == "__main__":
    manager = MiningManager()
    
    print("Available Pools:")
    for pool in manager.get_available_pools():
        print(f"  [{pool['id']}] {pool['name']}")
        print(f"      {pool['description']}")
    
    print("\n--- Joining C53 Pool ---")
    result = manager.join_pool("C53")
    if result["success"]:
        print(f"✓ Joined {result['pool']}")
    
    print("\n--- Mining with 10 power ---")
    mining_result = manager.mine(power=10, base_gain=1.5)
    print(f"Arobase: +{mining_result['arobase']:.2f}")
    print(f"Dollar: +${mining_result['dollar']}")
    for msg in mining_result['messages']:
        print(f"  {msg}")
    
    print("\n--- Trying to switch immediately ---")
    result = manager.join_pool("BTC")
    if not result["success"]:
        print(f"✗ {result['error']}")
    
    print("\n--- Unlocking ITS+ ---")
    result = manager.join_pool("ITS", secret_code="3667")
    if not result["success"]:
        print(f"✗ {result['error']}")
