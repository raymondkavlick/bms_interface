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
import RPi.GPIO as GPIO
from threading import Timer

class Bms_Dyno(QtCore.QObject):

    signalStatus = QtCore.pyqtSignal(str)
    signalPackVoltageEdit = QtCore.pyqtSignal(str)
    signalPVoltageEdit = QtCore.pyqtSignal(str)
    signalBVoltageEdit = QtCore.pyqtSignal(str)
    signalPackCurrentEdit = QtCore.pyqtSignal(str)
    signalSoCEdit = QtCore.pyqtSignal(str)
    signalCellMaxTempEdit = QtCore.pyqtSignal(str)
    signalCellMinTempEdit = QtCore.pyqtSignal(str)
    signalMaxCellVoltsEdit = QtCore.pyqtSignal(str)
    signalMinCellVoltsEdit = QtCore.pyqtSignal(str)
    signalChargerPWMEdit = QtCore.pyqtSignal(str)
    signalTimeRemainingEdit = QtCore.pyqtSignal(str)
    #signalPushButton = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        #class vars
        self.time_remaining = 1
        self.BMS_KEY = 21

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
        self.Dialog.showFullScreen()

    def _connectSignals(self):
        self.gui.pushButton.clicked.connect(self.worker.startWork)
        #self.gui.pushButton.clicked.connect(self.worker.startPowerDown)
        #self.gui.
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

        self.signalCellMaxTempEdit.connect(self.gui.updateStatusCellMaxTempEdit)
        self.worker.signalCellMaxTempEdit.connect(self.gui.updateStatusCellMaxTempEdit)
        self.signalCellMinTempEdit.connect(self.gui.updateStatusCellMinTempEdit)
        self.worker.signalCellMinTempEdit.connect(self.gui.updateStatusCellMinTempEdit)
        self.signalMaxCellVoltsEdit.connect(self.gui.updateStatusMaxCellVoltsEdit)
        self.worker.signalMaxCellVoltsEdit.connect(self.gui.updateStatusMaxCellVoltsEdit)
        self.signalMinCellVoltsEdit.connect(self.gui.updateStatusMinCellVoltsEdit)
        self.worker.signalMinCellVoltsEdit.connect(self.gui.updateStatusMinCellVoltsEdit)
        self.signalChargerPWMEdit.connect(self.gui.updateStatusChargerPWMEdit)
        self.worker.signalChargerPWMEdit.connect(self.gui.updateStatusChargerPWMEdit)

        self.signalTimeRemainingEdit.connect(self.gui.updateStatusTimeRemainingEdit)
        self.worker.signalTimeRemainingEdit.connect(self.gui.updateStatusTimeRemainingEdit)
        #self.signalPushButton.connect(self.gui.updatePushButton)
        #self.worker.signalPushButton.connect(self.gui.updatePushButton)


class worker(QtCore.QObject):
    signalStatus = QtCore.pyqtSignal(str)
    signalPackVoltageEdit = QtCore.pyqtSignal(str)
    signalPVoltageEdit = QtCore.pyqtSignal(str)
    signalBVoltageEdit = QtCore.pyqtSignal(str)
    signalPackCurrentEdit = QtCore.pyqtSignal(str)
    signalSoCEdit = QtCore.pyqtSignal(str)
    signalCellMaxTempEdit = QtCore.pyqtSignal(str)
    signalCellMinTempEdit = QtCore.pyqtSignal(str)
    signalMaxCellVoltsEdit = QtCore.pyqtSignal(str)
    signalMinCellVoltsEdit = QtCore.pyqtSignal(str)
    signalChargerPWMEdit = QtCore.pyqtSignal(str)
    signalTimeRemainingEdit = QtCore.pyqtSignal(str)
    #signalPushButton = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.m_objPCANBasic = PCANBasic()
        self.m_PcanHandle = 0

    def startWork(self, result=PCAN_ERROR_CAUTION):
            print "startWorker Thread Rx!"
            #self.gui.pushButton.setEnabled(False)
            #self.signalPushButton.emit("")
            self.signalStatus.emit("Connecting to Peak...")

            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(bms_dyno.BMS_KEY, GPIO.OUT)
            GPIO.output(bms_dyno.BMS_KEY, GPIO.HIGH)
            time.sleep(3)
            start_time_remain = self.get_seconds()

            self.m_PcanHandle = PCAN_USBBUS1
            self.baudrate = PCAN_BAUD_250K
            self.hwtype = PCAN_USBBUS1
            self.ioport = 0
            self.interrupt = 0

            # Connects a selected PCAN-Basic channel
            result = self.m_objPCANBasic.Initialize(self.m_PcanHandle,self.baudrate,self.hwtype,self.ioport,self.interrupt)

            if result != PCAN_ERROR_OK:
                print "Error - PCAN not initializing."
                if result != PCAN_ERROR_CAUTION:
                    self.signalStatus.emit('PeakCAN Dongle\'s Not Found.')
                #else:
                  #  result = PCAN_ERROR_OK
                  #  self.signalStatus.emit("PeakCAN Connected!.")
            else:
                # Prepares the PCAN-Basic's PCAN-Trace file
                print "PCAN - Initialized."
                self.signalStatus.emit("Connected. Waiting for BMS...")
                startTime = default_timer()
                timeout_count = 0

                while(1):


                    if default_timer() > startTime + .5:#.1 = 100ms
                        self.sendBMSPdo()
                        startTime = default_timer()
                        self.draw_time_remaining(start_time_remain)
                        timeout_count += 1

                        if timeout_count > 4:#timeout has occured
                            self.signalPackVoltageEdit.emit("CAN TIMEOUT");
                            self.signalPackCurrentEdit.emit("CAN TIMEOUT");
                            self.signalBVoltageEdit.emit("CAN TIMEOUT");
                            self.signalPVoltageEdit.emit("CAN TIMEOUT");
                            self.signalSoCEdit.emit("CAN TIMEOUT");
                            self.signalCellMaxTempEdit.emit("CAN TIMEOUT");
                            self.signalCellMinTempEdit.emit("CAN TIMEOUT");
                            self.signalMaxCellVoltsEdit.emit("CAN TIMEOUT");
                            self.signalMinCellVoltsEdit.emit("CAN TIMEOUT");
                            self.signalChargerPWMEdit.emit("CAN TIMEOUT");
                            self.signalStatus.emit("BMS Missing.")

                    readResult = self.m_objPCANBasic.Read(self.m_PcanHandle)
                    if readResult[0] == PCAN_ERROR_OK:
                        msg = readResult[1]  # readResult[1] TPCANMsg()
                        idhex = format(msg.ID, 'X')
                        if msg.ID == 0x1AD:
                            timeout_count = 0
                            self.signalStatus.emit("BMS Connected.")
                            PackVoltage = msg.DATA[0] + (msg.DATA[1] * 256)#endian
                            PackCurrent = msg.DATA[2] + (msg.DATA[3] * 256)#endian
                            PackCurrent = c_int16(PackCurrent)
                            SoC = msg.DATA[5]
                            MaxTemp = msg.DATA[6]
                            MinTemp = msg.DATA[7]
                            self.signalPackVoltageEdit.emit(str(float(PackVoltage) / 100) + " Volts")
                            self.signalPackCurrentEdit.emit(str(float(PackCurrent.value) / -10) + " Amps")
                            self.signalSoCEdit.emit(str(SoC) + "%")
                            self.signalCellMaxTempEdit.emit(str(MaxTemp) + " degC")
                            self.signalCellMinTempEdit.emit(str(MinTemp) + " degC")
                        elif msg.ID == 0x2AD:
                            MaxCellVolts = msg.DATA[0] + (msg.DATA[1] * 256)#endian
                            MinCellVolts = msg.DATA[2] + (msg.DATA[3] * 256)#endian
                            BVoltage = msg.DATA[4] + (msg.DATA[5] * 256)#endian
                            self.signalMaxCellVoltsEdit.emit(str(float(MaxCellVolts) / 1000) + " Volts")
                            self.signalMinCellVoltsEdit.emit(str(float(MinCellVolts) / 1000) + " Volts")
                            self.signalBVoltageEdit.emit(str(float(BVoltage) / 100) + " Volts")
                        elif msg.ID == 0x3AD:
                            PVoltage = msg.DATA[6] + (msg.DATA[7] * 256)#endian
                            self.signalPVoltageEdit.emit(str(float(PVoltage) / 100) + " Volts")
                        elif msg.ID == 0x4AD:
                            chargerPWM = msg.DATA[0]
                            self.signalChargerPWMEdit.emit(str(chargerPWM) + "%")

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

    def draw_time_remaining(self, start):
        if bms_dyno.time_remaining == 0:
            GPIO.output(bms_dyno.BMS_KEY, GPIO.LOW)
            self.signalStatus.emit("Entered Sleep Mode.")
        else:
            time_now = self.get_seconds()
            bms_dyno.time_remaining = (60 * 60 * 8) - (time_now - start)
            #bms_dyno.time_remaining = (10) - (time_now - start)
            string_time_remain = "%02d:" % (((bms_dyno.time_remaining / 3600) % 24),) \
                                 + "%02d:" % (((bms_dyno.time_remaining / 60) % 60),) \
                                 + "%02d" % ((bms_dyno.time_remaining % 60),)
            self.signalTimeRemainingEdit.emit(string_time_remain)

    def get_seconds(self):
        return int(round(time.time()))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    bms_dyno = Bms_Dyno(app)
    sys.exit(app.exec_())


def sign_extending(x, b):
    if x&(1<<(b-1)): # is the highest bit (sign) set? (x>>(b-1)) would be faster
        return x-(1<<b) # 2s complement
    return x
