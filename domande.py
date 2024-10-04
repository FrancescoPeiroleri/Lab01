from dataclasses import dataclass
import random

@dataclass
class Domande:

    domanda: str
    difficolta: int
    risposta: str
    opzioni: list[str]

    def opzioni_random(self):
        random.shuffle(self.opzioni)
        return self.opzioni





