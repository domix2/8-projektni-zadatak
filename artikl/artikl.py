from abc import ABC, abstractmethod

class Artikl(ABC):
    def __init__(self, naslov, opis, cijena):
        self._naslov = naslov
        self._opis = opis
        self._cijena = cijena

    @property
    def naslov(self):
        return self._naslov

    @naslov.setter
    def naslov(self, naslov):
        self._naslov = naslov

    @property
    def opis(self):
        return self._opis

    @opis.setter
    def opis(self, opis):
        self._opis = opis

    @property
    def cijena(self):
        return self._cijena

    @cijena.setter
    def cijena(self, cijena):
        self._cijena = cijena

    @abstractmethod
    def ispis(self):
        pass