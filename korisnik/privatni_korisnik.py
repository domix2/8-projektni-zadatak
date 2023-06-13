from .korisnik import Korisnik

class PrivatniKorisnik(Korisnik):

    def __init__(self, ime, prezime, drzavljanstvo, email, telefon):
        super().__init__(email, telefon)
        self.__ime = ime
        self.__prezime = prezime
        self.__drzavljanstvo = drzavljanstvo

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
      print("Informacije o privatnom korisniku: ")
      print(f'\tIme: {self.__ime}')
      print(f'\tPrezime: {self.__prezime}')
      print(f'\tDrzavljanstvo: {self.__drzavljanstvo}')
      print(f'\tTelefon: {self.telefon}')
      print(f'\tEmail: {self.email}')