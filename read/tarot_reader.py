# tarot_reader.py

class TarotReader:
    def __init__(self, cards):
        """
        Initialize the TarotReader with a list of tarot cards.

        :param cards: List of tarot card dictionaries.
        """
        self.cards = cards

    def generate_reading(self, spread, drawn_cards):
        """
        Generates a reading by assigning drawn cards to spread positions.

        :param spread: Dictionary representing the spread details.
        :param drawn_cards: List of tuples, each containing a card dictionary and a boolean indicating if it's reversed.
        :return: A dictionary representing the reading, with positions and card interpretations.
        """
        reading = {}
        for position, (card, is_reversed) in zip(spread['positions'], drawn_cards):
            reading[position['name']] = self.interpret_card(card, is_reversed)
        return reading

    def interpret_card(self, card, is_reversed):
        """
        Interprets the card's meaning based on its orientation.

        :param card: Dictionary representing a tarot card.
        :param is_reversed: Boolean indicating if the card is reversed.
        :return: A dictionary with card details and its interpreted meaning.
        """
        interpreted_card = {
            'Card Name': card['Card Name'],
            'Reversed': is_reversed,
            'Upright Meaning': card['Upright Meaning'],
            'Reversed Meaning': card['Reversed Meaning'],
            'Meaning': card['Reversed Meaning'] if is_reversed else card['Upright Meaning'],
            'Keywords': card['Keywords'],
            'Symbolism': card['Symbolism'],
            'Affirmation': card['Affirmation'],
            'Mythological Connection': card['Mythological Connection'],
            'Numerology': card['Numerology'],
            'Chakra Association': card['Chakra Association'],
            'Card Image Description': card['Card Image Description'],
            'Element': card['Element'],
            'Astrological Association': card['Astrological Association']
        }

        if not is_reversed:
            # Add details specific to the upright interpretation
            interpreted_card.update({
                'Traditional Interpretation': card['Traditional Interpretation'],
                'Modern Interpretation': card['Modern Interpretation'],
                'Rider-Waite Description': card['Rider-Waite Description'],
                'Alternative Deck Descriptions': card['Alternative Deck Descriptions'],
            })

        return interpreted_card