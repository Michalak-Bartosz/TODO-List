from __future__ import unicode_literals
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtGui import QColor, QFont

class TabTaskModel(QAbstractTableModel):
    def __init__(self, pola=[], dane=[], parent=None):
        super(TabTaskModel, self).__init__()
        self.pola_task = pola
        self.tabela_task = dane
        self.colors = dict()

    def aktualizuj(self, dane):
        """ Przypisuje źródło danych do modelu """
        self.tabela_task = dane

    def rowCount(self, parent=QModelIndex()):
        """ Zwraca ilość wierszy """
        return len(self.tabela_task)

    def columnCount(self, parent=QModelIndex()):
        """ Zwraca ilość kolumn """
        if self.tabela_task:
            return len(self.tabela_task[0])
        else:
            return 0

    def head(self):
        return

    def data(self, index, rola=Qt.DisplayRole):
        i = index.row()
        j = index.column()
        if rola == Qt.DisplayRole:
            return '{0}'.format(self.tabela_task[i][j])
        elif rola == Qt.EditRole and j == 4:
            return self.tabela_task[i][j]
        elif rola == Qt.BackgroundColorRole:
            color = self.colors.get((index.row(), index.column()))
            return color
        elif rola == Qt.TextColorRole:
            return QColor(Qt.white)
        elif rola == Qt.FontRole:
            return QFont("Consolas", 12)
        elif rola == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        else:
            return QVariant()

    def flags(self, index):
        """ Zwraca właściwości kolumn tabeli """
        flags = super(TabTaskModel, self).flags(index)
        j = index.column()
        if j == 4:
            flags |= Qt.ItemIsEditable

        return flags

    def setData(self, index, value, rola=Qt.DisplayRole):
        """ Zmiana danych """
        i = index.row()
        j = index.column()
        if rola == Qt.EditRole and j == 4:
            self.tabela_task[i][j] = value

        return True

    def headerData(self, sekcja_task, kierunek, rola=Qt.DisplayRole):
        """ Zwraca nagłówki kolumn """
        if rola == Qt.DisplayRole and kierunek == Qt.Horizontal:
            return self.pola_task[sekcja_task]
        elif rola == Qt.DisplayRole and kierunek == Qt.Vertical:
            return sekcja_task + 1
        else:
            return QVariant()

    def change_color(self, row, column, color):
        ix = self.index(row, column)
        self.colors[(row, column)] = color
        self.dataChanged.emit(ix, ix, (Qt.BackgroundRole,))