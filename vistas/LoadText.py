import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

class LoadTextWindow(QMainWindow):
	"""docstring for LoadFileWindow"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("LoadText.ui", self)
		self.setWindowTitle("Cargar noticias desde texto")
		self.setMinimumSize(700, 500)
		self.setMaximumSize(700, 500)
		self.show()
		qtfont = QFont("Arial", 13, QFont.Bold)
		self.load_label.setAlignment(Qt.AlignCenter)
		self.load_label.setFont(qtfont)