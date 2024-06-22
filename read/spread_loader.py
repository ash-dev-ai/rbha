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

    def list_available_spreads(self):
        """
        Lists all available spread files in the spreads directory.

        :return: A list of available spread names (without .json extension).
        """
        try:
            spreads = []
            for file_name in os.listdir(self.spreads_dir):
                if file_name.endswith('.json'):
                    spreads.append(file_name.replace('.json', ''))
            if not spreads:
                print("No spreads available in the directory.")
            return spreads
        except Exception as e:
            print(f"Error listing spreads: {e}")
            return []

    def load_spread(self, spread_name):
        """
        Loads the spread definition from the specified JSON file.

        :param spread_name: The name of the spread file to load (without .json extension).
        :return: A dictionary representing the spread details.
        :raises FileNotFoundError: If the spread file does not exist.
        :raises ValueError: If the spread file contains invalid JSON.
        """
        spread_file_path = os.path.join(self.spreads_dir, f'{spread_name}.json')
        if not os.path.exists(spread_file_path):
            raise FileNotFoundError(f"Spread file '{spread_name}.json' not found in {self.spreads_dir}.")
        
        try:
            with open(spread_file_path, 'r') as file:
                spread = json.load(file)
            self.validate_spread(spread)
            return spread
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from '{spread_name}.json': {e}")
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
        
        if not isinstance(spread['positions'], list) or not all(isinstance(pos, dict) and 'name' in pos for pos in spread['positions']):
            raise ValueError("Spread 'positions' must be a list of dictionaries each containing a 'name' key.")

# Example usage
if __name__ == '__main__':
    spreads_dir = 'spreads'
    loader = SpreadLoader(spreads_dir)
    
    print("Available Spreads:")
    available_spreads = loader.list_available_spreads()
    for spread in available_spreads:
        print(f"- {spread}")

    if available_spreads:
        chosen_spread = available_spreads[0]  # Selecting the first spread for demonstration
        try:
            spread_details = loader.load_spread(chosen_spread)
            print(f"\nLoaded Spread '{chosen_spread}':")
            print(json.dumps(spread_details, indent=4))
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

