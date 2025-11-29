"""
Market System - Deterministic course generation
Based on seed for synchronized multiplayer
"""

import random
import json


class MarketGenerator:
    """Generates deterministic market course based on seed"""
    
    def __init__(self, seed, variation_range=50):
        self.seed = seed
        self.variation_range = variation_range
        self.course_cache = {}
        
    def _generate_number(self, seed_val, turn):
        """Generate a large number deterministically"""
        nb = seed_val
        t = 1
        while nb < 10**700:
            t += 1 + turn * seed_val
            nb = nb * t
        return nb
    
    def _round_value(self, value):
        """Round value with 0.5 threshold"""
        if value - int(value) > 0.5:
            value += 1
        return int(value)
    
    def generate_course_chunk(self, start_turn, end_turn, min_val, max_val):
        """Generate course values for a range of turns"""
        difference = max_val - min_val
        k = 4  # Precision factor
        
        nb_str = str(self._generate_number(self.seed, 1))
        t = 0
        
        for turn in range(start_turn, end_turn + 1):
            if turn in self.course_cache:
                continue
                
            t += k
            if t > 500:
                t = 0
                nb_str = str(self._generate_number(self.seed, turn))
            
            # Extract k digits from the string
            fin = 0
            for tt in range(k):
                if t + tt < len(nb_str):
                    fin += int(nb_str[t + tt]) * (10 ** tt)
            
            # Scale to range
            scaled = (fin * difference) / (10 ** k)
            course_value = self._round_value(scaled) + min_val
            
            self.course_cache[turn] = course_value
    
    def get_course(self, turn):
        """Get course value for a specific turn"""
        if turn not in self.course_cache:
            # Generate chunk if not cached
            self.generate_course_chunk(max(1, turn - 100), turn + 100, 
                                       -self.variation_range, 
                                       self.variation_range + 50)
        return self.course_cache.get(turn, 70)


class Market:
    """Market system managing course and transactions"""
    
    def __init__(self, seed, starting_course=70):
        self.generator = MarketGenerator(seed)
        self.current_turn = 0
        self.base_course = starting_course
        self.current_course = starting_course
        self.previous_course = starting_course
        self.course_max = starting_course
        self.course_min = starting_course
        self.history = {0: starting_course}
        
    def advance_turn(self):
        """Advance to next turn and update course"""
        self.current_turn += 1
        self.previous_course = self.current_course
        
        # Get variation from generator
        variation = self.generator.get_course(self.current_turn)
        
        # Apply decay for high values
        temp_decay = int(self.current_turn / 35)
        if temp_decay > 25:
            temp_decay = 25
        
        # Update course based on current value
        if self.current_course > 100:
            self.current_course += variation - temp_decay
            self.current_course = int(self.current_course)
        else:
            self.current_course += variation / 10
            self.current_course = int(self.current_course * 100) / 100
        
        # Minimum course value
        if self.current_course < 1:
            self.current_course = 1
        
        # Update extremes
        if self.current_course > self.course_max:
            self.course_max = self.current_course
        if self.current_course < self.course_min:
            self.course_min = self.current_course
        
        # Store in history
        self.history[self.current_turn] = self.current_course
        
        return self.current_course
    
    def get_course_change(self):
        """Get course change from previous turn"""
        return self.current_course - self.previous_course
    
    def calculate_buy_amount(self, dollars, tax=0):
        """Calculate how much arobase can be bought with dollars"""
        if dollars <= tax:
            return 0
        available = dollars - tax
        return available / self.current_course
    
    def calculate_sell_value(self, arobase):
        """Calculate dollar value of arobase"""
        return arobase * self.current_course
    
    def get_statistics(self):
        """Get market statistics"""
        if len(self.history) < 2:
            return {
                "max": self.course_max,
                "min": self.course_min,
                "average": self.current_course,
                "volatility": 0
            }
        
        total = sum(self.history.values())
        avg = total / len(self.history)
        
        # Calculate volatility (standard deviation)
        variance = sum((v - avg) ** 2 for v in self.history.values()) / len(self.history)
        volatility = variance ** 0.5
        
        return {
            "max": self.course_max,
            "min": self.course_min,
            "average": round(avg, 2),
            "volatility": round(volatility, 2)
        }
    
    def get_trend(self, window=5):
        """Get recent trend (positive/negative/stable)"""
        if len(self.history) < window:
            return "stable"
        
        recent_turns = sorted(self.history.keys())[-window:]
        recent_values = [self.history[t] for t in recent_turns]
        
        # Simple linear regression slope
        avg_turn = sum(recent_turns) / len(recent_turns)
        avg_value = sum(recent_values) / len(recent_values)
        
        numerator = sum((recent_turns[i] - avg_turn) * (recent_values[i] - avg_value) 
                       for i in range(len(recent_turns)))
        denominator = sum((t - avg_turn) ** 2 for t in recent_turns)
        
        if denominator == 0:
            return "stable"
        
        slope = numerator / denominator
        
        if slope > 1:
            return "rising"
        elif slope < -1:
            return "falling"
        else:
            return "stable"
    
    def to_dict(self):
        """Convert to dictionary for saving"""
        return {
            "seed": self.generator.seed,
            "current_turn": self.current_turn,
            "base_course": self.base_course,
            "current_course": self.current_course,
            "previous_course": self.previous_course,
            "course_max": self.course_max,
            "course_min": self.course_min,
            "history": self.history
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create market from dictionary"""
        market = cls(data["seed"], data["base_course"])
        market.current_turn = data["current_turn"]
        market.current_course = data["current_course"]
        market.previous_course = data["previous_course"]
        market.course_max = data["course_max"]
        market.course_min = data["course_min"]
        market.history = {int(k): v for k, v in data["history"].items()}
        return market


# Example usage
if __name__ == "__main__":
    # Create market with seed
    market = Market(seed=937962751)
    
    print("Turn | Course | Change | Trend")
    print("-" * 40)
    
    # Simulate 20 turns
    for _ in range(20):
        course = market.advance_turn()
        change = market.get_course_change()
        trend = market.get_trend()
        
        change_str = f"+{change:.2f}" if change > 0 else f"{change:.2f}"
        print(f"{market.current_turn:4d} | {course:6.2f} | {change_str:7s} | {trend}")
    
    print("\n" + "="*40)
    stats = market.get_statistics()
    print(f"Max: {stats['max']:.2f}")
    print(f"Min: {stats['min']:.2f}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Volatility: {stats['volatility']:.2f}")
