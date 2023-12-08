# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_user.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 271)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color: rgb(182, 182, 182)")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.DataContainer = QVBoxLayout()
        self.DataContainer.setObjectName(u"DataContainer")
        self.Name = QLineEdit(Dialog)
        self.Name.setObjectName(u"Name")
        self.Name.setMinimumSize(QSize(0, 45))
        self.Name.setFont(font)

        self.DataContainer.addWidget(self.Name)

        self.Password = QLineEdit(Dialog)
        self.Password.setObjectName(u"Password")
        self.Password.setMinimumSize(QSize(0, 45))
        self.Password.setFont(font)

        self.DataContainer.addWidget(self.Password)

        self.PowerLevel = QComboBox(Dialog)
        self.PowerLevel.addItem("")
        self.PowerLevel.addItem("")
        self.PowerLevel.setObjectName(u"PowerLevel")
        self.PowerLevel.setMinimumSize(QSize(0, 45))
        self.PowerLevel.setFont(font)

        self.DataContainer.addWidget(self.PowerLevel)


        self.verticalLayout_2.addLayout(self.DataContainer)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(Dialog)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(100, 0))
        self.add.setFont(font)

        self.horizontalLayout.addWidget(self.add)

        self.back = QPushButton(Dialog)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(100, 0))
        self.back.setFont(font)

        self.horizontalLayout.addWidget(self.back)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u041d\u043e\u0432\u043e\u0433\u043e \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.Name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.PowerLevel.setItemText(0, QCoreApplication.translate("Dialog", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.PowerLevel.setItemText(1, QCoreApplication.translate("Dialog", u"\u0412\u0435\u0442\u0435\u0440\u0438\u043d\u0430\u0440", None))

        self.PowerLevel.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.add.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.back.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

