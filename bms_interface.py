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
    signalPackVoltageEdit = QtCore.pyqtSignal(str)
    signalPVoltageEdit = QtCore.pyqtSignal(str)
    signalBVoltageEdit = QtCore.pyqtSignal(str)
    signalPackCurrentEdit = QtCore.pyqtSignal(str)
    signalSoCEdit = QtCore.pyqtSignal(str)

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
        self.signalStatus.connect(self.gui.updateStatus)
        self.worker.signalStatus.connect(self.gui.updateStatus)
        self.signalPackVoltageEdit.connect(self.gui.updateStatusPackVoltageEdit)
        self.worker.signalPackVoltageEdit.connect(self.gui.updateStatusPackVoltageEdit)
        self.signalPVoltageEdit.connect(self.gui.updateStatusPVoltageEdit)
        self.worker.signalPVoltageEdit.connect(self.gui.updateStatusPVoltageEdit)
        self.signalBVoltageEdit.connect(self.gui.updateStatusBVoltageEdit)
        self.worker.signalBVoltageEdit.connect(self.gui.updateStatusBVoltageEdit)
        self.signalPackCurrentEdit.connect(self.gui.updateStatusPackCurrentEdit)
        self.worker.signalPackCurrentEdit.connect(self.gui.updateStatusPackCurrentEdit)
        self.signalSoCEdit.connect(self.gui.updateStatusSoCEdit)
        self.worker.signalSoCEdit.connect(self.gui.updateStatusSoCEdit)

class worker(QtCore.QObject):
    signalStatus = QtCore.pyqtSignal(str)
    signalPackVoltageEdit = QtCore.pyqtSignal(str)
    signalPVoltageEdit = QtCore.pyqtSignal(str)
    signalBVoltageEdit = QtCore.pyqtSignal(str)
    signalPackCurrentEdit = QtCore.pyqtSignal(str)
    signalSoCEdit = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = 0
    ''' for sending
    def startWork(self, result=PCAN_ERROR_CAUTION):
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

                time.sleep(1)
                stsResult = self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)
                if stsResult == PCAN_ERROR_OK:
                    print "Sending message..."
                    self.signalPackVoltageEdit.emit(str(x))
                else:
                    # An error occurred.  We show the error.
                    #
                    print "error2"
    '''
    def startWork(self, result=PCAN_ERROR_CAUTION):
            print "startWorker Thread Rx!"
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
                    result = PCAN_ERROR_OK
                    self.signalStatus.emit("PeakCAN Connected!.")
            else:
                # Prepares the PCAN-Basic's PCAN-Trace file
                print "PCAN - Initialized."
                self.signalStatus.emit("Connected. Receiving...")
                while(1):
                    readResult = self.m_objPCANBasic.Read(self.m_PcanHandle)
                    if readResult[0] == PCAN_ERROR_OK:
                        msg = readResult[1]  # readResult[1] TPCANMsg()
                        idhex = format(msg.ID, 'X')
                        print'ID = ', idhex,
                        print(format(msg.DATA[0], '02X')),
                        print(format(msg.DATA[1], '02X')),
                        print(format(msg.DATA[2], '02X')),
                        print(format(msg.DATA[3], '02X')),
                        print(format(msg.DATA[4], '02X')),
                        print(format(msg.DATA[5], '02X')),
                        print(format(msg.DATA[6], '02X')),
                        print(format(msg.DATA[7], '02X'))
                        #if idhex == 0x1AD:
                        if idhex == 0x726:
                            print "found 726"
                            PackVoltage = msg.DATA[0] + (msg.DATA[1] * 256)#endian
                            PackCurrent = msg.DATA[2] + (msg.DATA[3] * 256)#endian
                            SoC = msg.DATA[5]
                            self.signalPackVoltageEdit.emit(str(float(PackVoltage) / 100) + " Volts")
                            self.signalPackCurrentEdit.emit(str(PackCurrent))
                            self.signalSoCEdit.emit(str(SoC))
                        elif idhex == 0x2AD:
                            BVoltage = msg.DATA[4] + (msg.DATA[5] * 256)#endian
                            self.signalBVoltageEdit.emit(str(BVoltage))
                        elif idhex == 0x3AD:
                            PVoltage = msg.DATA[6] + (msg.DATA[7] * 256)#endian
                            self.signalPVoltageEdit.emit(str(PVoltage))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    bms_dyno = Bms_Dyno(app)
    sys.exit(app.exec_())
