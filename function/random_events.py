"""
Random Events System - Manages malus events and random occurrences
"""

import random


class RandomEvent:
    """Base class for random events"""
    
    def __init__(self, event_id, title, min_cost_percent, max_cost_percent):
        self.event_id = event_id
        self.title = title
        self.min_cost_percent = min_cost_percent
        self.max_cost_percent = max_cost_percent
    
    def calculate_cost(self, player_dollar):
        """Calculate event cost based on player's wealth"""
        base_cost = random.randint(10, 20)
        percent_cost = random.randint(
            int(player_dollar * self.min_cost_percent),
            int(player_dollar * self.max_cost_percent)
        )
        return base_cost + percent_cost
    
    def get_description(self, cost):
        """Get event description with cost"""
        return f"{self.title} - Cost: ${cost}"


class EventManager:
    """Manages random events that cost the player money"""
    
    def __init__(self):
        self.events = [
            RandomEvent(1, "You didn't declare your pool!", 0.005, 0.1),
            RandomEvent(2, "It's just another day", 0.005, 0.1),
            RandomEvent(3, "Time for grocery shopping", 0.005, 0.1),
            RandomEvent(4, "You've been robbed!", 0.1, 0.3),
            RandomEvent(5, "It's your friend's birthday", 0.005, 0.1),
            RandomEvent(6, "Netflix subscription", 0.001, 0.05),
            RandomEvent(7, "Gas bill", 0.01, 0.15),
            RandomEvent(8, "Electricity bill", 0.01, 0.15),
            RandomEvent(9, "Water bill", 0.005, 0.1),
            RandomEvent(10, "Need to buy a new fridge", 0.05, 0.2),
            RandomEvent(11, "Gave money to a homeless person", 0.001, 0.05),
            RandomEvent(12, "Roof leak repair", 0.05, 0.15),
            RandomEvent(13, "Wondering if you still have money", 0.005, 0.1),
            RandomEvent(14, "Graphics card broke", 0.1, 0.25),
            RandomEvent(15, "Caught a cold", 0.02, 0.1),
            RandomEvent(16, "Hospital visit for injury", 0.1, 0.3),
            RandomEvent(17, "Got scammed!", 0.15, 0.35),
            RandomEvent(18, "Annoying friend needs money", 0.05, 0.15),
            RandomEvent(19, "Need transportation - new car", 0.2, 0.5),
            RandomEvent(20, "Tuition fees", 0.1, 0.3),
            RandomEvent(21, "Cat destroyed mining rig", 0.15, 0.3),
            RandomEvent(22, "Cat died - vet bills", 0.05, 0.15),
            RandomEvent(23, "Speeding ticket", 0.02, 0.1),
            RandomEvent(24, "Phone bill", 0.005, 0.05),
            RandomEvent(25, "Restaurant bill", 0.01, 0.1),
            RandomEvent(26, "Didn't win the lottery", 0.005, 0.1),
        ]
    
    def should_trigger_event(self, malus_level, has_dollar_threshold, pool_reduces_malus):
        """Determine if an event should trigger"""
        if not has_dollar_threshold:
            return False
        
        # Base chance from malus level
        roll = random.randint(0, 9)
        
        if pool_reduces_malus:
            # ITS/ITS+ pools reduce malus chance
            malus_level = max(0, malus_level - 1)
        
        return roll <= malus_level
    
    def trigger_random_event(self, player_dollar):
        """Trigger a random event and return details"""
        if player_dollar <= 0:
            return None
        
        # Select random event
        event = random.choice(self.events)
        cost = event.calculate_cost(player_dollar)
        
        # Ensure cost doesn't exceed player's money
        cost = min(cost, int(player_dollar * 0.5))  # Max 50% of wealth
        
        return {
            "title": event.title,
            "cost": cost,
            "description": event.get_description(cost)
        }
    
    def display_event(self, event_info):
        """Display event to player"""
        print("\n" + "="*60)
        print("⚠️  RANDOM EVENT".center(60))
        print("="*60)
        print(f"\n{event_info['title']}")
        print(f"\nYou lost: ${event_info['cost']}")
        print("\n" + "="*60 + "\n")


class PepeEvent:
    """Special Pepe the Frog event - Quiz for money multiplier"""
    
    QUESTIONS = [
        {"question": "How much does an RTX 2080 cost?", "answer": 6000},
        {"question": "How much does an RTX 3070 cost?", "answer": 50000},
        {"question": "How much does an RTX 3090 cost?", "answer": 100000},
        {"question": "How much does the [#] trophy cost?", "answer": 1000000},
        {"question": "How much does the [!] trophy cost?", "answer": 50000000},
        {"question": "How much dollar does C53 pool give per turn?", "answer": 75},
    ]
    
    @staticmethod
    def trigger_pepe(current_course=None):
        """Trigger Pepe quiz event"""
        print("\n" + "="*60)
        print("🐸 PEPE THE FROG APPEARS!".center(60))
        print("="*60)
        print("\nPepe: Hello! I am Pepe the Frog.")
        print("Pepe: Are you ready?")
        
        response = input("\nAnswer 'yes' or 'no': ").lower().strip()
        
        if response != "yes":
            print("\nPepe: Okay, see you next time!")
            return {"success": False, "multiplier": 1.0}
        
        print("\nPepe: Let's see if you deserve your money!")
        
        # Select random question
        question_data = random.choice(PepeEvent.QUESTIONS)
        
        # If asking about course, use current course
        if current_course and random.randint(1, 3) == 1:
            question_data = {
                "question": "What was the last @ course value?",
                "answer": int(current_course)
            }
        
        print(f"\nQuestion: {question_data['question']}")
        
        try:
            answer = float(input("Your answer: "))
            
            if answer == question_data['answer']:
                print("\n✓ Correct!")
                print("Pepe: You deserve your money!")
                print("Pepe: I will multiply it by 1.5!")
                return {"success": True, "multiplier": 1.5}
            else:
                print("\n✗ Wrong!")
                print("Pepe: Too bad, I'll have to divide your money by 2")
                print("Pepe: Maybe next time you'll be more worthy.")
                return {"success": False, "multiplier": 0.5}
                
        except ValueError:
            print("\nPepe: Do you even speak our language?")
            return {"success": False, "multiplier": 1.0}
    
    @staticmethod
    def should_appear():
        """Check if Pepe should appear (1/20 chance)"""
        return random.randint(1, 20) == 1


class AchievementChecker:
    """Check for special achievements"""
    
    @staticmethod
    def check_mining_achievement(mining_percentage):
        """Check if player reached 99.99% mining efficiency"""
        return mining_percentage >= 99.99
    
    @staticmethod
    def check_bankruptcy(dollar_amount):
        """Check if player is bankrupt"""
        return dollar_amount < 0


# Example usage
if __name__ == "__main__":
    event_manager = EventManager()
    
    print("Simulating random events...\n")
    
    player_dollar = 10000
    malus_level = 2
    
    for i in range(5):
        print(f"--- Turn {i+1} ---")
        
        # Check if event triggers
        if event_manager.should_trigger_event(malus_level, True, False):
            event = event_manager.trigger_random_event(player_dollar)
            if event:
                event_manager.display_event(event)
                player_dollar -= event['cost']
                print(f"Remaining: ${player_dollar}\n")
        else:
            print("No event this turn.\n")
    
    # Pepe event
    print("\n" + "="*60)
    if PepeEvent.should_appear():
        print("Pepe might appear...")
        result = PepeEvent.trigger_pepe(current_course=150)
        
        if result['success']:
            player_dollar = int(player_dollar * result['multiplier'])
            print(f"\n💰 New balance: ${player_dollar}")
        elif result['multiplier'] < 1.0:
            player_dollar = int(player_dollar * result['multiplier'])
            print(f"\n💸 New balance: ${player_dollar}")
