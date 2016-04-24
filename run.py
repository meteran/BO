#!/usr/bin/python
# coding: utf-8
import sys
from ConfigParser import ConfigParser

from PyQt4 import QtGui, QtCore

from ui.MainWindow import Ui_MainWindow


class App(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, args):
        super(App, self).__init__()

        for arg in args:
            if arg.startswith("--config="):
                config_file = arg[9:]

        self.config = ConfigParser()

        try:
            self.config.read(config_file)
        except:
            self.config.read("config.ini")

        self.setupUi(self)

        self.labels = []
        self.parameters = {}
        for index, param in enumerate(self.config.options("INT_PARAMETERS")):
            self.add_parameter(index, param)
            print self.config.get("INT_PARAMETERS", param)

    def add_parameter(self, index, param):
        label = QtGui.QLabel(self.parameters_box)
        label.setObjectName("label_" + param)
        label.setText(param.replace("_", " ")+":")
        self.parameter_layout.setWidget(index, QtGui.QFormLayout.LabelRole, label)
        self.labels.append(label)
        spin_box = QtGui.QSpinBox(self.parameters_box)
        spin_box.setMaximumSize(QtCore.QSize(70, 16777215))
        spin_box.setObjectName("spin_box_"+param)
        self.parameter_layout.setWidget(index, QtGui.QFormLayout.FieldRole, spin_box)
        self.parameters[param] = spin_box



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = App(sys.argv)
    MainWindow.show()
    sys.exit(app.exec_())
