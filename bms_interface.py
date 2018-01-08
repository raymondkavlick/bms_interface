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
        self.Dialog = QtGui.QDialog()
        self.gui = bms_ui_form.Ui_Dialog()
        self.gui.setupUi(self.Dialog)

        # Setup the worker object and the worker_thread.
        self.worker = worker()
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # Make any cross object connections.
        self._connectSignals()

        self.Dialog.show()

    def _connectSignals(self):
        self.gui.pushButton.clicked.connect(self.worker.startWork)
        #self.gui.button_start.clicked.connect(self.worker.startWork)
        self.signalStatus.connect(self.gui.updateStatus)
        self.worker.signalStatus.connect(self.gui.updateStatus)

class worker(QtCore.QObject):
    signalStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = 0

    def startWork(self, result=PCAN_ERROR_CAUTION):
            self.signalStatus.emit("wtf")
            print "startWorker Thread!"
            self.m_PcanHandle = PCAN_USBBUS1
            self.baudrate = PCAN_BAUD_500K
            self.hwtype = PCAN_USBBUS1
            self.ioport = 0
            self.interrupt = 0

            # Connects a selected PCAN-Basic channel
            result = self.m_objPCANBasic.Initialize(self.m_PcanHandle,self.baudrate,self.hwtype,self.ioport,self.interrupt)

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
                stsResult = 1
                time.sleep(1)
                # The message is sent to the configured hardware
                #
                stsResult = self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)
                # The message was successfully sent
                #
                if stsResult == PCAN_ERROR_OK:
                    #self.IncludeTextMessage("Message was successfully SENT")
                    print "Sending message..."
                    print x
                    self.signalStatus.emit(x)
                else:
                    # An error occurred.  We show the error.
                    #
                    print "error2"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    bms_dyno = Bms_Dyno(app)
    sys.exit(app.exec_())
