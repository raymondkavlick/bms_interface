# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bms_interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import threading
import time
from PyQt4 import QtCore, QtGui

import bms_ui_form
from PCANBasic import *        ## PCAN-Basic library import
import sys

class Bms_Dyno(QtCore.QObject):

    signalStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        # Create a gui object.
        self.gui = bms_ui_form.Ui_Dialog()
        Dialog mydiag;
        self.gui.setupUi(mydiag)

        # Setup the worker object and the worker_thread.
        self.worker = worker()
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # Make any cross object connections.
        #self._connectSignals()

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

    @QtCore.pyqtSlot(str)
    def updateStatus(self, status):
        self.label_status.setText(status)

class worker(QtCore.QObject):
    signalStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = 0

    def startWork(self, result=PCAN_ERROR_CAUTION):
            self.m_PcanHandle = PCAN_USBBUS1
            baudrate = PCAN_BAUD_500K
            hwtype = PCAN_USBBUS1
            ioport = 0
            interrupt = 0

            # Connects a selected PCAN-Basic channel
            result =  self.m_objPCANBasic.Initialize(self.m_PcanHandle,baudrate,hwtype,ioport,interrupt)

            if result != PCAN_ERROR_OK:
                print "Error - PCAN not initializing."
                if result != PCAN_ERROR_CAUTION:
                    self.signalStatus.emit('PeakCAN Dongle Not Found.')
                else:
                    self.IncludeTextMessage('******************************************************')
                    self.IncludeTextMessage('The bitrate being used is different than the given one')
                    self.IncludeTextMessage('******************************************************')
                    result = PCAN_ERROR_OK
                    self.signalStatus.emit("PeakCAN Connected!.")
            else:
                # Prepares the PCAN-Basic's PCAN-Trace file
                print "PCAN - Initialized."
                self.signalStatus.emit('PeakCAN Dongle Found.')

            CANMsg = TPCANMsg()
            for i in range(CANMsg.LEN):
                CANMsg.DATA[i] = 3
            CANMsg.ID = 0x300
            CANMsg.LEN = 8
            CANMsg.MSGTYPE = PCAN_MESSAGE_STANDARD
            self.signalStatus.emit('Sending CAN Messages...')
            for x in range(0,100):
                #
                time.sleep(1)

                print x
                # The message is sent to the configured hardware
                #
                stsResult = self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)
                print "sent"
                # The message was successfully sent
                #
                if stsResult == PCAN_ERROR_OK:
                    #self.IncludeTextMessage("Message was successfully SENT")
                    print "error1"
                else:
                    # An error occurred.  We show the error.
                    #
                    print "error2"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    bms_dyno = Bms_Dyno(app)
    sys.exit(app.exec_())
