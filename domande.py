from dataclasses import dataclass

@dataclass
class Domande:

    domanda: str
    difficoltà: int
    risposta: str

    def readq(self):

