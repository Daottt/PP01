# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QHBoxLayout, QHeaderView, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1086, 667)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(182, 182, 182)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.ShowTables = QPushButton(self.centralwidget)
        self.ShowTables.setObjectName(u"ShowTables")
        self.ShowTables.setEnabled(False)
        self.ShowTables.setMinimumSize(QSize(250, 0))
        self.ShowTables.setFont(font)

        self.horizontalLayout_4.addWidget(self.ShowTables)

        self.ShowStats = QPushButton(self.centralwidget)
        self.ShowStats.setObjectName(u"ShowStats")
        self.ShowStats.setMinimumSize(QSize(250, 0))
        self.ShowStats.setFont(font)

        self.horizontalLayout_4.addWidget(self.ShowStats)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        font1 = QFont()
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.stackedWidget.setFont(font1)
        self.Tables = QWidget()
        self.Tables.setObjectName(u"Tables")
        self.horizontalLayout_3 = QHBoxLayout(self.Tables)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.TabelList = QListWidget(self.Tables)
        self.TabelList.setObjectName(u"TabelList")
        self.TabelList.setMinimumSize(QSize(200, 0))
        self.TabelList.setMaximumSize(QSize(250, 16777215))
        self.TabelList.setFont(font)

        self.horizontalLayout_3.addWidget(self.TabelList)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Add = QPushButton(self.Tables)
        self.Add.setObjectName(u"Add")
        self.Add.setMinimumSize(QSize(250, 0))
        self.Add.setFont(font)

        self.horizontalLayout.addWidget(self.Add)

        self.Update = QPushButton(self.Tables)
        self.Update.setObjectName(u"Update")
        self.Update.setMinimumSize(QSize(250, 0))
        self.Update.setFont(font)

        self.horizontalLayout.addWidget(self.Update)

        self.Delete = QPushButton(self.Tables)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setMinimumSize(QSize(250, 0))
        self.Delete.setFont(font)

        self.horizontalLayout.addWidget(self.Delete)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Table = QTableWidget(self.Tables)
        self.Table.setObjectName(u"Table")
        self.Table.setFont(font)
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Table.setTextElideMode(Qt.ElideNone)
        self.Table.horizontalHeader().setVisible(True)
        self.Table.horizontalHeader().setMinimumSectionSize(60)
        self.Table.horizontalHeader().setDefaultSectionSize(200)
        self.Table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.Table)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.Tables)
        self.Stats = QWidget()
        self.Stats.setObjectName(u"Stats")
        self.pushButton = QPushButton(self.Stats)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 250, 75, 24))
        self.verticalLayoutWidget = QWidget(self.Stats)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(139, 89, 281, 181))
        self.dada = QVBoxLayout(self.verticalLayoutWidget)
        self.dada.setObjectName(u"dada")
        self.dada.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.dada.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.dada.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDate(QDate(2023, 12, 8))

        self.dada.addWidget(self.dateEdit)

        self.stackedWidget.addWidget(self.Stats)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ShowTables.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.ShowStats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Update.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"STATbl", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"b", None))

    # retranslateUi

