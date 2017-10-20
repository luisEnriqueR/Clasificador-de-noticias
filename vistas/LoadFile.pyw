import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

class LoadFileWindow(QMainWindow):
	"""docstring for LoadFileWindow"""
	def __init__(self, arg):
		QMainWindow.__init__(self)
		self.arg = arg
		uic.loadUi("LoadFile.ui", self)
		self.setWindowTitle("Cargar noticias desde un archivo")
		self.setMaximumSize(500, 300)

app = QApplication(sys.argv)
_ventana = LoadFileWindow()
#_ventana.show()
app.exec_()