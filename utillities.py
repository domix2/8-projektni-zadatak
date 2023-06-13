from datetime import date
from iznimke import IznimkaPrazanTekst, IznimkaTelefon


def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Unesite poziticni cijeli broj!')

        except ValueError:
            print('Unesli ste slovo umjesto broja!')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati realni broj!')

        except ValueError:
            print('Unesli ste znak a ne realni broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_datuma(poruka):
    while True:
            try:
                dan = int(input(poruka))
                mjesec = int(input(f'Unesite mjesec isteka prodaje: '))
                godina = int(input(f'Unesite godinu isteka prodaje: '))
                datum = date(godina, mjesec, dan)

            except ValueError as e:
                print(e)
            else:
                return datum


def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj<min or broj>max:
                raise Exception(f"Unesite broj unutar intervala {min}-{max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_telefona(poruka):
    while True:
        try:
            broj = unos_pozitivnog_cijelog_broja(poruka)

            if len(str(broj)) !=8:
                raise Exception(f'Uneseni broj mora imat 8 znamenaka!')

        except Exception as e:
            print(e)

        else:
            return broj



def unos_mail(poruka):
    while True:
        try:
            mail = input(poruka)

            while '@' not in mail:
                raise Exception(f'Uneseni mail mora imati znak @!')

        except Exception as e:
            print(e)

        else:
            return mail


def unos_mail_m(poruka):
    while True:
        try:
            email = input(poruka)
            index = email.index('@')

        except ValueError:
            print('Uneseni mail mora sadržavati znak @!')

        else:
            return email


def unos_godina(poruka):
    while True:
        try:
            godine = unos_pozitivnog_cijelog_broja(poruka)

            if godine < 18 or godine > 120:
                raise Exception(f'Broj godina mora biti iznad 18 i ispod 120!')

        except Exception as e:
            print(e)
        else:
            return godine


def provjera_korisnickog_unos(telefon, email, ime_ili_naziv, prezime_ili_web):
    while True:
        try:
            if len(telefon) == 0 or len(email) == 0 or len(ime_ili_naziv) == 0 or len(prezime_ili_web) == 0:
                raise IznimkaPrazanTekst()
            elif len(str(telefon)) != 8:
                raise IznimkaTelefon()

            int(telefon)

        except IznimkaPrazanTekst as e:
            return str(e)

        except IznimkaTelefon as f:
            return str(f)

        except ValueError:
            return ('Telefon mora biti broj')

        else:
            return None
def provjera_unosa_artikla(naslov, opis, cijena, snaga):
    try:
        if len(naslov) == 0 or len(opis) == 0 or cijena == '' or snaga == '':
            raise IznimkaPrazanTekst()

        if int(cijena) < 0 or int(snaga) < 0:
            raise Exception(f"Potrebno upisati pozitivan cijeli broj!")

    except IznimkaPrazanTekst as e:
        return str(e)

    except ValueError:
        return('Potrebno upisati broj!')

    except Exception as e:
        return str(e)


def provjera_unosa_prodaje(korisnik, prodaja):
    try:
        if korisnik == '' or prodaja == '':
            raise IznimkaPrazanTekst()

    except IznimkaPrazanTekst as e:
        return str(e)
