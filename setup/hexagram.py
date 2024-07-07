# setup/hexagram.py

class Hexagram:
    def __init__(self, hexagram_number, hexagram_name, binary_sequence, judgment, image, lines, keywords, changing_lines, commentary, element, astrological_association, mythological_association, affirmation):
        self.hexagram_number = hexagram_number
        self.hexagram_name = hexagram_name
        self.binary_sequence = binary_sequence
        self.judgment = judgment
        self.image = image
        self.lines = lines
        self.keywords = keywords
        self.changing_lines = changing_lines
        self.commentary = commentary
        self.element = element
        self.astrological_association = astrological_association
        self.mythological_association = mythological_association
        self.affirmation = affirmation

    def to_dict(self):
        return {
            "Hexagram Number": self.hexagram_number,
            "Hexagram Name": self.hexagram_name,
            "Binary Sequence": self.binary_sequence,
            "Judgment": self.judgment,
            "Image": self.image,
            "Lines": self.lines,
            "Keywords": self.keywords,
            "Changing Lines": self.changing_lines,
            "Commentary": self.commentary,
            "Element": self.element,
            "Astrological Association": self.astrological_association,
            "Mythological Association": self.mythological_association,
            "Affirmation": self.affirmation
        }
