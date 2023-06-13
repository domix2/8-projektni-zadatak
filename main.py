from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from enumeratori import TipKorisnika
from korisnik import PoslovniKorisnik, PrivatniKorisnik

from utillities import provjera_korisnickog_unos


korisnici = []

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Objektno')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.initUI()

    def initUI(self):
        offset = 30
        self.font = QtGui.QFont('Times', 10)

        #Input tip korisnika
        self.tip_korisnika = QtWidgets.QComboBox(self)

        for korisnik in TipKorisnika:
            self.tip_korisnika.addItem(str(korisnik.value))

        self.tip_korisnika.setGeometry(QtCore.QRect(150, offset, 150, 25))
        self.tip_korisnika.currentTextChanged.connect(self.on_combobox_changed)

        #Label telefon
        self.label_telefon = QtWidgets.QLabel(self)
        self.label_telefon.setFont(self.font)
        self.label_telefon.setText('Telefon')
        self.label_telefon.move(50, offset * 2)

        #Input telefon
        self.text_telefon = QtWidgets.QLineEdit(self)
        self.text_telefon.setGeometry(QtCore.QRect(150, offset * 2, 150, 25))

        #Label email
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setFont(self.font)
        self.label_email.setText('E-mail')
        self.label_email.move(50, offset * 3)

        #Input email
        self.text_email = QtWidgets.QLineEdit(self)
        self.text_email.setGeometry(QtCore.QRect(150, offset * 3, 150, 25))

        #Label ime
        self.label_ime = QtWidgets.QLabel(self)
        self.label_ime.setFont(self.font)
        self.label_ime.setText('Ime')
        self.label_ime.move(50, offset * 4)

        #Input ime
        self.text_ime = QtWidgets.QLineEdit(self)
        self.text_ime.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))

        #Label prezime
        self.label_prezime = QtWidgets.QLabel(self)
        self.label_prezime.setFont(self.font)
        self.label_prezime.setText('Prezime')
        self.label_prezime.move(50, offset * 5)

        #Input prezime
        self.text_prezime = QtWidgets.QLineEdit(self)
        self.text_prezime.setGeometry(QtCore.QRect(150, offset * 5, 150, 25))

        #Label drzavljanstvo
        self.label_drzavljanstvo = QtWidgets.QLabel(self)
        self.label_drzavljanstvo.setFont(self.font)
        self.label_drzavljanstvo.setText('Drzavljanstvo')
        self.label_drzavljanstvo.move(50, offset * 6)

        # Input drzavljanstvo
        self.text_drzavljanstvo = QtWidgets.QLineEdit(self)
        self.text_drzavljanstvo.setGeometry(QtCore.QRect(150, offset * 6, 150, 25))

        #Label naziv
        self.label_naziv = QtWidgets.QLabel(self)
        self.label_naziv.setFont(self.font)
        self.label_naziv.setText('Naziv')
        self.label_naziv.move(50, offset * 4)
        self.label_naziv.hide()

        # Input naziv
        self.text_naziv = QtWidgets.QLineEdit(self)
        self.text_naziv.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))
        self.text_naziv.hide()

        #Input web
        self.label_web = QtWidgets.QLabel(self)
        self.label_web.setFont(self.font)
        self.label_web.setText('Web')
        self.label_web.move(50, offset * 5)
        self.label_web.hide()

        # Input web
        self.text_web = QtWidgets.QLineEdit(self)
        self.text_web.setGeometry(QtCore.QRect(150, offset * 5, 150, 25))
        self.text_web.hide()

        # Input oib
        self.label_oib = QtWidgets.QLabel(self)
        self.label_oib.setFont(self.font)
        self.label_oib.setText('OIB')
        self.label_oib.move(50, offset * 6)
        self.label_oib.hide()

        # Input oib
        self.text_oib = QtWidgets.QLineEdit(self)
        self.text_oib.setGeometry(QtCore.QRect(150, offset * 6, 150, 25))
        self.text_oib.hide()

        #Label error
        self.label_error = QtWidgets.QLabel(self)
        self.label_error.setFont(self.font)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setStyleSheet('color : red')
        self.label_error.setGeometry(QtCore.QRect(70, offset * 7, 200, 30))

        #Gumb za unos korisnika
        self.unos_korisnika_button = QtWidgets.QPushButton(self)
        self.unos_korisnika_button.setFont(self.font)
        self.unos_korisnika_button.setText('Unesi korisnika')
        self.unos_korisnika_button.setGeometry(QtCore.QRect(100, offset * 8, 150, 30))
        self.unos_korisnika_button.clicked.connect(self.unos_korisnika)

    #Metoda za prikazivanje/sakrivanje labela i inputa
    def on_combobox_changed(self):
        if self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            self.label_naziv.show()
            self.text_naziv.show()
            self.label_web.show()
            self.text_web.show()
            self.label_oib.show()
            self.text_oib.show()
            self.label_ime.hide()
            self.text_ime.hide()
            self.label_prezime.hide()
            self.text_prezime.hide()
            self.label_drzavljanstvo.hide()
            self.text_drzavljanstvo.hide()
        if self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            self.label_naziv.hide()
            self.text_naziv.hide()
            self.label_web.hide()
            self.text_web.hide()
            self.label_oib.hide()
            self.text_oib.hide()
            self.label_ime.show()
            self.text_ime.show()
            self.label_prezime.show()
            self.text_prezime.show()
            self.label_drzavljanstvo.show()
            self.text_drzavljanstvo.show()

    def unos_korisnika(self):

        if self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            error_privatni = provjera_korisnickog_unos(self.text_telefon.text(), self.text_email.text(),
                                                       self.text_ime.text() or self.text_naziv, self.text_prezime.text())
            if error_privatni is None:
                korisnici.append(PrivatniKorisnik(self.text_ime.text(), self.text_prezime.text(), self.text_drzavljanstvo.text(), self.text_email.text(),
                                                  self.text_telefon.text()))
                self.text_telefon.setText('')
                self.text_email.setText('')
                self.text_naziv.setText('')
                self.text_web.setText('')
                self.text_ime.setText('')
                self.text_prezime.setText('')
                self.text_drzavljanstvo.setText('')
                self.text_oib.setText('')
                self.label_error.setText('')

                korisnik = korisnici[len(korisnici)-1]
                korisnik.ispis()
            else:
                self.label_error.setText(error_privatni)

        elif self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            error_poslovni = provjera_korisnickog_unos(self.text_telefon.text(), self.text_email.text(),
                                                       self.text_naziv.text(), self.text_web.text())
            if error_poslovni is None:
                korisnici.append(PoslovniKorisnik(self.text_naziv.text(), self.text_web.text(), self.text_oib.text(),
                                                  self.text_email.text(), self.text_telefon.text()))
                self.text_telefon.setText('')
                self.text_email.setText('')
                self.text_naziv.setText('')
                self.text_web.setText('')
                self.text_ime.setText('')
                self.text_prezime.setText('')
                self.text_drzavljanstvo.setText('')
                self.text_oib.setText('')
                self.label_error.setText('')

                korisnik = korisnici[len(korisnici)-1]
                korisnik.ispis()
            else:
                self.label_error.setText(error_poslovni)





app = QtWidgets.QApplication(sys.argv)
win = App()
win.show()
sys.exit(app.exec_())

