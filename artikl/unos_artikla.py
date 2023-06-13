from utillities import unos_pozitivnog_realnog_broja, unos_intervala
from .automobil import Automobil
from .stan import Stan

def unos_artikla(redni_broj):
    naslov = input(f'Unesite naslov {redni_broj}. artikla:')
    opis = input(f'Unesite opis {redni_broj}. artikla:')
    cijena = unos_pozitivnog_realnog_broja(f'Unesite cijenu {redni_broj}. artikla:')
    print('Tipovi artikla: ')
    print('\t 1. Stan')
    print('\t 2. Automobil')

    tip_artikla = unos_intervala(1, 2)

    if tip_artikla == 1:
        kvadratura = unos_pozitivnog_realnog_broja(f'Unesite kvadraturu {redni_broj}. stana: ')

        return Stan(kvadratura, naslov, opis, cijena)

    elif tip_artikla == 2:
        snaga = unos_pozitivnog_realnog_broja(f'Unesite snagu {redni_broj}. auta: ')

        return Automobil(snaga, naslov, opis, cijena)




