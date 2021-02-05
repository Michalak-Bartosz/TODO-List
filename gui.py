from random import randint
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QTableView, QPushButton, QMessageBox, QDesktopWidget, QSizePolicy, QFrame, \
    QCheckBox, QSpacerItem, QToolButton, QSizeGrip, QDateTimeEdit, QComboBox, QTextEdit, QHeaderView
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QDateTime, QSize
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5 import QtCore

from speak import Threader


class GuiWindowStart(object):

    # Uklad komponentow graficznych okna startowego
    def __init__(self):
        self.image_background = QLabel(self)
        self.image_pen_nib = QLabel(self)
        self.text_logo = QLabel("TODO List", self)
        self.image_logo = QLabel(self)
        self.zarejestruj = QPushButton("Rejestracja")
        self.zaloguj = QPushButton("Logowanie")
        self.wyjdz = QPushButton("Wyjdź")

    def set_up_gui(self, widget):
        widget.setObjectName("Okno startowe")

        # Właściwości okna startowego
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(500, 500)

        # Tło ekranu startowego
        self.image_background.setPixmap(QPixmap("Image/StartWindow.png"))
        self.image_background.setScaledContents(True)
        self.image_background.resize(500, 500)

        # Stalówka
        self.image_pen_nib.setPixmap(QPixmap("Image/Pen-Nib.png"))
        self.image_pen_nib.setScaledContents(True)
        self.image_pen_nib.resize(250, 150)
        self.image_pen_nib.move(0, -10)

        # Tytuł aplikacji
        self.text_logo.setStyleSheet("QLabel { background-color: rgb(89, 166, 0); "
                                     "border-style: outset; "
                                     "border-width: 5px; "
                                     "border-radius: 10px; "
                                     "border-color: rgb(35, 35, 35); "
                                     "font: bold 35px; "
                                     "min-width: 4em; "
                                     "min-height: 1em; "
                                     "padding : 6px; }")
        self.text_logo.setFont(QFont("Forte", 35, QFont.Bold))
        self.text_logo.move(150, 100)

        # Logo aplikacji
        self.image_logo.setPixmap(QPixmap("Image/Ico/App_icon.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(100, 100)
        self.image_logo.move(320, 70)

        # Przyciski
        self.zarejestruj.setStyleSheet("QPushButton { background-color: black; "
                                       "border-style: outset; "
                                       "border-width: 5px; "
                                       "border-radius: 10px; "
                                       "border-color: rgb(50, 90, 0); "
                                       "min-width: 0px; "
                                       "min-height: 1em; "
                                       "font-color=white; "
                                       "padding: 6px; "
                                       "color: white }"
                                       "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                       "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.zarejestruj.setFont(QFont("Consolas", 15, QFont.Bold))

        self.zaloguj.setStyleSheet("QPushButton { background-color: black; "
                                   "border-style: outset; "
                                   "border-width: 5px; "
                                   "border-radius: 10px; "
                                   "border-color: rgb(50, 90, 0); "
                                   "min-width: 0px; "
                                   "min-height: 1em; "
                                   "font-color=white; "
                                   "padding: 6px; "
                                   "color: white }"
                                   "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                   "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.zaloguj.setFont(QFont("Consolas", 15, QFont.Bold))

        self.wyjdz.setStyleSheet("QPushButton { background-color: black; "
                                 "border-style: outset; "
                                 "border-width: 5px; "
                                 "border-radius: 10px; "
                                 "border-color: rgb(50, 90, 0); "
                                 "min-width: 0px; "
                                 "min-height: 1em; "
                                 "font-color=white; "
                                 "padding: 6px; "
                                 "color: white }"
                                 "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                 "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.wyjdz.setFont(QFont("Consolas", 15, QFont.Bold))

        # Dodawanie przyciskow do layout'u
        przyciski = QVBoxLayout()
        przyciski.setAlignment(Qt.AlignCenter)
        przyciski.addWidget(self.zarejestruj)
        przyciski.addWidget(self.zaloguj)
        przyciski.addWidget(self.wyjdz)

        # Dodawanie komponentow do okna
        okno = QVBoxLayout(self)
        okno.addLayout(przyciski)

        self.center()
        self.show()

    @staticmethod
    def gui_messagebox(self, tekst, type):
        self.msgBoxWarning = QMessageBox(self)
        self.msgBoxWarning.setWindowFlag(Qt.FramelessWindowHint)

        if type == "Warning":
            self.msgBoxWarning.setIcon(QMessageBox.Warning)
        elif type == "Information":
            self.msgBoxWarning.setIcon(QMessageBox.Information)
        elif type == "Critical":
            self.msgBoxWarning.setIcon(QMessageBox.Critical)

        self.msgBoxWarning.setStyleSheet(".QMessageBox { background-color: rgb(36, 36, 36);"
                                         "min-width: 1em; "
                                         "min-height: 1.6em; "
                                         "border-style: outset; "
                                         "border-color: rgb(243, 175, 12); "
                                         "border-width: 6px; } "
                                         "QLabel { background: transparent; "
                                         "color: white } "
                                         "QPushButton { background-color: black; "
                                         "border-style: outset; "
                                         "border-width: 5px; "
                                         "border-radius: 10px; "
                                         "border-color: rgb(243, 175, 12); "
                                         "min-width: 300px; "
                                         "min-height: 0.5em; "
                                         "font-size: 15px Bold; "
                                         "padding: 6px; "
                                         "color: white }"
                                         "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                         "QPushButton:pressed { background-color: rgb(255, 198, 59) }")
        self.msgBoxWarning.setFont(QFont("Consolas", 15, QFont.Bold))
        self.msgBoxWarning.setText(tekst)
        self.msgBoxWarning.setLayoutDirection(QtCore.Qt.RightToLeft)

        qr = self.msgBoxWarning.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        qr.setX(qr.x() - 120)
        qr.setY(qr.y() - 40)
        self.msgBoxWarning.move(qr.topLeft())

        self.msgBoxWarning.exec_()

    def center(self):
        qr = self.frameGeometry()  # Pobranie geometrii okna
        cp = QDesktopWidget().availableGeometry().center()  # Ustalenie srodkowego puntu na ekranie
        qr.moveCenter(cp)  # Przeniesienie srodkowego punktu geometrii okna do srodkowego punktu ekranu
        self.move(qr.topLeft())  # Przeniesienie okna w centrum ekranu


class GuiWidgetWindowApp(object):

    # Układ komponentow graficznych aplikacji
    def __init__(self):
        # Przyciski funkcyjne
        self.tray_check_box = QCheckBox('Minimalizuj do paska zadan')
        self.minimalize = QToolButton()
        self.normal_full_sceen = QToolButton()
        self.close_app = QToolButton()

        # Przyciski
        self.wyloguj = QPushButton("Wyloguj")
        self.dodaj = QPushButton("Dodaj notatkę")
        self.usun = QPushButton("Usuń zaznaczone")
        self.zapisz = QPushButton("Zapisz")
        self.zakoncz = QPushButton("Koniec")

    def set_up_gui(self, widget, login):

        # Właściwości okna aplikacji
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(1000, 500)

        # Ustawienia graficzne tabeli wyswietlajacej notatki
        self.view_task = self.gui_view_tab()
        self.view_user = self.gui_view_tab()

        # Ustawienia graficzne przycisków funkcyjnych
        self.tray_check_box.setChecked(True)
        self.tray_check_box.setGeometry(200, 150, 100, 30)
        self.tray_check_box.setStyleSheet("QCheckBox { color: rgb(23, 100, 169) }"
                                          "QCheckBox::indicator { width :20; "
                                          "height :20; "
                                          "border-style: outset; "
                                          "border-width: 3px; "
                                          "border-radius: 5px; "
                                          "border-color: rgb(23, 100, 169) }"
                                          "QCheckBox::indicator:checked { image: url("
                                          "Image/Ico/Management_icon/CheckBox/checkbox_check.png) } "
                                          "QCheckBox::indicator:unchecked { image: url("
                                          "Image/Ico/Management_icon/CheckBox/checkbox_uncheck.png) }")
        self.tray_check_box.setFont(QFont("Consolas", 12, QFont.Bold))

        self.edit = self.gui_edytuj_uzytkownika_settings_button()
        self.edit.setText("Edytuj konto")

        self.minimalize.setToolTip("Minimalizacja\nokna")
        self.minimalize.setStyleSheet("QToolButton { border-image: url(Image/Ico/Management_icon/Minimalize_icon.png); "
                                      "min-width: 25px; "
                                      "min-height: 25px }"
                                      "QToolButton:hover { background-color: rgb(80, 80, 80) }"
                                      "QToolButton:pressed { background-color: rgb(89, 166, 0) }")

        self.normal_full_sceen.setToolTip("Maksymalizacja\nokna")
        self.normal_full_sceen.setStyleSheet(
            "QToolButton { border-image: url(Image/Ico/Management_icon/Fullscreen_icon.png); "
            "min-width: 25px; "
            "min-height: 25px }"
            "QToolButton:hover { background-color: rgb(80, 80, 80) }"
            "QToolButton:pressed { background-color: rgb(89, 166, 0) }")

        self.close_app.setToolTip("Zamknij\naplikację")
        self.close_app.setStyleSheet(
            "QToolButton { border-image: url(Image/Ico/Management_icon/Close_icon.png); "
            "min-width: 25px; "
            "min-height: 25px }"
            "QToolButton:hover { background-color: rgb(80, 80, 80) }"
            "QToolButton:pressed { background-color: rgb(89, 166, 0) }")

        self.frame_window = QFrame(widget)
        self.frame_window.resize(self.frameGeometry().width(), self.frameGeometry().height())
        self.frame_window.setStyleSheet("QFrame { background-color: rgb(36, 36, 36); "
                                        "border-style: outset; "
                                        "border-color: rgb(50, 90, 0); "
                                        "border-width: 6px; "
                                        "border-radius: 10px }")

        self.frame_bar = QFrame(widget)
        self.frame_bar.resize(self.frameGeometry().width(), 50)
        self.frame_bar.setStyleSheet("QFrame { background-color: rgb(10, 10, 10); "
                                     "border-style: outset; "
                                     "border-color: rgb(50, 90, 0); "
                                     "border-width: 6px; "
                                     "border-radius: 10px }")

        # Tworzenie tool bara
        tool_bar_layout = QHBoxLayout()

        # Dodawanie przyciskow funkcyjnych do layout'u
        przyciski_funkcyjne = QHBoxLayout()
        przyciski_funkcyjne.addWidget(self.tray_check_box)
        przyciski_funkcyjne.addWidget(self.edit)
        przyciski_funkcyjne.addWidget(self.minimalize)
        przyciski_funkcyjne.addWidget(self.normal_full_sceen)
        przyciski_funkcyjne.addWidget(self.close_app)
        przyciski_funkcyjne.setAlignment(Qt.AlignRight)

        # Dodanie layout'u przyciskow funkcyjnych do tool bara
        tool_bar_layout.addLayout(przyciski_funkcyjne)

        # Ustawienia graficzne przycisków
        self.wyloguj.setStyleSheet("QPushButton { background-color: black; "
                                   "border-style: outset; "
                                   "border-width: 5px; "
                                   "border-radius: 10px; "
                                   "border-color: rgb(50, 90, 0); "
                                   "min-width: 10em; "
                                   "min-height: 2em; "
                                   "font-color=white; "
                                   "padding: 6px; "
                                   "color: white }"
                                   "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                   "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.wyloguj.setFont(QFont("Consolas", 15, QFont.Bold))

        self.dodaj.setStyleSheet("QPushButton { background-color: black; "
                                 "border-style: outset; "
                                 "border-width: 5px; "
                                 "border-radius: 10px; "
                                 "border-color: rgb(50, 90, 0); "
                                 "min-width: 14em; "
                                 "min-height: 2em; "
                                 "font-color=white; "
                                 "padding: 6px; "
                                 "color: white }"
                                 "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                 "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.dodaj.setFont(QFont("Consolas", 15, QFont.Bold))

        self.usun.setStyleSheet("QPushButton { background-color: black; "
                                "border-style: outset; "
                                "border-width: 5px; "
                                "border-radius: 10px; "
                                "border-color: rgb(50, 90, 0); "
                                "min-width: 16em; "
                                "min-height: 2em; "
                                "font-color=white; "
                                "padding: 6px; "
                                "color: white }"
                                "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.usun.setFont(QFont("Consolas", 15, QFont.Bold))
        self.usun.setToolTip("Nacisnij na numer wiersza notatki,\naby ją zaznaczyć")

        if login == "Admin":
            self.uzytkownicy = QPushButton("Zarządzaj użytkownikami")
            self.uzytkownicy.setStyleSheet("QPushButton { background-color: black; "
                                           "border-style: outset; "
                                           "border-width: 5px; "
                                           "border-radius: 10px; "
                                           "border-color: rgb(50, 90, 0); "
                                           "min-width: 20em; "
                                           "min-height: 2em; "
                                           "font-color=white; "
                                           "padding: 6px; "
                                           "color: white }"
                                           "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                           "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
            self.uzytkownicy.setFont(QFont("Consolas", 15, QFont.Bold))

        self.zapisz.setStyleSheet("QPushButton { background-color: black; "
                                  "border-style: outset; "
                                  "border-width: 5px; "
                                  "border-radius: 10px; "
                                  "border-color: rgb(50, 90, 0); "
                                  "min-width: 10em; "
                                  "min-height: 2em; "
                                  "font-color=white; "
                                  "padding: 6px; "
                                  "color: white }"
                                  "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                  "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.zapisz.setFont(QFont("Consolas", 15, QFont.Bold))

        self.zakoncz.setStyleSheet("QPushButton { background-color: black; "
                                   "border-style: outset; "
                                   "border-width: 5px; "
                                   "border-radius: 10px; "
                                   "border-color: rgb(50, 90, 0); "
                                   "min-width: 8em; "
                                   "min-height: 1em; "
                                   "font-color=white; "
                                   "padding: 6px; "
                                   "color: white }"
                                   "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                   "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.zakoncz.setFont(QFont("Consolas", 15, QFont.Bold))

        # Dodawanie przyciskow do layout'u
        przyciski = QHBoxLayout()
        przyciski.addWidget(self.wyloguj)
        przyciski.addWidget(self.dodaj)
        przyciski.addWidget(self.usun)
        if login == "Admin":
            przyciski.addWidget(self.uzytkownicy)
        przyciski.addWidget(self.zapisz)
        przyciski.addWidget(self.zakoncz)

        # Dodawanie komponentow do okna
        okno = QVBoxLayout(self)
        # okno.setContentsMargins(QMargins())
        # okno.setSpacing(0)
        okno.addLayout(tool_bar_layout)
        okno.addItem(QSpacerItem(QSizePolicy.Expanding, 10))
        okno.addWidget(self.view_task)
        okno.addWidget(self.view_user)
        okno.addLayout(przyciski)
        okno.addWidget(QSizeGrip(self), 0, Qt.AlignBottom | Qt.AlignRight)

        # Tytuł aplikacji
        self.text_logo = QLabel("TODO List", self)
        self.text_logo.setStyleSheet("QLabel { background-color: none; "
                                     "font-style: outset; "
                                     "font: bold 35px; "
                                     "min-width: 4em; "
                                     "min-height: 1.1em; "
                                     "color: rgb(23, 100, 169) }")
        self.text_logo.setFont(QFont("Forte", 35, QFont.Bold))
        self.text_logo.move(10, 0)

        # Logo aplikacji
        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/App_icon_fill.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(41, 41)
        self.image_logo.move(10, 58)

        self.center()
        self.show()

    @staticmethod
    def gui_messagebox(self, tekst, type):
        self.msgBoxWarning = QMessageBox(self)
        self.msgBoxWarning.setWindowFlag(Qt.FramelessWindowHint)

        if type == "Warning":
            self.msgBoxWarning.setIcon(QMessageBox.Warning)
        elif type == "Information":
            self.msgBoxWarning.setIcon(QMessageBox.Information)
        elif type == "Critical":
            self.msgBoxWarning.setIcon(QMessageBox.Critical)

        self.msgBoxWarning.setStyleSheet(".QMessageBox { background-color: rgb(36, 36, 36);"
                                         "min-width: 1em; "
                                         "min-height: 1.6em; "
                                         "border-style: outset; "
                                         "border-color: rgb(243, 175, 12); "
                                         "border-width: 6px; } "
                                         "QLabel { background: transparent; "
                                         "color: white } "
                                         "QPushButton { background-color: black; "
                                         "border-style: outset; "
                                         "border-width: 5px; "
                                         "border-radius: 10px; "
                                         "border-color: rgb(243, 175, 12); "
                                         "min-width: 300px; "
                                         "min-height: 0.5em; "
                                         "font-size: 15px Bold; "
                                         "padding: 6px; "
                                         "color: white }"
                                         "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                         "QPushButton:pressed { background-color: rgb(255, 198, 59) }")
        self.msgBoxWarning.setFont(QFont("Consolas", 15, QFont.Bold))
        self.msgBoxWarning.setText(tekst)
        self.msgBoxWarning.setLayoutDirection(QtCore.Qt.RightToLeft)

        qr = self.msgBoxWarning.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        qr.setX(qr.x() - 120)
        qr.setY(qr.y() - 40)
        self.msgBoxWarning.move(qr.topLeft())

        self.msgBoxWarning.exec_()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def gui_view_tab(self):
        view = QTableView()
        view.setStyleSheet("QTableView { background-color: rgb(12, 37, 0); "
                           "min-width: 15em }")

        view.horizontalHeader().setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        view.horizontalHeader().setStyleSheet("QHeaderView { background-color: rgb(12, 37, 0) }"
                                              "QHeaderView::section {background-color: rgb(1, 61, 115); "
                                              "color: white; "
                                              "border-style: outset; "
                                              "border-color: rgb(1, 61, 115); "
                                              "border-width: 6px; "
                                              "border-radius: 0; "
                                              "min-width: 8em; "
                                              "min-height: 2em }")
        view.horizontalHeader().setFont(QFont("Consolas", 12, QFont.Bold))
        view.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        view.verticalHeader().setStyleSheet("QHeaderView { background-color: rgb(12, 37, 0) }"
                                            "QHeaderView::section {background-color: rgb(1, 61, 115); "
                                            "color: white; "
                                            "border-style: outset; "
                                            "border-color: rgb(1, 61, 115); "
                                            "border-width: 6px; "
                                            "min-width: 2em }")
        view.verticalHeader().setFont(QFont("Consolas", 12, QFont.Bold))
        view.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        view.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        return view

    def gui_usun_notatke_button(self):
        button = QPushButton("Usuń")
        button.setStyleSheet(
            "QPushButton { background-color: rgb(171, 0, 0); color: white}"
            "QPushButton:hover { background-color: rgb(240, 0, 0) }"
            "QPushButton:pressed { background-color: rgb(140, 0, 0) }")
        button.setIcon(QIcon("Image/Ico/Management_icon/Rubbish_bin_icon.png"))
        button.setIconSize(QSize(25, 25))
        button.setFont(QFont("Consolas", 12, QFont.Bold))
        button.clicked.connect(self.usun_notatke_fun)
        return button

    def gui_odswiez_notatke_button(self):
        button = QPushButton("Odśwież")
        button.setStyleSheet(
            "QPushButton { background-color: rgb(32, 129, 255); color: white}"
            "QPushButton:hover { background-color: rgb(72, 151, 255) }"
            "QPushButton:pressed { background-color: rgb(0, 32, 74) }")
        button.setIcon(QIcon("Image/Ico/Management_icon/Edit_note_icon.png"))
        button.setIconSize(QSize(25, 25))
        button.setFont(QFont("Consolas", 12, QFont.Bold))
        button.clicked.connect(self.update_note_windows_fun)
        return button

    def gui_usun_uzytkownika_button(self):
        button = QPushButton("Usuń")
        button.setStyleSheet(
            "QPushButton { background-color: rgb(171, 0, 0); color: white}"
            "QPushButton:hover { background-color: rgb(240, 0, 0) }"
            "QPushButton:pressed { background-color: rgb(140, 0, 0) }")
        button.setIcon(QIcon("Image/Ico/Management_icon/Rubbish_bin_icon.png"))
        button.setIconSize(QSize(25, 25))
        button.setFont(QFont("Consolas", 12, QFont.Bold))
        button.clicked.connect(self.usun_uzytkownika_fun)
        return button

    def gui_edytuj_uzytkownika_button(self):
        button = QPushButton("Edytuj")
        button.setStyleSheet(
            "QPushButton { background-color: rgb(32, 129, 255); color: white}"
            "QPushButton:hover { background-color: rgb(72, 151, 255) }"
            "QPushButton:pressed { background-color: rgb(0, 32, 74) }")
        button.setIcon(QIcon("Image/Ico/Management_icon/Edit_user_icon.png"))
        button.setIconSize(QSize(25, 25))
        button.setFont(QFont("Consolas", 12, QFont.Bold))
        button.clicked.connect(self.edytuj_uzytkownika_fun)
        return button

    def gui_edytuj_uzytkownika_settings_button(self):
        button = QPushButton("Edytuj")
        button.setStyleSheet(
            "QPushButton { background-color: rgb(32, 129, 255); color: white}"
            "QPushButton:hover { background-color: rgb(72, 151, 255) }"
            "QPushButton:pressed { background-color: rgb(0, 32, 74) }")
        button.setIcon(QIcon("Image/Ico/Management_icon/Edit_user_icon.png"))
        button.setIconSize(QSize(25, 25))
        button.setFont(QFont("Consolas", 12, QFont.Bold))
        button.clicked.connect(self.edytuj_uzytkownika_settings_fun)
        return button

    def gui_czytaj_button(self):
        czytaj = QPushButton("")
        czytaj.setStyleSheet(
            "QPushButton { background-color: rgb(32, 129, 255); color: white}"
            "QPushButton:hover { background-color: rgb(72, 151, 255) }"
            "QPushButton:pressed { background-color: rgb(0, 32, 74) }")
        czytaj.setIcon(QIcon("Image/Ico/Management_icon/Speaker_icon.png"))
        czytaj.setIconSize(QSize(25, 25))
        czytaj.setFont(QFont("Consolas", 15, QFont.Bold))
        czytaj.clicked.connect(self.czytaj_tekst_fun)
        return czytaj

    def gui_zrobione_checkbox(self, status):
        zrobione = QCheckBox("")
        if status == 'TAK':
            zrobione.setChecked(True)
        else:
            zrobione.setChecked(False)
        zrobione.setGeometry(200, 150, 100, 30)
        zrobione.setStyleSheet("QCheckBox { color: rgb(23, 100, 169) }"
                               "QCheckBox::indicator { width :20; "
                               "height :20; "
                               "border-style: outset; "
                               "border-width: 3px; "
                               "border-radius: 5px; "
                               "border-color: rgb(23, 100, 169) }"
                               "QCheckBox::indicator:checked { image: url("
                               "Image/Ico/Management_icon/CheckBox/checkbox_check.png) } "
                               "QCheckBox::indicator:unchecked { image: url("
                               "Image/Ico/Management_icon/CheckBox/checkbox_uncheck.png) }")
        zrobione.setFont(QFont("Consolas", 12, QFont.Bold))
        zrobione.toggled.connect(self.zrobione_fun)
        return zrobione

    def gui_wyroznione_checkbox(self, status):
        wyroznione = QCheckBox("")
        if status == 'TAK':
            wyroznione.setChecked(True)
        else:
            wyroznione.setChecked(False)
        wyroznione.setGeometry(200, 150, 100, 30)
        wyroznione.setStyleSheet("QCheckBox { color: rgb(23, 100, 169) }"
                                 "QCheckBox::indicator { width :20; "
                                 "height :20; "
                                 "border-style: outset; "
                                 "border-width: 3px; "
                                 "border-radius: 5px; "
                                 "border-color: rgb(23, 100, 169) }"
                                 "QCheckBox::indicator:checked { image: url("
                                 "Image/Ico/Management_icon/CheckBox/checkbox_check.png) } "
                                 "QCheckBox::indicator:unchecked { image: url("
                                 "Image/Ico/Management_icon/CheckBox/checkbox_uncheck.png) }")
        wyroznione.setFont(QFont("Consolas", 12, QFont.Bold))
        wyroznione.toggled.connect(self.wyroznione_fun)
        return wyroznione

    def gui_administrator_label(self):
        label = QLabel("Administrator")
        label.setStyleSheet("QLabel { background-color: rgb(50, 90, 0); color: white }")
        label.setFont(QFont("Consolas", 12, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        return label


class GuiWidgetWindowNote(object):
    def __init__(self):
        self.offset = None

    def set_up_gui(self, login, numer, wyroznienie, tresc, na_kiedy, priorytet):

        self.numer = numer
        self.login = login

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(500, 500)

        r = randint(0, 150)
        g = randint(0, 150)
        b = randint(0, 150)
        qss = "QFrame { background-color: rgba(" + str(r) + "," + str(g) + "," + str(b) + ", 230); "\
              "border-style: outset; "\
              "border-color: rgb(50, 90, 0); "\
              "border-width: 6px; "\
              "border-radius: 10px }"
        self.frame = QFrame(self)
        self.frame.resize(500, 500)
        self.frame.setStyleSheet(qss)

        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/Management_icon/Fav_Notes_icon.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(55, 55)
        self.image_logo.move(20, 15)

        # Etykiety
        self.logo_label = QLabel('  NOTATKA NUMER 0' + self.numer)
        self.logo_label.setStyleSheet("QLabel { color: white }")
        self.logo_label.setFont(QFont("Consolas", 25, QFont.Bold))
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.zadanie_label = QLabel('Treść: ')
        self.zadanie_label.setStyleSheet("QLabel { color: white }")
        self.zadanie_label.setFont(QFont("Consolas", 15, QFont.Bold))
        self.zadanie_label.setAlignment(Qt.AlignCenter)

        self.data_label = QLabel('Na kiedy: ')
        self.data_label.setStyleSheet("QLabel { color: white }")
        self.data_label.setFont(QFont("Consolas", 15, QFont.Bold))
        self.data_label.setAlignment(Qt.AlignCenter)

        self.priorytet_label = QLabel('Jaki priorytet zadania: ')
        self.priorytet_label.setStyleSheet("QLabel { color: white }")
        self.priorytet_label.setFont(QFont("Consolas", 15, QFont.Bold))
        self.priorytet_label.setAlignment(Qt.AlignCenter)

        # Pole edycyjne
        self.wyroznienie_checkbox = QCheckBox("Wyróżniona")
        self.wyroznienie_checkbox.setChecked(True)
        self.wyroznienie_checkbox.setEnabled(False)
        self.wyroznienie_checkbox.setGeometry(200, 150, 100, 30)
        self.wyroznienie_checkbox.setStyleSheet("QCheckBox { color: rgb(255, 255, 255) }"
                                                "QCheckBox::indicator { width :20; "
                                                "height :20; "
                                                "border-style: outset; "
                                                "border-width: 3px; "
                                                "border-radius: 5px; "
                                                "border-color: rgb(23, 100, 169) }"
                                                "QCheckBox::indicator:checked { image: url("
                                                "Image/Ico/Management_icon/CheckBox/checkbox_check.png) } "
                                                "QCheckBox::indicator:unchecked { image: url("
                                                "Image/Ico/Management_icon/CheckBox/checkbox_uncheck.png) }")
        self.wyroznienie_checkbox.setFont(QFont("Consolas", 12, QFont.Bold))
        self.wyroznienie_checkbox.setLayoutDirection(Qt.RightToLeft)

        self.zadanie = QTextEdit(tresc)
        self.zadanie.setStyleSheet("QTextEdit { color: white; "
                                   "background-color: rgb(36, 36, 36); "
                                   "border-style: outset; "
                                   "border-color: rgb(255, 255, 255); "
                                   "border-width: 2px; "
                                   "border-radius: 5px }")
        self.zadanie.setFont(QFont("Consolas", 12, QFont.Bold))
        self.zadanie.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.zadanie.setEnabled(False)

        self.data = QDateTimeEdit()
        self.data.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.data.setStyleSheet("QDateTimeEdit { color: white; "
                                "background-color: rgb(36, 36, 36); "
                                "border-style: outset; "
                                "border-color: rgb(255, 255, 255); "
                                "border-width: 2px; "
                                "border-radius: 5px }")
        self.data.setFont(QFont("Consolas", 12, QFont.Bold))
        current_time = QDateTime.currentDateTime()
        self.data.setDateTime(na_kiedy)
        self.data.setEnabled(False)

        self.priorytet = QLabel(priorytet)
        self.priorytet.setEnabled(False)
        # priorytet_list = ["Na wczoraj", "Super mało czasu", "Super ważne", "Ważne", "Normalne", "Mało ważne",
        #                   "Wcale nieważne"]
        # self.priorytet.addItems(priorytet_list)

        self.priorytet.setStyleSheet("QLabel { color: white; "
                                     "background-color: rgb(36, 36, 36); "
                                     "border-style: outset; "
                                     "border-color: rgb(255, 255, 255); "
                                     "border-width: 2px; "
                                     "border-radius: 5px }"
                                     "QListView { background-color: rgb(70, 192, 242) }"
                                     "QComboBox::item:hover { background-color: rgb(70, 192, 242) }")
        self.priorytet.setFont(QFont("Consolas", 12, QFont.Bold))

        self.czytaj = QPushButton("Naciśnij aby przeczytać notatkę")
        self.czytaj.setStyleSheet(
            "QPushButton { background-color: rgb(32, 129, 255); border-radius: 10px; color: white}"
            "QPushButton:hover { background-color: rgb(72, 151, 255) }"
            "QPushButton:pressed { background-color: rgb(0, 32, 74) }")
        self.czytaj.setIcon(QIcon("Image/Ico/Management_icon/Speaker_icon.png"))
        self.czytaj.setIconSize(QSize(25, 25))
        self.czytaj.setFont(QFont("Consolas", 15, QFont.Bold))
        self.czytaj.clicked.connect(self.czytaj_tekst)

        # Układ okna logowania (kolumny)
        okno = QVBoxLayout(self)
        okno.setAlignment(Qt.AlignCenter)
        okno.addWidget(self.logo_label)
        okno.addWidget(self.wyroznienie_checkbox)
        okno.addWidget(self.zadanie_label)
        okno.addWidget(self.zadanie)
        okno.addWidget(self.data_label)
        okno.addWidget(self.data)
        okno.addWidget(self.priorytet_label)
        okno.addWidget(self.priorytet)
        okno.addWidget(self.czytaj)

        # Właściwości okna
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        if self.login == "Admin":
            qr.setX(qr.x() + 950)
        else:
            qr.setX(qr.x() + 750)
        self.move(qr.topLeft())

    def czytaj_tekst(self):
        tekst = self.zadanie.toPlainText()
        import pyttsx3
        tts_engine = pyttsx3.init()
        speaker_thread = Threader(args=[tekst, tts_engine])
        speaker_thread.start()

    def update_data(self, numer, tresc, na_kiedy, priorytet):
        self.logo_label.setText('  NOTATKA NUMER 0' + numer)
        self.zadanie.setText(tresc)
        self.data.setDateTime(na_kiedy)
        self.priorytet.setText(priorytet)

class WelcomeWindow(QDialog):

    # Okno rejestracji
    def __init__(self, login, parent=None):
        super(WelcomeWindow, self).__init__(parent)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(600, 200)

        self.frame = QFrame(self)
        self.frame.resize(600, 200)
        self.frame.setStyleSheet("QFrame { background-color: rgba(0, 66, 166, 240); "
                                 "border-style: outset; "
                                 "border-color: rgb(50, 90, 0); "
                                 "border-width: 6px; "
                                 "border-radius: 10px }")

        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/App_icon.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(50, 50)
        self.image_logo.move(15, 10)

        # Etykiety
        self.logo_label = QLabel('      TODO List')
        self.logo_label.setStyleSheet("QLabel { color: rgb(89, 166, 0) }")
        self.logo_label.setFont(QFont("Forte", 25, QFont.Bold))
        self.logo_label.setAlignment(Qt.AlignLeft)

        self.wiadomosc = QLabel('Witaj ' + login + '!\nTwoje notatki juz na Ciebie czekają!')
        self.wiadomosc.setStyleSheet("QLabel { color: white }")
        self.wiadomosc.setFont(QFont("Consolas", 20, QFont.Bold))
        self.wiadomosc.setAlignment(Qt.AlignCenter)

        # Przyciski
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok, Qt.Horizontal, self)
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        self.przyciski.button(QDialogButtonBox.Ok).setText("Rozpocznij notowanie!")
        self.przyciski.button(QDialogButtonBox.Ok).setStyleSheet("QPushButton { background-color: black; "
                                                                 "border-style: outset; "
                                                                 "border-width: 5px; "
                                                                 "border-radius: 10px; "
                                                                 "border-color: rgb(50, 90, 0); "
                                                                 "min-width: 1em; "
                                                                 "min-height: 1.6em; "
                                                                 "font-color=white; "
                                                                 "padding: 6px; "
                                                                 "color: white }"
                                                                 "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                                                 "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.przyciski.button(QDialogButtonBox.Ok).setFont(QFont("Consolas", 15, QFont.Bold))

        # Układ okna logowania (kolumny)
        okno = QVBoxLayout(self)
        okno.setAlignment(Qt.AlignCenter)
        okno.addWidget(self.logo_label)
        okno.addWidget(self.wiadomosc)
        okno.addWidget(self.przyciski)

        # Sygnały z przycisków
        self.przyciski.accepted.connect(self.accept)

        # Właściwości okna
        self.setModal(True)
        self.set_position()

    def set_position(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @staticmethod
    def show_welcome(login, parent=None):
        okno = WelcomeWindow(login, parent)
        ok = okno.exec_()


class RegisterWindowDialog(QDialog):

    # Okno rejestracji
    def __init__(self, parent=None):
        super(RegisterWindowDialog, self).__init__(parent)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(420, 250)
        self.set_position()

        self.frame = QFrame(self)
        self.frame.resize(420, 250)
        self.frame.setStyleSheet("QFrame { background-color: rgb(36, 36, 36); "
                                 "border-style: outset; "
                                 "border-color: rgb(50, 90, 0); "
                                 "border-width: 6px; "
                                 "border-radius: 10px }")

        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/Register.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(45, 40)
        self.image_logo.move(55, 15)

        # Etykiety
        self.logo_label = QLabel('  REJESTRACJA')
        self.logo_label.setStyleSheet("QLabel { color: white }")
        self.logo_label.setFont(QFont("Consolas", 25, QFont.Bold))

        self.login_label = QLabel('Nowy login: ')
        self.login_label.setStyleSheet("QLabel { color: white }")
        self.login_label.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo_label1 = QLabel('Nowe hasło: ')
        self.haslo_label1.setStyleSheet("QLabel { color: white }")
        self.haslo_label1.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo_label2 = QLabel('Powtórz\nnowe hasło: ')
        self.haslo_label2.setAlignment(Qt.AlignCenter)
        self.haslo_label2.setStyleSheet("QLabel { color: white }")
        self.haslo_label2.setFont(QFont("Consolas", 15, QFont.Bold))

        # Pole edycyjne
        self.login = QLineEdit()
        self.login.setStyleSheet("QLineEdit { color: white; "
                                 "background-color: rgb(36, 36, 36); "
                                 "border-style: outset; "
                                 "border-color: rgb(255, 255, 255); "
                                 "border-width: 2px; "
                                 "border-radius: 5px }")
        self.login.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo1 = QLineEdit()
        self.haslo1.setStyleSheet("QLineEdit { color: white; "
                                  "background-color: rgb(36, 36, 36); "
                                  "border-style: outset; "
                                  "border-color: rgb(255, 255, 255); "
                                  "border-width: 2px; "
                                  "border-radius: 5px }")
        self.haslo1.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo2 = QLineEdit()
        self.haslo2.setStyleSheet("QLineEdit { color: white; "
                                  "background-color: rgb(36, 36, 36); "
                                  "border-style: outset; "
                                  "border-color: rgb(255, 255, 255); "
                                  "border-width: 2px; "
                                  "border-radius: 5px }")
        self.haslo2.setFont(QFont("Consolas", 15, QFont.Bold))

        # Przyciski
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        self.przyciski.button(QDialogButtonBox.Ok).setText("Zarejestruj")
        self.przyciski.button(QDialogButtonBox.Ok).setStyleSheet("QPushButton { background-color: black; "
                                                                 "border-style: outset; "
                                                                 "border-width: 5px; "
                                                                 "border-radius: 10px; "
                                                                 "border-color: rgb(50, 90, 0); "
                                                                 "min-width: 1em; "
                                                                 "min-height: 1.6em; "
                                                                 "font-color=white; "
                                                                 "padding: 6px; "
                                                                 "color: white }"
                                                                 "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                                                 "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.przyciski.button(QDialogButtonBox.Ok).setFont(QFont("Consolas", 15, QFont.Bold))

        self.przyciski.button(QDialogButtonBox.Cancel).setText("Anuluj")
        self.przyciski.button(QDialogButtonBox.Cancel).setStyleSheet("QPushButton { background-color: black; "
                                                                     "border-style: outset; "
                                                                     "border-width: 5px; "
                                                                     "border-radius: 10px; "
                                                                     "border-color: rgb(50, 90, 0); "
                                                                     "min-width: 1em; "
                                                                     "min-height: 1.6em; "
                                                                     "font-color=white; "
                                                                     "padding: 6px; "
                                                                     "color: white }"
                                                                     "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                                                     "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.przyciski.button(QDialogButtonBox.Cancel).setFont(QFont("Consolas", 15, QFont.Bold))

        # Układ okna logowania (kolumny)
        okno = QGridLayout(self)
        okno.addWidget(self.logo_label, 0, 1, )
        okno.addWidget(self.login_label, 1, 0)
        okno.addWidget(self.login, 1, 1)
        okno.addWidget(self.haslo_label1, 2, 0)
        okno.addWidget(self.haslo1, 2, 1)
        okno.addWidget(self.haslo_label2, 3, 0)
        okno.addWidget(self.haslo2, 3, 1)
        okno.addWidget(self.przyciski, 4, 0, 4, 0)

        # Sygnały z przycisków
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # Właściwości okna
        self.setModal(True)

    def set_position(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        qr.setY(qr.y() + 50)
        self.move(qr.topLeft())

    def return_login_haslo(self):
        return (self.login.text().strip(), self.haslo1.text().strip(), self.haslo2.text().strip())

    # metoda statyczna, pobiera login i hasło od użytkownika i zwraca te wartości
    @staticmethod
    def set_login_haslo(self, parent=None):
        okno = RegisterWindowDialog(parent)
        okno.login.setFocus()
        ok = okno.exec_()
        login, haslo1, haslo2 = okno.return_login_haslo()
        return (login, haslo1, haslo2, ok == QDialog.Accepted)


class LoginWindowDialog(QDialog):

    # Okno logowania
    def __init__(self, parent=None):
        super(LoginWindowDialog, self).__init__(parent)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(350, 200)
        self.set_position()

        self.frame = QFrame(self)
        self.frame.resize(350, 200)
        self.frame.setStyleSheet("QFrame { background-color: rgb(36, 36, 36); "
                                 "border-style: outset; "
                                 "border-color: rgb(50, 90, 0); "
                                 "border-width: 6px; "
                                 "border-radius: 10px }")

        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/Login.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(45, 40)
        self.image_logo.move(20, 15)

        # Etykiety
        self.logo_label = QLabel('  LOGOWANIE')
        self.logo_label.setStyleSheet("QLabel { color: white }")
        self.logo_label.setFont(QFont("Consolas", 25, QFont.Bold))

        self.login_label = QLabel('Login: ')
        self.login_label.setStyleSheet("QLabel { color: white }")
        self.login_label.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo_label = QLabel('Hasło: ')
        self.haslo_label.setStyleSheet("QLabel { color: white }")
        self.haslo_label.setFont(QFont("Consolas", 15, QFont.Bold))

        # Pole edycyjne
        self.login = QLineEdit()
        self.login.setStyleSheet("QLineEdit { color: white; "
                                 "background-color: rgb(36, 36, 36); "
                                 "border-style: outset; "
                                 "border-color: rgb(255, 255, 255); "
                                 "border-width: 2px; "
                                 "border-radius: 5px }")
        self.login.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo = QLineEdit()
        self.haslo.setStyleSheet("QLineEdit { color: white; "
                                 "background-color: rgb(36, 36, 36); "
                                 "border-style: outset; "
                                 "border-color: rgb(255, 255, 255); "
                                 "border-width: 2px; "
                                 "border-radius: 5px }")
        self.haslo.setFont(QFont("Consolas", 15, QFont.Bold))

        # Przyciski
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        self.przyciski.button(QDialogButtonBox.Ok).setText("Zaloguj")
        self.przyciski.button(QDialogButtonBox.Ok).setStyleSheet("QPushButton { background-color: black; "
                                                                 "border-style: outset; "
                                                                 "border-width: 5px; "
                                                                 "border-radius: 10px; "
                                                                 "border-color: rgb(50, 90, 0); "
                                                                 "min-width: 1em; "
                                                                 "min-height: 1.6em; "
                                                                 "font-color=white; "
                                                                 "padding: 6px; "
                                                                 "color: white }"
                                                                 "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                                                 "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.przyciski.button(QDialogButtonBox.Ok).setFont(QFont("Consolas", 15, QFont.Bold))

        self.przyciski.button(QDialogButtonBox.Cancel).setText("Anuluj")
        self.przyciski.button(QDialogButtonBox.Cancel).setStyleSheet("QPushButton { background-color: black; "
                                                                     "border-style: outset; "
                                                                     "border-width: 5px; "
                                                                     "border-radius: 10px; "
                                                                     "border-color: rgb(50, 90, 0); "
                                                                     "min-width: 1em; "
                                                                     "min-height: 1.6em; "
                                                                     "font-color=white; "
                                                                     "padding: 6px; "
                                                                     "color: white }"
                                                                     "QPushButton:hover { background-color: rgb(80, 80, 80) }"
                                                                     "QPushButton:pressed { background-color: rgb(89, 166, 0) }")
        self.przyciski.button(QDialogButtonBox.Cancel).setFont(QFont("Consolas", 15, QFont.Bold))

        # Układ okna logowania (kolumny)
        okno = QGridLayout(self)
        okno.addWidget(self.logo_label, 0, 1, )
        okno.addWidget(self.login_label, 1, 0)
        okno.addWidget(self.login, 1, 1)
        okno.addWidget(self.haslo_label, 2, 0)
        okno.addWidget(self.haslo, 2, 1)
        okno.addWidget(self.przyciski, 3, 0, 3, 0)

        # Właściwości okna
        self.setModal(True)

    def set_position(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        qr.setY(qr.y() + 25)
        self.move(qr.topLeft())

    def return_login_haslo(self):
        return (self.login.text().strip(), self.haslo.text().strip())

    # metoda statyczna, pobiera login i hasło od użytkownika i zwraca te wartości
    @staticmethod
    def get_login_haslo(parent=None):
        okno = LoginWindowDialog(parent)
        okno.login.setFocus()
        ok = okno.exec_()
        login, haslo = okno.return_login_haslo()
        return (login, haslo, ok == QDialog.Accepted)


class AddTaskWindowDialog(QDialog):

    # Okno logowania
    def __init__(self, parent=None):
        super(AddTaskWindowDialog, self).__init__(parent)

        self.offset = None

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(500, 500)

        self.frame = QFrame(self)
        self.frame.resize(500, 500)
        self.frame.setStyleSheet("QFrame { background-color: rgba(1, 61, 115, 230); "
                                 "border-style: outset; "
                                 "border-color: rgb(70, 192, 242); "
                                 "border-width: 6px; "
                                 "border-radius: 10px }")

        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/Management_icon/Add_Notes_icon.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(50, 55)
        self.image_logo.move(20, 15)

        # Etykiety
        self.logo_label = QLabel('  DODAJ NOWE ZADANIE')
        self.logo_label.setStyleSheet("QLabel { color: white }")
        self.logo_label.setFont(QFont("Consolas", 25, QFont.Bold))
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.zadanie_label = QLabel('Treść: ')
        self.zadanie_label.setStyleSheet("QLabel { color: white }")
        self.zadanie_label.setFont(QFont("Consolas", 15, QFont.Bold))
        self.zadanie_label.setAlignment(Qt.AlignCenter)

        self.data_label = QLabel('Na kiedy: ')
        self.data_label.setStyleSheet("QLabel { color: white }")
        self.data_label.setFont(QFont("Consolas", 15, QFont.Bold))
        self.data_label.setAlignment(Qt.AlignCenter)

        self.priorytet_label = QLabel('Jaki priorytet zadania: ')
        self.priorytet_label.setStyleSheet("QLabel { color: white }")
        self.priorytet_label.setFont(QFont("Consolas", 15, QFont.Bold))
        self.priorytet_label.setAlignment(Qt.AlignCenter)

        # Pole edycyjne
        self.wyroznienie_checkbox = QCheckBox("Wyróżniona")
        self.wyroznienie_checkbox.setChecked(False)
        self.wyroznienie_checkbox.setGeometry(200, 150, 100, 30)
        self.wyroznienie_checkbox.setStyleSheet("QCheckBox { color: rgb(255, 255, 255) }"
                                                "QCheckBox::indicator { width :20; "
                                                "height :20; "
                                                "border-style: outset; "
                                                "border-width: 3px; "
                                                "border-radius: 5px; "
                                                "border-color: rgb(23, 100, 169) }"
                                                "QCheckBox::indicator:checked { image: url("
                                                "Image/Ico/Management_icon/CheckBox/checkbox_check.png) } "
                                                "QCheckBox::indicator:unchecked { image: url("
                                                "Image/Ico/Management_icon/CheckBox/checkbox_uncheck.png) }")
        self.wyroznienie_checkbox.setFont(QFont("Consolas", 12, QFont.Bold))
        self.wyroznienie_checkbox.setLayoutDirection(Qt.RightToLeft)

        self.zadanie = QTextEdit()
        self.zadanie.setStyleSheet("QTextEdit { color: white; "
                                   "background-color: rgb(36, 36, 36); "
                                   "border-style: outset; "
                                   "border-color: rgb(255, 255, 255); "
                                   "border-width: 2px; "
                                   "border-radius: 5px }")
        self.zadanie.setFont(QFont("Consolas", 12, QFont.Bold))
        self.zadanie.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.data = QDateTimeEdit()
        self.data.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.data.setStyleSheet("QDateTimeEdit { color: white; "
                                "background-color: rgb(36, 36, 36); "
                                "border-style: outset; "
                                "border-color: rgb(255, 255, 255); "
                                "border-width: 2px; "
                                "border-radius: 5px }")
        self.data.setFont(QFont("Consolas", 12, QFont.Bold))
        current_time = QDateTime.currentDateTime()
        self.data.setDateTime(current_time.addDays(-1))

        self.priorytet = QComboBox()
        self.priorytet.setEditable(False)
        priorytet_list = ["Na wczoraj", "Super mało czasu", "Super ważne", "Ważne", "Normalne", "Mało ważne",
                          "Wcale nieważne"]
        self.priorytet.addItems(priorytet_list)

        self.priorytet.setStyleSheet("QComboBox { color: white; "
                                     "background-color: rgb(36, 36, 36); "
                                     "border-style: outset; "
                                     "border-color: rgb(255, 255, 255); "
                                     "border-width: 2px; "
                                     "border-radius: 5px }"
                                     "QListView { background-color: rgb(70, 192, 242) }"
                                     "QComboBox::item:hover { background-color: rgb(70, 192, 242) }")
        self.priorytet.setFont(QFont("Consolas", 12, QFont.Bold))

        self.czytaj = QPushButton("Naciśnij aby przeczytać notatkę")
        self.czytaj.setStyleSheet(
            "QPushButton { background-color: rgb(32, 129, 255); border-radius: 10px; color: white}"
            "QPushButton:hover { background-color: rgb(72, 151, 255) }"
            "QPushButton:pressed { background-color: rgb(0, 32, 74) }")
        self.czytaj.setIcon(QIcon("Image/Ico/Management_icon/Speaker_icon.png"))
        self.czytaj.setIconSize(QSize(25, 25))
        self.czytaj.setFont(QFont("Consolas", 15, QFont.Bold))
        self.czytaj.clicked.connect(self.czytaj_tekst)

        # Przyciski
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        self.przyciski.button(QDialogButtonBox.Ok).setText("Dodaj")
        self.przyciski.button(QDialogButtonBox.Ok).setStyleSheet("QPushButton { background-color: black; "
                                                                 "border-style: outset; "
                                                                 "border-width: 5px; "
                                                                 "border-radius: 10px; "
                                                                 "border-color: rgb(70, 192, 242); "
                                                                 "min-width: 1em; "
                                                                 "min-height: 1.6em; "
                                                                 "font-color=white; "
                                                                 "padding: 6px; "
                                                                 "color: white }"
                                                                 "QPushButton:hover { "
                                                                 "background-color: rgb(23, 100, 169) }"
                                                                 "QPushButton:pressed { "
                                                                 "background-color: rgb(23, 100, 169) }")
        self.przyciski.button(QDialogButtonBox.Ok).setFont(QFont("Consolas", 15, QFont.Bold))

        self.przyciski.button(QDialogButtonBox.Cancel).setText("Anuluj")
        self.przyciski.button(QDialogButtonBox.Cancel).setStyleSheet("QPushButton { background-color: black; "
                                                                     "border-style: outset; "
                                                                     "border-width: 5px; "
                                                                     "border-radius: 10px; "
                                                                     "border-color: rgb(70, 192, 242); "
                                                                     "min-width: 1em; "
                                                                     "min-height: 1.6em; "
                                                                     "font-color=white; "
                                                                     "padding: 6px; "
                                                                     "color: white }"
                                                                     "QPushButton:hover { "
                                                                     "background-color: rgb(23, 100, 169) }"
                                                                     "QPushButton:pressed { "
                                                                     "background-color: rgb(23, 100, 169) }")
        self.przyciski.button(QDialogButtonBox.Cancel).setFont(QFont("Consolas", 15, QFont.Bold))

        # Układ okna logowania (kolumny)
        okno = QVBoxLayout(self)
        okno.setAlignment(Qt.AlignCenter)
        okno.addWidget(self.logo_label)
        okno.addWidget(self.wyroznienie_checkbox)
        okno.addWidget(self.zadanie_label)
        okno.addWidget(self.zadanie)
        okno.addWidget(self.data_label)
        okno.addWidget(self.data)
        okno.addWidget(self.priorytet_label)
        okno.addWidget(self.priorytet)
        okno.addWidget(self.czytaj)
        okno.addWidget(self.przyciski)

        # Właściwości okna
        self.setModal(True)
        self.center()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def czytaj_tekst(self):
        tekst = self.zadanie.toPlainText()
        import pyttsx3
        tts_engine = pyttsx3.init()
        speaker_thread = Threader(args=[tekst, tts_engine])
        speaker_thread.start()

    def return_add_task_data(self):
        if self.wyroznienie_checkbox.isChecked():
            wyroznienie = "TAK"
        else:
            wyroznienie = "NIE"
        return self.zadanie.toPlainText().strip(), self.data.dateTime().toPyDateTime(), self.priorytet.currentText().strip(), wyroznienie

    # metoda statyczna, pobiera login i hasło od użytkownika i zwraca te wartości
    @staticmethod
    def get_add_task_data(parent=None):
        okno = AddTaskWindowDialog(parent)
        okno.zadanie.setFocus()
        ok = okno.exec_()
        zadanie, data, priorytet, wyroznione = okno.return_add_task_data()
        return zadanie, data, priorytet, wyroznione, ok == QDialog.Accepted


class ExitWindowDialog(QDialog):

    # Okno Wyjścia
    def __init__(self, parent=None):
        super(ExitWindowDialog, self).__init__(parent)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(420, 200)

        self.frame = QFrame(self)
        self.frame.resize(420, 200)
        self.frame.setStyleSheet("QFrame { background-color: rgba(0, 0, 0, 200); "
                                 "border-style: outset; "
                                 "border-color: rgb(243, 175, 12); "
                                 "border-width: 6px; "
                                 "border-radius: 10px }")

        # Tytuł aplikacji
        self.text_logo = QLabel("       TODO List", self)
        self.text_logo.setStyleSheet("QLabel { color: rgb(243, 175, 12) }")
        self.text_logo.setFont(QFont("Forte", 35, QFont.Bold))
        self.text_logo.move(55, 20)

        # Logo aplikacji
        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/App_icon.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(55, 50)
        self.image_logo.move(20, 15)

        # Etykiety
        self.window_label = QLabel('Czy zapisać wprowadzone zmiany\nprzed zamknięciem aplikacji?')
        self.window_label.setStyleSheet("QLabel { color: white }")
        self.window_label.setFont(QFont("Consolas", 15, QFont.Bold))

        # Przyciski
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        self.przyciski.button(QDialogButtonBox.Ok).setText("Tak")
        self.przyciski.button(QDialogButtonBox.Ok).setStyleSheet("QPushButton { background-color: black; "
                                                                 "border-style: outset; "
                                                                 "border-width: 5px; "
                                                                 "border-radius: 10px; "
                                                                 "border-color: rgb(243, 175, 12); "
                                                                 "min-width: 1em; "
                                                                 "min-height: 1.6em; "
                                                                 "font-color=white; "
                                                                 "padding: 6px; "
                                                                 "color: white }"
                                                                 "QPushButton:hover { background-color: rgb(80, 80, "
                                                                 "80) }"
                                                                 "QPushButton:pressed { "
                                                                 "background-color: rgb(243, 175, 0) }")
        self.przyciski.button(QDialogButtonBox.Ok).setFont(QFont("Consolas", 15, QFont.Bold))

        self.przyciski.button(QDialogButtonBox.Cancel).setText("Nie")
        self.przyciski.button(QDialogButtonBox.Cancel).setStyleSheet("QPushButton { background-color: black; "
                                                                     "border-style: outset; "
                                                                     "border-width: 5px; "
                                                                     "border-radius: 10px; "
                                                                     "border-color: rgb(243, 175, 12); "
                                                                     "min-width: 1em; "
                                                                     "min-height: 1.6em; "
                                                                     "font-color=white; "
                                                                     "padding: 6px; "
                                                                     "color: white }"
                                                                     "QPushButton:hover { background-color: rgb(80, "
                                                                     "80, 80) } "
                                                                     "QPushButton:pressed { "
                                                                     "background-color: rgb(243, 175, 0) }")
        self.przyciski.button(QDialogButtonBox.Cancel).setFont(QFont("Consolas", 15, QFont.Bold))

        # Układ okna logowania (kolumny)
        okno = QVBoxLayout(self)
        okno.setAlignment(Qt.AlignCenter)
        # okno.addItem(QSpacerItem(QSizePolicy.Expanding, 50))
        okno.addWidget(self.text_logo)
        okno.addWidget(self.window_label)
        okno.addWidget(self.przyciski)

        # Właściwości okna
        self.setModal(True)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # metoda statyczna, pobiera login i hasło od użytkownika i zwraca te wartości
    @staticmethod
    def get_user_consent(parent=None):
        okno = ExitWindowDialog(parent)
        ok = okno.exec_()
        return ok == QDialog.Accepted


class EditUserWindowDialog(QDialog):

    def __init__(self, login, parent=None):
        super(EditUserWindowDialog, self).__init__(parent)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.resize(550, 280)
        self.center()

        self.frame = QFrame(self)
        self.frame.resize(550, 280)
        self.frame.setStyleSheet("QFrame { background-color: rgba(60, 122, 203, 230); "
                                 "border-style: outset; "
                                 "border-color: rgb(0, 51, 117); "
                                 "border-width: 6px; "
                                 "border-radius: 10px }")

        self.image_logo = QLabel(self)
        self.image_logo.setPixmap(QPixmap("Image/Ico/Management_icon/Edit_user_icon.png"))
        self.image_logo.setScaledContents(True)
        self.image_logo.resize(50, 55)
        self.image_logo.move(55, 15)

        # Etykiety
        self.logo_label = QLabel('Edycja danych użytkownika:\n' + login)
        self.logo_label.setStyleSheet("QLabel { color: white }")
        self.logo_label.setFont(QFont("Consolas", 20, QFont.Bold))
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.login_label = QLabel('Nowy login: ')
        self.login_label.setStyleSheet("QLabel { color: white }")
        self.login_label.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo_label1 = QLabel('Nowe hasło: ')
        self.haslo_label1.setStyleSheet("QLabel { color: white }")
        self.haslo_label1.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo_label2 = QLabel('Podaj stare\nhasło: ')
        self.haslo_label2.setAlignment(Qt.AlignCenter)
        self.haslo_label2.setStyleSheet("QLabel { color: white }")
        self.haslo_label2.setFont(QFont("Consolas", 15, QFont.Bold))

        # Pole edycyjne
        if login == "Admin":
            self.login = QLabel("Admin nie może zmieniać loginu")
            self.login.setStyleSheet("QLabel { color: white; "
                                     "background-color: rgb(36, 36, 36); "
                                     "border-style: outset; "
                                     "border-color: rgb(255, 255, 255); "
                                     "border-width: 2px; "
                                     "border-radius: 5px }")
            self.login.setFont(QFont("Consolas", 15, QFont.Bold))
        else:
            self.login = QLineEdit()
            self.login.setStyleSheet("QLineEdit { color: white; "
                                     "background-color: rgb(36, 36, 36); "
                                     "border-style: outset; "
                                     "border-color: rgb(255, 255, 255); "
                                     "border-width: 2px; "
                                     "border-radius: 5px }")
            self.login.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo1 = QLineEdit()
        self.haslo1.setStyleSheet("QLineEdit { color: white; "
                                  "background-color: rgb(36, 36, 36); "
                                  "border-style: outset; "
                                  "border-color: rgb(255, 255, 255); "
                                  "border-width: 2px; "
                                  "border-radius: 5px }")
        self.haslo1.setFont(QFont("Consolas", 15, QFont.Bold))

        self.haslo2 = QLineEdit()
        self.haslo2.setStyleSheet("QLineEdit { color: white; "
                                  "background-color: rgb(36, 36, 36); "
                                  "border-style: outset; "
                                  "border-color: rgb(255, 255, 255); "
                                  "border-width: 2px; "
                                  "border-radius: 5px }")
        self.haslo2.setFont(QFont("Consolas", 15, QFont.Bold))

        # Przyciski
        self.przyciski = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        self.przyciski.button(QDialogButtonBox.Ok).setText("Zapisz zmiany")
        self.przyciski.button(QDialogButtonBox.Ok).setStyleSheet("QPushButton { background-color: black; "
                                                                 "border-style: outset; "
                                                                 "border-width: 5px; "
                                                                 "border-radius: 10px; "
                                                                 "border-color: rgb(0, 51, 117); "
                                                                 "min-width: 1em; "
                                                                 "min-height: 1.6em; "
                                                                 "font-color=white; "
                                                                 "padding: 6px; "
                                                                 "color: white }"
                                                                 "QPushButton:hover { background-color: rgb(92, 163, 255) }"
                                                                 "QPushButton:pressed { background-color: rgb(0, 111, 255) }")
        self.przyciski.button(QDialogButtonBox.Ok).setFont(QFont("Consolas", 15, QFont.Bold))

        self.przyciski.button(QDialogButtonBox.Cancel).setText("Anuluj")
        self.przyciski.button(QDialogButtonBox.Cancel).setStyleSheet("QPushButton { background-color: black; "
                                                                     "border-style: outset; "
                                                                     "border-width: 5px; "
                                                                     "border-radius: 10px; "
                                                                     "border-color: rgb(0, 51, 117); "
                                                                     "min-width: 1em; "
                                                                     "min-height: 1.6em; "
                                                                     "font-color=white; "
                                                                     "padding: 6px; "
                                                                     "color: white }"
                                                                     "QPushButton:hover { background-color: rgb(92, 163, 255) }"
                                                                     "QPushButton:pressed { background-color: rgb(0, 111, 255) }")
        self.przyciski.button(QDialogButtonBox.Cancel).setFont(QFont("Consolas", 15, QFont.Bold))

        # Układ okna logowania (kolumny)
        okno = QGridLayout(self)
        okno.addWidget(self.logo_label, 0, 1, )
        okno.addWidget(self.login_label, 1, 0)
        okno.addWidget(self.login, 1, 1)
        okno.addWidget(self.haslo_label1, 2, 0)
        okno.addWidget(self.haslo1, 2, 1)
        okno.addWidget(self.haslo_label2, 3, 0)
        okno.addWidget(self.haslo2, 3, 1)
        okno.addWidget(self.przyciski, 4, 0, 4, 0)

        # Sygnały z przycisków
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # Właściwości okna
        self.setModal(True)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def return_login_haslo(self):
        return (self.login.text().strip(), self.haslo1.text().strip(), self.haslo2.text().strip())

    @staticmethod
    def set_login_haslo(login, parent=None):
        okno = EditUserWindowDialog(login, parent)
        okno.login.setFocus()
        ok = okno.exec_()
        login, haslo1, haslo2 = okno.return_login_haslo()

        return login, haslo1, haslo2, ok
