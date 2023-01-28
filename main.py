import sys

from PyQt5.QtWidgets import *

class MDEVWord(QMainWindow):
    def __int__(self):
        super().__int__()

app=QApplication(sys.argv)

window=MDEVWord()
window.show()
sys.exit(app.exec_())
