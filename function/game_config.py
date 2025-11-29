"""
Game Configuration System
Manages different game modes and settings
"""

import json
import time
from enum import Enum

class GameMode(Enum):
    """Different game modes available"""
    UNLIMITED = "unlimited"
    TIME_LIMITED = "time_limited"
    COMPETITIVE = "competitive"
    TUTORIAL = "tutorial"

class GameConfig:
    """Configuration for a game session"""
    
    def __init__(self, mode=GameMode.UNLIMITED):
        self.mode = mode
        self.settings = self._get_default_settings(mode)
    
    def _get_default_settings(self, mode):
        """Get default settings based on game mode"""
        base_settings = {
            "starting_dollar": 250,
            "starting_arobase": 0,
            "starting_course": 70,
            "tax_enabled": True,
            "random_events": True,
            "mining_enabled": True,
            "pools_enabled": True,
            "exchange_enabled": True,
            "twitter_enabled": True,
        }
        
        if mode == GameMode.UNLIMITED:
            return {
                **base_settings,
                "time_limit": None,
                "turn_limit": None,
                "difficulty": "normal",
            }
        
        elif mode == GameMode.TIME_LIMITED:
            return {
                **base_settings,
                "time_limit": 7 * 24 * 3600,  # 7 days in seconds
                "turn_limit": None,
                "turn_duration": 1800,  # 30 minutes per turn
                "difficulty": "normal",
            }
        
        elif mode == GameMode.COMPETITIVE:
            return {
                **base_settings,
                "time_limit": 3 * 24 * 3600,  # 3 days
                "turn_limit": 100,
                "turn_duration": 1800,
                "difficulty": "hard",
                "shared_seed": True,  # All players use same seed
                "leaderboard_enabled": True,
            }
        
        elif mode == GameMode.TUTORIAL:
            return {
                **base_settings,
                "starting_dollar": 1000,
                "time_limit": None,
                "turn_limit": 20,
                "random_events": False,
                "difficulty": "easy",
                "hints_enabled": True,
            }
        
        return base_settings
    
    def to_dict(self):
        """Convert config to dictionary"""
        return {
            "mode": self.mode.value,
            "settings": self.settings
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create config from dictionary"""
        mode = GameMode(data["mode"])
        config = cls(mode)
        config.settings = data["settings"]
        return config
    
    def save_to_file(self, filepath):
        """Save configuration to file"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=4)
    
    @classmethod
    def load_from_file(cls, filepath):
        """Load configuration from file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)


class GameSession:
    """Manages a game session with its configuration"""
    
    def __init__(self, game_name, seed, config):
        self.game_name = game_name
        self.seed = seed
        self.sync_seed = seed  # For market synchronization
        self.config = config
        self.created_at = time.time()
        self.last_update = time.time()
        self.turn_count = 0
        
    def is_time_expired(self):
        """Check if game time limit is exceeded"""
        if self.config.settings.get("time_limit") is None:
            return False
        
        elapsed = time.time() - self.created_at
        return elapsed >= self.config.settings["time_limit"]
    
    def is_turn_limit_reached(self):
        """Check if turn limit is reached"""
        turn_limit = self.config.settings.get("turn_limit")
        if turn_limit is None:
            return False
        return self.turn_count >= turn_limit
    
    def is_game_over(self):
        """Check if game should end"""
        return self.is_time_expired() or self.is_turn_limit_reached()
    
    def get_time_remaining(self):
        """Get remaining time in seconds"""
        if self.config.settings.get("time_limit") is None:
            return None
        
        elapsed = time.time() - self.created_at
        remaining = self.config.settings["time_limit"] - elapsed
        return max(0, remaining)
    
    def get_turns_remaining(self):
        """Get remaining turns"""
        turn_limit = self.config.settings.get("turn_limit")
        if turn_limit is None:
            return None
        return max(0, turn_limit - self.turn_count)
    
    def format_time_remaining(self):
        """Format remaining time as string"""
        remaining = self.get_time_remaining()
        if remaining is None:
            return "Unlimited"
        
        days = int(remaining // 86400)
        hours = int((remaining % 86400) // 3600)
        minutes = int((remaining % 3600) // 60)
        seconds = int(remaining % 60)
        
        return f"{days}d {hours}h {minutes}m {seconds}s"
    
    def to_dict(self):
        """Convert session to dictionary"""
        return {
            "game_name": self.game_name,
            "seed": self.seed,
            "sync_seed": self.sync_seed,
            "config": self.config.to_dict(),
            "created_at": self.created_at,
            "last_update": self.last_update,
            "turn_count": self.turn_count,
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create session from dictionary"""
        config = GameConfig.from_dict(data["config"])
        session = cls(data["game_name"], data["seed"], config)
        session.sync_seed = data.get("sync_seed", data["seed"])
        session.created_at = data["created_at"]
        session.last_update = data["last_update"]
        session.turn_count = data["turn_count"]
        return session


def create_game_mode_selector():
    """Interactive game mode selector"""
    print("\n" + "="*60)
    print("SELECT GAME MODE".center(60))
    print("="*60)
    
    modes = [
        ("1", "Unlimited", "Play without time or turn limits"),
        ("2", "Time Limited", "7-day challenge mode"),
        ("3", "Competitive", "3-day competitive mode with friends"),
        ("4", "Tutorial", "Learn the game basics"),
    ]
    
    for num, name, desc in modes:
        print(f"\n  [{num}] {name}")
        print(f"      {desc}")
    
    print("\n" + "="*60)
    
    choice = input("\nSelect mode (1-4): ").strip()
    
    mode_map = {
        "1": GameMode.UNLIMITED,
        "2": GameMode.TIME_LIMITED,
        "3": GameMode.COMPETITIVE,
        "4": GameMode.TUTORIAL,
    }
    
    return mode_map.get(choice, GameMode.UNLIMITED)


# Example usage
if __name__ == "__main__":
    # Create a competitive game session
    mode = GameMode.COMPETITIVE
    config = GameConfig(mode)
    session = GameSession("my_competitive_game", 937962751, config)
    
    print(f"Game: {session.game_name}")
    print(f"Mode: {session.config.mode.value}")
    print(f"Time remaining: {session.format_time_remaining()}")
    print(f"Turns remaining: {session.get_turns_remaining()}")
    print(f"\nSettings:")
    for key, value in session.config.settings.items():
        print(f"  {key}: {value}")
