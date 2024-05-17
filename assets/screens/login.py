# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import assets.img.login_images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 530)
        MainWindow.setMinimumSize(QSize(600, 530))
        MainWindow.setMaximumSize(QSize(600, 530))
        MainWindow.setStyleSheet(u"background-color: #000;\n"
"font: \"Inter\" 12pt ;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 330, 151, 31))
        self.pushButton.setMinimumSize(QSize(111, 0))
        font = QFont()
        font.setFamilies([u"12pt"])
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.557, y1:0.534364, x2:1, y2:0.506, stop:0.0397727 rgba(0, 215, 241, 1), stop:0.994318 rgba(93, 215, 241, 1));\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"width: 100px;\n"
"height: 100px;\n"
"border-radius: 15px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 190, 41, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0);\n"
"background-color:none")
        self.label_senha = QLabel(self.centralwidget)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setGeometry(QRect(90, 260, 31, 21))
        self.label_senha.setFont(font)
        self.label_senha.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,0);\n"
"background-color:none")
        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(380, 200, 151, 81))
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color:none")
        self.label_title_login = QLabel(self.centralwidget)
        self.label_title_login.setObjectName(u"label_title_login")
        self.label_title_login.setGeometry(QRect(80, 130, 121, 51))
        self.label_title_login.setFont(font)
        self.label_title_login.setStyleSheet(u"background-color:none;\n"
"color:#FFF;\n"
"")
        self.usuario = QTextEdit(self.centralwidget)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(80, 210, 171, 31))
        self.usuario.setFont(font)
        self.usuario.setStyleSheet(u"background-color:#FFF;\n"
"width: 100px;\n"
"height: 100px;\n"
"border-radius: 11px;\n"
"")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 280, 171, 31))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color:#FFF;\n"
"width: 100px;\n"
"height: 100px;\n"
"border-radius: 11px;")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(60, 110, 481, 281))
        self.graphicsView.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.557, y1:0.534364, x2:1, y2:0.506, stop:0.0397727 rgba(0, 0, 0, 1), stop:0.994318 rgba(93, 215, 241, 1));\n"
"\n"
"border-radius: 10px;\n"
"border: 3px solid #fff")
        self.logo_image = QGraphicsView(self.centralwidget)
        self.logo_image.setObjectName(u"logo_image")
        self.logo_image.setGeometry(QRect(410, 260, 81, 81))
        self.logo_image.setStyleSheet(u"background-color: transparent;\n"
"background-image: url(:/images/Logo_Resolution_speed.png);\n"
"background-repeat: none;\n"
"border: none")
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(200, 150, 25, 25))
        self.graphicsView_2.setMaximumSize(QSize(25, 25))
        self.graphicsView_2.setStyleSheet(u"border: none;\n"
"background-image: url(:/images/Resolution_speed_small.png);\n"
"\n"
"background-repeat: none;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.graphicsView.raise_()
        self.label_title_login.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_senha.raise_()
        self.label_logo.raise_()
        self.usuario.raise_()
        self.textEdit.raise_()
        self.logo_image.raise_()
        self.graphicsView_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Resolution Speed</span></p></body></html>", None))
        self.label_title_login.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Login</span></p></body></html>", None))
    # retranslateUi

