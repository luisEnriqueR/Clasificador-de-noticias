import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from Preprocesamiento.tokenizaNoticias import tokenizar
from Preprocesamiento.lematizaNoticias import lematizar

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
		self.add_new.clicked.connect(self.loadNew)

	def loadNew(self):
		output_file = open('/home/salida.txt', 'w')
		temp_file = open('/home/temp.txt', 'w')
		text = self.textEdit.toPlainText()
		temp_file.write(text)
		temp_file.close()
		myfile = open('/home/temp.txt', 'r')
		for line in myfile:
			print(line)
			if len(line) > 1:
				line2 = lematizar(tokenizar(line))
				output_file.write(line2)
				output_file.write("\n")
		output_file.close()
		self.loaded_label.setText("Texto cargado")
		#print(text)
		"""for content in text:
			print(content)
			if len(content) > 1:
				#print(content)
				line2 = lematizar(tokenizar(content))
				output_file.write(line2)
				output_file.write("\n")
				documents_counter += 1
		output_file.close()"""