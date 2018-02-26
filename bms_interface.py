#!/usr/bin/python
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
import ui_helper
from timeit import default_timer

class Bms_Dyno(QtCore.QObject):

    signalStatus = QtCore.pyqtSignal(str)
    signalPackVoltageEdit = QtCore.pyqtSignal(str)
    signalPVoltageEdit = QtCore.pyqtSignal(str)
    signalBVoltageEdit = QtCore.pyqtSignal(str)
    signalPackCurrentEdit = QtCore.pyqtSignal(str)
    signalSoCEdit = QtCore.pyqtSignal(str)
    signal2PackVoltageEdit = QtCore.pyqtSignal(str)
    signal2PVoltageEdit = QtCore.pyqtSignal(str)
    signal2BVoltageEdit = QtCore.pyqtSignal(str)
    signal2PackCurrentEdit = QtCore.pyqtSignal(str)
    signal2SoCEdit = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        # Create a gui object.
        self.Dialog = QtGui.QDialog()
        self.gui = ui_helper.Ui_Dialog_Derived()
        self.gui.setupUi(self.Dialog)

        # Setup the worker object and the worker_thread.
        self.worker = worker()
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # Make any cross object connections.
        self._connectSignals()

        #self.Dialog.show()
        self.Dialog.showFullScreen()
        #self.worker.startWork()#auto connect at bootup

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

        self.signal2PackVoltageEdit.connect(self.gui.updateStatus2PackVoltageEdit)
        self.worker.signal2PackVoltageEdit.connect(self.gui.updateStatus2PackVoltageEdit)
        self.signal2PVoltageEdit.connect(self.gui.updateStatus2PVoltageEdit)
        self.worker.signal2PVoltageEdit.connect(self.gui.updateStatus2PVoltageEdit)
        self.signal2BVoltageEdit.connect(self.gui.updateStatus2BVoltageEdit)
        self.worker.signal2BVoltageEdit.connect(self.gui.updateStatus2BVoltageEdit)
        self.signal2PackCurrentEdit.connect(self.gui.updateStatus2PackCurrentEdit)
        self.worker.signal2PackCurrentEdit.connect(self.gui.updateStatus2PackCurrentEdit)
        self.signal2SoCEdit.connect(self.gui.updateStatus2SoCEdit)
        self.worker.signal2SoCEdit.connect(self.gui.updateStatus2SoCEdit)

class worker(QtCore.QObject):
    signalStatus = QtCore.pyqtSignal(str)
    signalPackVoltageEdit = QtCore.pyqtSignal(str)
    signalPVoltageEdit = QtCore.pyqtSignal(str)
    signalBVoltageEdit = QtCore.pyqtSignal(str)
    signalPackCurrentEdit = QtCore.pyqtSignal(str)
    signalSoCEdit = QtCore.pyqtSignal(str)
    signal2PackVoltageEdit = QtCore.pyqtSignal(str)
    signal2PVoltageEdit = QtCore.pyqtSignal(str)
    signal2BVoltageEdit = QtCore.pyqtSignal(str)
    signal2PackCurrentEdit = QtCore.pyqtSignal(str)
    signal2SoCEdit = QtCore.pyqtSignal(str)


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
            self.baudrate = PCAN_BAUD_250K
            self.hwtype = PCAN_USBBUS1
            self.ioport = 0
            self.interrupt = 0

            self.m_PcanHandle2 = PCAN_USBBUS2
            self.baudrate2 = PCAN_BAUD_250K
            self.hwtype2 = PCAN_USBBUS2
            self.ioport2 = 0
            self.interrupt2 = 0

            # Connects a selected PCAN-Basic channel
            result = self.m_objPCANBasic.Initialize(self.m_PcanHandle,self.baudrate,self.hwtype,self.ioport,self.interrupt)
            result2 = self.m_objPCANBasic.Initialize(self.m_PcanHandle2,self.baudrate2,self.hwtype2,self.ioport2,self.interrupt2)

            if result != PCAN_ERROR_OK or result2 != PCAN_ERROR_OK:
                print "Error - PCAN not initializing."
                if result != PCAN_ERROR_CAUTION:
                    self.signalStatus.emit('PeakCAN Dongle\'s Not Found.')
                else:
                    result = PCAN_ERROR_OK
                    self.signalStatus.emit("PeakCAN Connected!.")
            else:
                # Prepares the PCAN-Basic's PCAN-Trace file
                print "PCAN 1 & 2 - Initialized."
                self.signalStatus.emit("Connected. Waiting for BMS...")
                startTime = default_timer()
                while(1):

                    if default_timer() > startTime + .5:#.1 = 100ms
                        self.sendBMSPdo()
                        startTime = default_timer()

                    readResult = self.m_objPCANBasic.Read(self.m_PcanHandle)
                    if readResult[0] == PCAN_ERROR_OK:
                        msg = readResult[1]  # readResult[1] TPCANMsg()
                        idhex = format(msg.ID, 'X')
                        #print'ID = ', idhex,
                        #print(format(msg.DATA[0], '02X')),
                        #print(format(msg.DATA[1], '02X')),
                        #print(format(msg.DATA[2], '02X')),
                        #print(format(msg.DATA[3], '02X')),
                        #print(format(msg.DATA[4], '02X')),
                        #print(format(msg.DATA[5], '02X')),
                        #print(format(msg.DATA[6], '02X')),
                        #print(format(msg.DATA[7], '02X'))
                        if msg.ID == 0x1AD:
                            self.signalStatus.emit("BMS Connected.")
                            PackVoltage = msg.DATA[0] + (msg.DATA[1] * 256)#endian
                            PackCurrent = msg.DATA[2] + (msg.DATA[3] * 256)#endian
                            PackCurrent = 0xFC18
                            PackCurrent = c_int16(PackCurrent)
                            #if(PackCurrent & 0x8000):
                            #    PackCurrent |= 0xFFFFFFFFFFFF0000
                            SoC = msg.DATA[5]
                            self.signalPackVoltageEdit.emit(str(float(PackVoltage) / 100) + " Volts")
                            self.signalPackCurrentEdit.emit(str(PackCurrent.value) + " Amps")
                            self.signalSoCEdit.emit(str(SoC) + "%")
                        elif msg.ID == 0x2AD:
                            BVoltage = msg.DATA[4] + (msg.DATA[5] * 256)#endian
                            self.signalBVoltageEdit.emit(str(float(BVoltage) / 100) + " Volts")
                        elif msg.ID == 0x3AD:
                            PVoltage = msg.DATA[6] + (msg.DATA[7] * 256)#endian
                            self.signalPVoltageEdit.emit(str(float(PVoltage) / 100) + " Volts")

                    readResult2 = self.m_objPCANBasic.Read(self.m_PcanHandle2)
                    if readResult2[0] == PCAN_ERROR_OK:
                        msg2 = readResult2[1]  # readResult[1] TPCANMsg()
                        idhex2 = format(msg2.ID, 'X')
                        print'ID = ', idhex2,
                        print(format(msg2.DATA[0], '02X')),
                        print(format(msg2.DATA[1], '02X')),
                        print(format(msg2.DATA[2], '02X')),
                        print(format(msg2.DATA[3], '02X')),
                        print(format(msg2.DATA[4], '02X')),
                        print(format(msg2.DATA[5], '02X')),
                        print(format(msg2.DATA[6], '02X')),
                        print(format(msg2.DATA[7], '02X'))
                        if msg2.ID == 0x1AD:
                            #self.signalStatus.emit("BMS Connected.")
                            PackVoltage2 = msg2.DATA[0] + (msg2.DATA[1] * 256)  # endian
                            PackCurrent2 = msg2.DATA[2] + (msg2.DATA[3] * 256)  # endian
                            SoC2 = msg2.DATA[5]
                            self.signal2PackVoltageEdit.emit(str(float(PackVoltage2) / 100) + " Volts")
                            self.signal2PackCurrentEdit.emit(str(float(PackCurrent2) / 100) + " Amps")
                            self.signal2SoCEdit.emit(str(SoC2) + "%")
                        elif msg2.ID == 0x2AD:
                            BVoltage2 = msg2.DATA[4] + (msg2.DATA[5] * 256)  # endian
                            self.signal2BVoltageEdit.emit(str(float(BVoltage2) / 100) + " Volts")
                        elif msg2.ID == 0x3AD:
                            PVoltage2 = msg2.DATA[6] + (msg2.DATA[7] * 256)  # endian
                            self.signal2PVoltageEdit.emit(str(float(PVoltage2) / 100) + " Volts")

    def sendBMSPdo(self):
        CANMsg = TPCANMsg()
        for i in range(CANMsg.LEN):
            CANMsg.DATA[i] = 0

        CHARGER_CONNECTED = 1
        CHARGER_DISCONNECTED = 0
        chargerState = CHARGER_DISCONNECTED
        TOW_MODE_ON = 2
        TOW_MODE_OFF = 0
        towState = TOW_MODE_OFF
        CANMsg.DATA[0] = towState + chargerState
        RXV = 0
        TXT = 1
        CANMsg.DATA[1] = RXV
        CANMsg.ID = 0x22D
        CANMsg.LEN = 8
        CANMsg.MSGTYPE = PCAN_MESSAGE_STANDARD
        self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)
        self.m_objPCANBasic.Write(self.m_PcanHandle2, CANMsg)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    bms_dyno = Bms_Dyno(app)
    sys.exit(app.exec_())

    '''
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
    
    '''

def sign_extending(x, b):
    if x&(1<<(b-1)): # is the highest bit (sign) set? (x>>(b-1)) would be faster
        return x-(1<<b) # 2s complement
    return x