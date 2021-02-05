from peewee import *
from datetime import datetime
from PyQt5 import QtCore

db = SqliteDatabase('Db/BazaZadan.db')
pola_task = ['Id', 'Wyróżnione', 'Priorytet', 'Dodano', 'Zadanie', 'Do kiedy', 'Zrobione', 'Odśwież', 'Usuń', 'Czytaj']
pola_user = ['Id', 'Login', 'Hasło', 'Edytuj', 'Usuń']


# Klasa bazy danych
class BazaModel(Model):
    class Meta:
        database = db


# Osoby
class Person(BazaModel):
    login = CharField(null=False, unique=True)
    haslo = CharField()

    class Meta:
        order_by = ('login',)


# Zadania
class Task(BazaModel):
    wyroznione = TextField(null=False, default="NIE")
    priorytet = TextField(null=False, default='Normalne')
    data_utw = DateTimeField(default=datetime.now)
    tresc = TextField(null=False)
    data_zrb = DateTimeField(default=datetime.now)
    wykonane = TextField(null=False, default="NIE")
    osoba = ForeignKeyField(Person, related_name='zadania')

    class Meta:
        order_by = ('data_utw',)


def polacz():
    # Połączenie z bazą
    db.connect()
    # Utworzenie tabel w bazie danych
    db.create_tables([Person, Task], safe=True)
    # Dodawanie przykładowych danych
    tworzenie_administratora()
    return True


def zarejestruj(login, haslo):
    osoba = Person.get_or_none(login=login)
    if osoba is None:
        o = Person.create(login=login, haslo=haslo)
        o.save()
        db.commit()
        db.close()
        return True
    else:
        return False


def zaloguj(login, haslo):
    osoba = Person.get_or_none(login=login, haslo=haslo)
    if osoba is None:
        return False
    return True


def get_osoba(login, haslo):
    osoba = Person.get_or_none(login=login, haslo=haslo)
    return osoba


def tworzenie_administratora():
    if Person.select().count() > 0:
        return
    osoby = ('Admin', 'Bartek')
    zadania = ('Pierwsze zadanie', 'Drugie zadanie', 'Trzecie zadanie')
    for login in osoby:
        o = Person(login=login, haslo='123456')
        o.save()
        for tresc in zadania:
            z = Task(tresc=tresc, osoba=o)
            z.save()
    db.commit()
    db.close()


def czytaj_dane(self, osoba):
    """ Pobranie zadań danego użytkownika z bazy """
    tasks = []  # lista zadań
    wpisy = Task.select().where(Task.osoba == osoba)
    numer = 1
    for w in wpisy:
        self.notes_window_list.append(w.id)
        self.notes_window_list.append(self.make_note_window_fun(osoba.login, numer, w.wyroznione, w.tresc, w.data_zrb, w.priorytet))
        if w.wyroznione == "TAK":
            self.show_note_windows_fun(w.id)
        numer += 1
        tasks.append([
            w.id,
            w.wyroznione,
            w.priorytet,
            '{0:%Y-%m-%d %H:%M:%S}'.format(w.data_utw),
            w.tresc,
            '{0:%Y-%m-%d %H:%M:%S}'.format(w.data_zrb),
            w.wykonane,
            "",
            "",
            ""])
    return tasks


def czytaj_uzytkownikow():
    users = []
    wpisy = Person.select()
    for w in wpisy:
        users.append([
            w.id,
            w.login,
            w.haslo,
            "",
            ""])
    return users


def dodaj_zadanie(osoba, zadanie, data, priorytet, wyroznione):
    task = Task(tresc=zadanie, osoba=osoba, data_zrb=data, priorytet=priorytet, wyroznione=wyroznione)
    task.save()
    return [
        task.id,
        task.wyroznione,
        task.priorytet,
        '{0:%Y-%m-%d %H:%M:%S}'.format(task.data_utw),
        task.tresc,
        '{0:%Y-%m-%d %H:%M:%S}'.format(task.data_zrb),
        task.wykonane,
        "",
        "",
        ""]


def zapisz_dane(zadania):
    """ Zapisywanie zmian """
    for i, z in enumerate(zadania):
        zadanie = Task.select().where(Task.id == z[0]).get()
        zadanie.wyroznione = z[1]
        zadanie.tresc = z[4]
        zadanie.wykonane = z[6]
        zadanie.save()


def usun_notatke(self, index):
    db_index = self.model_task.tabela_task[index.row()][0]
    self.close_note_windows_fun(db_index)
    self.del_note_windows_fun(db_index)
    zadanie = Task.select().where(Task.id == db_index).get()
    zadanie.delete_instance()
    del self.model_task.tabela_task[index.row()]
    self.update_note_windows_fun()


def usun_notatki(self):
    index_list = []
    for model_index in self.view_task.selectionModel().selectedRows():
        index = QtCore.QPersistentModelIndex(model_index)
        index_list.append(index)

    for index in sorted(index_list, reverse=True):
        usun_notatke(self, index)

def usun_uzytkownika(self, index):
    db_index = self.model_user.tabela_user[index.row()][0]
    uzytkownik = Person.select().where(Person.id == db_index).get()

    wpisy = Task.select().where(Task.osoba == uzytkownik)
    for w in wpisy:
        w.delete_instance()

    uzytkownik.delete_instance()
    del self.model_user.tabela_user[index.row()]

def edytuj_uzytkownika(self, index, login, haslo):
    db_index = self.model_user.tabela_user[index.row()][0]
    uzytkownik = Person.select().where(Person.id == db_index).get()
    uzytkownik.login = login
    uzytkownik.haslo = haslo
    uzytkownik.save()

def edytuj_uzytkownika_settings(self, login, haslo):
    uzytkownik = Person.select().where(Person.login == self.login).get()
    uzytkownik.login = login
    uzytkownik.haslo = haslo
    uzytkownik.save()