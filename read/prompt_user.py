# prompt_user.py

class UserPrompter:
    def __init__(self, spread_loader):
        self.spread_loader = spread_loader

    def prompt_for_reading_type(self):
        print("Available Reading Types:")
        print("1. Tarot")
        print("2. Rune")
        print("3. iching")
        choice = input("Choose a reading type by number: ")
        if choice == '1':
            return 'Tarot'
        elif choice == '2':
            return 'Rune'
        elif choice == '3':
            return 'iching'
        else:
            return None

    def prompt_for_spread(self, reading_type):
        available_spreads = self.spread_loader.list_available_spreads(reading_type)
        if not available_spreads:
            return None
        print(f"Available {reading_type} Spreads:")
        for idx, spread in enumerate(available_spreads, 1):
            print(f"{idx}. {spread}")
        choice = int(input(f"Choose a {reading_type} spread by number: "))
        if 1 <= choice <= len(available_spreads):
            return available_spreads[choice - 1]
        else:
            return None

    def display_reading(self, spread_name, reading):
        print(f"\nReading for Spread: {spread_name}")
        print("=" * 40)
        if isinstance(reading, dict):
            for position, details in reading.items():
                print(f"{position}:")
                if 'Card Name' in details:
                    print(f"  Card Name: {details['Card Name']}")
                    print(f"  Orientation: {'Reversed' if details['Reversed'] else 'Upright'}")
                    print(f"  Meaning: {details['Reversed Meaning'] if details['Reversed'] else details['Upright Meaning']}")
                    print(f"  Keywords: {details['Keywords']}")
                    print(f"  Symbolism: {details['Symbolism']}")
                    print(f"  Affirmation: {details['Affirmation']}")
                    print(f"  Mythological Connection: {details['Mythological Connection']}")
                    print(f"  Numerology: {details['Numerology']}")
                    print(f"  Chakra Association: {details['Chakra Association']}")
                    print(f"  Card Image Description: {details['Card Image Description']}")
                    print(f"  Element: {details['Element']}")
                    print(f"  Astrological Association: {details['Astrological Association']}")
                    if not details['Reversed']:
                        print(f"  Traditional Interpretation: {details['Traditional Interpretation']}")
                        print(f"  Modern Interpretation: {details['Modern Interpretation']}")
                        print(f"  Rider-Waite Description: {details['Rider-Waite Description']}")
                        print(f"  Alternative Deck Descriptions: {details['Alternative Deck Descriptions']}")
                elif 'Rune Name' in details:
                    print(f"  Rune Name: {details['Rune Name']}")
                    print(f"  Symbol: {details['Symbol']}")
                    print(f"  Meaning: {details['Meaning']}")
                    print(f"  Keywords: {details['Keywords']}")
                    print(f"  Mythological Association: {details['Mythological Association']}")
                    print(f"  Astrological Association: {details['Astrological Association']}")
                    print(f"  Element: {details['Element']}")
                    print(f"  Affirmation: {details['Affirmation']}")
                else:  # Handle I Ching details
                    print(f"  Hexagram Number: {details['Hexagram Number']}")
                    print(f"  Hexagram Name: {details['Hexagram Name']}")
                    print(f"  Binary Sequence: {details['Binary Sequence']}")
                    print(f"  Judgment: {details['Judgment']}")
                    print(f"  Image: {details['Image']}")
                    print(f"  Lines: {details['Lines']}")
                    print(f"  Keywords: {details['Keywords']}")
                    print(f"  Changing Lines: {details.get('Changing Lines', '')}")
                    print(f"  Commentary: {details.get('Commentary', '')}")
                    print(f"  Element: {details['Element']}")
                    print(f"  Astrological Association: {details['Astrological Association']}")
                    print(f"  Mythological Association: {details['Mythological Association']}")
                    print(f"  Affirmation: {details['Affirmation']}")
                print("-" * 40)
        else:
            for line in reading:
                print(line)
            print("-" * 40)
