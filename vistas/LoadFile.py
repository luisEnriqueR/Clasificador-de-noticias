import sys 
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Preprocesamiento.tokenizaNoticias import tokenizar
from Preprocesamiento.lematizaNoticias import lematizar

class LoadFileWindow(QMainWindow):
	"""docstring for LoadFileWindow"""
	nombre = " "
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("LoadFile.ui", self)
		self.setWindowTitle("Cargar noticias desde un archivo")
		self.setMinimumSize(550, 250)
		self.setMaximumSize(550, 250)
		self.show()
		qtfont = QFont("Arial", 13, QFont.Bold)
		self.load_label.setAlignment(Qt.AlignCenter)
		self.load_label.setFont(qtfont)
		self.load_file_button.clicked.connect(self.loadFile)

	def loadFile(self):
		print("cargar archivo")
		dialog = LoadFileWidget()
		nombre = dialog.openFileDialog()
		self.file_name_label.setText(nombre)
		
class LoadFileWidget(QWidget):
	def __init__(self):
		super().__init__()
		print("en la clase de carga")
		self.setWindowTitle("Selecciona tu archivo...")
		self.setGeometry(10, 10, 640, 400)
		self.show()
		"""nombre = self.openFileDialog()
		if nombre:
			print(nombre)"""

	def openFileDialog(self):
		print("umm...")
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"Seleccion la(s) noticias", "/Documentos/","Text files (*.txt)", options=options)
		if fileName:
			return fileName