#!/usr/bin/python
# coding: utf-8
import sys
from ConfigParser import ConfigParser

from PyQt4 import QtGui, QtCore

from ui.MainWindow import Ui_MainWindow


# noinspection PyCallByClass
class App(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, args):
        super(App, self).__init__()

        self.input_file = ''
        self.output_file = ''

        self.read_config(args)
        self.setupUi(self)
        self.setup_parameters()
        self.connect_signals()

    def connect_signals(self):
        self.find_input.pressed.connect(
            lambda: self.input_file_edit.setText(QtGui.QFileDialog.getOpenFileName(self, "Input File")))
        self.find_output.pressed.connect(
            lambda: self.output_file_edit.setText(QtGui.QFileDialog.getSaveFileName(self, "Output File")))
        self.input_file_edit.textChanged.connect(self.files_edited)
        self.output_file_edit.textChanged.connect(self.files_edited)
        self.start_computing_button.pressed.connect(self.start_computing)
        self.stop_computing_button.pressed.connect(self.stop_computing)

    def sleep_progressbar(self, progress):
        if self.go and progress <= 100:
            self.progress_bar.setValue(progress)
            QtCore.QTimer.singleShot(100, lambda: self.sleep_progressbar(progress+1))
        else:
            self.progress_bar.setValue(0)

    def start_computing(self):
        self.go = True
        self.sleep_progressbar(1)

    def stop_computing(self):
        self.go = False

    def files_edited(self):
        self.input_file = str(self.input_file_edit.text())
        self.output_file = str(self.output_file_edit.text())
        self.computing_box.setEnabled(bool(self.input_file and self.output_file))

    def setup_parameters(self):
        self.labels = []
        self.parameters = {}
        for index, param in enumerate(self.config.options("INT_PARAMETERS")):
            self.add_parameter(index, param)

    def read_config(self, args):
        for arg in args:
            if arg.startswith("--config="):
                config_file = arg[9:]
        self.config = ConfigParser()
        try:
            self.config.read(config_file)
        except:
            self.config.read("config.ini")

    def add_parameter(self, index, param):
        label = QtGui.QLabel(self.parameters_box)
        label.setObjectName("label_" + param)
        label.setText(param.replace("_", " ") + ":")
        self.parameter_layout.setWidget(index, QtGui.QFormLayout.LabelRole, label)
        self.labels.append(label)
        spin_box = QtGui.QSpinBox(self.parameters_box)
        spin_box.setMaximumSize(QtCore.QSize(100, 16777215))
        spin_box.setObjectName("spin_box_" + param)
        spin_box.setMaximum(100000)
        spin_box.setMinimum(1)
        spin_box.setValue(int(self.config.get("INT_PARAMETERS", param)))
        self.parameter_layout.setWidget(index, QtGui.QFormLayout.FieldRole, spin_box)
        self.parameters[param] = spin_box


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = App(sys.argv)
    MainWindow.show()
    sys.exit(app.exec_())
