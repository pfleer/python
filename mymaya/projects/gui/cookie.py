from PySide import QtGui, QtCore
import os
import maya.cmds as mc


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle('Cucoloris Light Rig')
        self.setFixedSize(200, 400)

        # make a central widget
        self.centralWidget = QtGui.QWidget(self)

        # attach widget to the PyQt window
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QtGui.QVBoxLayout(self.centralWidget)

        # initialise UI specifics
        self.initUI()

    def initUI(self):

        comboBox = QtGui.QComboBox()
        # comboBox.set
        # set directory for cookie images
        directory = mc.internalVar(uad=True) + "scripts/assets/cookie/"
        # save list of images in directory
        images = os.listdir(directory)
        # remove DS_Store
        images.pop(0)
        # populate combo box with image names
        comboBox.addItems(images)
        self.mainLayout.addWidget(comboBox)

        # make image preview area

        # make a create button
        create_btn = QtGui.QPushButton("Create")

        # connect button's click slot to create_cookie method
        create_btn.clicked.connect(self.create_cookie)

        # add the button to the main layout
        self.mainLayout.addWidget(create_btn)

        # make a create button
        replace_btn = QtGui.QPushButton("Replace")

        # connect button's click slot to create_cookie method
        replace_btn.clicked.connect(self.replace_cookie)

        # add the button to the main layout
        self.mainLayout.addWidget(replace_btn)

    def create_cookie(self):
        print 'Creating'

    def replace_cookie(self):
        print 'Replacing'


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

mainwindow = MainWindow()
mainwindow.show()