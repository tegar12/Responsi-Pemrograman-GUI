import sys

from PyQt5 import Qt
from PyQt5.uic import loadUi

class Antri(Qt.QMainWindow):
    B = 0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loadUi("Gui.ui", self) #memanggil gui
        self.Daftar.clicked.connect(self.set) #clik daftar dan memanggil def set
        self.Reset.clicked.connect(self.cuk) #clik daftar dan memanggil def cuk

    def set(self):
        self.B += 1
        lbl = str(self.B) + " " +self.Nama.text()
        cuk = lbl #cuk
        self.Antri.setText(lbl) #set lebel
        self.List.insertItem(self.B, str(cuk)) #menambah list item
        self.Nama.clear()
    def cuk(self):
        self.B = 0
        self.Antri.setText("") #set lebel
        self.List.clear() #menghapus seluruh isi list


app = Qt.QApplication(sys.argv)

watch = Antri()
watch.show()

app.exec_()
