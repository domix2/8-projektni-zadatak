from .korisnik import Korisnik


class PrivatniKorisnik(Korisnik):
    def __init__(self, ime, prezime, telefon, email):
        super().__init__(telefon, email)
        self.__ime = ime
        self.__prezime = prezime

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    def ispis(self):
        return f'{self.ime} {self.prezime}, {self.email}, {self.telefon}'