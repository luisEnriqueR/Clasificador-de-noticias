import sys 
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TabsWindow(QMainWindow):
	"""docstring for LoadFileWindow"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("ClassifierTabs.ui", self)
		self.setWindowTitle("Clasificación por diarios")
		self.setMinimumSize(550, 250)
		self.setMaximumSize(550, 250)
		self.show()
		qtfont = QFont("Arial", 13, QFont.Bold)
		#self.load_label.setAlignment(Qt.AlignCenter)
		self.label.setFont(qtfont)
		self.prueba_btn.clicked.connect(self.loadFile)

	def loadFile(self):
		print("abrir tabs")
		
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
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			return fileName