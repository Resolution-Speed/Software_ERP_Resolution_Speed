from PyQt5 import uic, QtWidgets

def main_function():
    print("teste")

app=QtWidgets.QApplication([])
home = uic.loadUi("assets/screens/HOME.ui")

home.show()
app.exec()