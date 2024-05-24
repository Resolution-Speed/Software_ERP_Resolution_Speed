# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
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
from cadastro_produto import Ui_RegProductPage
from pedido_venda import Ui_PedVendaPage
from main import regProdOpen, pedidoVendaOpen

class Ui_HomePage(object):
    def regProdOpen(self):
        self.window3 = QMainWindow()
        self.ui = Ui_RegProductPage()
        self.ui.setupUi(self.window3)
        self.window3.show()
        
    def pedVenOpen(self):
        self.window4 = QMainWindow()
        self.ui = Ui_PedVendaPage()
        self.ui.setupUi(self.window4)
        self.window4.show()

    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(600, 530)
        HomePage.setMinimumSize(QSize(600, 530))
        HomePage.setMaximumSize(QSize(600, 530))
        HomePage.setStyleSheet(u"background-color: rgb(93, 215, 241);\n"
"font: 12pt \"Inter\";")
        self.centralwidget = QWidget(HomePage)
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
        self.homeTitle.setGeometry(QRect(280, 20, 41, 16))
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
        self.homeButton_cad_prod = QPushButton(self.centralwidget)
        self.homeButton_cad_prod.setObjectName(u"homeButton_cad_prod")
        self.homeButton_cad_prod.setGeometry(QRect(80, 230, 100, 100))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setBold(True)
        font1.setItalic(False)
        self.homeButton_cad_prod.setFont(font1)
        self.homeButton_cad_prod.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton_cad_prod.setStyleSheet(u"QPushButton\n"
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
        self.homeButton_ped_ven = QPushButton(self.centralwidget)
        self.homeButton_ped_ven.setObjectName(u"homeButton_ped_ven")
        self.homeButton_ped_ven.setGeometry(QRect(250, 230, 100, 100))
        self.homeButton_ped_ven.setFont(font1)
        self.homeButton_ped_ven.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton_ped_ven.setStyleSheet(u"QPushButton\n"
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
        self.homeButton_nfe = QPushButton(self.centralwidget)
        self.homeButton_nfe.setObjectName(u"homeButton_nfe")
        self.homeButton_nfe.setGeometry(QRect(420, 230, 100, 100))
        self.homeButton_nfe.setFont(font1)
        self.homeButton_nfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton_nfe.setStyleSheet(u"QPushButton\n"
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
        HomePage.setCentralWidget(self.centralwidget)
        self.wrapperHeader.raise_()
        self.exitButton.raise_()
        self.wrapperMenu.raise_()
        self.textBrowser.raise_()
        self.homeButton.raise_()
        self.homeTitle.raise_()
        self.homeButton_cad_prod.raise_()
        self.homeButton_ped_ven.raise_()
        self.homeButton_nfe.raise_()
        QWidget.setTabOrder(self.homeButton, self.exitButton)
        QWidget.setTabOrder(self.exitButton, self.homeButton_cad_prod)
        QWidget.setTabOrder(self.homeButton_cad_prod, self.homeButton_ped_ven)
        QWidget.setTabOrder(self.homeButton_ped_ven, self.homeButton_nfe)
        QWidget.setTabOrder(self.homeButton_nfe, self.wrapperMenu)
        QWidget.setTabOrder(self.wrapperMenu, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.wrapperHeader)

        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)

        #Function open "Registrar Projeto"
        def actionOpenProd():
            regProdOpen(self)

        def actionOpenPed():
            pedidoVendaOpen(self)

        def exitWindow():
            HomePage.close()
        
        self.exitButton.clicked.connect(exitWindow)
        self.homeButton_cad_prod.clicked.connect(actionOpenProd)
        self.homeButton_ped_ven.clicked.connect(actionOpenPed)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Pagina Inicial", None))
        self.homeButton.setText(QCoreApplication.translate("HomePage", u"HOME", None))
        self.exitButton.setText(QCoreApplication.translate("HomePage", u"SAIR", None))
        self.homeTitle.setText(QCoreApplication.translate("HomePage", u"HOME", None))
        self.textBrowser.setHtml(QCoreApplication.translate("HomePage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">MENU PRINCIPAL</span></p></body></html>", None))
        self.homeButton_cad_prod.setText(QCoreApplication.translate("HomePage", u"Cadastro de Produto", None))
        self.homeButton_ped_ven.setText(QCoreApplication.translate("HomePage", u"Pedido de Venda", None))
        self.homeButton_nfe.setText(QCoreApplication.translate("HomePage", u"Nota Fiscal de Sa\u00edda", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_window = QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(home_window)
    home_window.show()
    sys.exit(app.exec())