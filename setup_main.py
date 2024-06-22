# setup_main.py

from setup.card_writer import CardCSVWriter

def main():
    cards_dir = 'cards'
    data_dir = 'data'
    csv_filename = 'tarot_cards.csv'

    csv_writer = CardCSVWriter(cards_dir, data_dir, csv_filename)
    csv_writer.read_json_files()
    csv_writer.write_to_csv()

if __name__ == '__main__':
    main()


