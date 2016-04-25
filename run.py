#!/usr/bin/python
# coding: utf-8
import sys
from ConfigParser import ConfigParser

from PyQt4 import QtGui, QtCore

from optimizer.optimizer import BeesAlgorithm
from ui.MainWindow import Ui_MainWindow


# noinspection PyCallByClass
from utils.data_loader import load_data_from_file


class App(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, args):
        super(App, self).__init__()

        self.input_file = ''
        self.output_file = ''

        self.read_config(args)
        self.setupUi(self)
        self.setup_parameters()
        self.connect_signals()

        self.problem = None
        self.algorithm = None

        self.input_file_edit.setText(self.config.get("FILES", "input"))
        self.output_file_edit.setText(self.config.get("FILES", "output"))

    def connect_signals(self):
        self.find_input.pressed.connect(
            lambda: self.input_file_edit.setText(QtGui.QFileDialog.getOpenFileName(self, "Input File")))
        self.find_output.pressed.connect(
            lambda: self.output_file_edit.setText(QtGui.QFileDialog.getSaveFileName(self, "Output File")))
        self.input_file_edit.textChanged.connect(self.files_edited)
        self.output_file_edit.textChanged.connect(self.files_edited)
        self.start_computing_button.pressed.connect(self.start_computing)
        self.cancel_computing_button.pressed.connect(self.cancel_computing)

    def sleep_progressbar(self, progress):
        if self.go and progress <= 100:
            self.progress_bar.setValue(progress)
            QtCore.QTimer.singleShot(100, lambda: self.sleep_progressbar(progress + 1))
        else:
            self.progress_bar.setValue(0)

    def create_problem(self):
        params = {k: v.getValue() for (k, v) in self.parameters.items()}
        data = load_data_from_file(self.input_file)
        self.algorithm = BeesAlgorithm(data, **params)
        self.problem = self.algorithm.get_problem()

    def start_computing(self):
        if not self.problem:
            try:
                self.create_problem()
                open(self.output_file, 'w').close()
                self.parameters_box.setEnabled(False)
                self.files_box.setEnabled(False)
            except:
                return

        self.start_computing_button.setEnabled(False)
        self.cancel_computing_button.setEnabled(True)
        self.pause_computing_button.setEnabled(True)

        self.canceled = False
        self.paused = False
        self.algorithm_runner()
        self.start_computing_button.setEnabled(True)
        self.pause_computing_button.setEnabled(False)

        if not (self.canceled or self.paused):
            self.save_solution()

    def save_solution(self):
        pass

    def algorithm_runner(self):
        for progress in self.problem:
            self.progress_bar.setValue(progress + 1)
            if self.canceled:
                break
            if self.paused:
                return
        self.clear_problem()

    def clear_problem(self):
        self.progress_bar.setValue(0)
        self.problem = None
        self.algorithm = None
        self.files_box.setEnabled(True)
        self.parameters_box.setEnabled(True)

    def pause_computing(self):
        self.paused = True

    def cancel_computing(self):
        self.canceled = True
        self.cancel_computing_button.setEnabled(False)
        if self.paused:
            self.clear_problem()

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
