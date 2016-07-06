from PySide import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle('Template GUI')
        self.setFixedSize(500, 500)

        # make a central widget
        self.centralWidget = QtGui.QWidget(self)

        # attach widget to the PyQt window
        self.setCentralWidget(self.centralWidget)

        # initialise UI specifics
        self.initUI()

    def initUI(self):
        return


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())


mainwindow = MainWindow()
mainwindow.show()