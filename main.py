"""
Main file for Public functions
"""
from PySide6.QtWidgets import QMainWindow
from home import Ui_HomePage
from login import Ui_LoginPage

#Function "Validar Login" start
def validarLogin(self, username, password, LoginPage):
    if username == "teste" and password == "teste":
        print("Certa resposta")
        self.homeOpen()
        LoginPage.close()
    else:
        print("Errado, digite novamente :)")
#Function "Validar Login" end