from PySide6.QtWidgets import QMainWindow, QLineEdit, QComboBox, QDateEdit, QDialog, QTableWidgetItem

from src.client.ui_main import Ui_MainWindow
from src.client.new_user import Ui_Dialog as user
from src.client.new_record import Ui_Dialog as record
from src.client.api.resolver import *

TablesList = ["Users", "Requests"]
WindowList = [user, record]

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.current_table_index = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ShowTables.clicked.connect(lambda: self.ChangeTab(0))
        self.ui.ShowStats.clicked.connect(lambda: self.ChangeTab(1))
        self.ui.Add.clicked.connect(self.OpenNewWindow)
        self.ui.Update.clicked.connect(self.OpenNewWindow)
        self.ui.Delete.clicked.connect(self.delete_data)

        table_list = self.ui.TabelList
        table_list.currentRowChanged.connect(self.TableSelect)
        table_list.addItems(TablesList)

    def TableSelect(self, table_index):
        print(f"Таблица: {table_index}")
        self.current_table_index = table_index
        self.UpdateTableData()

    def UpdateTableData(self):
        data = getAll(TablesList[self.current_table_index])

        table = self.ui.Table
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))
        table.setHorizontalHeaderLabels(list(data[0].keys()))
        table.setColumnWidth(0, 60)

        row_index = 0
        for values in data:
            for item in values.values():
                for i in range(len(data[0])):
                    table.setItem(i, row_index, QTableWidgetItem(str(item)))
                row_index += 1

    def ChangeTab(self, tab_index):
        self.ui.ShowTables.setEnabled(not self.ui.ShowTables.isEnabled())
        self.ui.ShowStats.setEnabled(not self.ui.ShowStats.isEnabled())

        self.ui.stackedWidget.setCurrentIndex(tab_index)

    def OpenNewWindow(self):
        self.new_window = QDialog()
        self.ui_window = user()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.back.clicked.connect(lambda : self.new_window.close())

        sender = self.sender()
        if sender.objectName() == "Add":
            self.ui_window.add.clicked.connect(self.add_data)
            self.ui_window.label.setText("Создать запись")
            self.ui_window.add.setText("Создать")
        else:
            self.ui_window.add.clicked.connect(self.update_data)
            self.ui_window.label.setText("Обновить запись")
            self.ui_window.add.setText("Обновить")

        self.new_window.show()

    def get_model(self) -> dict:
        #TODO проверка на отсутствие данных

        data = getAll(TablesList[self.current_table_index])
        keys: list = data[0].keys()
        values: list = ['0']
        for layout_item in self.layout_widgets(self.ui_window.DataContainer):
            widget = layout_item.widget()
            values.append(self.get_data_from_widget(widget))
        self.new_window.close()
        return dict(zip(keys, values))

    def get_current_id(self) -> int:
        index = self.ui.Table.selectedIndexes()[0]
        return self.ui.Table.model().data(index)

    def add_data(self):
        create(TablesList[self.current_table_index], self.get_model())
        self.UpdateTableData()

    def update_data(self):
        update(TablesList[self.current_table_index], self.get_model(), self.get_current_id())
        self.UpdateTableData()

    def delete_data(self):
        delete(TablesList[self.current_table_index], self.get_current_id())
        #TODO Окно подтверждения
        self.UpdateTableData()

    def layout_widgets(self, layout):
        return (layout.itemAt(i) for i in range(layout.count()))

    def get_data_from_widget(self, widget):
        if isinstance(widget, QLineEdit):
            return widget.text()
        elif isinstance(widget, QComboBox):
            return widget.currentIndex()
        elif isinstance(widget, QDateEdit):
            return widget.text()
        else:
            print("Виджет неизвестного типа")

