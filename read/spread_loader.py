# spread_loader.py
import os
import json

class SpreadLoader:
    def __init__(self, spreads_dir):
        """
        Initialize the SpreadLoader with the directory containing spread files.

        :param spreads_dir: Directory path where spread JSON files are stored.
        """
        self.spreads_dir = spreads_dir

    def list_available_spreads(self, spread_type):
        """
        Lists all available spread files of a certain type in the spreads directory.

        :param spread_type: Type of the spread ('tarot', 'rune', 'iching').
        :return: A list of available spread names (with .json extension).
        """
        try:
            spreads = []
            for file_name in os.listdir(self.spreads_dir):
                print(f"Processing file: {file_name}")  # Debugging output
                if spread_type == 'rune' and '_rune_spread.json' in file_name:
                    print(f"Identified rune spread: {file_name}")
                    spreads.append(file_name)
                elif spread_type == 'iching' and '_hexagram_spread.json' in file_name:
                    print(f"Identified iching spread: {file_name}")
                    spreads.append(file_name)
                elif spread_type == 'tarot' and '_rune_spread.json' not in file_name and '_hexagram_spread.json' not in file_name:
                    print(f"Identified tarot spread: {file_name}")
                    spreads.append(file_name)
                else:
                    print(f"File {file_name} did not match any spread type.")
            print(f"Identified {spread_type} spreads: {spreads}")  # Debugging output
            if not spreads:
                print(f"No {spread_type} spreads available in the directory.")
            return spreads
        except Exception as e:
            print(f"Error listing {spread_type} spreads: {e}")
            return []

    def load_spread(self, spread_name):
        """
        Loads the spread definition from the specified JSON file.

        :param spread_name: The name of the spread file to load (with .json extension).
        :return: A dictionary representing the spread details.
        :raises FileNotFoundError: If the spread file does not exist.
        :raises ValueError: If the spread file contains invalid JSON.
        """
        if spread_name is None:
            raise ValueError("No spread name provided.")
        spread_file_path = os.path.join(self.spreads_dir, spread_name)
        if not os.path.exists(spread_file_path):
            raise FileNotFoundError(f"Spread file '{spread_name}' not found in {self.spreads_dir}.")
        
        try:
            with open(spread_file_path, 'r', encoding='utf-8') as file:
                spread = json.load(file)
            self.validate_spread(spread)
            return spread
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from '{spread_name}': {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error loading spread '{spread_name}': {e}")

    def validate_spread(self, spread):
        """
        Validates the structure of the loaded spread JSON.

        :param spread: The spread dictionary to validate.
        :raises ValueError: If the spread structure is invalid.
        """
        if not isinstance(spread, dict):
            raise ValueError("Spread JSON must be a dictionary.")
        
        required_keys = {'spread_name', 'positions'}
        if not required_keys.issubset(spread.keys()):
            raise ValueError(f"Spread JSON must contain the keys: {required_keys}")
        
        if not isinstance(spread['positions'], list) or not all(isinstance(pos, dict) and ('position' in pos or 'name' in pos) for pos in spread['positions']):
            raise ValueError("Spread 'positions' must be a list of dictionaries each containing a 'position' or 'name' key.")

# Example usage
if __name__ == '__main__':
    spreads_dir = '../spreads/'
    loader = SpreadLoader(spreads_dir)
    
    print("Available Tarot Spreads:")
    tarot_spreads = loader.list_available_spreads('tarot')
    for spread in tarot_spreads:
        print(f"- {spread}")

    print("Available Rune Spreads:")
    rune_spreads = loader.list_available_spreads('rune')
    for spread in rune_spreads:
        print(f"- {spread}")

    print("Available I Ching Spreads:")
    iching_spreads = loader.list_available_spreads('iching')
    for spread in iching_spreads:
        print(f"- {spread}")

    if iching_spreads:
        chosen_spread = iching_spreads[0]  # Selecting the first spread for demonstration
        try:
            spread_details = loader.load_spread(chosen_spread)
            print(f"\nLoaded Spread '{chosen_spread}':")
            print(json.dumps(spread_details, indent=4))
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
