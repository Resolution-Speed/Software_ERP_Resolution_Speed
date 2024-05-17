# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HOME.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
import assets.img.home_images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 530)
        MainWindow.setMinimumSize(QSize(600, 530))
        MainWindow.setMaximumSize(QSize(600, 530))
        MainWindow.setStyleSheet(u"background-color: rgb(93, 215, 241);\n"
"font: 12pt \"Inter\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 10, 105, 31))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(False)
        font.setItalic(False)
        self.homeButton.setFont(font)
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(93, 215, 241); \n"
"	border: 1px solid rgb(93, 215, 241);\n"
"	border-radius: 5px;\n"
"	font-size: 10px;	\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #000000;\n"
"	color : rgb(93, 215, 241);\n"
"}\n"
"")
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(490, 10, 105, 31))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(93, 215, 241); \n"
"	border: 1px solid rgb(93, 215, 241);\n"
"	border-radius: 5px;\n"
"	font-size: 10px;	\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #000000;\n"
"	color : rgb(93, 215, 241);\n"
"}\n"
"")
        self.homeTitle = QLabel(self.centralwidget)
        self.homeTitle.setObjectName(u"homeTitle")
        self.homeTitle.setGeometry(QRect(280, 20, 47, 13))
        self.homeTitle.setStyleSheet(u"background-color: transparent;\n"
"color: #fff;\n"
"font-size: 12px")
        self.wrapperMenu = QGraphicsView(self.centralwidget)
        self.wrapperMenu.setObjectName(u"wrapperMenu")
        self.wrapperMenu.setGeometry(QRect(60, 70, 481, 430))
        self.wrapperMenu.setStyleSheet(u"border: 5px solid #000;\n"
"border-radius: 10px;\n"
"")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(200, 70, 210, 35))
        self.textBrowser.setStyleSheet(u"background-color: #000;\n"
"color: #fff;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;")
        self.wrapperHeader = QGraphicsView(self.centralwidget)
        self.wrapperHeader.setObjectName(u"wrapperHeader")
        self.wrapperHeader.setGeometry(QRect(0, 0, 601, 50))
        self.wrapperHeader.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.homeButton_2 = QPushButton(self.centralwidget)
        self.homeButton_2.setObjectName(u"homeButton_2")
        self.homeButton_2.setGeometry(QRect(80, 230, 100, 100))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setBold(True)
        font1.setItalic(False)
        self.homeButton_2.setFont(font1)
        self.homeButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(:/menuImg/product.png);\n"
"	border: 1px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-size: 7px;\n"
"	color: #fff;\n"
"	font-weight: 700;\n"
"	text-align: bottom;\n"
"	background-color: #000;\n"
"	padding: 10px 11px;\n"
"	transition:  1s;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	image: url(:/menuImg/product_hover.png);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: #000000;\n"
"}")
        self.homeButton_3 = QPushButton(self.centralwidget)
        self.homeButton_3.setObjectName(u"homeButton_3")
        self.homeButton_3.setGeometry(QRect(250, 230, 100, 100))
        self.homeButton_3.setFont(font1)
        self.homeButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(:/menuImg/sell_request.png);\n"
"	border: 1px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-size: 7px;\n"
"	color: #fff;\n"
"	font-weight: 700;\n"
"	text-align: bottom;\n"
"	background-color: #000;\n"
"	padding: 10px 11px;\n"
"	transition:  1s;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	image: url(:/menuImg/sell_request_hover.png);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: #000000;\n"
"}")
        self.homeButton_4 = QPushButton(self.centralwidget)
        self.homeButton_4.setObjectName(u"homeButton_4")
        self.homeButton_4.setGeometry(QRect(420, 230, 100, 100))
        self.homeButton_4.setFont(font1)
        self.homeButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(:/menuImg/nfe.png);\n"
"	border: 1px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-size: 7px;\n"
"	color: #fff;\n"
"	font-weight: 700;\n"
"	text-align: bottom;\n"
"	background-color: #000;\n"
"	padding: 10px 11px;\n"
"	transition:  1s;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	image: url(:/menuImg/nfe_hover.png);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: #000000;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.wrapperHeader.raise_()
        self.exitButton.raise_()
        self.wrapperMenu.raise_()
        self.textBrowser.raise_()
        self.homeButton.raise_()
        self.homeTitle.raise_()
        self.homeButton_2.raise_()
        self.homeButton_3.raise_()
        self.homeButton_4.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.homeTitle.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">MENU PRINCIPAL</span></p></body></html>", None))
        self.homeButton_2.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Produto", None))
        self.homeButton_3.setText(QCoreApplication.translate("MainWindow", u"Pedido de Venda", None))
        self.homeButton_4.setText(QCoreApplication.translate("MainWindow", u"Nota Fiscal de Sa\u00edda", None))
    # retranslateUi

