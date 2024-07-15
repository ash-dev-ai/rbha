# read_main.py

import os
import csv
from read.spread_loader import SpreadLoader
from read.card_shuffler import CardShuffler
from read.rune_shuffler import RuneShuffler
from read.coin_tosser import CoinTosser
from read.reading_saver import ReadingSaver
from read.tarot_reader import TarotReader
from read.rune_reader import RuneReader
from read.iching_reader import IChingReader
from read.prompt_user import UserPrompter

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    spreads_dir = os.path.join(base_dir, 'spreads')
    readings_dir = os.path.join(base_dir, 'readings')
    tarot_csv_file_path = os.path.join(base_dir, 'data/tarot_cards.csv')
    rune_csv_file_path = os.path.join(base_dir, 'data/rune.csv')
    hexagram_csv_file_path = os.path.join(base_dir, 'data/hexagrams.csv')

    spread_loader = SpreadLoader(spreads_dir)
    user_prompter = UserPrompter(spread_loader)

    reading_type = user_prompter.prompt_for_reading_type()
    chosen_spread_name = user_prompter.prompt_for_spread(reading_type.lower())
    
    if chosen_spread_name is None:
        print("No spread selected or available. Exiting.")
        return

    try:
        chosen_spread = spread_loader.load_spread(chosen_spread_name)
        print(f"Loaded spread: {chosen_spread}")
        print(f"Type of chosen_spread: {type(chosen_spread)}")
    except Exception as e:
        print(f"Error loading spread: {e}")
        return

    if reading_type == 'Tarot':
        with open(tarot_csv_file_path, newline='', encoding='utf-8') as csvfile:
            tarot_cards = list(csv.DictReader(csvfile))

        shuffler = CardShuffler(tarot_cards)
        shuffler.shuffle_cards()
        drawn_cards = shuffler.draw_cards(len(chosen_spread['positions']))

        reader = TarotReader(tarot_cards)
        reading = reader.generate_reading(chosen_spread, drawn_cards)

    elif reading_type == 'Rune':
        with open(rune_csv_file_path, newline='', encoding='utf-8') as csvfile:
            runes = list(csv.DictReader(csvfile))

        shuffler = RuneShuffler(runes)
        shuffler.shuffle_runes()
        drawn_runes = shuffler.draw_runes(len(chosen_spread['positions']))

        reader = RuneReader(runes)
        reading = reader.generate_reading(chosen_spread, drawn_runes)

    elif reading_type == 'iching':
        tosser = CoinTosser()
        hexagrams = [tosser.toss_and_interpret() for _ in range(len(chosen_spread['positions']))]

        with open(hexagram_csv_file_path, newline='', encoding='utf-8') as csvfile:
            hexagram_data = list(csv.DictReader(csvfile))
            print(f"Hexagram data keys: {hexagram_data[0].keys()}")  # Debugging statement
            
            # Print all binary sequences for debugging
            for row in hexagram_data:
                print(f"Binary Sequence: {row['Binary Sequence']}")

            hexagram_dict = {row['Binary Sequence']: row for row in hexagram_data}

        # Ensure each hexagram sequence is a valid key
        drawn_hexagrams = []
        for hexagram in hexagrams:
            if hexagram in hexagram_dict:
                drawn_hexagrams.append(hexagram_dict[hexagram])
            else:
                print(f"Hexagram {hexagram} not found in hexagram_dict")

        if not drawn_hexagrams:
            print("No valid hexagrams drawn. Exiting.")
            return

        reader = IChingReader(drawn_hexagrams)
        reading = reader.generate_reading(chosen_spread, drawn_hexagrams)

    else:
        print("Invalid reading type. Exiting.")
        return

    print(f"Type of chosen_spread before saving: {type(chosen_spread)}")  # Debugging statement
    print(f"Chosen spread before saving: {chosen_spread}")  # Debugging statement

    saver = ReadingSaver(readings_dir)
    saver.save_reading(reading_type.lower(), chosen_spread, reading)

    user_prompter.display_reading(chosen_spread['spread_name'], reading)

if __name__ == '__main__':
    main()
3