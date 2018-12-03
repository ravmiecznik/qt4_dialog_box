"""
author: Rafal Miecznik
contact: ravmiecznk@gmail.com
"""

from PyQt4.QtGui import QMessageBox
from PyQt4 import QtCore, QtGui
import sys


class WarningBox(QMessageBox):
    def __init__(self, msg, title='Warning', detailed_msg='', parent=None, pos=None):
        QMessageBox.__init__(self, parent=parent)
        self.setIcon(self.Warning)
        self.setText(msg)
        self.setStandardButtons(self.Ok)
        self.setDetailedText(detailed_msg)
        self.setWindowTitle(title)
        if pos:
            self.move(*pos)

    def mousePressEvent(self, QMouseEvent):
        print "{}: Mouse clicked at:{}".format(__name__, QMouseEvent.pos())