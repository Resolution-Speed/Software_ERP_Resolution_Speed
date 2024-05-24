"""
Main file for Public functions
"""
import mysql.connector
#Function "Validar Login" start
def validarLogin(self, username_write, username_sql, password_write, password_sql, LoginPage):
    if username_write == username_sql and password_write == password_sql:
        print("Certa resposta")
        self.homeOpen()
        LoginPage.close()
    else:
        print("Errado, digite novamente :)")
#Function "Validar Login" end

#function abrir tela cadastro
def regProdOpen(self):
    self.regProdOpen()

#Function abrir tela pedido de venda
def pedidoVendaOpen(self):
    self.pedVenOpen()