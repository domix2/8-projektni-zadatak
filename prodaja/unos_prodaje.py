from artikl import ispis_artikla
from kategorija import get_kategorija
from korisnik import get_korisnik
from utillities import unos_datuma, unos_intervala
from .prodaja import Prodaja

def unos_prodaje(korisnici, kategorije, redni_broj):
    datum = unos_datuma(f"Unesite datum isteka {redni_broj}. prodaje: ")

#Odabir korisnika
    print(f"Odaberite korisnika {redni_broj}. prodaje: ")
    for i, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(i, korisnik))

    odabrani_korisnik = unos_intervala(1,i)

#Odabir kategorije
    print(f"Odaberite kategoriju {redni_broj}. prodaje: ")
    for i, kategorija in enumerate(kategorije, start=1):
        print(get_kategorija(i, kategorija))

    odabrana_kategorija = unos_intervala(1,i)

#Odabir artikla
    print(f"Odaberite artikl {redni_broj}. prodaje: ")

    for i, artikl in enumerate(kategorije[odabrana_kategorija - 1].artikl, start=1):
        print(ispis_artikla(i, artikl))

    odabrani_artikl = unos_intervala(1,i)

    korisnik = korisnici[odabrani_korisnik - 1]
    artikl = kategorije[odabrana_kategorija - 1].artikl[odabrani_artikl - 1]

    return Prodaja(datum, korisnik, artikl)