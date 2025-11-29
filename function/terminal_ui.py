"""
Terminal UI - Display and interface utilities
"""

import os
import sys


class TerminalUI:
    """Terminal user interface utilities"""
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_header(title, width=60):
        """Print a formatted header"""
        print("\n" + "="*width)
        print(title.center(width))
        print("="*width + "\n")
    
    @staticmethod
    def print_separator(width=60):
        """Print a separator line"""
        print("_"*width)
    
    @staticmethod
    def print_box(lines, width=60):
        """Print text in a box"""
        print("┌" + "─"*width + "┐")
        for line in lines:
            padding = width - len(line)
            print("│ " + line + " "*padding + "│")
        print("└" + "─"*width + "┘")
    
    @staticmethod
    def get_input(prompt, valid_options=None):
        """Get user input with optional validation"""
        while True:
            user_input = input(prompt).strip().lower()
            
            if valid_options is None:
                return user_input
            
            if user_input in valid_options:
                return user_input
            
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")
    
    @staticmethod
    def get_number_input(prompt, min_val=None, max_val=None):
        """Get numeric input with validation"""
        while True:
            try:
                value = float(input(prompt).strip())
                
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}")
                    continue
                
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}")
                    continue
                
                return value
            except ValueError:
                print("Please enter a valid number")
    
    @staticmethod
    def confirm(prompt):
        """Ask for yes/no confirmation"""
        response = TerminalUI.get_input(f"{prompt} (yes/no): ", ["yes", "no", "y", "n"])
        return response in ["yes", "y"]
    
    @staticmethod
    def pause(message="Press Enter to continue..."):
        """Pause and wait for user"""
        input(message)
    
    @staticmethod
    def display_market_status(market, wallet):
        """Display market and wallet status"""
        change = market.get_course_change()
        change_str = f"+{change:.2f}" if change > 0 else f"{change:.2f}"
        trend = market.get_trend()
        
        # Trend emoji
        trend_emoji = {
            "rising": "📈",
            "falling": "📉",
            "stable": "➡️"
        }
        
        print(f"\n{'='*60}")
        print(f"@ Course: ${market.current_course:.2f} [{change_str}] {trend_emoji.get(trend, '')}")
        print(f"Power: {wallet.get_total_power()} | Turn: {market.current_turn}")
        print(f"\nYou have: {wallet.arobase:.5f}@ and ${wallet.dollar:.2f}")
        
        if wallet.arobase_for_sale > 0:
            print(f"For sale: {wallet.arobase_for_sale:.5f}@")
        
        print(f"{'='*60}\n")
    
    @staticmethod
    def display_main_menu():
        """Display main menu options"""
        options = [
            "[V] Sell @",
            "[A] Buy @",
            "[E] Cancel sale",
            "[M] Mine",
            "",
            "[C] Shop",
            "[P] Mining Pools",
            "[Z] Exchange",
            "[L] Market Chart",
            "",
            "[I] Info/Save",
            "[Q] Quit"
        ]
        
        print("ACTIONS:")
        for i in range(0, len(options), 2):
            left = options[i] if i < len(options) else ""
            right = options[i+1] if i+1 < len(options) else ""
            print(f"  {left:<25} {right}")
        print()
    
    @staticmethod
    def display_shop_menu(wallet):
        """Display shop menu"""
        TerminalUI.print_header("SHOP")
        
        print(f"You have: ${wallet.dollar:.2f}\n")
        
        print("GRAPHICS CARDS:")
        cards = [
            ("1", "RTX 2080", 6000, 2, 5, wallet.cards["RTX_2080"]),
            ("2", "RTX 3070", 50000, 5, 6, wallet.cards["RTX_3070"]),
            ("3", "RTX 3090", 100000, 10, 5, wallet.cards["RTX_3090"]),
        ]
        
        for num, name, price, power, max_qty, owned in cards:
            print(f"  [{num}] {name:<12} ${price:>8} | Power: {power:<2} | Max: {max_qty} | Owned: {owned}")
        
        print("\nCOLLECTIBLES:")
        items = [
            ("4", "#", "Trophy", 1000000, wallet.collectibles["hashtag"]),
            ("5", "!", "Pro Trader Trophy", 50000000, wallet.collectibles["exclamation"]),
            ("6", "?", "99.99% Mining Trophy", "Achievement", wallet.collectibles["question"]),
        ]
        
        for num, symbol, name, price, owned in items:
            price_str = f"${price}" if isinstance(price, int) else price
            print(f"  [{num}] {symbol} {name:<20} {price_str:>12} | Owned: {owned}")
        
        if not wallet.victory_purchased:
            print("\nVICTORY:")
            print("  [7] ★ Victory            $500,000,000 + 600@")
        
        print("\nOTHER:")
        print("  [8] Sell graphics card")
        print("  [9] Back")
    
    @staticmethod
    def display_pool_menu(mining_manager):
        """Display mining pool menu"""
        TerminalUI.print_header("MINING POOLS")
        
        current = mining_manager.get_current_pool_name()
        print(f"Current Pool: {current}")
        
        if mining_manager.cooldown_remaining > 0:
            print(f"⏳ Cooldown: {mining_manager.cooldown_remaining} turns remaining\n")
        else:
            print("✓ Can switch pools\n")
        
        print("AVAILABLE POOLS:")
        pools = mining_manager.get_available_pools()
        
        for i, pool in enumerate(pools, 1):
            print(f"  [{i}] {pool['name']}")
            print(f"      {pool['description']}")
        
        print(f"\n  [8] Leave pool")
        print(f"  [9] Back")
    
    @staticmethod
    def display_chart(market, start_pos=None, end_pos=None):
        """Display market chart"""
        TerminalUI.print_header("MARKET CHART")
        
        if len(market.history) < 2:
            print("Not enough data to display chart")
            return
        
        # Default to full history if no range specified
        if start_pos is None:
            start_pos = 1
        if end_pos is None:
            end_pos = market.current_turn
        
        # Validate range
        if start_pos < 1 or end_pos > market.current_turn or start_pos >= end_pos:
            print("Invalid range")
            return
        
        # Extract data for range
        data_points = {}
        for turn in range(start_pos, end_pos + 1):
            if turn in market.history:
                data_points[turn] = market.history[turn]
        
        if not data_points:
            print("No data in range")
            return
        
        # Calculate chart dimensions
        chart_width = 60
        chart_height = 20
        
        # Find min/max in range
        values = list(data_points.values())
        min_val = min(values)
        max_val = max(values)
        
        if min_val == max_val:
            print("No variation in selected range")
            return
        
        # Create chart grid
        grid = [[' ' for _ in range(chart_width)] for _ in range(chart_height)]
        
        # Plot data
        turns = sorted(data_points.keys())
        for i, turn in enumerate(turns):
            x = int((i / len(turns)) * (chart_width - 1))
            value = data_points[turn]
            
            # Normalize to chart height
            normalized = (value - min_val) / (max_val - min_val)
            y = int(normalized * (chart_height - 1))
            y = chart_height - 1 - y  # Flip Y axis
            
            if 0 <= x < chart_width and 0 <= y < chart_height:
                grid[y][x] = '█'
        
        # Print chart
        print("┌" + "─"*chart_width + "┐")
        for row in grid:
            print("│" + "".join(row) + "│")
        print("└" + "─"*chart_width + "┘")
        
        # Print statistics
        print(f"\nRange: Turn {start_pos} to {end_pos}")
        print(f"Max: ${max_val:.2f} | Min: ${min_val:.2f}")
        avg = sum(values) / len(values)
        print(f"Average: ${avg:.2f}")
    
    @staticmethod
    def display_game_over(wallet, market, reason, victory=False):
        """Display game over screen"""
        TerminalUI.clear_screen()
        
        if victory:
            TerminalUI.print_header("🎉 VICTORY! 🎉")
        else:
            TerminalUI.print_header("GAME OVER")
        
        print(f"Reason: {reason}\n")
        
        print("FINAL STATS:")
        print(f"  Turns played: {market.current_turn}")
        print(f"  Final balance: ${wallet.dollar:.2f}")
        print(f"  Final arobase: {wallet.arobase:.5f}@")
        print(f"  Total power: {wallet.get_total_power()}")
        
        score = wallet.calculate_score(market.current_course)
        print(f"\n  FINAL SCORE: {score}")
        
        print("\nSTATISTICS:")
        print(f"  Max dollar: ${wallet.max_dollar:.2f}")
        print(f"  Min dollar: ${wallet.min_dollar:.2f}")
        print(f"  Max arobase: {wallet.max_arobase:.5f}@")
        print(f"  Min arobase: {wallet.min_arobase:.5f}@")
        
        market_stats = market.get_statistics()
        print(f"\nMARKET:")
        print(f"  Max course: ${market_stats['max']:.2f}")
        print(f"  Min course: ${market_stats['min']:.2f}")
        print(f"  Average: ${market_stats['average']:.2f}")
        
        print("\n" + "="*60 + "\n")


class ColorText:
    """ANSI color codes for terminal"""
    
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
    @staticmethod
    def colored(text, color):
        """Return colored text"""
        return f"{color}{text}{ColorText.RESET}"
    
    @staticmethod
    def success(text):
        """Green success message"""
        return ColorText.colored(f"✓ {text}", ColorText.GREEN)
    
    @staticmethod
    def error(text):
        """Red error message"""
        return ColorText.colored(f"✗ {text}", ColorText.RED)
    
    @staticmethod
    def warning(text):
        """Yellow warning message"""
        return ColorText.colored(f"⚠ {text}", ColorText.YELLOW)
    
    @staticmethod
    def info(text):
        """Cyan info message"""
        return ColorText.colored(f"ℹ {text}", ColorText.CYAN)


# Example usage
if __name__ == "__main__":
    from src.wallet_system import Wallet
    from src.market_system import Market
    
    ui = TerminalUI()
    wallet = Wallet()
    market = Market(937962751)
    
    # Simulate some turns
    for _ in range(10):
        market.advance_turn()
    
    wallet.dollar = 5000
    wallet.arobase = 25.5
    wallet.buy_card("RTX_2080")
    
    # Display examples
    ui.display_market_status(market, wallet)
    ui.display_main_menu()
    
    print("\n" + "="*60 + "\n")
    
    ui.display_shop_menu(wallet)
    
    print("\n" + "="*60 + "\n")
    
    # Color examples
    print(ColorText.success("Operation successful!"))
    print(ColorText.error("An error occurred"))
    print(ColorText.warning("Warning message"))
    print(ColorText.info("Information"))
