"""
Save System - Handles game saving/loading with optional encoding
"""

import json
import os
import random
from datetime import datetime


class SaveEncoder:
    """Encode/decode save data for basic protection"""
    
    @staticmethod
    def encode_value(value, key):
        """Encode a numeric value"""
        if not isinstance(value, (int, float)):
            return value
        
        # Multiply by random key
        encoded = value * key
        return encoded
    
    @staticmethod
    def decode_value(value, key):
        """Decode a numeric value"""
        if not isinstance(value, (int, float)):
            return value
        
        try:
            decoded = value / key
            return decoded
        except ZeroDivisionError:
            return value
    
    @staticmethod
    def generate_key():
        """Generate random encoding key"""
        return random.randint(50000, 1000000)


class SaveManager:
    """Manages game save and load operations"""
    
    def __init__(self, save_directory="Game_data/Parties"):
        self.save_directory = save_directory
        self.ensure_directory_exists()
    
    def ensure_directory_exists(self):
        """Create save directory if it doesn't exist"""
        os.makedirs(self.save_directory, exist_ok=True)
    
    def save_game(self, game_name, game_data, encode=True):
        """
        Save game data to file
        
        Args:
            game_name: Name of the save file
            game_data: Dictionary containing all game data
            encode: Whether to encode numeric values
        """
        save_path = os.path.join(self.save_directory, game_name)
        os.makedirs(save_path, exist_ok=True)
        
        file_path = os.path.join(save_path, "game_save.json")
        
        # Prepare save data
        save_dict = {
            "version": "2.0",
            "saved_at": datetime.now().isoformat(),
            "encoded": encode,
            "data": {}
        }
        
        if encode:
            # Generate encoding key
            key = SaveEncoder.generate_key()
            save_dict["key"] = key
            
            # Encode numeric values
            encoded_data = self._encode_data(game_data, key)
            save_dict["data"] = encoded_data
        else:
            save_dict["data"] = game_data
        
        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(save_dict, f, indent=4, ensure_ascii=False)
        
        return True
    
    def load_game(self, game_name):
        """
        Load game data from file
        
        Args:
            game_name: Name of the save file
        
        Returns:
            Dictionary containing game data or None if not found
        """
        file_path = os.path.join(self.save_directory, game_name, "game_save.json")
        
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                save_dict = json.load(f)
            
            # Check if data is encoded
            if save_dict.get("encoded", False):
                key = save_dict.get("key")
                if key is None:
                    return None
                
                # Decode data
                decoded_data = self._decode_data(save_dict["data"], key)
                return decoded_data
            else:
                return save_dict["data"]
                
        except (json.JSONDecodeError, KeyError):
            return None
    
    def _encode_data(self, data, key):
        """Recursively encode numeric values in dictionary"""
        if isinstance(data, dict):
            return {k: self._encode_data(v, key) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._encode_data(item, key) for item in data]
        elif isinstance(data, (int, float)):
            return SaveEncoder.encode_value(data, key)
        else:
            return data
    
    def _decode_data(self, data, key):
        """Recursively decode numeric values in dictionary"""
        if isinstance(data, dict):
            return {k: self._decode_data(v, key) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._decode_data(item, key) for item in data]
        elif isinstance(data, (int, float)):
            return SaveEncoder.decode_value(data, key)
        else:
            return data
    
    def list_saves(self):
        """List all available save files"""
        if not os.path.exists(self.save_directory):
            return []
        
        saves = []
        for item in os.listdir(self.save_directory):
            save_path = os.path.join(self.save_directory, item)
            if os.path.isdir(save_path):
                # Check if it has a save file
                save_file = os.path.join(save_path, "game_save.json")
                if os.path.exists(save_file):
                    try:
                        with open(save_file, 'r', encoding='utf-8') as f:
                            save_data = json.load(f)
                        
                        saves.append({
                            "name": item,
                            "saved_at": save_data.get("saved_at", "Unknown"),
                            "version": save_data.get("version", "Unknown")
                        })
                    except:
                        pass
        
        return saves
    
    def delete_save(self, game_name):
        """Delete a save file"""
        save_path = os.path.join(self.save_directory, game_name)
        
        if os.path.exists(save_path):
            import shutil
            shutil.rmtree(save_path)
            return True
        return False
    
    def get_most_recent_save(self):
        """Get the most recently saved game"""
        saves = self.list_saves()
        
        if not saves:
            return None
        
        # Sort by saved_at timestamp
        saves.sort(key=lambda x: x["saved_at"], reverse=True)
        return saves[0]["name"]


class AutoSaveManager:
    """Manages automatic saving"""
    
    def __init__(self, save_manager, interval_seconds=30):
        self.save_manager = save_manager
        self.interval_seconds = interval_seconds
        self.last_save_time = 0
    
    def should_auto_save(self, current_time):
        """Check if it's time to auto-save"""
        return (current_time - self.last_save_time) >= self.interval_seconds
    
    def auto_save(self, game_name, game_data, current_time):
        """Perform auto-save if needed"""
        if self.should_auto_save(current_time):
            print("\n~~~~~~~~~~~ AUTO-SAVE ~~~~~~~~~~~")
            success = self.save_manager.save_game(game_name, game_data)
            self.last_save_time = current_time
            if success:
                print("Game saved successfully!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            return success
        return False


# Example usage
if __name__ == "__main__":
    save_manager = SaveManager()
    
    # Example game data
    game_data = {
        "player": {
            "dollar": 1500.50,
            "arobase": 25.123,
            "cards": {"RTX_2080": 2, "RTX_3070": 1}
        },
        "market": {
            "turn": 50,
            "course": 125.75
        },
        "session": {
            "game_name": "test_game",
            "seed": 937962751
        }
    }
    
    print("Saving game with encoding...")
    save_manager.save_game("test_game", game_data, encode=True)
    print("✓ Saved\n")
    
    print("Loading game...")
    loaded_data = save_manager.load_game("test_game")
    
    if loaded_data:
        print("✓ Loaded successfully")
        print("\nLoaded data:")
        print(json.dumps(loaded_data, indent=2))
    else:
        print("✗ Failed to load")
    
    print("\n" + "="*60)
    print("Available saves:")
    for save in save_manager.list_saves():
        print(f"  - {save['name']} (saved: {save['saved_at']})")
