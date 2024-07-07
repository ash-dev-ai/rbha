# setup_main.py

from setup.card_writer import CardCSVWriter
from setup.rune_writer import RuneCSVWriter
from setup.hexagram_writer import HexagramCSVWriter

def main():
    cards_dir = 'cards'
    runes_dir = 'runes'
    hexagrams_dir = 'hexagrams'
    data_dir = 'data'
    tarot_csv_filename = 'tarot_cards.csv'
    runes_csv_filename = 'rune.csv'
    hexagrams_csv_filename = 'hexagrams.csv'

    # Process and write tarot cards to CSV
    card_csv_writer = CardCSVWriter(cards_dir, data_dir, tarot_csv_filename)
    card_csv_writer.read_json_files()
    card_csv_writer.write_to_csv()

    # Process and write runes to CSV
    rune_csv_writer = RuneCSVWriter(runes_dir, data_dir, runes_csv_filename)
    rune_csv_writer.load_runes_from_json()
    rune_csv_writer.write_to_csv()

    # Process and write hexagrams to CSV
    hexagram_csv_writer = HexagramCSVWriter(hexagrams_dir, data_dir, hexagrams_csv_filename)
    hexagram_csv_writer.write_to_csv()

if __name__ == '__main__':
    main()