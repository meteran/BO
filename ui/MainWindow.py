# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(537, 274)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.files_box = QtGui.QGroupBox(self.centralwidget)
        self.files_box.setMaximumSize(QtCore.QSize(16777215, 79))
        self.files_box.setObjectName(_fromUtf8("files_box"))
        self.formLayout = QtGui.QFormLayout(self.files_box)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.files_box)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.splitter_4 = QtGui.QSplitter(self.files_box)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.input_file_edit = QtGui.QLineEdit(self.splitter_4)
        self.input_file_edit.setObjectName(_fromUtf8("input_file_edit"))
        self.find_input = QtGui.QToolButton(self.splitter_4)
        self.find_input.setMaximumSize(QtCore.QSize(30, 16777215))
        self.find_input.setObjectName(_fromUtf8("find_input"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.splitter_4)
        self.label_2 = QtGui.QLabel(self.files_box)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.splitter_2 = QtGui.QSplitter(self.files_box)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.output_file_edit = QtGui.QLineEdit(self.splitter_2)
        self.output_file_edit.setObjectName(_fromUtf8("output_file_edit"))
        self.find_output = QtGui.QToolButton(self.splitter_2)
        self.find_output.setMaximumSize(QtCore.QSize(30, 16777215))
        self.find_output.setObjectName(_fromUtf8("find_output"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.splitter_2)
        self.gridLayout_2.addWidget(self.files_box, 2, 0, 1, 1)
        self.parameters_box = QtGui.QGroupBox(self.centralwidget)
        self.parameters_box.setMaximumSize(QtCore.QSize(150, 16777215))
        self.parameters_box.setObjectName(_fromUtf8("parameters_box"))
        self.parameter_layout = QtGui.QFormLayout(self.parameters_box)
        self.parameter_layout.setObjectName(_fromUtf8("parameter_layout"))
        self.gridLayout_2.addWidget(self.parameters_box, 1, 0, 1, 1)
        self.computing_box = QtGui.QGroupBox(self.centralwidget)
        self.computing_box.setEnabled(False)
        self.computing_box.setMaximumSize(QtCore.QSize(16777215, 85))
        self.computing_box.setObjectName(_fromUtf8("computing_box"))
        self.gridLayout = QtGui.QGridLayout(self.computing_box)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.computing_box)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_7 = QtGui.QLabel(self.splitter)
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.progress_bar = QtGui.QProgressBar(self.splitter)
        self.progress_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_3 = QtGui.QSplitter(self.computing_box)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.start_computing_button = QtGui.QPushButton(self.splitter_3)
        self.start_computing_button.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_computing_button.setFont(font)
        self.start_computing_button.setObjectName(_fromUtf8("start_computing_button"))
        self.pause_computing_button = QtGui.QPushButton(self.splitter_3)
        self.pause_computing_button.setEnabled(False)
        self.pause_computing_button.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pause_computing_button.setFont(font)
        self.pause_computing_button.setObjectName(_fromUtf8("pause_computing_button"))
        self.cancel_computing_button = QtGui.QPushButton(self.splitter_3)
        self.cancel_computing_button.setEnabled(False)
        self.cancel_computing_button.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel_computing_button.setFont(font)
        self.cancel_computing_button.setObjectName(_fromUtf8("cancel_computing_button"))
        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.computing_box, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.files_box.setTitle(_translate("MainWindow", "Files", None))
        self.label.setText(_translate("MainWindow", "input file:", None))
        self.find_input.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "output file:", None))
        self.find_output.setText(_translate("MainWindow", "...", None))
        self.parameters_box.setTitle(_translate("MainWindow", "Parameters", None))
        self.computing_box.setTitle(_translate("MainWindow", "Computing", None))
        self.label_7.setText(_translate("MainWindow", "progress:", None))
        self.start_computing_button.setText(_translate("MainWindow", "start", None))
        self.pause_computing_button.setText(_translate("MainWindow", "pause", None))
        self.cancel_computing_button.setText(_translate("MainWindow", "cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

