import random
import pandas as pd

class CardShuffler:
    def __init__(self, cards):
        """
        Initialize the CardShuffler with a list of tarot cards.

        :param cards: List of tarot card dictionaries.
        """
        self.cards = cards.copy()  # Copy to avoid modifying the original list
        self.shuffled_deck = []

    def shuffle_cards(self):
        """
        Shuffles the deck of tarot cards.
        """
        self.shuffled_deck = self.cards.copy()  # Copy the original list to shuffle
        random.shuffle(self.shuffled_deck)
        print("Deck shuffled.")

    def draw_cards(self, count):
        """
        Draws a specified number of cards from the shuffled deck.
        Each card is randomly assigned as upright or reversed.

        :param count: Number of cards to draw.
        :return: A list of tuples, each containing a card dictionary and a boolean indicating if it's reversed.
        """
        if count > len(self.shuffled_deck):
            raise ValueError("Not enough cards in the deck to draw the requested number of cards.")
        
        drawn_cards = []
        for _ in range(count):
            card = self.shuffled_deck.pop()
            is_reversed = random.choice([True, False])
            drawn_cards.append((card, is_reversed))
        return drawn_cards

# Example usage
if __name__ == '__main__':
    # Load tarot cards from the CSV
    csv_file_path = 'data/tarot_cards.csv'
    tarot_df = pd.read_csv(csv_file_path)
    
    # Convert the DataFrame to a list of dictionaries
    tarot_cards = tarot_df.to_dict(orient='records')
    
    shuffler = CardShuffler(tarot_cards)
    shuffler.shuffle_cards()
    drawn = shuffler.draw_cards(3)
    
    print("Drawn Cards:")
    for card, reversed in drawn:
        print(f"{'Reversed' if reversed else 'Upright'}: {card['Card Name']}")
