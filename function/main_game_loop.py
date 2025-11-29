"""
Main Game Loop - Complete game engine
Integrates all systems and manages game flow
"""

import time
import random
import sys
import os

# Import all game systems
try:
    from function.game_config import GameConfig, GameSession, GameMode, create_game_mode_selector
    from function.market_system import Market
    from function.wallet_system import Wallet, GraphicsCard
    from function.mining_pools import MiningManager
    from function.random_events import EventManager, PepeEvent, AchievementChecker
    from function.save_system import SaveManager, AutoSaveManager
    from function.exchange_qrcode import ExchangeManager
    from function.terminal_ui import TerminalUI, ColorText
except ImportError:
    print("Error: Missing required modules")
    print("Make sure all game modules are in the same directory")
    sys.exit(1)


class TraderGameLife:
    """Main game class orchestrating all systems"""
    
    def __init__(self):
        self.session = None
        self.market = None
        self.wallet = None
        self.mining_manager = None
        self.event_manager = None
        self.exchange_manager = None
        self.save_manager = SaveManager()
        self.auto_save = None
        
        self.ui = TerminalUI()
        self.running = False
        self.pepe_available = False
    
    def initialize_new_game(self, game_name, seed, game_mode):
        """Initialize a new game"""
        # Create game configuration
        config = GameConfig(game_mode)
        self.session = GameSession(game_name, seed, config)
        
        # Initialize market
        self.market = Market(seed, config.settings["starting_course"])
        
        # Initialize wallet
        self.wallet = Wallet(
            config.settings["starting_dollar"],
            config.settings["starting_arobase"]
        )
        
        # Initialize managers
        self.mining_manager = MiningManager()
        self.event_manager = EventManager()
        self.exchange_manager = ExchangeManager()
        
        # Auto-save manager
        self.auto_save = AutoSaveManager(self.save_manager)
        
        print(ColorText.success("Game initialized!"))
        self.ui.pause()
    
    def load_game(self, game_name):
        """Load an existing game"""
        data = self.save_manager.load_game(game_name)
        
        if data is None:
            print(ColorText.error(f"Could not load game: {game_name}"))
            return False
        
        try:
            # Restore session
            self.session = GameSession.from_dict(data["session"])
            
            # Restore market
            self.market = Market.from_dict(data["market"])
            
            # Restore wallet
            self.wallet = Wallet.from_dict(data["wallet"])
            
            # Restore mining manager
            self.mining_manager = MiningManager.from_dict(data["mining"])
            
            # Initialize managers that don't save state
            self.event_manager = EventManager()
            self.exchange_manager = ExchangeManager()
            
            # Auto-save manager
            self.auto_save = AutoSaveManager(self.save_manager)
            
            print(ColorText.success(f"Game loaded: {game_name}"))
            self.display_game_status()
            self.ui.pause()
            return True
            
        except (KeyError, ValueError) as e:
            print(ColorText.error(f"Corrupted save file: {e}"))
            return False
    
    def save_game(self):
        """Save current game state"""
        if self.session is None:
            print(ColorText.error("No active game to save"))
            return False
        
        # Update last update time
        self.session.last_update = time.time()
        
        # Prepare save data
        save_data = {
            "session": self.session.to_dict(),
            "market": self.market.to_dict(),
            "wallet": self.wallet.to_dict(),
            "mining": self.mining_manager.to_dict()
        }
        
        success = self.save_manager.save_game(
            self.session.game_name,
            save_data,
            encode=True
        )
        
        if success:
            print(ColorText.success("Game saved!"))
        else:
            print(ColorText.error("Failed to save game"))
        
        return success
    
    def display_game_status(self):
        """Display current game status"""
        print("\n" + "="*60)
        print(f"Game: {self.session.game_name}")
        print(f"Mode: {self.session.config.mode.value}")
        print(f"Seed: {self.session.seed}")
        
        if self.session.config.settings.get("time_limit"):
            print(f"Time remaining: {self.session.format_time_remaining()}")
        
        turns_remaining = self.session.get_turns_remaining()
        if turns_remaining is not None:
            print(f"Turns remaining: {turns_remaining}")
        
        print(f"\nTurn: {self.market.current_turn}")
        print(f"Balance: ${self.wallet.dollar:.2f} | {self.wallet.arobase:.5f}@")
        print(f"Power: {self.wallet.get_total_power()}")
        print(f"Pool: {self.mining_manager.get_current_pool_name()}")
        
        score = self.wallet.calculate_score(self.market.current_course)
        print(f"Score: {score}")
        print("="*60 + "\n")
    
    def process_turn(self):
        """Process game turn (mining, sales, events)"""
        self.session.turn_count += 1
        
        # Advance market
        self.market.advance_turn()
        
        # Check for market alerts (HELLO pool)
        alerts = self.mining_manager.get_market_alerts(
            self.market.current_course,
            self.market.course_max,
            self.market.course_min
        )
        for alert in alerts:
            print(ColorText.warning(alert))
        
        # Process arobase sales
        if self.wallet.arobase_for_sale > 0:
            sold_amount = self.mining_manager.process_sale(
                self.wallet.arobase_for_sale,
                self.market.current_course
            )
            
            if sold_amount > 0:
                dollar_received = sold_amount * self.market.current_course
                actual_sold = self.wallet.process_sale(sold_amount, dollar_received)
                print(ColorText.success(f"Sold {actual_sold:.5f}@ for ${dollar_received:.2f}"))
        
        # Mining rewards
        if self.mining_manager.current_pool:
            mining_result = self.mining_manager.mine(
                self.wallet.get_total_power(),
                self.session.config.settings.get("base_gain", 1.0)
            )
            
            if mining_result["arobase"] > 0:
                self.wallet.add_arobase(mining_result["arobase"])
            
            if mining_result["dollar"] != 0:
                if mining_result["dollar"] > 0:
                    self.wallet.add_dollar(mining_result["dollar"])
                else:
                    self.wallet.remove_dollar(abs(mining_result["dollar"]))
            
            for msg in mining_result["messages"]:
                print(msg)
        
        # Random events (malus)
        if self.session.config.settings.get("random_events", True):
            malus_level = self.calculate_malus_level()
            has_threshold = self.wallet.dollar > 1000
            reduces_malus = self.mining_manager.reduces_malus()
            
            if self.event_manager.should_trigger_event(malus_level, has_threshold, reduces_malus):
                event = self.event_manager.trigger_random_event(self.wallet.dollar)
                if event:
                    self.event_manager.display_event(event)
                    self.wallet.remove_dollar(event["cost"])
        
        # Check Pepe appearance
        if random.randint(1, 20) == 1:
            self.pepe_available = True
        
        # Round values
        self.wallet.round_values()
    
    def calculate_malus_level(self):
        """Calculate malus level from seed"""
        return int(self.session.seed / 10000)
    
    def calculate_tax(self):
        """Calculate transaction tax"""
        tax = int(self.wallet.max_dollar / 1000)
        return tax
    
    def handle_sell_arobase(self):
        """Handle selling arobase"""
        tax = self.calculate_tax()
        
        print(f"\nTax: ${tax}")
        print(f"Available: {self.wallet.arobase:.5f}@")
        
        amount = self.ui.get_number_input("Amount to sell (@): ", min_val=0)
        
        if amount == 0:
            return
        
        if amount > self.wallet.arobase:
            print(ColorText.error("Insufficient arobase"))
            return
        
        if not self.wallet.can_afford(tax):
            print(ColorText.error("Cannot afford tax"))
            return
        
        # Confirm
        dollar_value = amount * self.market.current_course
        print(f"\nSelling {amount:.5f}@ ≈ ${dollar_value:.2f}")
        
        if self.ui.confirm("Confirm"):
            self.wallet.put_arobase_for_sale(amount)
            self.wallet.remove_dollar(tax)
            print(ColorText.success("Put up for sale!"))
    
    def handle_buy_arobase(self):
        """Handle buying arobase"""
        tax = self.calculate_tax()
        max_spend = self.wallet.dollar - tax
        
        print(f"\nTax: ${tax}")
        print(f"Available to spend: ${max_spend:.2f}")
        print(f"Current course: ${self.market.current_course:.2f}")
        
        if max_spend <= 0:
            print(ColorText.error("Cannot afford tax"))
            return
        
        amount = self.ui.get_number_input("Amount to spend ($): ", min_val=0, max_val=max_spend)
        
        if amount == 0:
            return
        
        arobase_amount = self.market.calculate_buy_amount(amount, 0)
        
        print(f"\nBuying {arobase_amount:.5f}@ for ${amount:.2f}")
        
        if self.ui.confirm("Confirm"):
            self.wallet.remove_dollar(amount + tax)
            self.wallet.add_arobase(arobase_amount)
            print(ColorText.success(f"Bought {arobase_amount:.5f}@"))
    
    def handle_shop(self):
        """Handle shop menu"""
        while True:
            self.ui.clear_screen()
            self.ui.display_shop_menu(self.wallet)
            
            choice = input("\nChoice: ").strip()
            
            if choice == "1":  # RTX 2080
                result = self.wallet.buy_card("RTX_2080")
                if result["success"]:
                    print(ColorText.success(f"Bought RTX 2080! Power: {result['power']}"))
                else:
                    print(ColorText.error(result["error"]))
                self.ui.pause()
            
            elif choice == "2":  # RTX 3070
                result = self.wallet.buy_card("RTX_3070")
                if result["success"]:
                    print(ColorText.success(f"Bought RTX 3070! Power: {result['power']}"))
                else:
                    print(ColorText.error(result["error"]))
                self.ui.pause()
            
            elif choice == "3":  # RTX 3090
                result = self.wallet.buy_card("RTX_3090")
                if result["success"]:
                    print(ColorText.success(f"Bought RTX 3090! Power: {result['power']}"))
                else:
                    print(ColorText.error(result["error"]))
                self.ui.pause()
            
            elif choice == "4":  # Collectible #
                result = self.wallet.buy_collectible("hashtag")
                if result["success"]:
                    print(ColorText.success("Bought Trophy #!"))
                else:
                    print(ColorText.error(result["error"]))
                self.ui.pause()
            
            elif choice == "5":  # Collectible !
                result = self.wallet.buy_collectible("exclamation")
                if result["success"]:
                    print(ColorText.success("Bought Pro Trader Trophy !"))
                else:
                    print(ColorText.error(result["error"]))
                self.ui.pause()
            
            elif choice == "6":  # Info about ?
                print("\nThe [?] trophy is awarded for achieving 99.99% mining efficiency")
                self.ui.pause()
            
            elif choice == "7" and not self.wallet.victory_purchased:  # Victory
                result = self.wallet.buy_victory()
                if result["success"]:
                    print(ColorText.success("🎉 VICTORY PURCHASED! 🎉"))
                    self.ui.pause()
                    self.end_game(victory=True)
                    return
                else:
                    print(ColorText.error(result["error"]))
                self.ui.pause()
            
            elif choice == "8":  # Sell card
                self.handle_sell_card()
            
            elif choice == "9":
                break
            
            else:
                print("Invalid choice")
                self.ui.pause()
    
    def handle_sell_card(self):
        """Handle selling graphics cards"""
        print("\nSELL GRAPHICS CARD:")
        print("  [1] RTX 2080 - $4,500")
        print("  [2] RTX 3070 - $37,500")
        print("  [3] RTX 3090 - $75,000")
        
        choice = input("\nChoice: ").strip()
        
        card_map = {"1": "RTX_2080", "2": "RTX_3070", "3": "RTX_3090"}
        card_type = card_map.get(choice)
        
        if card_type:
            result = self.wallet.sell_card(card_type)
            if result["success"]:
                print(ColorText.success(f"Sold for ${result['amount']}"))
            else:
                print(ColorText.error(result["error"]))
        
        self.ui.pause()
    
    def handle_mining_pools(self):
        """Handle mining pool menu"""
        while True:
            self.ui.clear_screen()
            self.ui.display_pool_menu(self.mining_manager)
            
            choice = input("\nChoice: ").strip()
            
            pool_map = {
                "1": "C53",
                "2": "BTC",
                "3": "FBG",
                "4": "HELLO",
                "5": "ITS",
                "6": "+=+"
            }
            
            if choice in pool_map:
                # Check for secret code
                secret = None
                if choice == "5":
                    print("\n(Enter secret code or press Enter)")
                    secret = input("Code: ").strip()
                
                result = self.mining_manager.join_pool(pool_map[choice], secret)
                
                if result["success"]:
                    print(ColorText.success(f"Joined {result['pool']}!"))
                    
                    if "welcome_bonus" in result:
                        self.wallet.add_dollar(result["welcome_bonus"])
                        print(ColorText.success(result["message"]))
                else:
                    print(ColorText.error(result["error"]))
                
                self.ui.pause()
            
            elif choice == "8":
                self.mining_manager.leave_pool()
                print(ColorText.success("Left pool"))
                self.ui.pause()
            
            elif choice == "9":
                break
    
    def handle_exchange(self):
        """Handle exchange menu"""
        print("\nEXCHANGE:")
        print("  [1] Send")
        print("  [2] Receive")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            self.handle_send_exchange()
        elif choice == "2":
            self.handle_receive_exchange()
    
    def handle_send_exchange(self):
        """Handle sending exchange"""
        print("\n[1] Dollar  [2] Arobase")
        currency_choice = input("Currency: ").strip()
        
        if currency_choice == "1":
            currency_type = "dollar"
            available = self.wallet.dollar
        elif currency_choice == "2":
            currency_type = "arobase"
            available = self.wallet.arobase
        else:
            return
        
        print(f"\nAvailable: {available}")
        amount = self.ui.get_number_input("Amount to send: ", min_val=0, max_val=available)
        
        if amount == 0:
            return
        
        if self.ui.confirm("Confirm"):
            # Deduct from wallet
            if currency_type == "dollar":
                self.wallet.remove_dollar(amount)
            else:
                self.wallet.remove_arobase(amount)
            
            # Create exchange code
            code = self.exchange_manager.create_exchange_code(
                int(amount),
                currency_type,
                self.session.game_name
            )
            
            if code:
                self.exchange_manager.display_exchange_code(code)
    
    def handle_receive_exchange(self):
        """Handle receiving exchange"""
        print("\nEnter exchange code:")
        code_str = input("Code: ").strip()
        
        result = self.exchange_manager.receive_exchange(code_str)
        
        if result["success"]:
            if result["currency_type"] == "dollar":
                self.wallet.add_dollar(result["amount"])
            else:
                self.wallet.add_arobase(result["amount"])
            
            print(ColorText.success(
                f"Received {result['amount']} {result['currency_type'].upper()}!"
            ))
        else:
            print(ColorText.error(result["error"]))
        
        self.ui.pause()
    
    def handle_chart(self):
        """Handle market chart display"""
        self.ui.display_chart(self.market)
        self.ui.pause()
    
    def handle_info(self):
        """Handle info/save menu"""
        print("\nINFO & SAVE:")
        print("  [1] Save game")
        print("  [2] Game status")
        print("  [3] Statistics")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            self.save_game()
            self.ui.pause()
        elif choice == "2":
            self.display_game_status()
            self.ui.pause()
        elif choice == "3":
            self.display_statistics()
            self.ui.pause()
    
    def display_statistics(self):
        """Display detailed statistics"""
        print("\n" + "="*60)
        print("STATISTICS")
        print("="*60)
        
        print("\nWALLET:")
        print(f"  Max dollar: ${self.wallet.max_dollar:.2f}")
        print(f"  Min dollar: ${self.wallet.min_dollar:.2f}")
        print(f"  Max arobase: {self.wallet.max_arobase:.5f}@")
        print(f"  Min arobase: {self.wallet.min_arobase:.5f}@")
        
        print("\nMARKET:")
        stats = self.market.get_statistics()
        print(f"  Max course: ${stats['max']:.2f}")
        print(f"  Min course: ${stats['min']:.2f}")
        print(f"  Average: ${stats['average']:.2f}")
        print(f"  Volatility: {stats['volatility']:.2f}")
        
        print("\nPORTFOLIO:")
        for card_type, count in self.wallet.cards.items():
            if count > 0:
                print(f"  {card_type}: {count}")
        
        for item_type, count in self.wallet.collectibles.items():
            if count > 0:
                print(f"  {item_type}: {count}")
        
        print("="*60)
    
    def check_game_over_conditions(self):
        """Check if game should end"""
        # Bankruptcy
        if self.wallet.dollar < 0:
            self.end_game(reason="Bankruptcy - Negative balance")
            return True
        
        # Time/turn limit
        if self.session.is_game_over():
            reason = "Time limit reached" if self.session.is_time_expired() else "Turn limit reached"
            self.end_game(reason=reason)
            return True
        
        # Victory condition
        if self.wallet.victory_purchased:
            self.end_game(victory=True)
            return True
        
        return False
    
    def end_game(self, reason="Game ended", victory=False):
        """End game and show final screen"""
        self.ui.display_game_over(self.wallet, self.market, reason, victory)
        self.running = False
    
    def main_loop(self):
        """Main game loop"""
        self.running = True
        
        while self.running:
            # Auto-save
            if self.auto_save:
                self.auto_save.auto_save(
                    self.session.game_name,
                    {
                        "session": self.session.to_dict(),
                        "market": self.market.to_dict(),
                        "wallet": self.wallet.to_dict(),
                        "mining": self.mining_manager.to_dict()
                    },
                    time.time()
                )
            
            # Check game over
            if self.check_game_over_conditions():
                break
            
            # Display status
            self.ui.clear_screen()
            self.ui.display_market_status(self.market, self.wallet)
            self.ui.display_main_menu()
            
            if self.pepe_available:
                print(ColorText.info("[PEPE] Pepe the Frog appeared!"))
            
            self.ui.print_separator()
            
            # Get action
            action = input("Action: ").strip().lower()
            
            # Handle actions
            if action == "v":
                self.handle_sell_arobase()
            elif action == "a":
                self.handle_buy_arobase()
            elif action == "e":
                self.wallet.cancel_sale()
                print(ColorText.success("Sale cancelled"))
                self.ui.pause()
            elif action == "m":
                self.process_turn()
                self.ui.pause()
            elif action == "c":
                self.handle_shop()
            elif action == "p":
                self.handle_mining_pools()
            elif action == "z":
                self.handle_exchange()
            elif action == "l":
                self.handle_chart()
            elif action == "i":
                self.handle_info()
            elif action == "pepe" and self.pepe_available:
                result = PepeEvent.trigger_pepe(self.market.current_course)
                self.wallet.dollar *= result["multiplier"]
                self.pepe_available = False
                self.ui.pause()
            elif action == "q":
                if self.ui.confirm("Save before quitting?"):
                    self.save_game()
                self.running = False
            else:
                print("Invalid action")
                self.ui.pause()


def main_menu():
    """Main menu"""
    game = TraderGameLife()
    ui = TerminalUI()
    
    ui.clear_screen()
    ui.print_header("TRADER GAME LIFE")
    print("A cryptocurrency trading and mining simulation game\n")
    
    # Check for existing saves
    saves = game.save_manager.list_saves()
    
    if saves:
        print("OPTIONS:")
        print("  [1] Continue most recent game")
        print("  [2] Load game")
        print("  [3] New game")
        print("  [4] Exit")
        
        choice = ui.get_input("\nChoice: ", ["1", "2", "3", "4"])
        
        if choice == "1":
            recent_save = game.save_manager.get_most_recent_save()
            if game.load_game(recent_save):
                game.main_loop()
        
        elif choice == "2":
            print("\nAvailable saves:")
            for i, save in enumerate(saves, 1):
                print(f"  [{i}] {save['name']} - {save['saved_at']}")
            
            save_num = int(ui.get_input("\nSelect save: ")) - 1
            if 0 <= save_num < len(saves):
                if game.load_game(saves[save_num]["name"]):
                    game.main_loop()
        
        elif choice == "3":
            start_new_game(game)
        
    else:
        print("No saved games found. Starting new game...\n")
        ui.pause()
        start_new_game(game)


def start_new_game(game):
    """Start a new game"""
    ui = TerminalUI()
    
    # Select game mode
    mode = create_game_mode_selector()
    
    # Get game name
    game_name = input("\nEnter game name: ").strip()
    if not game_name:
        game_name = f"game_{int(time.time())}"
    
    # Get seed
    print("\nSeed options:")
    print("  [1] Random seed")
    print("  [2] Enter custom seed")
    print("  [3] Quick start (seed: 35042)")
    
    seed_choice = ui.get_input("Choice: ", ["1", "2", "3"])
    
    if seed_choice == "1":
        seed = random.randint(10000, 99999)
    elif seed_choice == "2":
        seed = int(ui.get_number_input("Enter seed: ", min_val=0, max_val=99999))
    else:
        seed = 35042
    
    print(f"\nGame seed: {seed}")
    
    # Initialize and start
    game.initialize_new_game(game_name, seed, mode)
    game.main_loop()


def start_game():
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        import traceback
        traceback.print_exc()
