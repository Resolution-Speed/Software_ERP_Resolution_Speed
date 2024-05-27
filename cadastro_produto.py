# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_produto.ui'
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

class Ui_RegProductPage(object):
    def setupUi(self, RegProductPage):
        if not RegProductPage.objectName():
            RegProductPage.setObjectName(u"RegProductPage")
        RegProductPage.resize(600, 530)
        RegProductPage.setMinimumSize(QSize(600, 530))
        RegProductPage.setMaximumSize(QSize(600, 530))
        RegProductPage.setStyleSheet(u"background-color: #fff;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(RegProductPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.embrulho = QGraphicsView(self.centralwidget)
        self.embrulho.setObjectName(u"embrulho")
        self.embrulho.setGeometry(QRect(60, 70, 486, 429))
        self.embrulho.setStyleSheet(u"border: 5px solid rgb(93,215,241);\n"
"\n"
"border-radius:10px;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(60, 70, 207, 27))
        self.textBrowser.setStyleSheet(u"background-color:#5DD7F1;\n"
"\n"
"border: nome;\n"
"\n"
"color: #fff;\n"
"\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"border-top-left-radius: 10px;")
        self.codigo = QLabel(self.centralwidget)
        self.codigo.setObjectName(u"codigo")
        self.codigo.setGeometry(QRect(80, 130, 47, 13))
        font = QFont()
        font.setBold(True)
        self.codigo.setFont(font)
        self.unidade = QLabel(self.centralwidget)
        self.unidade.setObjectName(u"unidade")
        self.unidade.setGeometry(QRect(80, 180, 61, 16))
        self.unidade.setFont(font)
        self.ncm_nbm = QLabel(self.centralwidget)
        self.ncm_nbm.setObjectName(u"ncm_nbm")
        self.ncm_nbm.setGeometry(QRect(210, 130, 61, 16))
        self.ncm_nbm.setFont(font)
        self.nome_produto = QLabel(self.centralwidget)
        self.nome_produto.setObjectName(u"nome_produto")
        self.nome_produto.setGeometry(QRect(350, 130, 131, 16))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        self.nome_produto.setFont(font1)
        self.nome_produto.setStyleSheet(u"")
        self.comprimento = QLabel(self.centralwidget)
        self.comprimento.setObjectName(u"comprimento")
        self.comprimento.setGeometry(QRect(80, 240, 91, 16))
        self.comprimento.setFont(font)
        self.largura = QLabel(self.centralwidget)
        self.largura.setObjectName(u"largura")
        self.largura.setGeometry(QRect(390, 240, 61, 16))
        self.largura.setFont(font)
        self.altura = QLabel(self.centralwidget)
        self.altura.setObjectName(u"altura")
        self.altura.setGeometry(QRect(230, 240, 47, 13))
        self.altura.setFont(font)
        self.fornecedor = QLabel(self.centralwidget)
        self.fornecedor.setObjectName(u"fornecedor")
        self.fornecedor.setGeometry(QRect(80, 300, 81, 16))
        self.fornecedor.setFont(font)
        self.preso_bruto = QLabel(self.centralwidget)
        self.preso_bruto.setObjectName(u"preso_bruto")
        self.preso_bruto.setGeometry(QRect(420, 180, 81, 16))
        self.preso_bruto.setFont(font)
        self.peso_liquido = QLabel(self.centralwidget)
        self.peso_liquido.setObjectName(u"peso_liquido")
        self.peso_liquido.setGeometry(QRect(300, 180, 81, 16))
        self.peso_liquido.setFont(font)
        self.Especie = QLabel(self.centralwidget)
        self.Especie.setObjectName(u"Especie")
        self.Especie.setGeometry(QRect(170, 180, 47, 13))
        self.Especie.setFont(font)
        self.preco_de_custo = QLabel(self.centralwidget)
        self.preco_de_custo.setObjectName(u"preco_de_custo")
        self.preco_de_custo.setGeometry(QRect(230, 300, 101, 16))
        self.preco_de_custo.setFont(font)
        self.btn_cadastro = QPushButton(self.centralwidget)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setGeometry(QRect(230, 410, 121, 31))
        self.btn_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro.setStyleSheet(u"QPushButton\n"
"{\n"
"    background-color: rgb(93, 215, 241); \n"
"    border: 1px solid rgb(93, 215, 241);\n"
"    border-radius: 5px;\n"
"    font-size: 10px;    \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #fff;\n"
"    color : rgb(93, 215, 241); ;\n"
"}")
        self.wrapperHeader = QGraphicsView(self.centralwidget)
        self.wrapperHeader.setObjectName(u"wrapperHeader")
        self.wrapperHeader.setGeometry(QRect(0, 0, 601, 50))
        self.wrapperHeader.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 10, 105, 31))
        font2 = QFont()
        self.homeButton.setFont(font2)
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
        self.homeTitle = QLabel(self.centralwidget)
        self.homeTitle.setObjectName(u"homeTitle")
        self.homeTitle.setGeometry(QRect(230, 10, 141, 31))
        self.homeTitle.setStyleSheet(u"background-color: transparent;\n"
"color: #fff;\n"
"font-size: 15px")
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
        self.prod_cod = QLineEdit(self.centralwidget)
        self.prod_cod.setObjectName(u"prod_cod")
        self.prod_cod.setMaxLength(4)
        self.prod_cod.setGeometry(QRect(80, 150, 100, 25))
        self.prod_nbmncm = QLineEdit(self.centralwidget)
        self.prod_nbmncm.setObjectName(u"prod_nbmncm")
        self.prod_nbmncm.setMaxLength(8)
        self.prod_nbmncm.setGeometry(QRect(210, 150, 100, 25))
        self.prod_descricao = QLineEdit(self.centralwidget)
        self.prod_descricao.setObjectName(u"prod_descricao")
        self.prod_descricao.setMaxLength(80)
        self.prod_descricao.setGeometry(QRect(350, 150, 171, 25))
        self.prod_unidade = QLineEdit(self.centralwidget)
        self.prod_unidade.setObjectName(u"prod_unidade")
        self.prod_unidade.setMaxLength(4)
        self.prod_unidade.setGeometry(QRect(80, 200, 51, 25))
        self.prod_especie = QLineEdit(self.centralwidget)
        self.prod_especie.setMaxLength(1)
        self.prod_especie.setObjectName(u"prod_especie")
        self.prod_especie.setGeometry(QRect(170, 200, 100, 25))
        self.prod_pesoL = QLineEdit(self.centralwidget)
        self.prod_pesoL.setObjectName(u"prod_pesoL")
        self.prod_pesoL.setMaxLength(10)
        self.prod_pesoL.setGeometry(QRect(300, 200, 100, 25))
        self.prod_pesoB = QLineEdit(self.centralwidget)
        self.prod_pesoB.setObjectName(u"prod_pesoB")
        self.prod_pesoB.setMaxLength(10)
        self.prod_pesoB.setGeometry(QRect(420, 200, 100, 25))
        self.prod_comprimento = QLineEdit(self.centralwidget)
        self.prod_comprimento.setObjectName(u"prod_comprimento")
        self.prod_comprimento.setMaxLength(10)
        self.prod_comprimento.setGeometry(QRect(80, 260, 100, 25))
        self.prod_altura = QLineEdit(self.centralwidget)
        self.prod_altura.setObjectName(u"prod_altura")
        self.prod_altura.setMaxLength(5)
        self.prod_altura.setGeometry(QRect(230, 260, 100, 25))
        self.prod_largura = QLineEdit(self.centralwidget)
        self.prod_largura.setObjectName(u"prod_largura")
        self.prod_largura.setMaxLength(5)
        self.prod_largura.setGeometry(QRect(390, 260, 100, 25))
        self.prod_precoCusto = QLineEdit(self.centralwidget)
        self.prod_precoCusto.setObjectName(u"prod_precoCusto")
        self.prod_precoCusto.setMaxLength(10)
        self.prod_precoCusto.setGeometry(QRect(230, 320, 100, 25))
        self.prod_fornecedor = QLineEdit(self.centralwidget)
        self.prod_fornecedor.setObjectName(u"prod_fornecedor")
        self.prod_fornecedor.setGeometry(QRect(80, 320, 100, 25))
        RegProductPage.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.homeButton, self.exitButton)
        QWidget.setTabOrder(self.exitButton, self.prod_cod)
        QWidget.setTabOrder(self.prod_cod, self.prod_nbmncm)
        QWidget.setTabOrder(self.prod_nbmncm, self.prod_descricao)
        QWidget.setTabOrder(self.prod_descricao, self.prod_unidade)
        QWidget.setTabOrder(self.prod_unidade, self.prod_especie)
        QWidget.setTabOrder(self.prod_especie, self.prod_pesoL)
        QWidget.setTabOrder(self.prod_pesoL, self.prod_pesoB)
        QWidget.setTabOrder(self.prod_pesoB, self.prod_comprimento)
        QWidget.setTabOrder(self.prod_comprimento, self.prod_altura)
        QWidget.setTabOrder(self.prod_altura, self.prod_largura)
        QWidget.setTabOrder(self.prod_largura, self.prod_fornecedor)
        QWidget.setTabOrder(self.prod_fornecedor, self.prod_precoCusto)
        QWidget.setTabOrder(self.prod_precoCusto, self.btn_cadastro)
        QWidget.setTabOrder(self.btn_cadastro, self.wrapperHeader)
        QWidget.setTabOrder(self.wrapperHeader, self.textBrowser)
        QWidget.setTabOrder(self.textBrowser, self.embrulho)

        self.retranslateUi(RegProductPage)

        QMetaObject.connectSlotsByName(RegProductPage)

        def resetFields():
            self.prod_cod.setText("")
            self.prod_nbmncm.setText("")
            self.prod_descricao.setText("")
            self.prod_unidade.setText("")
            self.prod_especie.setText("")
            self.prod_pesoL.setText("")
            self.prod_pesoB.setText("")
            self.prod_comprimento.setText("")
            self.prod_altura.setText("")
            self.prod_largura.setText("")
            self.prod_fornecedor.setText("")
            self.prod_precoCusto.setText("")

        #Inicio conexão com banco de dados  
        banco = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="erp_resolution_speed"
        )
        #Fim conexão com banco de dados

        def registerAction():
        #Inicio declarando valores de entrada
            codWrited = self.prod_cod.text()
            ncmNbmWrited = self.prod_nbmncm.text()
            descWrited = self.prod_descricao.text()
            unidWrited = self.prod_unidade.text()
            especieWrited = self.prod_especie.text()
            pesoLiqWrited = self.prod_pesoL.text()
            pesoBruWrited = self.prod_pesoB.text()
            comprimentoWrited = self.prod_comprimento.text()
            alturaWrited = self.prod_altura.text()
            larguraWrited = self.prod_largura.text()
            fornecedorWrited = self.prod_fornecedor.text()
            precoCustoWrited = self.prod_precoCusto.text()
            #Fim declarando valores de entrada

            cursor = banco.cursor()
            comandoSQL = "INSERT INTO produto (codigoProduto, ncm_nbm, nomeProduto, unidade, especie, pesoLiquido, pesoBruto, alturaProduto, larguraProduto, comprimentoProduto, fornecedorProduto, preco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            dados = (str(codWrited), str(ncmNbmWrited), str(descWrited), str(unidWrited), str(especieWrited), str(pesoLiqWrited), str(pesoBruWrited), str(alturaWrited), str(larguraWrited), str(comprimentoWrited), str(fornecedorWrited), str(precoCustoWrited))

            cursor.execute(comandoSQL, dados)
            banco.commit()
            print(dados)
            resetFields()

        def exitWindow():
             RegProductPage.close()

        self.homeButton.clicked.connect(exitWindow)
        self.exitButton.clicked.connect(exitWindow)
        self.btn_cadastro.clicked.connect(registerAction)
    # setupUi

    def retranslateUi(self, RegProductPage):
        RegProductPage.setWindowTitle(QCoreApplication.translate("RegProductPage", u"Cadastro de Produto", None))
        self.textBrowser.setHtml(QCoreApplication.translate("RegProductPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">CADASTRO DE PRODUTO</span></p></body></html>", None))
        self.codigo.setText(QCoreApplication.translate("RegProductPage", u"C\u00d3DIGO", None))
        self.unidade.setText(QCoreApplication.translate("RegProductPage", u"UNIDADE", None))
        self.ncm_nbm.setText(QCoreApplication.translate("RegProductPage", u"NCM/NBM", None))
        self.nome_produto.setText(QCoreApplication.translate("RegProductPage", u"DESCRI\u00c7\u00c3O/NOME", None))
        self.comprimento.setText(QCoreApplication.translate("RegProductPage", u"COMPRIMENTO", None))
        self.largura.setText(QCoreApplication.translate("RegProductPage", u"LARGURA", None))
        self.altura.setText(QCoreApplication.translate("RegProductPage", u"ALTURA", None))
        self.fornecedor.setText(QCoreApplication.translate("RegProductPage", u"FORNECEDOR", None))
        self.preso_bruto.setText(QCoreApplication.translate("RegProductPage", u"PESO BRUTO", None))
        self.peso_liquido.setText(QCoreApplication.translate("RegProductPage", u"PESO LIQUIDO", None))
        self.Especie.setText(QCoreApplication.translate("RegProductPage", u"ESP\u00c9CIE", None))
        self.preco_de_custo.setText(QCoreApplication.translate("RegProductPage", u"PRE\u00c7O DE CUSTO", None))
        self.btn_cadastro.setText(QCoreApplication.translate("RegProductPage", u"CADASTRAR", None))
        self.homeButton.setText(QCoreApplication.translate("RegProductPage", u"HOME", None))
        self.homeTitle.setText(QCoreApplication.translate("RegProductPage", u"RESOLUTION SPEED", None))
        self.exitButton.setText(QCoreApplication.translate("RegProductPage", u"SAIR", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    product_window = QMainWindow()
    ui = Ui_RegProductPage()
    ui.setupUi(product_window)
    product_window.show()
    sys.exit(app.exec())

