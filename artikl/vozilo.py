class Vozilo:
    def __izracunaj_kw(self, konjska_snaga):
        kw = int(konjska_snaga * 0.7355)
        return kw

    def cijena_osiguranja(self, konjska_snaga):
        cijena = 15 * self.__izracunaj_kw(konjska_snaga)
        return cijena