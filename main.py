"""
Main file for Public functions
"""
#Function "Validar Login" start
def validarLogin(self, username, password, LoginPage):
    if username == "teste" and password == "teste":
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