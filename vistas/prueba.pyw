import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from LoadFile import LoadFileWindow
from LoadText import LoadTextWindow
from Classifier import *
import ctypes

"""class LoadFileWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("LoadFile.ui", self)
		self.setWindowTitle("Cargar noticias desde un archivo")
		self.setMaximumSize(500, 300)
		self.show()"""

class Ventana(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("prueba.ui", self)
		self.setWindowTitle("Clasificador de noticias")
		self.setMinimumSize(600, 400)
		self.setMaximumSize(600, 400)
		self.load_news_files_button.clicked.connect(self.openLoadFileWindow)
		self.load_news_text_button.clicked.connect(self.openLoadTextWindow)
		self.open_classifier_button.clicked.connect(self.openClassifierWindow)
		#self.description_label.setAlignment(Qt.Qt.AlignCenter)
		"""qtfont = QFont("Arial", 12, QFont.Bold)
		self.setFont(qtfont)"""

	#eventos que se pueden encontrar en la referencia http://pyqt.sourceforge.net/Docs/PyQt4/qevent.html
	def showEvent(self, event):
		qtfont = QFont("Arial", 12, QFont.Bold)
		self.description_label.setAlignment(Qt.AlignCenter)
		self.description_label.setFont(qtfont)
		self.description_label.setText("Clasificador de noticias de diarios de circulación nacional")

	def closeEvent(self, event):
		resultado = QMessageBox.question(self, "Salir", "¿Desea salir del clasificador?", QMessageBox.Yes | QMessageBox.No)
		if resultado == QMessageBox.Yes: event.accept()
		else: event.ignore()

	def openLoadFileWindow(self):
		self.ui = LoadFileWindow()

	def openLoadTextWindow(self):
		self.ui1 = LoadTextWindow()

	def openClassifierWindow(self):
		self.ui2 = Classifier()

app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()