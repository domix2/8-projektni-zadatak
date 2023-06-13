from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from enumeratori import TipKorisnika, TipArtikla
from korisnik import PoslovniKorisnik, PrivatniKorisnik
from artikl import Automobil, Stan
from prodaja import Prodaja
from utillities import provjera_korisnickog_unos, provjera_unosa_artikla, provjera_unosa_prodaje

korisnici = []
artikli = []
prodaje = []


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Projektni zadatak')
        self.setGeometry(200, 200, 1000, 530)
        self.initUI()

    def initUI(self):
        self.font = QtGui.QFont('Arial', 8)

# Frame korisnik
        self.frame_korisnik = QtWidgets.QFrame(self)
        self.frame_korisnik.setGeometry(QtCore.QRect(25, 30, 460, 220))
        self.frame_korisnik.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_korisnik.setFrameShadow(QtWidgets.QFrame.Raised)

        # Horizontal layout for korisnik
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_korisnik)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 431, 201))
        self.h_layout_all_k = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.h_layout_all_k.setContentsMargins(5, 5, 5, 5)

        # Grid layout for korisnik
        self.g_layout_k = QtWidgets.QGridLayout()
        self.g_layout_k.setContentsMargins(5, 5, 5, 5)

        # Label email
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setFont(self.font)
        self.label_email.setText('Email')
        self.label_email.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.label_email, 1, 0, 1, 1)

        # Text email
        self.text_email = QtWidgets.QLineEdit(self)
        self.text_email.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.text_email, 1, 1, 1, 1)

        # Label telefon
        self.label_telefon = QtWidgets.QLabel(self)
        self.label_telefon.setFont(self.font)
        self.label_telefon.setText('Telefon')
        self.label_telefon.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.label_telefon, 2, 0, 1, 1)

        # Text telefon
        self.text_telefon = QtWidgets.QLineEdit(self)
        self.text_telefon.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.text_telefon, 2, 1, 1, 1)

        # Label ime
        self.label_ime = QtWidgets.QLabel(self)
        self.label_ime.setFont(self.font)
        self.label_ime.setText('Ime')
        self.label_ime.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.label_ime, 3, 0, 1, 1)

        # Text ime
        self.text_ime = QtWidgets.QLineEdit(self)
        self.text_ime.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.text_ime, 3, 1, 1, 1)

        # label prezime
        self.label_prezime = QtWidgets.QLabel(self)
        self.label_prezime.setFont(self.font)
        self.label_prezime.setText('Prezime')
        self.label_prezime.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.label_prezime, 4, 0, 1, 1)

        # Text prezime
        self.text_prezime = QtWidgets.QLineEdit(self)
        self.text_prezime.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_k.addWidget(self.text_prezime, 4, 1, 1, 1)

        # Label Naziv
        self.label_naziv = QtWidgets.QLabel(self)
        self.label_naziv.setFont(self.font)
        self.label_naziv.setText('Naziv')
        self.label_naziv.setMaximumSize(QtCore.QSize(150, 26))
        self.label_naziv.hide()

        # Text Naziv
        self.text_naziv = QtWidgets.QLineEdit(self)
        self.text_naziv.setMaximumSize(QtCore.QSize(150, 26))
        self.text_naziv.hide()

        # Label Web
        self.label_web = QtWidgets.QLabel(self)
        self.label_web.setFont(self.font)
        self.label_web.setText('Web')
        self.label_web.setMaximumSize(QtCore.QSize(150, 26))
        self.label_web.hide()

        # Text Web
        self.text_web = QtWidgets.QLineEdit(self)
        self.text_web.setMaximumSize(QtCore.QSize(150, 26))
        self.text_web.hide()

        # Combobox tip_korisnika
        self.tip_korisnika = QtWidgets.QComboBox(self)

        for korisnik in TipKorisnika:
            self.tip_korisnika.addItem(str(korisnik.value))

        self.tip_korisnika.currentTextChanged.connect(self.combobox_changed_tip_korisnika)
        self.g_layout_k.addWidget(self.tip_korisnika, 0, 1, 1, 1)
        self.h_layout_all_k.addLayout(self.g_layout_k)

        # Label popis korisnika
        self.v_layout_popis_k = QtWidgets.QVBoxLayout()
        self.v_layout_popis_k.setContentsMargins(5, 5, 5, 5)
        self.label_popis_korisnika = QtWidgets.QLabel(self)
        self.label_popis_korisnika.setText('Popis korisnika')
        self.v_layout_popis_k.addWidget(self.label_popis_korisnika)

        # List ispis korisnika za ScrollArea
        self.list_ispis_korisnik = QtWidgets.QListWidget(self)
        self.list_ispis_korisnik.setStyleSheet("background-color: rgb(255, 255, 255);")

        # ScrollArea ispis podataka korisnika
        self.scrollArea_k = QtWidgets.QScrollArea(self)
        self.scrollArea_k.setMinimumSize(QtCore.QSize(250, 95))
        self.scrollArea_k.setWidgetResizable(True)
        self.scrollArea_k.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea_k.setWidget(self.list_ispis_korisnik)
        self.v_layout_popis_k.addWidget(self.scrollArea_k)

        # Button dodaj korisnika
        self.h_layout_button_k = QtWidgets.QHBoxLayout()
        self.button_dodaj_korisnika = QtWidgets.QPushButton(self)
        self.button_dodaj_korisnika.setText('Dodaj korisnika')
        self.button_dodaj_korisnika.clicked.connect(self.unos_korisnika)
        self.h_layout_button_k.addWidget(self.button_dodaj_korisnika)

        # Button obrisi korisnika
        self.button_obris_korisnika = QtWidgets.QPushButton(self)
        self.button_obris_korisnika.setText('Obrisi korisnika')
        self.button_obris_korisnika.clicked.connect(self.obrisi_korisnika)
        self.h_layout_button_k.addWidget(self.button_obris_korisnika)
        self.v_layout_popis_k.addLayout(self.h_layout_button_k)

        # Label error korisnik
        self.label_error_korisnik = QtWidgets.QLabel(self)
        self.label_error_korisnik.setFont(self.font)
        self.label_error_korisnik.setText('')
        self.label_error_korisnik.setMaximumSize(QtCore.QSize(250, 26))
        self.label_error_korisnik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_korisnik.setStyleSheet('color: red;')
        self.v_layout_popis_k.addWidget(self.label_error_korisnik)
        self.h_layout_all_k.addLayout(self.v_layout_popis_k)

        # Frame za naziv frame-a korisnik
        self.frame_label_korisnik = QtWidgets.QFrame(self.frame_korisnik)
        self.frame_label_korisnik.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.frame_label_korisnik.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_label_korisnik.setFrameShadow(QtWidgets.QFrame.Raised)

        # Label naziv frame-a korisnik
        self.label_frame_korisnik = QtWidgets.QLabel(self.frame_label_korisnik)
        self.label_frame_korisnik.setGeometry(QtCore.QRect(7, 7, 51, 16))
        self.label_frame_korisnik.setText('Korisnik')



        # Frame artikl
        self.frame_artikl = QtWidgets.QFrame(self)
        self.frame_artikl.setGeometry(QtCore.QRect(510, 30, 460, 220))
        self.frame_artikl.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_artikl.setFrameShadow(QtWidgets.QFrame.Raised)

        # Horizontal layout for artikl
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_artikl)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 431, 201))
        self.h_layout_all_a = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.h_layout_all_a.setContentsMargins(5, 5, 5, 5)

        # Grid layout for artikl
        self.g_layout_a = QtWidgets.QGridLayout()
        self.g_layout_a.setContentsMargins(5, 5, 5, 5)

        # Label naslov
        self.label_naslov = QtWidgets.QLabel(self)
        self.label_naslov.setMaximumSize(QtCore.QSize(150, 26))
        self.label_naslov.setFont(self.font)
        self.label_naslov.setText('Naslov')
        self.g_layout_a.addWidget(self.label_naslov, 1, 0, 1, 1)

        # Text naslov
        self.text_naslov = QtWidgets.QLineEdit(self)
        self.text_naslov.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_a.addWidget(self.text_naslov, 1, 1, 1, 1)

        # Label opis
        self.label_opis = QtWidgets.QLabel(self)
        self.label_opis.setMaximumSize(QtCore.QSize(150, 26))
        self.label_opis.setFont(self.font)
        self.label_opis.setText('Opis')
        self.g_layout_a.addWidget(self.label_opis, 2, 0, 1, 1)

        # Text opis
        self.text_opis = QtWidgets.QLineEdit(self)
        self.text_opis.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_a.addWidget(self.text_opis, 2, 1, 1, 1)

        # Label cijena
        self.label_cijena = QtWidgets.QLabel(self)
        self.label_cijena.setMaximumSize(QtCore.QSize(150, 26))
        self.label_cijena.setFont(self.font)
        self.label_cijena.setText('Cijena')
        self.g_layout_a.addWidget(self.label_cijena, 3, 0, 1, 1)

        # Text cijena
        self.text_cijena = QtWidgets.QLineEdit(self)
        self.text_cijena.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_a.addWidget(self.text_cijena, 3, 1, 1, 1)

        # Label snaga
        self.label_snaga = QtWidgets.QLabel(self)
        self.label_snaga.setMaximumSize(QtCore.QSize(150, 26))
        self.label_snaga.setFont(self.font)
        self.label_snaga.setText('Snaga')
        self.g_layout_a.addWidget(self.label_snaga, 5, 0, 1, 1)

        # Text snaga
        self.text_snaga = QtWidgets.QLineEdit(self)
        self.text_snaga.setMaximumSize(QtCore.QSize(150, 26))
        self.g_layout_a.addWidget(self.text_snaga, 5, 1, 1, 1)

        # Label kvadratura
        self.label_kvadratura = QtWidgets.QLabel(self)
        self.label_kvadratura.setMaximumSize(QtCore.QSize(150, 26))
        self.label_kvadratura.setFont(self.font)
        self.label_kvadratura.setText('Kvadrata')
        self.label_kvadratura.hide()

        # Text kvadratura
        self.text_kvadratura = QtWidgets.QLineEdit(self)
        self.text_kvadratura.setMaximumSize(QtCore.QSize(150, 26))
        self.text_kvadratura.hide()

        # Combobox tip_artikla
        self.tip_artikla = QtWidgets.QComboBox(self)

        for artikl in TipArtikla:
            self.tip_artikla.addItem(str(artikl.value))

        self.tip_artikla.currentTextChanged.connect(self.combobox_changed_tip_artikla)
        self.g_layout_a.addWidget(self.tip_artikla, 0, 1, 1, 1)
        self.h_layout_all_a.addLayout(self.g_layout_a)

        # Label popis artikla
        self.v_layout_popis_a = QtWidgets.QVBoxLayout()
        self.v_layout_popis_a.setContentsMargins(5, 5, 5, 5)
        self.label_popis_artikla = QtWidgets.QLabel(self)
        self.label_popis_artikla.setText('Popis Artikla')
        self.v_layout_popis_a.addWidget(self.label_popis_artikla)

        # List ispis artikla za ScrollArea
        self.list_ispis_artikla = QtWidgets.QListWidget(self)
        self.list_ispis_artikla.setStyleSheet("background-color: rgb(255, 255, 255);")

        # ScrollArea ispis podataka artikla
        self.scrollArea_a = QtWidgets.QScrollArea(self)
        self.scrollArea_a.setMinimumSize(QtCore.QSize(250, 95))
        self.scrollArea_a.setWidgetResizable(True)
        self.scrollArea_a.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea_a.setWidget(self.list_ispis_artikla)
        self.v_layout_popis_a.addWidget(self.scrollArea_a)

        # Button dodaj artikl
        self.h_layout_button_a = QtWidgets.QHBoxLayout()
        self.button_dodaj_artikl = QtWidgets.QPushButton(self)
        self.button_dodaj_artikl.setText('Dodaj artikl')
        self.button_dodaj_artikl.clicked.connect(self.unos_artikla)
        self.h_layout_button_a.addWidget(self.button_dodaj_artikl)

        # Button obrisi artikl
        self.button_obrisi_artikl = QtWidgets.QPushButton(self)
        self.button_obrisi_artikl.setText('Obrisi artikl')
        self.button_obrisi_artikl.clicked.connect(self.obrisi_artikl)
        self.h_layout_button_a.addWidget(self.button_obrisi_artikl)
        self.v_layout_popis_a.addLayout(self.h_layout_button_a)

        self.label_error_artikl = QtWidgets.QLabel(self)
        self.label_error_artikl.setFont(self.font)
        self.label_error_artikl.setText('')
        self.label_error_artikl.setMaximumSize(QtCore.QSize(250, 26))
        self.label_error_artikl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_artikl.setStyleSheet('color: red;')
        self.v_layout_popis_a.addWidget(self.label_error_artikl)
        self.h_layout_all_a.addLayout(self.v_layout_popis_a)

        # Frame za naziv frame-a artikl
        self.frame_label_artikl = QtWidgets.QFrame(self.frame_artikl)
        self.frame_label_artikl.setGeometry(QtCore.QRect(0, 0, 48, 31))
        self.frame_label_artikl.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_label_artikl.setFrameShadow(QtWidgets.QFrame.Raised)

        # Label naziv frame-a artikl
        self.label_frame_artikl = QtWidgets.QLabel(self.frame_label_artikl)
        self.label_frame_artikl.setText('Artikl')
        self.label_frame_artikl.setGeometry(QtCore.QRect(7, 7, 35, 16))



        # Frame prodaja
        self.frame_prodaja = QtWidgets.QFrame(self)
        self.frame_prodaja.setGeometry(QtCore.QRect(245, 290, 510, 195))
        self.frame_prodaja.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_prodaja.setFrameShadow(QtWidgets.QFrame.Raised)

        # Horizontal layout for prodaja
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_prodaja)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 481, 181))
        self.h_layout_all_p = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.h_layout_all_p.setContentsMargins(5, 5, 5, 5)

        # Grid layout for prodaja
        self.g_layout_p = QtWidgets.QGridLayout()
        self.g_layout_p.setRowMinimumHeight(1, 30)
        self.g_layout_p.setRowMinimumHeight(2, 30)

        self.v_layout_prodaja = QtWidgets.QVBoxLayout()
        self.v_layout_prodaja.setContentsMargins(5, 25, 5, 15)
        self.h_layout_all_p.addLayout(self.v_layout_prodaja)
        self.v_layout_prodaja.addLayout(self.g_layout_p)

        # Label izbor tipa korisnika u prodaji
        self.label_prodaja_korisnik = QtWidgets.QLabel(self)
        self.label_prodaja_korisnik.setText('Korisnik')
        self.label_prodaja_korisnik.setMinimumSize(QtCore.QSize(40, 0))
        self.label_prodaja_korisnik.setMaximumSize(QtCore.QSize(50, 26))
        self.g_layout_p.addWidget(self.label_prodaja_korisnik, 1, 0, 1, 1)

        # Combobox tip korisnika u prodaji
        self.prodaja_tip_korisnika = QtWidgets.QComboBox(self)
        self.prodaja_tip_korisnika.setMinimumSize(QtCore.QSize(120, 0))
        self.prodaja_tip_korisnika.setMaximumSize(QtCore.QSize(120, 26))
        self.g_layout_p.addWidget(self.prodaja_tip_korisnika, 1, 1, 1, 1)

        # Label izbor tipa prodaje u prodaji
        self.label_prodaja_prodaja = QtWidgets.QLabel(self)
        self.label_prodaja_prodaja.setText('Prodaja')
        self.g_layout_p.addWidget(self.label_prodaja_prodaja, 2, 0, 1, 1)

        # Combobox tip prodaje u prodaji
        self.prodaja_tip_prodaje = QtWidgets.QComboBox(self)
        self.prodaja_tip_prodaje.setMinimumSize(QtCore.QSize(120, 0))
        self.prodaja_tip_prodaje.setMaximumSize(QtCore.QSize(120, 26))
        self.g_layout_p.addWidget(self.prodaja_tip_prodaje, 2, 1, 1, 1)

        # Label datum prodaje
        self.label_prodaja_datum = QtWidgets.QLabel(self)
        self.label_prodaja_datum.setText('Datum')
        self.g_layout_p.addWidget(self.label_prodaja_datum, 3, 0, 1, 1)

        # DateEdit datum prodaje
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(120, 26))
        self.g_layout_p.addWidget(self.dateEdit, 3, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(139, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.g_layout_p.addItem(spacerItem2, 4, 1, 1, 1)

        self.label_error_prodaja = QtWidgets.QLabel(self)
        self.label_error_prodaja.setFont(self.font)
        self.label_error_prodaja.setText('')
        self.label_error_prodaja.setMaximumSize(QtCore.QSize(250, 26))
        self.label_error_prodaja.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_prodaja.setStyleSheet('color: red;')
        self.v_layout_prodaja.addWidget(self.label_error_prodaja)

        # Label popis prodaja
        self.h_layout_all_p.addLayout(self.g_layout_p)
        self.v_layout_popis_p = QtWidgets.QVBoxLayout()
        self.v_layout_popis_p.setContentsMargins(5, 5, 5, 5)
        self.label_popis_prodaja = QtWidgets.QLabel(self)
        self.label_popis_prodaja.setText('Popis prodaja')
        self.v_layout_popis_p.addWidget(self.label_popis_prodaja)

        # List ispis prodaje za ScrollArea
        self.list_ispis_prodaja = QtWidgets.QListWidget(self)
        self.list_ispis_prodaja.setStyleSheet("background-color: rgb(255, 255, 255);")

        # ScrollArea ispis podataka prodaja
        self.scrollArea_p = QtWidgets.QScrollArea(self)
        self.scrollArea_p.setMinimumSize(QtCore.QSize(250, 95))
        self.scrollArea_p.setWidgetResizable(True)
        self.scrollArea_p.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea_p.setWidget(self.list_ispis_prodaja)
        self.v_layout_popis_p.addWidget(self.scrollArea_p)

        # Button dodaj prodaju
        self.h_layout_p = QtWidgets.QHBoxLayout()
        self.button_dodaj_prodaju = QtWidgets.QPushButton(self)
        self.button_dodaj_prodaju.setText('Dodaj prodaju')
        self.button_dodaj_prodaju.clicked.connect(self.unos_prodaje)
        self.h_layout_p.addWidget(self.button_dodaj_prodaju)

        # Button obrisi prodaju
        self.button_obrisi_prodaju = QtWidgets.QPushButton(self)
        self.button_obrisi_prodaju.setText('Obrisi prodaju')
        self.button_obrisi_prodaju.clicked.connect(self.obrisi_prodaju)
        self.h_layout_p.addWidget(self.button_obrisi_prodaju)
        self.v_layout_popis_p.addLayout(self.h_layout_p)
        self.h_layout_all_p.addLayout(self.v_layout_popis_p)

        # Frame za naziv frame-a prodaje
        self.frame_label_prodaja = QtWidgets.QFrame(self.frame_prodaja)
        self.frame_label_prodaja.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.frame_label_prodaja.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_label_prodaja.setFrameShadow(QtWidgets.QFrame.Raised)

        # Label naziv frame-a prodaje
        self.label_prodaja = QtWidgets.QLabel(self.frame_label_prodaja)
        self.label_prodaja.setText('Prodaja')
        self.label_prodaja.setGeometry(QtCore.QRect(7, 7, 51, 16))


# Odabir i unos korisnika

    def combobox_changed_tip_korisnika(self):
        if self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            self.label_naziv.hide()
            self.label_web.hide()
            self.text_naziv.hide()
            self.text_web.hide()
            self.label_ime.show()
            self.label_prezime.show()
            self.text_ime.show()
            self.text_prezime.show()

            self.g_layout_k.removeWidget(self.label_naziv)
            self.g_layout_k.removeWidget(self.text_naziv)
            self.g_layout_k.removeWidget(self.label_web)
            self.g_layout_k.removeWidget(self.text_web)
            self.g_layout_k.addWidget(self.label_ime, 3, 0, 1, 1)
            self.g_layout_k.addWidget(self.text_ime, 3, 1, 1, 1)
            self.g_layout_k.addWidget(self.label_prezime, 4, 0, 1, 1)
            self.g_layout_k.addWidget(self.text_prezime, 4, 1, 1, 1)

        elif self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            self.label_ime.hide()
            self.label_prezime.hide()
            self.text_ime.hide()
            self.text_prezime.hide()
            self.label_naziv.show()
            self.label_web.show()
            self.text_naziv.show()
            self.text_web.show()

            self.g_layout_k.removeWidget(self.label_ime)
            self.g_layout_k.removeWidget(self.text_ime)
            self.g_layout_k.removeWidget(self.label_prezime)
            self.g_layout_k.removeWidget(self.text_prezime)
            self.g_layout_k.addWidget(self.label_naziv, 3, 0, 1, 1)
            self.g_layout_k.addWidget(self.text_naziv, 3, 1, 1, 1)
            self.g_layout_k.addWidget(self.label_web, 4, 0, 1, 1)
            self.g_layout_k.addWidget(self.text_web, 4, 1, 1, 1)

    # Dodavanje korisnika
    def unos_korisnika(self):
        if self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            error_k = provjera_korisnickog_unos(self.text_telefon.text(), self.text_email.text(), self.text_ime.text(),
                                               self.text_prezime.text())

        elif self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            error_k = provjera_korisnickog_unos(self.text_telefon.text(), self.text_email.text(), self.text_naziv.text(),
                                               self.text_web.text())

        if error_k is None:
            if self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
                korisnici.append(PrivatniKorisnik(self.text_ime.text(), self.text_prezime.text(),
                                                  self.text_telefon.text(), self.text_email.text()))

            elif self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
                korisnici.append(PoslovniKorisnik(self.text_naziv.text(), self.text_web.text(),
                                                  self.text_telefon.text(), self.text_email.text()))

            korisnik = korisnici[len(korisnici) - 1]
            self.list_ispis_korisnik.addItem(korisnik.ispis())
            # Dodavanje korisnika u comboboxa u prodaju
            self.prodaja_tip_korisnika.addItem(str(korisnik.email))

            self.text_ime.setText('')
            self.text_prezime.setText('')
            self.text_naziv.setText('')
            self.text_web.setText('')
            self.text_telefon.setText('')
            self.text_email.setText('')
            self.label_error_korisnik.setText('')

        else:
            self.label_error_korisnik.setText(error_k)

    # Brisanje korisnika iz liste
    def obrisi_korisnika(self):
        list_items = self.list_ispis_korisnik.selectedItems()
        list_row = self.list_ispis_korisnik.currentRow()

        if not list_items:
            return

        for item in list_items:
            self.list_ispis_korisnik.takeItem(self.list_ispis_korisnik.row(item))

        # Brisanje korisnika iz comboboxa u prodaji
        self.prodaja_tip_korisnika.removeItem(list_row)

        del korisnici[list_row]


# Odabir i unos artikla

    def combobox_changed_tip_artikla(self):
        if self.tip_artikla.currentText() == TipArtikla.AUTOMOBIL.value:
            self.label_kvadratura.hide()
            self.text_kvadratura.hide()
            self.label_snaga.show()
            self.text_snaga.show()

            self.g_layout_a.removeWidget(self.label_kvadratura)
            self.g_layout_a.removeWidget(self.text_kvadratura)
            self.g_layout_a.addWidget(self.label_snaga, 5, 0, 1, 1)
            self.g_layout_a.addWidget(self.text_snaga, 5, 1, 1, 1)

        elif self.tip_artikla.currentText() == TipArtikla.STAN.value:
            self.label_snaga.hide()
            self.text_snaga.hide()
            self.label_kvadratura.show()
            self.text_kvadratura.show()

            self.g_layout_a.removeWidget(self.label_snaga)
            self.g_layout_a.removeWidget(self.text_snaga)
            self.g_layout_a.addWidget(self.label_kvadratura, 5, 0, 1, 1)
            self.g_layout_a.addWidget(self.text_kvadratura, 5, 1, 1, 1)

    # Dodavanje artikla
    def unos_artikla(self):
        if self.tip_artikla.currentText() == TipArtikla.AUTOMOBIL.value:
            error_a = provjera_unosa_artikla(self.text_naslov.text(), self.text_opis.text(), self.text_cijena.text(),
                                             self.text_snaga.text())

        elif self.tip_artikla.currentText() == TipArtikla.STAN.value:
            error_a = provjera_unosa_artikla(self.text_naslov.text(), self.text_opis.text(), self.text_cijena.text(),
                                             self.text_kvadratura.text())

        if error_a is None:
            if self.tip_artikla.currentText() == TipArtikla.AUTOMOBIL.value:
                artikli.append(Automobil(self.text_naslov.text(), self.text_opis.text(), self.text_cijena.text(),
                                         self.text_snaga.text()))

            elif self.tip_artikla.currentText() == TipArtikla.STAN.value:
                artikli.append(Stan(self.text_naslov.text(), self.text_opis.text(), self.text_cijena.text(),
                                    self.text_kvadratura.text()))

            artikl = artikli[len(artikli) - 1]
            self.list_ispis_artikla.addItem(artikl.ispis())
            # Dodavanje prodaje u comboboxa u prodaju
            self.prodaja_tip_prodaje.addItem(str(artikl.opis))

            self.text_naslov.setText('')
            self.text_opis.setText('')
            self.text_cijena.setText('')
            self.text_snaga.setText('')
            self.text_kvadratura.setText('')
            self.label_error_artikl.setText('')

        else:
            self.label_error_artikl.setText(error_a)

    # Brisanje artikla
    def obrisi_artikl(self):
        list_items = self.list_ispis_artikla.selectedItems()
        list_row = self.list_ispis_artikla.currentRow()

        if not list_items:
            return

        for item in list_items:
            self.list_ispis_artikla.takeItem(self.list_ispis_artikla.row(item))

        # Brisanje prodaje iz comboboxa u prodaji
        self.prodaja_tip_prodaje.removeItem(list_row)

        del artikli[list_row]


# Odabir i unos korisnika

    def unos_prodaje(self):
        error_p = provjera_unosa_prodaje(self.prodaja_tip_korisnika.currentText(),
                                         self.prodaja_tip_prodaje.currentText())

        if error_p is None:
            broj_korisnika = int(self.prodaja_tip_korisnika.currentIndex())
            broj_artikla = int(self.prodaja_tip_prodaje.currentIndex())



            prodaje.append(Prodaja(self.dateEdit.date(), korisnici[broj_korisnika], artikli[broj_artikla]))

            prodaja = prodaje[len(prodaje) - 1]
            self.list_ispis_prodaja.addItem(prodaja.ispis())

            self.label_error_prodaja.setText('')

        else:
            self.label_error_prodaja.setText(error_p)

    # Brisanje prodaje
    def obrisi_prodaju(self):
        list_items = self.list_ispis_prodaja.selectedItems()
        list_row = self.list_ispis_prodaja.currentRow()

        if not list_items:
            return

        for item in list_items:
            self.list_ispis_prodaja.takeItem(self.list_ispis_prodaja.row(item))

        del prodaje[list_row]



app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())