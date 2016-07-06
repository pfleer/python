from PySide import QtGui

# from mw_gui import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setMaximumSize(300, 300)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
