class IznimkaPrazanTekst(Exception):
    def __init__(self):
        super(IznimkaPrazanTekst, self).__init__('Niste unijeli sve podatke')
