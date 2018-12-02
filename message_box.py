"""
author: Rafal Miecznik
contact: ravmiecznk@gmail.com
"""

from PyQt4.QtGui import QMessageBox
from PyQt4 import QtCore, QtGui
import sys


class WarningBox(QMessageBox):
    def __init__(self, msg, title='Warning', detailed_msg='', parent=None):
        #super(WarningBox, self).__init__(parent=parent)
        QMessageBox.__init__(self, parent=parent)
        self.setIcon(self.Warning)
        self.setText(msg)
        self.setStandardButtons(self.Ok)
        self.btn = self.Ok
        self.setDetailedText(detailed_msg)
        self.setWindowTitle(title)
        self.move(0, 0)
        #self.exec_()

    def get_clicked(self):
        return self.clickedButton()

    def mousePressEvent(self, QMouseEvent):
        print "wb", QMouseEvent.pos()