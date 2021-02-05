from __future__ import unicode_literals
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtGui import QColor, QFont


class TabUserModel(QAbstractTableModel):
    def __init__(self, pola=[], dane=[], parent=None):
        super(TabUserModel, self).__init__()
        self.pola_user = pola
        self.tabela_user = dane

    def aktualizuj(self, dane):
        """ Przypisuje źródło danych do modelu """
        self.tabela_user = dane

    def rowCount(self, parent=QModelIndex()):
        """ Zwraca ilość wierszy """
        return len(self.tabela_user)

    def columnCount(self, parent=QModelIndex()):
        """ Zwraca ilość kolumn """
        if self.tabela_user:
            return len(self.tabela_user[0])
        else:
            return 0

    def head(self):
        return

    def data(self, index, rola=Qt.DisplayRole):
        """ Wyświetlanie danych """
        i = index.row()
        j = index.column()
        if rola == Qt.DisplayRole:
            return '{0}'.format(self.tabela_user[i][j])
        elif rola == Qt.BackgroundColorRole and j % 2 == 0:
            return QColor(10, 10, 10)
        elif rola == Qt.BackgroundColorRole:
            return QColor(36, 36, 36)
        elif rola == Qt.TextColorRole:
            return QColor(Qt.white)
        elif rola == Qt.FontRole:
            return QFont("Consolas", 12)
        elif rola == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        else:
            return QVariant()

    def headerData(self, sekcja_user, kierunek, rola=Qt.DisplayRole):
        """ Zwraca nagłówki kolumn """
        if rola == Qt.DisplayRole and kierunek == Qt.Horizontal:
            return self.pola_user[sekcja_user]
        elif rola == Qt.DisplayRole and kierunek == Qt.Vertical:
            return sekcja_user + 1
        else:
            return QVariant()