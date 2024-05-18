import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from assets.screens.home import Ui_HomePage
from assets.screens.login import Ui_LoginPage

#Inicio Funções Pagina Home
class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.ui.homeButton.clicked.connect(self.funcao_teste)

    def funcao_teste(self):
        print("teste")
#Fim Funções Pagina Home

#Inicio Funções Pagina Login
class LoginPage(QMainWindow):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)
#Fim Funções Pagina Login

#Inicio Chamando e exutando Funções
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = HomePage()
    window.show()

    sys.exit(app.exec())
#Fim Chamando e exutando Funções