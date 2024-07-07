# setup/hexagram_writer.py

import csv
import json
import os
from setup.hexagram import Hexagram

class HexagramCSVWriter:
    def __init__(self, json_dir, csv_dir, csv_filename):
        self.json_dir = json_dir
        self.csv_dir = csv_dir
        self.csv_filename = csv_filename

    def load_hexagrams_from_json(self):
        hexagrams = []
        for file_name in os.listdir(self.json_dir):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.json_dir, file_name)
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    for hexagram_data in data['hexagrams']:
                        hexagram = Hexagram(
                            hexagram_number=hexagram_data['hexagram_number'],
                            hexagram_name=hexagram_data['hexagram_name'],
                            binary_sequence=hexagram_data['binary_sequence'],
                            judgment=hexagram_data['judgment'],
                            image=hexagram_data['image'],
                            lines=hexagram_data['lines'],
                            keywords=hexagram_data['keywords'],
                            changing_lines=hexagram_data.get('changing_lines', ''),
                            commentary=hexagram_data.get('commentary', ''),
                            element=hexagram_data['element'],
                            astrological_association=hexagram_data['astrological_association'],
                            mythological_association=hexagram_data['mythological_association'],
                            affirmation=hexagram_data['affirmation']
                        )
                        hexagrams.append(hexagram)
        return hexagrams

    def write_to_csv(self):
        hexagrams = self.load_hexagrams_from_json()
        csv_path = os.path.join(self.csv_dir, self.csv_filename)
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Hexagram Number", "Hexagram Name", "Binary Sequence", "Judgment", "Image", "Lines", "Keywords", "Changing Lines", "Commentary", "Element", "Astrological Association", "Mythological Association", "Affirmation"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for hexagram in hexagrams:
                writer.writerow(hexagram.to_dict())
        print(f"CSV file '{self.csv_filename}' created in the '{self.csv_dir}' directory with hexagram details.")

if __name__ == "__main__":
    json_dir = "hexagrams"
    csv_dir = "data"
    csv_filename = "hexagrams.csv"
    hexagram_writer = HexagramCSVWriter(json_dir, csv_dir, csv_filename)
    hexagram_writer.write_to_csv()
