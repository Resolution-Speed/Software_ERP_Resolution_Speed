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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import assets.img.login_images 

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(600, 530)
        LoginPage.setMinimumSize(QSize(600, 530))
        LoginPage.setMaximumSize(QSize(600, 530))
        LoginPage.setStyleSheet(u"background-color: #000;\n"
"font: \"Inter\" 12pt ;\n"
"\n"
"")
        self.centralwidget = QWidget(LoginPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_login = QPushButton(self.centralwidget)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(90, 330, 151, 31))
        self.button_login.setMinimumSize(QSize(111, 0))
        font = QFont()
        font.setFamilies([u"12pt"])
        font.setBold(False)
        font.setItalic(False)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.557, y1:0.534364, x2:1, y2:0.506, stop:0.0397727 rgba(0, 215, 241, 1), stop:0.994318 rgba(93, 215, 241, 1));\n"
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
        self.lineField_password = QLineEdit(self.centralwidget)
        self.lineField_password.setObjectName(u"lineField_password")
        self.lineField_password.setGeometry(QRect(80, 210, 171, 31))
        self.lineField_password.setStyleSheet(u"background-color:#FFF;\n"
"width: 100px;\n"
"height: 100px;\n"
"border-radius: 11px;\n"
"")
        self.lineField_username = QLineEdit(self.centralwidget)
        self.lineField_username.setObjectName(u"lineField_username")
        self.lineField_username.setGeometry(QRect(80, 280, 171, 31))
        self.lineField_username.setStyleSheet(u"background-color:#FFF;\n"
"width: 100px;\n"
"height: 100px;\n"
"border-radius: 11px;\n"
"")
        LoginPage.setCentralWidget(self.centralwidget)
        self.graphicsView.raise_()
        self.label_title_login.raise_()
        self.button_login.raise_()
        self.label_3.raise_()
        self.label_senha.raise_()
        self.label_logo.raise_()
        self.logo_image.raise_()
        self.graphicsView_2.raise_()
        self.lineField_password.raise_()
        self.lineField_username.raise_()

        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Login", None))
        self.button_login.setText(QCoreApplication.translate("LoginPage", u"Entrar", None))
        self.label_3.setText(QCoreApplication.translate("LoginPage", u"Usu\u00e1rio", None))
        self.label_senha.setText(QCoreApplication.translate("LoginPage", u"Senha", None))
        self.label_logo.setText(QCoreApplication.translate("LoginPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Resolution Speed</span></p></body></html>", None))
        self.label_title_login.setText(QCoreApplication.translate("LoginPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Login</span></p></body></html>", None))
        self.lineField_password.setText("")
        self.lineField_username.setText("")
    # retranslateUi
