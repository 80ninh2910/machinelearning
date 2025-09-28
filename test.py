from PyQt6.QtWidgets import QApplication
from dataprocessing.MainWindowEx import MainWindowEx

app = QApplication([])
mywindow = MainWindowEx()
mywindow.show()
app.exec()
