class Prodaja:
    def __init__(self, datum, korisnik, artikl):
        self.datum = datum
        self.korisnik = korisnik
        self.artikl = artikl

    def ispis(self):
        return f'{self.korisnik.email}: {self.artikl.naslov}'

        #self.korisnik.ispis()

        #self.artikl.ispis()

        #print('Datum isteka prodaje: ')
        #print(f'\t Dan: {self.datum.day}')
        #print(f'\t Mjesec: {self.datum.month}')
        #print(f'\t Godina: {self.datum.year}')

        #print("\n")