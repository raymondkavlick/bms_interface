# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bms_interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import threading
import time
from PyQt4 import QtCore, QtGui
from PCANBasic import *        ## PCAN-Basic library import


import sys

class Bms_Dyno(QtCore.QObject):

    signalStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        # Create a gui object.
        self.gui = bms_window()

        # Setup the worker object and the worker_thread.
        self.worker = worker()
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # Make any cross object connections.
        self._connectSignals()

        self.gui.show()

    def _connectSignals(self):
        self.gui.button_start.clicked.connect(self.worker.startWork)
        self.signalStatus.connect(self.gui.updateStatus)
        self.worker.signalStatus.connect(self.gui.updateStatus)


class bms_window(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("BMS Interface")
        self.button_start = QtGui.QPushButton('Connect', self)
        self.label_status = QtGui.QLabel('', self)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button_start)
        layout.addWidget(self.label_status)

        self.setFixedSize(400, 200)
        self.m_objPCANBasic = PCANBasic()

    @QtCore.pyqtSlot(str)
    def updateStatus(self, status):
        self.label_status.setText(status)

class worker(QtCore.QObject):
    signalStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

    def startWork(self, result=PCAN_ERROR_CAUTION):


            baudrate = PCAN_BAUD_500K
            HwType = TPCANType(0),
            IOPort = c_uint(0),
            Interrupt = c_ushort(0)

            # Connects a selected PCAN-Basic channel
            self.m_objPCANBasic.Initialize(self.m_PcanHandle, baudrate, hwtype, ioport, interrupt)

            if result != PCAN_ERROR_OK:
                if result != PCAN_ERROR_CAUTION:
                    self.signalStatus.emit('ERRRRRR.')
                else:
                    self.IncludeTextMessage('******************************************************')
                    self.IncludeTextMessage('The bitrate being used is different than the given one')
                    self.IncludeTextMessage('******************************************************')
                    result = PCAN_ERROR_OK
                    self.signalStatus.emit("GOOD")
            else:
                # Prepares the PCAN-Basic's PCAN-Trace file
                #
                self.ConfigureTraceFile()
                self.signalStatus.emit( u'{0}'.format(1))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    bms_dyno = Bms_Dyno(app)
    sys.exit(app.exec_())
