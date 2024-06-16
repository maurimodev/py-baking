import PyQt5.QtWidgets as qtw
import sys


class MyWindow(qtw.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("this is my new QT window :)")
        self.initUI()

    def initUI(self):
        # labels are made with QtWidgets
        self.label = qtw.QLabel(self)
        self.label.setText("this is a fun nice label! :D")
        self.label.move(50, 50)

        self.b1 = qtw.QPushButton(self)
        self.b1.setText("Click me now!")
        self.b1.clicked.connect(self.clicked)

        self.updateLabelSize()

    def clicked(self):
        self.label.setText("Oh! I've been clicked!")
        self.updateLabelSize()

    def updateLabelSize(self):
        self.label.adjustSize()


def window():
    app = qtw.QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
