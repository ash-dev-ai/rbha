# setup/rune_writer.py

import csv
import json
import os
from setup.rune import Rune

class RuneCSVWriter:
    def __init__(self, json_dir, csv_dir, csv_filename):
        self.json_dir = json_dir
        self.csv_dir = csv_dir
        self.csv_filename = csv_filename

    def load_runes_from_json(self):
        runes = []
        for file_name in os.listdir(self.json_dir):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.json_dir, file_name)
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    for rune_data in data['runes']:
                        rune = Rune(
                            name=rune_data['rune_name'],
                            symbol=rune_data['symbol'],
                            meaning=rune_data['meaning'],
                            keywords=rune_data['keywords'],
                            mythological_association=rune_data.get('mythological_association', ''),
                            astrological_association=rune_data.get('astrological_association', ''),
                            element=rune_data.get('element', ''),
                            affirmation=rune_data.get('affirmation', '')
                        )
                        runes.append(rune)
        return runes

    def write_to_csv(self):
        runes = self.load_runes_from_json()
        csv_path = os.path.join(self.csv_dir, self.csv_filename)
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Name", "Symbol", "Meaning", "Keywords", "Mythological Association", "Astrological Association", "Element", "Affirmation"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for rune in runes:
                writer.writerow(rune.to_dict())
        print(f"CSV file '{self.csv_filename}' created in the '{self.csv_dir}' directory with rune details.")

if __name__ == "__main__":
    json_dir = "runes"
    csv_dir = "data"
    csv_filename = "rune.csv"
    rune_writer = RuneCSVWriter(json_dir, csv_dir, csv_filename)
    rune_writer.write_to_csv()
