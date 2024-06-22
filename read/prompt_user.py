# prompt_user.py

class UserPrompter:
    def __init__(self, spread_loader):
        self.spread_loader = spread_loader

    def prompt_for_spread(self):
        """
        Prompts the user to select a spread from the available options.
        Returns the selected spread name.
        """
        available_spreads = self.spread_loader.list_available_spreads()
        print("Available Spreads:")
        for i, spread in enumerate(available_spreads):
            print(f"{i + 1}. {spread}")
        
        spread_choice = int(input("Choose a spread by number: ")) - 1
        chosen_spread = available_spreads[spread_choice]
        return chosen_spread

    def display_reading(self, spread_name, reading):
        """
        Displays the generated reading to the user.
        """
        print(f"\nReading for Spread: {spread_name}")
        print("=" * 40)
        for position, card in reading.items():
            print(f"{position}:")
            print(f"  Card Name: {card['Card Name']}")
            print(f"  Orientation: {'Reversed' if card['Reversed'] else 'Upright'}")
            print(f"  Meaning: {card['Reversed Meaning'] if card['Reversed'] else card['Upright Meaning']}")
            print("-" * 40)

# Example usage
if __name__ == '__main__':
    from read.spread_loader import SpreadLoader
    
    spreads_dir = 'spreads'
    loader = SpreadLoader(spreads_dir)
    prompter = UserPrompter(loader)
    
    chosen_spread = prompter.prompt_for_spread()
    # Example reading data for display purposes
    example_reading = {
        "Present": {"Card Name": "The Fool", "Reversed": False, "Upright Meaning": "New beginnings", "Reversed Meaning": "Recklessness"},
        "Challenge": {"Card Name": "The Magician", "Reversed": True, "Upright Meaning": "Skill and power", "Reversed Meaning": "Deception"}
        # ... add more positions and cards for testing
    }
    prompter.display_reading(chosen_spread, example_reading)
