# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedido_venda.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)
import mysql.connector

class Ui_PedVendaPage(object):
    def setupUi(self, PedVendaPage):
        if not PedVendaPage.objectName():
            PedVendaPage.setObjectName(u"PedVendaPage")
        PedVendaPage.resize(1100, 600)
        PedVendaPage.setMinimumSize(QSize(1100, 600))
        PedVendaPage.setMaximumSize(QSize(1100, 600))
        PedVendaPage.setStyleSheet(u"background-color: #fff;")
        self.centralwidget = QWidget(PedVendaPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.embrulho_2 = QGraphicsView(self.centralwidget)
        self.embrulho_2.setObjectName(u"embrulho_2")
        self.embrulho_2.setGeometry(QRect(60, 80, 981, 491))
        self.embrulho_2.setStyleSheet(u"border: 5px solid rgb(93,215,241);\n"
"\n"
"border-radius:10px;")
        self.textBrowser_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(60, 80, 207, 27))
        self.textBrowser_3.setStyleSheet(u"background-color:#5DD7F1;\n"
"\n"
"border: nome;\n"
"\n"
"color: #fff;\n"
"\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"border-top-left-radius: 10px;")
        self.line_npedido = QLineEdit(self.centralwidget)
        self.line_npedido.setObjectName(u"line_npedido")
        self.line_npedido.setGeometry(QRect(80, 190, 291, 25))
        self.line_tipovenda = QLineEdit(self.centralwidget)
        self.line_tipovenda.setObjectName(u"line_tipovenda")
        self.line_tipovenda.setGeometry(QRect(700, 190, 291, 25))
        self.line_ordemcompra = QLineEdit(self.centralwidget)
        self.line_ordemcompra.setObjectName(u"line_ordemcompra")
        self.line_ordemcompra.setGeometry(QRect(700, 260, 291, 25))
        self.line_cliente = QLineEdit(self.centralwidget)
        self.line_cliente.setObjectName(u"line_cliente")
        self.line_cliente.setGeometry(QRect(390, 190, 291, 25))
        self.line_prazopgt = QLineEdit(self.centralwidget)
        self.line_prazopgt.setObjectName(u"line_prazopgt")
        self.line_prazopgt.setGeometry(QRect(80, 260, 281, 25))
        self.line_vendedor = QLineEdit(self.centralwidget)
        self.line_vendedor.setObjectName(u"line_vendedor")
        self.line_vendedor.setGeometry(QRect(390, 260, 291, 25))
        self.lb_npedido = QLabel(self.centralwidget)
        self.lb_npedido.setObjectName(u"lb_npedido")
        self.lb_npedido.setGeometry(QRect(80, 170, 81, 16))
        font = QFont()
        font.setBold(True)
        self.lb_npedido.setFont(font)
        self.lb_cliente = QLabel(self.centralwidget)
        self.lb_cliente.setObjectName(u"lb_cliente")
        self.lb_cliente.setGeometry(QRect(390, 170, 47, 13))
        self.lb_cliente.setFont(font)
        self.lb_tipovenda = QLabel(self.centralwidget)
        self.lb_tipovenda.setObjectName(u"lb_tipovenda")
        self.lb_tipovenda.setGeometry(QRect(700, 170, 91, 16))
        self.lb_tipovenda.setFont(font)
        self.lb_prazopgt = QLabel(self.centralwidget)
        self.lb_prazopgt.setObjectName(u"lb_prazopgt")
        self.lb_prazopgt.setGeometry(QRect(80, 240, 71, 16))
        self.lb_prazopgt.setFont(font)
        self.lb_vendedor = QLabel(self.centralwidget)
        self.lb_vendedor.setObjectName(u"lb_vendedor")
        self.lb_vendedor.setGeometry(QRect(390, 240, 91, 16))
        self.lb_vendedor.setFont(font)
        self.lb_ordemcompra = QLabel(self.centralwidget)
        self.lb_ordemcompra.setObjectName(u"lb_ordemcompra")
        self.lb_ordemcompra.setGeometry(QRect(700, 240, 121, 16))
        self.lb_ordemcompra.setFont(font)
        self.button_home_2 = QPushButton(self.centralwidget)
        self.button_home_2.setObjectName(u"button_home_2")
        self.button_home_2.setGeometry(QRect(310, 370, 191, 71))
        self.button_home_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_home_2.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(93, 215, 241); \n"
"    border: 1px solid rgb(93, 215, 241);\n"
"    border-radius: 5px;\n"
"    font-size: 10px;\n"
"	color: #fff\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #fff;\n"
"    color : rgb(93, 215, 241);\n"
"}")
        self.button_gnfe = QPushButton(self.centralwidget)
        self.button_gnfe.setObjectName(u"button_gnfe")
        self.button_gnfe.setGeometry(QRect(600, 370, 191, 71))
        self.button_gnfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_gnfe.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(93, 215, 241); \n"
"    border: 1px solid rgb(93, 215, 241);\n"
"    border-radius: 5px;\n"
"    font-size: 10px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #fff;\n"
"    color : rgb(93, 215, 241);\n"
"}")
        self.wrapperHeader = QGraphicsView(self.centralwidget)
        self.wrapperHeader.setObjectName(u"wrapperHeader")
        self.wrapperHeader.setGeometry(QRect(0, 0, 1101, 50))
        self.wrapperHeader.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(980, 10, 105, 31))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(93, 215, 241); \n"
"	border: 1px solid rgb(93, 215, 241);\n"
"	border-radius: 5px;\n"
"	font-size: 10px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #000000;\n"
"	color : rgb(93, 215, 241);\n"
"}\n"
"")
        self.homeTitle = QLabel(self.centralwidget)
        self.homeTitle.setObjectName(u"homeTitle")
        self.homeTitle.setGeometry(QRect(530, 20, 101, 16))
        self.homeTitle.setStyleSheet(u"background-color: transparent;\n"
"color: #fff;\n"
"font-size: 12px")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 10, 105, 31))
        font1 = QFont()
        self.homeButton.setFont(font1)
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(93, 215, 241); \n"
"	border: 1px solid rgb(93, 215, 241);\n"
"	border-radius: 5px;\n"
"	font-size: 10px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #000000;\n"
"	color : rgb(93, 215, 241);\n"
"}\n"
"")
        PedVendaPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.homeButton, self.exitButton)
        QWidget.setTabOrder(self.exitButton, self.line_npedido)
        QWidget.setTabOrder(self.line_npedido, self.line_cliente)
        QWidget.setTabOrder(self.line_cliente, self.line_tipovenda)
        QWidget.setTabOrder(self.line_tipovenda, self.line_prazopgt)
        QWidget.setTabOrder(self.line_prazopgt, self.line_vendedor)
        QWidget.setTabOrder(self.line_vendedor, self.line_ordemcompra)
        QWidget.setTabOrder(self.line_ordemcompra, self.button_home_2)
        QWidget.setTabOrder(self.button_home_2, self.button_gnfe)
        QWidget.setTabOrder(self.button_gnfe, self.textBrowser_3)
        QWidget.setTabOrder(self.textBrowser_3, self.wrapperHeader)
        QWidget.setTabOrder(self.wrapperHeader, self.embrulho_2)

        self.retranslateUi(PedVendaPage)

        QMetaObject.connectSlotsByName(PedVendaPage)

        #Inicio conexão com banco de dados  
        banco = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="erp_resolution_speed"
        )
        #Fim conexão com banco de dados

        def resetFields():
            self.line_npedido.setText("")
            self.line_cliente.setText("")
            self.line_tipovenda.setText("")
            self.line_prazopgt.setText("")
            self.line_vendedor.setText("")
            self.line_ordemcompra.setText("")
        
        def registerAction():
        #Inicio declarando valores de entrada
            codPvWrited = self.line_npedido.text()
            clientePvWrited = self.line_cliente.text()
            tpVendaWrited = self.line_tipovenda.text()
            przWrited = self.line_prazopgt.text()
            vendedorWrited = self.line_vendedor.text()
            ordemCompWrited = self.line_ordemcompra.text()
            #Fim declarando valores de entrada

            cursor = banco.cursor()
            comandoSQL = "INSERT INTO pedidoVenda (numPedido, clientePedido, tipoVenda, prazoPedido, vendedorPedido, ordemCompra) VALUES (%s, %s, %s, %s, %s, %s)"

            dados = (str(codPvWrited), str(clientePvWrited), str(tpVendaWrited), str(przWrited), str(vendedorWrited), str(ordemCompWrited))

            cursor.execute(comandoSQL, dados)
            banco.commit()
            print(dados)
            resetFields()

        def exitWindow():
            PedVendaPage.close()
        
        self.homeButton.clicked.connect(exitWindow)
        self.exitButton.clicked.connect(exitWindow)

        self.button_home_2.clicked.connect(registerAction)
    # setupUi

    def retranslateUi(self, PedVendaPage):
        PedVendaPage.setWindowTitle(QCoreApplication.translate("PedVendaPage", u"Pedido de Venda", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("PedVendaPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PEDIDO DE VENDAS</p></body></html>", None))
        self.line_npedido.setText("")
        self.line_tipovenda.setText("")
        self.line_ordemcompra.setText("")
        self.line_cliente.setText("")
        self.line_prazopgt.setText("")
        self.line_vendedor.setText("")
        self.lb_npedido.setText(QCoreApplication.translate("PedVendaPage", u"NUM PEDIDO", None))
        self.lb_cliente.setText(QCoreApplication.translate("PedVendaPage", u"CLIENTE", None))
        self.lb_tipovenda.setText(QCoreApplication.translate("PedVendaPage", u"TIPO DE VENDA", None))
        self.lb_prazopgt.setText(QCoreApplication.translate("PedVendaPage", u"PRAZO PGT", None))
        self.lb_vendedor.setText(QCoreApplication.translate("PedVendaPage", u"VENDEDOR", None))
        self.lb_ordemcompra.setText(QCoreApplication.translate("PedVendaPage", u"ORDEM DE COMPRA", None))
        self.button_home_2.setText(QCoreApplication.translate("PedVendaPage", u"GRAVAR", None))
        self.button_gnfe.setText(QCoreApplication.translate("PedVendaPage", u"GERAR NFE", None))
        self.exitButton.setText(QCoreApplication.translate("PedVendaPage", u"SAIR", None))
        self.homeTitle.setText(QCoreApplication.translate("PedVendaPage", u"Pedido de Venda", None))
        self.homeButton.setText(QCoreApplication.translate("PedVendaPage", u"HOME", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pedido_window = QMainWindow()
    ui = Ui_PedVendaPage()
    ui.setupUi(pedido_window)
    pedido_window.show()
    sys.exit(app.exec())