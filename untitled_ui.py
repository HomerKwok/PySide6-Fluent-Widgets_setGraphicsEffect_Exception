# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(387, 517)
        MainWindow.setStyleSheet(u"QFrame#frame_background {\n"
"	background: balck;\n"
"}\n"
"\n"
"QFrame#frame {\n"
"	background: cyan;\n"
"}\n"
"\n"
"QFrame#frame_buttons {\n"
"	background: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_background = QFrame(self.centralwidget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setStyleSheet(u"")
        self.frame_background.setFrameShape(QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_background)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.frame_background)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_4.addWidget(self.frame)

        self.frame_buttons = QFrame(self.frame_background)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setStyleSheet(u"")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_normal = QPushButton(self.frame_buttons)
        self.pushButton_normal.setObjectName(u"pushButton_normal")

        self.verticalLayout_3.addWidget(self.pushButton_normal)

        self.pushButton_abnormal = QPushButton(self.frame_buttons)
        self.pushButton_abnormal.setObjectName(u"pushButton_abnormal")

        self.verticalLayout_3.addWidget(self.pushButton_abnormal)


        self.verticalLayout_4.addWidget(self.frame_buttons)


        self.verticalLayout.addWidget(self.frame_background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_normal.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5e38InfoBar\n"
"parent=self", None))
        self.pushButton_abnormal.setText(QCoreApplication.translate("MainWindow", u"\u5f02\u5e38InfoBar\n"
"parent=self.frame", None))
    # retranslateUi

