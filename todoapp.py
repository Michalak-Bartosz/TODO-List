import sys
from datetime import datetime

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu

import db
from gui import GuiWidgetWindowApp, GuiWindowStart, LoginWindowDialog, RegisterWindowDialog, AddTaskWindowDialog, \
    ExitWindowDialog, EditUserWindowDialog, WelcomeWindow, GuiWidgetWindowNote
from speak import Threader
from tabtaskmodel import TabTaskModel
from tabusermodel import TabUserModel


class StartWindow(QWidget, GuiWindowStart):

    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.set_up_gui(self)
        self.zarejestruj.clicked.connect(self.zarejestruj_fun)
        self.zaloguj.clicked.connect(self.zaloguj_fun)
        self.wyjdz.clicked.connect(self.wyjdz_fun)

    def zarejestruj_fun(self):
        login, haslo1, haslo2, ok = RegisterWindowDialog.set_login_haslo(self)
        if not ok:
            return
        if not login or not haslo1 or not haslo2:
            self.gui_messagebox(self, "Wypełnij wymagane pola!", "Warning")
            return
        if haslo1 != haslo2:
            self.gui_messagebox(self, "Hasło musi być identyczne\ndo powtórzonego!", "Warning")
            return

        self.osoba = db.zarejestruj(login, haslo1)

        if self.osoba is False:
            self.gui_messagebox(self, 'Użytkownik o takiej nazwie\njuż istnieje!', "Critical")
            return
        else:
            self.gui_messagebox(self, 'Utwożono nowe konto:\nLogin: ' + login + '\nHasło: ' + haslo1, "Information")

    def zaloguj_fun(self):
        login, haslo, ok = LoginWindowDialog.get_login_haslo(self)

        if not ok:
            return
        if not login or not haslo:
            self.gui_messagebox(self, "Pusty login lub hasło!", "Warning")
            return

        self.osoba = db.zaloguj(login, haslo)

        if self.osoba is False:
            self.gui_messagebox(self, 'Błedny login lub hasło!', "Warning")
            return

        self.close()
        self.okno_aplikacji = AppWindow(login, haslo)
        self.okno_aplikacji.showNormal()

    def wyjdz_fun(self):
        self.close()


class AppWindow(QWidget, GuiWidgetWindowApp):

    def __init__(self, login, haslo):
        QWidget.__init__(self)
        GuiWidgetWindowApp.__init__(self)

        self.offset = None
        self.notes_window_list = []

        # Ustawienie gui i pobranie osoby, ktora jest zalogowana
        self.login = login
        self.haslo = haslo
        self.osoba = db.get_osoba(self.login, self.haslo)
        self.set_up_gui(self, self.login)

        # Przypisanie funkcji do przyciskow funkcyjnych
        self.minimalize.clicked.connect(self.showMinimized)
        self.normal_full_sceen.clicked.connect(self.show_normal_max_event)
        self.close_app.clicked.connect(self.exit_event)

        # Przypisanie funkcji do przyciskow
        self.wyloguj.clicked.connect(self.wyloguj_fun)
        self.dodaj.clicked.connect(self.dodaj_fun)
        self.usun.clicked.connect(self.usun_notatki_fun)
        self.zapisz.clicked.connect(self.zapisz_fun)
        self.zakoncz.clicked.connect(self.exit_event)
        if self.login == "Admin":
            self.uzytkownicy.clicked.connect(self.admin_fun)
            self.inicjalizuj_widok_uzytkownikow_fun()

        self.view_user.hide()
        # Wyświetlenie zapisanych notatek użytkownika
        self.inicjalizuj_widok_notatek_fun()

        # Tworzenie ikony aplikacji na pasku zadan
        self.tray_icon_fun()

        # Komunikat powitalny użytkownika
        self.powitanie()

    def powitanie(self):
        WelcomeWindow.show_welcome(self.login)

    def inicjalizuj_widok_notatek_fun(self):
        self.model_task = TabTaskModel(db.pola_task)
        self.tasks = db.czytaj_dane(self, self.osoba)
        self.model_task.aktualizuj(self.tasks)
        self.model_task.layoutChanged.emit()
        self.view_task.setModel(self.model_task)
        self.koloruj_model_task_fun()
        self.odswiez_widok_notatek()
        self.view_task.hideColumn(0)

    def inicjalizuj_widok_uzytkownikow_fun(self):
        self.model_user = TabUserModel(db.pola_user)
        self.users = db.czytaj_uzytkownikow()
        self.model_user.aktualizuj(self.users)
        self.model_user.layoutChanged.emit()
        self.view_user.setModel(self.model_user)
        self.view_user.hideColumn(0)

    def odswiez_widok_notatek(self):
        self.view_task.show()
        self.wyroznione_checkbox_read_fun()
        self.zrobione_checkbox_read_fun()
        self.usun_notatke_button_read_fun()
        self.czytaj_button_read_fun()
        self.update_note_windows_button_read_fun()
        self.koloruj_model_task_fun()

    def odswiez_widok_uzytkownikow(self):
        self.view_user.show()
        self.usun_uzytkownika_button_read_fun()
        self.edytuj_uzytkownika_button_read_fun()

    def dodaj_fun(self):
        """ Dodawanie nowego zadania """
        zadanie, data, priorytet, wyroznione, ok = AddTaskWindowDialog.get_add_task_data(self)
        if not ok:
            return
        if not zadanie.strip():
            self.gui_messagebox(self, "Zadanie nie może być puste.", "Critical")
            return

        task = db.dodaj_zadanie(self.osoba, zadanie, data, priorytet, wyroznione)
        self.model_task.tabela_task.append(task)
        self.model_task.layoutChanged.emit()
        if len(self.model_task.tabela_task) == 1:
            self.view_task.hideColumn(0)
            self.odswiez_widok_notatek()

        row = self.model_task.rowCount() - 1
        id = self.model_task.tabela_task[row][0]
        button1 = self.gui_usun_notatke_button()
        self.view_task.setIndexWidget(self.model_task.index(row, 8), button1);
        button2 = self.gui_czytaj_button()
        self.view_task.setIndexWidget(self.model_task.index(row, 9), button2);
        button3 = self.gui_odswiez_notatke_button()
        self.view_task.setIndexWidget(self.model_task.index(row, 7), button3);
        checkbox1 = self.gui_zrobione_checkbox("NIE")
        self.view_task.setIndexWidget(self.model_task.index(row, 6), checkbox1);
        self.notes_window_list.append(id)
        self.notes_window_list.append(self.make_note_window_fun(self.login, row + 1, wyroznione, zadanie, data, priorytet))
        if wyroznione == "TAK":
            checkbox2 = self.gui_wyroznione_checkbox("TAK")
            self.show_note_windows_fun(id)
        else:
            checkbox2 = self.gui_wyroznione_checkbox("NIE")
        self.view_task.setIndexWidget(self.model_task.index(row, 1), checkbox2)
        self.koloruj_wiersze_model_task_fun(row, 10, 10, 10)

    def koloruj_model_task_fun(self):
        for row in range(self.model_task.rowCount()):
            status = self.model_task.tabela_task[row][6]
            if status == "NIE":
                self.koloruj_wiersze_model_task_fun(row, 10, 10, 10)
            else:
                self.koloruj_wiersze_model_task_fun(row, 0, 127, 9)

    def koloruj_wiersze_model_task_fun(self, row, r, g, b):
        wyroznione = self.model_task.tabela_task[row][1]
        for column in range(self.model_task.columnCount()):
            if column == 1 and wyroznione == "TAK":
                self.model_task.change_color(row, column, QColor(160, 123, 0))
            else:
                if column % 2 == 0:
                    self.model_task.change_color(row, column, QColor(r, g, b))
                else:
                    self.model_task.change_color(row, column, QColor(r + 16, g + 16, b + 16))

    def koloruj_komorke_model_task_fun(self, row, column, r, g, b):
        if column % 2 == 0:
            self.model_task.change_color(row, column, QColor(r, g, b))
        else:
            self.model_task.change_color(row, column, QColor(r + 16, g + 16, b + 16))

    def admin_fun(self):
        if self.uzytkownicy.text() == "Zarządzaj użytkownikami":
            self.view_task.hide()
            self.odswiez_widok_uzytkownikow()
            self.uzytkownicy.setText("Zarządzaj notatkami")
        else:
            self.view_user.hide()
            self.odswiez_widok_notatek()
            self.uzytkownicy.setText("Zarządzaj użytkownikami")

    def zapisz_fun(self):
        db.zapisz_dane(self.model_task.tabela_task)
        self.model_task.layoutChanged.emit()

    def usun_notatke_button_read_fun(self):
        for index in range(self.model_task.rowCount()):
            button = self.gui_usun_notatke_button()
            self.view_task.setIndexWidget(self.model_task.index(index, 8), button)

    def usun_notatke_fun(self):
        button = self.sender()
        index = self.view_task.indexAt(button.pos())
        if index.isValid():
            db.usun_notatke(self, index)
            self.model_task.layoutChanged.emit()
            self.odswiez_widok_notatek()

    def usun_notatki_fun(self):
        db.usun_notatki(self)
        self.model_task.layoutChanged.emit()
        self.odswiez_widok_notatek()

    def usun_uzytkownika_button_read_fun(self):
        for index in range(self.model_user.rowCount()):
            button = self.gui_usun_uzytkownika_button()
            label = self.gui_administrator_label()
            if self.model_user.tabela_user[index][1] != "Admin":
                self.view_user.setIndexWidget(self.model_user.index(index, 4), button)
            else:
                self.view_user.setIndexWidget(self.model_user.index(index, 4), label)

    def usun_uzytkownika_fun(self):
        button = self.sender()
        index = self.view_user.indexAt(button.pos())
        if index.isValid():
            db.usun_uzytkownika(self, index)
            self.model_user.layoutChanged.emit()
            self.odswiez_widok_uzytkownikow()

    def edytuj_uzytkownika_button_read_fun(self):
        for index in range(self.model_user.rowCount()):
            button = self.gui_edytuj_uzytkownika_button()
            self.view_user.setIndexWidget(self.model_user.index(index, 3), button)

    def edytuj_uzytkownika_fun(self):
        button = self.sender()
        index = self.view_user.indexAt(button.pos())
        if index.isValid():
            self.view_user.selectRow(index.row())
            login = self.model_user.tabela_user[index.row()][1]
            haslo = self.model_user.tabela_user[index.row()][2]
            login, haslo1, haslo2, ok = EditUserWindowDialog.set_login_haslo(login)

            if ok:
                if not login.strip() or not haslo1.strip() or not haslo2.strip():
                    self.gui_messagebox(self, "Należy uzupełnić wszystkie\nwymagane dane!", "Warning")
                    return
                if haslo2 != haslo:
                    self.gui_messagebox(self, "Niepoprawne stare hasło użytkownika!", "Critical")
                    return
                else:
                    db.edytuj_uzytkownika(self, index, login, haslo1)
                    self.users = db.czytaj_uzytkownikow()
                    self.model_user.aktualizuj(self.users)
                    self.model_user.layoutChanged.emit()
            else:
                return

    def edytuj_uzytkownika_settings_fun(self):
        login, haslo1, haslo2, ok = EditUserWindowDialog.set_login_haslo(self.login)

        if ok:
            if not login.strip() or not haslo1.strip() or not haslo2.strip():
                self.gui_messagebox(self, "Należy uzupełnić wszystkie\nwymagane dane!", "Warning")
                return
            if haslo2 != self.haslo:
                self.gui_messagebox(self, "Niepoprawne stare hasło użytkownika!", "Critical")
                return
            else:
                db.edytuj_uzytkownika_settings(self, login, haslo1)
                self.gui_messagebox(self, "Zmieniono dane logowania użytkownika!", "Information")
        else:
            return

    def czytaj_button_read_fun(self):
        for index in range(self.model_task.rowCount()):
            button = self.gui_czytaj_button()
            self.view_task.setIndexWidget(self.model_task.index(index, 9), button)

    def czytaj_tekst_fun(self):
        button = self.sender()
        index = self.view_task.indexAt(button.pos())
        if index.isValid():
            self.view_user.selectRow(index.row())
            tekst = self.model_task.tabela_task[index.row()][4]

            import pyttsx3
            tts_engine = pyttsx3.init()
            speaker_thread = Threader(args=[tekst, tts_engine])
            speaker_thread.start()

    def zrobione_checkbox_read_fun(self):
        for index in range(self.model_task.rowCount()):
            status = self.model_task.tabela_task[index][6]
            checkbox = self.gui_zrobione_checkbox(status)
            self.view_task.setIndexWidget(self.model_task.index(index, 6), checkbox)

    def zrobione_fun(self):
        checbox = self.sender()
        index = self.view_task.indexAt(checbox.pos())
        if index.isValid():
            if checbox.isChecked():
                self.koloruj_wiersze_model_task_fun(index.row(), 0, 127, 9)
                status = "TAK"
            else:
                self.koloruj_wiersze_model_task_fun(index.row(), 10, 10, 10)
                status = "NIE"
            self.model_task.tabela_task[index.row()][6] = status

    def make_note_window_fun(self, login, numer, wyroznienie, tresc, na_kiedy, priorytet):
        return NoteWindow(login, numer, wyroznienie, tresc, na_kiedy, priorytet)

    def show_note_windows_fun(self, id):
        for i in range(len(self.notes_window_list)):
            if self.notes_window_list[i] == id:
                self.notes_window_list[i + 1].show()

    def close_note_windows_fun(self, id):
        for i in range(len(self.notes_window_list)):
            if self.notes_window_list[i] == id:
                self.notes_window_list[i + 1].close()

    def del_note_windows_fun(self, id):
        for i in range(len(self.notes_window_list)):
            if self.notes_window_list[i] == id:
                self.notes_window_list[i + 1].close()
                del self.notes_window_list[i]
                del self.notes_window_list[i]
                break

    def update_note_windows_button_read_fun(self):
        for index in range(self.model_task.rowCount()):
            button = self.gui_odswiez_notatke_button()
            self.view_task.setIndexWidget(self.model_task.index(index, 7), button)

    def update_note_windows_fun(self):
        for index in range(self.model_task.rowCount()):
            numer = index + 1
            tresc = self.model_task.tabela_task[index][4]
            na_kiedy = datetime.strptime(self.model_task.tabela_task[index][5], '%Y-%m-%d %H:%M:%S')
            priorytet = self.model_task.tabela_task[index][2]
            for index_note in range(len(self.notes_window_list)):
                if self.notes_window_list[index_note] == self.model_task.tabela_task[index][0]:
                    self.notes_window_list[index_note + 1].update_data(str(numer), tresc, na_kiedy, priorytet)

    def wyroznione_checkbox_read_fun(self):
        for index in range(self.model_task.rowCount()):
            status = self.model_task.tabela_task[index][1]
            checkbox = self.gui_wyroznione_checkbox(status)
            self.view_task.setIndexWidget(self.model_task.index(index, 1), checkbox)

    def wyroznione_fun(self):
        checbox = self.sender()
        index = self.view_task.indexAt(checbox.pos())
        if index.isValid():
            id = self.model_task.tabela_task[index.row()][0]
            if checbox.isChecked():
                self.koloruj_komorke_model_task_fun(index.row(), index.column(), 160, 123, 0)
                self.show_note_windows_fun(id)
                status = "TAK"
            else:
                self.close_note_windows_fun(id)
                zrobione = self.model_task.tabela_task[index.row()][6]
                if zrobione == "TAK":
                    self.koloruj_komorke_model_task_fun(index.row(), index.column(), 0, 127, 9)
                else:
                    self.koloruj_komorke_model_task_fun(index.row(), index.column(), 10, 10, 10)
                status = "NIE"
            self.model_task.tabela_task[index.row()][1] = status

    def wyloguj_fun(self):
        ok = ExitWindowDialog.get_user_consent(self)
        if ok:
            self.zapisz_fun()

        for i in range(len(self.notes_window_list)):
            if i % 2 == 0:
                self.notes_window_list[i + 1].close()

        self.close()
        self.tray_icon.hide()
        self.okno_logowania = StartWindow()
        self.okno_logowania.show()

    def tray_icon_fun(self):
        self.tray_icon = QSystemTrayIcon(QtGui.QIcon("Image/Ico/App_icon.png"), parent=self)
        self.tray_icon.show()
        self.tray_menu = QMenu()

        self.show_action = self.tray_menu.addAction("Pokaż")
        self.hide_action = self.tray_menu.addAction("Schowaj")
        self.exit_action = self.tray_menu.addAction("Zakończ")

        self.show_action.triggered.connect(self.show_event)
        self.hide_action.triggered.connect(self.hide_event)
        self.exit_action.triggered.connect(self.exit_save_event)

        self.show_action.setDisabled(True)

        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        if reason == self.tray_icon.DoubleClick:
            if self.isHidden():
                self.show_event()
            else:
                self.hide_event()

    def show_normal_max_event(self):
        if self.isMaximized():
            self.showNormal()
            self.normal_full_sceen.setStyleSheet(
                "QToolButton { border-image: url(Image/Ico/Management_icon/Fullscreen_icon.png); "
                "min-width: 25px; "
                "min-height: 25px }"
                "QToolButton:hover { background-color: rgb(80, 80, 80) }"
                "QToolButton:pressed { background-color: rgb(89, 166, 0) }")
        else:
            self.showMaximized()
            self.normal_full_sceen.setStyleSheet(
                "QToolButton { border-image: url(Image/Ico/Management_icon/Normalize_icon.png); "
                "min-width: 25px; "
                "min-height: 25px }"
                "QToolButton:hover { background-color: rgb(80, 80, 80) }"
                "QToolButton:pressed { background-color: rgb(89, 166, 0) }")

    def show_event(self):
        if self.isHidden():
            self.hide_action.setEnabled(True)
            self.show_action.setDisabled(True)
        self.showNormal()

    def hide_event(self):
        if self.isVisible():
            self.show_action.setEnabled(True)
            self.hide_action.setDisabled(True)
            self.hide()

    def exit_event(self):
        if self.tray_check_box.isChecked():
            self.hide()
            self.show_action.setEnabled(True)
            self.hide_action.setDisabled(True)
            self.tray_icon.showMessage('TODO List', 'Aplikacja została zminimalizowana do paska zadan',
                                       QSystemTrayIcon.Information, 5000)
        else:
            self.exit_save_event()

    def exit_save_event(self):
        ok = ExitWindowDialog.get_user_consent(self)
        if ok:
            self.zapisz_fun()
        app.quit()

    def resizeEvent(self, event):
        self.frame_window.resize(self.frameGeometry().width(), self.frameGeometry().height())
        self.frame_bar.resize(self.frameGeometry().width(), 50)

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


class NoteWindow(QWidget, GuiWidgetWindowNote):

    def __init__(self, login, numer, wyroznienie, tresc, na_kiedy, priorytet):
        QWidget.__init__(self)
        GuiWidgetWindowNote.__init__(self)

        self.offset = None

        # Ustawienie gui
        self.set_up_gui(login, str(numer), wyroznienie, tresc, na_kiedy, priorytet)

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


if __name__ == '__main__':
    # Tworzenie aplikacji
    app = QApplication(sys.argv)

    # Ustawianie ikony aplikacji
    app_icon = QtGui.QIcon()
    app_icon.addFile('Image/Ico/App_icon/App_icon_16x16.png', QtCore.QSize(16, 16))
    app_icon.addFile('Image/Ico/App_icon/App_icon_24x24.png', QtCore.QSize(24, 24))
    app_icon.addFile('Image/Ico/App_icon/App_icon_32x32.png', QtCore.QSize(32, 32))
    app_icon.addFile('Image/Ico/App_icon/App_icon_48x48.png', QtCore.QSize(48, 48))
    app_icon.addFile('Image/Ico/App_icon/App_icon_256x256.png', QtCore.QSize(256, 256))
    app.setWindowIcon(app_icon)

    # Lączenie z baza danych
    db.polacz()

    # Tworzenie okna startowego aplikacji
    okno = StartWindow()
    okno.setWindowIcon(app_icon)
    okno.show()

    sys.exit(app.exec_())
