# setup/rune.py

class Rune:
    def __init__(self, name, symbol, meaning, keywords, mythological_association='', astrological_association='', element='', affirmation=''):
        self.name = name
        self.symbol = symbol
        self.meaning = meaning
        self.keywords = keywords
        self.mythological_association = mythological_association
        self.astrological_association = astrological_association
        self.element = element
        self.affirmation = affirmation

    def to_dict(self):
        return {
            "Name": self.name,
            "Symbol": self.symbol,
            "Meaning": self.meaning,
            "Keywords": self.keywords,
            "Mythological Association": self.mythological_association,
            "Astrological Association": self.astrological_association,
            "Element": self.element,
            "Affirmation": self.affirmation
        }
