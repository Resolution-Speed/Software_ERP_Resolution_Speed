import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from assets.screens.home import Ui_HomePage
from assets.screens.login import Ui_LoginPage
from assets.screens.cadastro_produto import Ui_RegProductPage
from assets.screens.pedido_venda import Ui_PedVendaPage

def MainExitPage(self):
    self.ui = Ui_LoginPage()
    self.ui.setupUi(self)

def MainHomePage(self):
    self.ui = Ui_HomePage()
    self.ui.setupUi(self)

#Inicio Classe Pagina Home
class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.ui.homeButton.clicked.connect(self.openHomePage)
        self.ui.exitButton.clicked.connect(self.exitHomePage)
        self.ui.homeButton_cad_prod.clicked.connect(self.openRegProd)
        self.ui.homeButton_ped_ven.clicked.connect(self.openPedVenda)

    def openHomePage(self):
        MainHomePage(self)

    #Função para sair da página e voltar ao Login
    def exitHomePage(self):
        MainExitPage(self)

    #Função para abrir tela "cadastro de produto"
    def openRegProd(self):
        self.ui = Ui_RegProductPage()
        self.ui.setupUi(self)

    #Função para abrir tela "cadastro de produto"
    def openPedVenda(self):
        self.ui = Ui_PedVendaPage()
        self.ui.setupUi(self)
#Fim Classe Pagina Home

#Inicio Chamando e exutando Funções
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()

    sys.exit(app.exec())
#Fim Chamando e exutando Funções