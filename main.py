import sys

from PyQt5.QtWidgets import *


class MDEVWord(QMainWindow):
    def __init__(self):
        super(MDEVWord, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)


app = QApplication(sys.argv)

window = MDEVWord()
window.show()
sys.exit(app.exec_())
