# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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
        MainWindow.resize(537, 268)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 85))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.groupBox_3)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_7 = QtGui.QLabel(self.splitter)
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.progress_bar = QtGui.QProgressBar(self.splitter)
        self.progress_bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_3 = QtGui.QSplitter(self.groupBox_3)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.start_computing = QtGui.QPushButton(self.splitter_3)
        self.start_computing.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.start_computing.setFont(font)
        self.start_computing.setObjectName(_fromUtf8("start_computing"))
        self.stop_computing = QtGui.QPushButton(self.splitter_3)
        self.stop_computing.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stop_computing.setFont(font)
        self.stop_computing.setObjectName(_fromUtf8("stop_computing"))
        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.parameters_box = QtGui.QGroupBox(self.centralwidget)
        self.parameters_box.setMaximumSize(QtCore.QSize(135, 16777215))
        self.parameters_box.setObjectName(_fromUtf8("parameters_box"))
        self.parameter_layout = QtGui.QFormLayout(self.parameters_box)
        self.parameter_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.parameter_layout.setObjectName(_fromUtf8("parameter_layout"))
        self.gridLayout_2.addWidget(self.parameters_box, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 79))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.splitter_4 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.input_file = QtGui.QLineEdit(self.splitter_4)
        self.input_file.setObjectName(_fromUtf8("input_file"))
        self.find_input = QtGui.QToolButton(self.splitter_4)
        self.find_input.setMaximumSize(QtCore.QSize(30, 16777215))
        self.find_input.setObjectName(_fromUtf8("find_input"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.splitter_4)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.splitter_2 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.output_file = QtGui.QLineEdit(self.splitter_2)
        self.output_file.setObjectName(_fromUtf8("output_file"))
        self.find_output = QtGui.QToolButton(self.splitter_2)
        self.find_output.setMaximumSize(QtCore.QSize(30, 16777215))
        self.find_output.setObjectName(_fromUtf8("find_output"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.splitter_2)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)
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
        self.groupBox_3.setTitle(_translate("MainWindow", "Computing", None))
        self.label_7.setText(_translate("MainWindow", "progress:", None))
        self.start_computing.setText(_translate("MainWindow", "start", None))
        self.stop_computing.setText(_translate("MainWindow", "stop", None))
        self.parameters_box.setTitle(_translate("MainWindow", "Parameters", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Files", None))
        self.label.setText(_translate("MainWindow", "input file:", None))
        self.find_input.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "output file:", None))
        self.find_output.setText(_translate("MainWindow", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

