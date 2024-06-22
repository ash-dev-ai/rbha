# read_main.py

import csv
from read.spread_loader import SpreadLoader
from read.card_shuffler import CardShuffler
from read.reading_saver import ReadingSaver
from read.tarot_reader import TarotReader
from read.prompt_user import UserPrompter

def main():
    # Define directories and file paths
    spreads_dir = 'spreads'
    readings_dir = 'readings'
    csv_file_path = 'data/tarot_cards.csv'

    # Load spreads using SpreadLoader
    spread_loader = SpreadLoader(spreads_dir)
    user_prompter = UserPrompter(spread_loader)

    # Prompt the user to select a spread
    chosen_spread = user_prompter.prompt_for_spread()
    spread_details = spread_loader.load_spread(chosen_spread)

    # Load tarot cards from the CSV file
    with open(csv_file_path, newline='') as csvfile:
        tarot_cards = list(csv.DictReader(csvfile))

    # Shuffle the tarot cards and draw the required number of cards
    shuffler = CardShuffler(tarot_cards)
    shuffler.shuffle_cards()
    drawn_cards = shuffler.draw_cards(len(spread_details['positions']))

    # Generate the reading using TarotReader
    reader = TarotReader(tarot_cards)
    reading = reader.generate_reading(spread_details, drawn_cards)

    # Save the reading using ReadingSaver
    saver = ReadingSaver(readings_dir)
    saver.save_reading(chosen_spread, reading)

    # Display the reading to the user
    user_prompter.display_reading(chosen_spread, reading)

if __name__ == '__main__':
    main()
