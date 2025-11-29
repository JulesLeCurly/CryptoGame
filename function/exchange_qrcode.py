"""
Exchange System with QR Code generation for terminal
Allows players to exchange currency using time-limited codes
"""

import time
import random
import json


class ExchangeCode:
    """Represents a time-limited exchange code"""
    
    def __init__(self, amount, currency_type, sender_id):
        self.amount = amount
        self.currency_type = currency_type  # 'dollar' or 'arobase'
        self.sender_id = sender_id
        self.created_at = time.time()
        self.expires_in = 60  # seconds
        self.code = self._generate_code()
    
    def _generate_code(self):
        """Generate encoded exchange code"""
        # Encode: amount, timestamp, currency type, random divider
        security_id = int(time.time() % 1000000)
        encoded = int(self.amount * 1000000 + security_id)
        
        divider = random.randint(70, 99)
        tip = 1 if self.currency_type == 'dollar' else 2
        
        code = ((encoded * 1000) + (tip * 100)) * divider
        code = code + divider
        
        # Replace digits with letters for obfuscation
        code_str = str(code).replace('3', 'e').replace('8', 'm')
        code_str = code_str.replace('7', 'j').replace('5', 't')
        
        return code_str
    
    def is_expired(self):
        """Check if code has expired"""
        return (time.time() - self.created_at) > self.expires_in
    
    def time_remaining(self):
        """Get remaining time in seconds"""
        elapsed = time.time() - self.created_at
        remaining = self.expires_in - elapsed
        return max(0, int(remaining))
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "code": self.code,
            "amount": self.amount,
            "currency_type": self.currency_type,
            "sender_id": self.sender_id,
            "created_at": self.created_at,
            "expires_in": self.expires_in
        }


class ExchangeCodeDecoder:
    """Decodes exchange codes"""
    
    @staticmethod
    def decode(code_str):
        """Decode an exchange code"""
        try:
            # Reverse letter replacements
            code_str = code_str.replace('e', '3').replace('m', '8')
            code_str = code_str.replace('j', '7').replace('t', '5')
            code = int(code_str)
            
            # Extract divider
            divider = code % 100
            if divider < 70 or divider > 99:
                return None
            
            # Extract encoded value
            code = code // 100
            encoded = code // divider
            
            # Extract currency type
            tip = encoded % 10
            if tip not in [1, 2]:
                return None
            currency_type = 'dollar' if tip == 1 else 'arobase'
            
            # Extract amount and timestamp
            encoded = encoded // 10
            timestamp = encoded % 1000000
            amount = encoded // 1000000
            
            # Verify timestamp is reasonable
            current_time = int(time.time() % 1000000)
            time_diff = abs(current_time - timestamp)
            
            # Code is valid if within 60 seconds
            if time_diff > 60 and time_diff < 999940:  # Account for wraparound
                return None
            
            return {
                "amount": amount,
                "currency_type": currency_type,
                "timestamp": timestamp
            }
            
        except (ValueError, ZeroDivisionError):
            return None


class QRCodeGenerator:
    """Generate ASCII QR-like codes for terminal display"""
    
    @staticmethod
    def generate_simple_qr(data, size=25):
        """Generate a simple visual representation"""
        # Use hash of data to create pattern
        hash_val = hash(data)
        random.seed(hash_val)
        
        # Create border
        result = []
        result.append("┌" + "─" * (size + 2) + "┐")
        
        # Create pattern grid
        for i in range(size):
            row = "│ "
            for j in range(size):
                # Use pseudo-random pattern based on position and hash
                val = (hash_val + i * 17 + j * 31) % 2
                row += "█" if val else " "
            row += " │"
            result.append(row)
        
        result.append("└" + "─" * (size + 2) + "┘")
        
        return "\n".join(result)
    
    @staticmethod
    def generate_compact_visual(code_str):
        """Generate compact visual code representation"""
        lines = []
        lines.append("╔═══════════════════════════════╗")
        lines.append("║      EXCHANGE CODE            ║")
        lines.append("╠═══════════════════════════════╣")
        
        # Split code into chunks for readability
        chunk_size = 8
        chunks = [code_str[i:i+chunk_size] for i in range(0, len(code_str), chunk_size)]
        
        for chunk in chunks:
            lines.append(f"║  {chunk:<27s}  ║")
        
        lines.append("╠═══════════════════════════════╣")
        lines.append("║  Scan or enter manually       ║")
        lines.append("╚═══════════════════════════════╝")
        
        return "\n".join(lines)


class ExchangeManager:
    """Manages exchange operations between players"""
    
    def __init__(self):
        self.active_code = None
    
    def create_exchange_code(self, amount, currency_type, sender_id):
        """Create a new exchange code"""
        if self.active_code and not self.active_code.is_expired():
            return None  # Already have active code
        
        self.active_code = ExchangeCode(amount, currency_type, sender_id)
        return self.active_code
    
    def get_active_code(self):
        """Get current active code if not expired"""
        if self.active_code and self.active_code.is_expired():
            self.active_code = None
        return self.active_code
    
    def receive_exchange(self, code_str):
        """Receive currency using a code"""
        decoded = ExchangeCodeDecoder.decode(code_str)
        
        if decoded is None:
            return {"success": False, "error": "Invalid code"}
        
        return {
            "success": True,
            "amount": decoded["amount"],
            "currency_type": decoded["currency_type"]
        }
    
    def display_exchange_code(self, exchange_code):
        """Display exchange code with visual elements"""
        print("\n" + "="*60)
        print("EXCHANGE CODE GENERATED".center(60))
        print("="*60)
        
        print(f"\nAmount: {exchange_code.amount} {exchange_code.currency_type.upper()}")
        print(f"Expires in: {exchange_code.time_remaining()} seconds")
        
        print("\n" + QRCodeGenerator.generate_compact_visual(exchange_code.code))
        
        print(f"\nCode: {exchange_code.code}")
        print("\nShare this code with the receiver.")
        print("="*60 + "\n")


# Example usage
if __name__ == "__main__":
    manager = ExchangeManager()
    
    # Create exchange code
    print("Creating exchange code for 100 dollars...")
    code = manager.create_exchange_code(100, "dollar", "player1")
    
    if code:
        manager.display_exchange_code(code)
        
        # Simulate receiving
        print("\n\nReceiving exchange...")
        result = manager.receive_exchange(code.code)
        
        if result["success"]:
            print(f"✓ Received: {result['amount']} {result['currency_type']}")
        else:
            print(f"✗ Error: {result['error']}")
    
    # Test with expired code
    print("\n\nWaiting for code to expire...")
    time.sleep(61)
    
    result = manager.receive_exchange(code.code)
    if not result["success"]:
        print(f"✗ Code expired: {result['error']}")
