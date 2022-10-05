from dataclasses import dataclass, field
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

@dataclass
class TextParse:
    filepath: str
    text: str = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        self.text = self.parsedata()


    def parsedata(self) -> list:
        self._lines: list = []

        with open(self.filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line != '':
                    self._lines.append(line)
        return self._cleantext()


    def _cleantext(self) ->list:      
        clean_text: list = []

        for line in self._lines:
            line = line.lower()
            line= re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)
            tokens = word_tokenize(line)
            words = [word for word in tokens if word.isalpha()]

            clean_text += words
        return clean_text


