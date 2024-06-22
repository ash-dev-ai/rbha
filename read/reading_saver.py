# reading_saver.py
import os
from datetime import datetime

class ReadingSaver:
    def __init__(self, readings_dir):
        """
        Initialize the ReadingSaver with the directory for storing readings.

        :param readings_dir: Base directory where readings will be stored.
        """
        self.readings_dir = readings_dir

    def save_reading(self, spread_name, reading):
        """
        Saves the reading to a file in a dated directory within the readings directory.

        :param spread_name: Name of the spread used for the reading.
        :param reading: Dictionary representing the reading details.
        """
        # Get the current date
        today = datetime.now().strftime('%Y-%m-%d')
        date_dir = os.path.join(self.readings_dir, today)
        
        # Ensure the directory exists
        os.makedirs(date_dir, exist_ok=True)
        
        # Generate a unique filename
        file_index = len([name for name in os.listdir(date_dir) if os.path.isfile(os.path.join(date_dir, name))]) + 1
        file_name = f'{spread_name}_reading_{file_index}.txt'
        file_path = os.path.join(date_dir, file_name)
        
        # Save the reading to the file
        with open(file_path, 'w') as file:
            file.write(f"Reading for Spread: {spread_name}\n")
            file.write("=" * 40 + "\n")
            for position, card in reading.items():
                file.write(f"{position}:\n")
                file.write(f"  Card Name: {card['Card Name']}\n")
                file.write(f"  Orientation: {'Reversed' if card['Reversed'] else 'Upright'}\n")
                file.write(f"  Meaning: {card['Meaning']}\n")
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
        
        print(f'Reading saved to {file_path}')
