import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, a0):
        qp = QPainter()
        qp.begin(self)
        diameter = random.randint(30, 300)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(10, 10, diameter, diameter)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())