# setup/card.py

class Card:
    def __init__(self, data):
        self.card_number = data.get("Card Number", "")
        self.card_name = data.get("Card Name", "")
        self.suit = data.get("Suit", "")
        self.arcana = data.get("Arcana", "")
        self.numerical_value = data.get("Numerical Value", "")
        self.element = data.get("Element", "")
        self.astrological_association = data.get("Astrological Association", "")
        self.keywords = data.get("Keywords", "")
        self.upright_meaning = data.get("Upright Meaning", "")
        self.reversed_meaning = data.get("Reversed Meaning", "")
        self.symbolism = data.get("Symbolism", "")
        self.affirmation = data.get("Affirmation", "")
        self.traditional_interpretation = data.get("Traditional Interpretation", "")
        self.modern_interpretation = data.get("Modern Interpretation", "")
        self.mythological_connection = data.get("Mythological Connection", "")
        self.numerology = data.get("Numerology", "")
        self.chakra_association = data.get("Chakra Association", "")
        self.rider_waite_description = data.get("Rider-Waite Description", "")
        self.alternative_deck_descriptions = data.get("Alternative Deck Descriptions", "")
        self.card_image_description = data.get("Card Image Description", "")

    def to_dict(self):
        return {
            "Card Number": self.card_number,
            "Card Name": self.card_name,
            "Suit": self.suit,
            "Arcana": self.arcana,
            "Numerical Value": self.numerical_value,
            "Element": self.element,
            "Astrological Association": self.astrological_association,
            "Keywords": self.keywords,
            "Upright Meaning": self.upright_meaning,
            "Reversed Meaning": self.reversed_meaning,
            "Symbolism": self.symbolism,
            "Affirmation": self.affirmation,
            "Traditional Interpretation": self.traditional_interpretation,
            "Modern Interpretation": self.modern_interpretation,
            "Mythological Connection": self.mythological_connection,
            "Numerology": self.numerology,
            "Chakra Association": self.chakra_association,
            "Rider-Waite Description": self.rider_waite_description,
            "Alternative Deck Descriptions": self.alternative_deck_descriptions,
            "Card Image Description": self.card_image_description
        }
