
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

    @QtCore.pyqtSlot(str)
    def updateStatusCellMinTempEdit(self, status):
        self.textEdit_10.setText(status)

    @QtCore.pyqtSlot(str)
    def updateStatusCellMaxTempEdit(self, status):
        self.textEdit_12.setText(status)

    @QtCore.pyqtSlot(str)
    def updateStatusMaxCellVoltsEdit(self, status):
        self.textEdit_8.setText(status)

    @QtCore.pyqtSlot(str)
    def updateStatusMinCellVoltsEdit(self, status):
        self.textEdit_9.setText(status)

    @QtCore.pyqtSlot(str)
    def updateStatusChargerPWMEdit(self, status):
        self.textEdit_11.setText(status)

    @QtCore.pyqtSlot(str)
    def updateStatusTimeRemainingEdit(self, status):
        self.textEdit_6.setText(status)

    @QtCore.pyqtSlot(str)
    def catchAll(self,action):
        if action == "buttonDisable":
            self.connectButton.setEnabled(False)
            self.powerDownButton.setEnabled(True)
        elif action == "regen":
            self.textEdit_4.setTextBackgroundColor(QtGui.QColor(0,255,0))
        elif action == "discharge":
            self.textEdit_4.setTextBackgroundColor(QtGui.QColor(255,0,0))
        elif action == "idlecurrent":
            self.textEdit_4.setTextBackgroundColor(QtGui.QColor(255,255,255))
