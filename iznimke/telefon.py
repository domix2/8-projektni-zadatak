class IznimkaTelefon(Exception):
    def __init__(self):
        super(IznimkaTelefon, self).__init__('Telefon mora imati 8 znamenki')
