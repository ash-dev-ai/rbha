# setup/card_writer.py

import os
import csv
import json
from .card import Card

class CardCSVWriter:
    def __init__(self, cards_dir, data_dir, csv_filename):
        self.cards_dir = cards_dir
        self.data_dir = data_dir
        self.csv_filename = csv_filename
        self.cards = []

    def read_json_files(self):
        """Read all JSON files in the specified directory and store the card data."""
        for json_file in os.listdir(self.cards_dir):
            if json_file.endswith('.json'):
                with open(os.path.join(self.cards_dir, json_file), 'r') as file:
                    card_data = json.load(file)
                    for data in card_data:
                        card = Card(data)
                        self.cards.append(card)

    def write_to_csv(self):
        """Write the card data to a CSV file."""
        os.makedirs(self.data_dir, exist_ok=True)
        csv_path = os.path.join(self.data_dir, self.csv_filename)
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Card({}).to_dict().keys())
            writer.writeheader()
            for card in self.cards:
                writer.writerow(card.to_dict())
        print(f"CSV file '{self.csv_filename}' created in the '{self.data_dir}' directory with card details.")
