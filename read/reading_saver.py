# reading_saver.py
import os
from datetime import datetime

class ReadingSaver:
    def __init__(self, readings_dir):
        self.readings_dir = readings_dir

    def save_reading(self, reading_type, spread, reading):
        """
        Saves the reading to a file in a dated directory within the readings directory.

        :param reading_type: Type of the reading (tarot, rune, iching).
        :param spread: Spread dictionary containing spread details.
        :param reading: Dictionary representing the reading details.
        """
        today = datetime.now().strftime('%Y-%m-%d')
        date_dir = os.path.join(self.readings_dir, today, reading_type)
        
        # Ensure the directory exists
        os.makedirs(date_dir, exist_ok=True)
        
        # Generate a unique filename
        spread_name = spread['spread_name']  # Correct way to get the spread name
        file_index = len([name for name in os.listdir(date_dir) if os.path.isfile(os.path.join(date_dir, name))]) + 1
        file_name = f'{spread_name}_reading_{file_index}.txt'
        file_path = os.path.join(date_dir, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Reading for Spread: {spread_name}\n")
            file.write("=" * 40 + "\n")
            if reading_type == 'tarot':
                for position, card in reading.items():
                    file.write(f"{position}:\n")
                    file.write(f"  Card Name: {card['Card Name']}\n")
                    file.write(f"  Orientation: {'Reversed' if card['Reversed'] else 'Upright'}\n")
                    file.write(f"  Meaning: {card['Reversed Meaning'] if card['Reversed'] else card['Upright Meaning']}\n")
                    file.write(f"  Keywords: {card['Keywords']}\n")
                    file.write(f"  Symbolism: {card['Symbolism']}\n")
                    file.write(f"  Affirmation: {card['Affirmation']}\n")
                    file.write(f"  Mythological Connection: {card['Mythological Connection']}\n")
                    file.write(f"  Numerology: {card['Numerology']}\n")
                    file.write(f"  Chakra Association: {card['Chakra Association']}\n")
                    file.write(f"  Card Image Description: {card['Card Image Description']}\n")
                    file.write(f"  Element: {card['Element']}\n")
                    file.write(f"  Astrological Association: {card['Astrological Association']}\n")

                    if not card['Reversed']:
                        file.write(f"  Traditional Interpretation: {card['Traditional Interpretation']}\n")
                        file.write(f"  Modern Interpretation: {card['Modern Interpretation']}\n")
                        file.write(f"  Rider-Waite Description: {card['Rider-Waite Description']}\n")
                        file.write(f"  Alternative Deck Descriptions: {card['Alternative Deck Descriptions']}\n")
                    
                    file.write("-" * 40 + "\n")
            elif reading_type == 'rune':
                for rune in reading:
                    file.write(f"Rune Name: {rune['Name']}\n")
                    file.write(f"Symbol: {rune['Symbol']}\n")
                    file.write(f"Meaning: {rune['Meaning']}\n")
                    file.write(f"Keywords: {rune['Keywords']}\n")
                    file.write(f"Mythological Association: {rune['Mythological Association']}\n")
                    file.write(f"Astrological Association: {rune['Astrological Association']}\n")
                    file.write(f"Element: {rune['Element']}\n")
                    file.write(f"Affirmation: {rune['Affirmation']}\n")
                    file.write("-" * 40 + "\n")
            elif reading_type == 'iching':
                for position, hexagram in reading.items():
                    file.write(f"{position}:\n")
                    file.write(f"  Hexagram Number: {hexagram['Hexagram Number']}\n")
                    file.write(f"  Hexagram Name: {hexagram['Hexagram Name']}\n")
                    file.write(f"  Binary Sequence: {hexagram['Binary Sequence']}\n")
                    file.write(f"  Judgment: {hexagram['Judgment']}\n")
                    file.write(f"  Image: {hexagram['Image']}\n")
                    file.write(f"  Lines: {hexagram['Lines']}\n")
                    file.write(f"  Keywords: {hexagram['Keywords']}\n")
                    file.write(f"  Changing Lines: {hexagram.get('Changing Lines', '')}\n")
                    file.write(f"  Commentary: {hexagram.get('Commentary', '')}\n")
                    file.write(f"  Element: {hexagram['Element']}\n")
                    file.write(f"  Astrological Association: {hexagram['Astrological Association']}\n")
                    file.write(f"  Mythological Association: {hexagram['Mythological Association']}\n")
                    file.write(f"  Affirmation: {hexagram['Affirmation']}\n")
                    file.write("-" * 40 + "\n")

        print(f'Reading saved to {file_path}')
