"""
author: Rafal Miecznik
contact: ravmiecznk@gmail.com
"""

import sys
sys.path.append('../my_thread')
sys.path.append('../qt_thread')
import pytest
from message_box import WarningBox
from PyQt4.QtTest import QTest
from PyQt4 import QtCore, QtGui
from pynput.mouse import Controller, Button
from my_thread import MyThread

def left_click():
    mouse = Controller()
    mouse.click(Button.left, 1)

@pytest.fixture(scope='module')
def warning_box():
    app = QtGui.QApplication(sys.argv)
    wb = WarningBox("test")
    yield wb
    try:
        sys.exit(0)
    except:
        pass


def test_warningbox_ok_clicked(warning_box):
    QTest.mouseMove(warning_box, pos=QtCore.QPoint(54, 85))
    click_thread = MyThread(process=left_click, delay=0.5)
    click_thread.start()
    clicked_key = warning_box.exec_()
    click_thread.get_result(timeout=1)
    assert clicked_key == WarningBox.Ok

def test_warningbox_add_button_cancel_clicked(warning_box):
    warning_box.addButton(WarningBox.Cancel)
    QTest.mouseMove(warning_box, pos=QtCore.QPoint(130, 85))
    click_thread = MyThread(process=left_click, delay=0.5)
    click_thread.start()
    clicked_key = warning_box.exec_()
    click_thread.get_result(timeout=1)
    assert clicked_key == WarningBox.Cancel

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw = WarningBox("test")
    r = mw.exec_()
    print r
    sys.exit(0)
    sys.exit(app.exec_())
    print "bye"