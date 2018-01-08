
from PyQt4 import QtCore, QtGui
import bms_ui_form



class Ui_Dialog_Derived(bms_ui_form.Ui_Dialog):

    @QtCore.pyqtSlot(str)
    def updateStatus(self, status):
        self.m_Status.setText(status)


    @QtCore.pyqtSlot(str)
    def updateStatusPackVoltageEdit(self, status):
        self.textEdit.setText(status)


    @QtCore.pyqtSlot(str)
    def updateStatusPVoltageEdit(self, status):
        self.textEdit_2.setText(status)


    @QtCore.pyqtSlot(str)
    def updateStatusBVoltageEdit(self, status):
        self.textEdit_3.setText(status)


    @QtCore.pyqtSlot(str)
    def updateStatusPackCurrentEdit(self, status):
        self.textEdit_4.setText(status)


    @QtCore.pyqtSlot(str)
    def updateStatusSoCEdit(self, status):
        self.textEdit_5.setText(status)