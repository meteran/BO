#!/usr/bin/python
# coding: utf-8
from PyQt4.QtCore import QThread, pyqtSignal


class Thread(QThread):
    computing_finished = pyqtSignal()
    change_progress = pyqtSignal(int)

    def __init__(self, problem):
        QThread.__init__(self)
        self.problem = problem
        self.canceled = False
        self.paused = False

    def run(self):
        for progress in self.problem:
            print progress
            self.change_progress.emit(progress+1)
            if self.canceled:
                break
            if self.paused:
                return
        self.computing_finished.emit()

    def pause(self):
        self.paused = True

    def cancel(self):
        self.canceled = True
