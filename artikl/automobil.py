from .artikl import Artikl
from .vozilo import Vozilo


class Automobil(Artikl, Vozilo):
    def __init__(self, naslov, opis, cijena, snaga):
        super().__init__(naslov, opis, cijena)
        self.snaga = snaga

    def ispis(self):
        return f'{self.naslov}, {self.opis}, {self.cijena}, {self.snaga}'
        #print('Informaccije o vozilu: ')
        #print(f'\tNaslov: {self.naslov}')
        #print(f'\tOpis: {self.opis}')
        #print(f'\tCijena: {self.cijena}')
        #print(f'\tCijena osiguranja: {self.cijena_osiguranja(self.snaga)}')