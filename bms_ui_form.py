# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bms_ui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1825, 986)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(1420, 930, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.connectButton = QtGui.QPushButton(Dialog)
        self.connectButton.setGeometry(QtCore.QRect(1050, 880, 151, 61))
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.m_Status = QtGui.QTextEdit(Dialog)
        self.m_Status.setGeometry(QtCore.QRect(1230, 880, 271, 61))
        self.m_Status.setAcceptDrops(False)
        self.m_Status.setFrameShape(QtGui.QFrame.WinPanel)
        self.m_Status.setFrameShadow(QtGui.QFrame.Raised)
        self.m_Status.setLineWidth(100)
        self.m_Status.setReadOnly(True)
        self.m_Status.setAcceptRichText(False)
        self.m_Status.setObjectName(_fromUtf8("m_Status"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 171, 361, 541))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(109, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.textEdit_2 = QtGui.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.textEdit_3 = QtGui.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.verticalLayout_2.addWidget(self.textEdit_3)
        self.textEdit_4 = QtGui.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.verticalLayout_2.addWidget(self.textEdit_4)
        self.textEdit_5 = QtGui.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.verticalLayout_2.addWidget(self.textEdit_5)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(131, 162, 432, 551))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(630, 61, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 920, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_6 = QtGui.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(170, 930, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_6.setAcceptDrops(False)
        self.textEdit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_6.setAutoFillBackground(False)
        self.textEdit_6.setStyleSheet(_fromUtf8(""))
        self.textEdit_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setAcceptRichText(False)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_8 = QtGui.QTextEdit(Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(1290, 389, 359, 103))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_9 = QtGui.QTextEdit(Dialog)
        self.textEdit_9.setGeometry(QtCore.QRect(1290, 498, 359, 103))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.textEdit_10 = QtGui.QTextEdit(Dialog)
        self.textEdit_10.setGeometry(QtCore.QRect(1290, 280, 359, 103))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.textEdit_11 = QtGui.QTextEdit(Dialog)
        self.textEdit_11.setGeometry(QtCore.QRect(1290, 607, 359, 103))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.textEdit_12 = QtGui.QTextEdit(Dialog)
        self.textEdit_12.setGeometry(QtCore.QRect(1290, 171, 359, 103))
        self.textEdit_12.setMinimumSize(QtCore.QSize(109, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(920, 493, 430, 105))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(920, 271, 430, 105))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(920, 382, 430, 105))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(920, 604, 430, 105))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(920, 160, 430, 105))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(1350, 10, 111, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.powerDownButton = QtGui.QPushButton(Dialog)
        self.powerDownButton.setGeometry(QtCore.QRect(870, 880, 151, 61))
        self.powerDownButton.setObjectName(_fromUtf8("powerDownButton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(1340, 850, 61, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(1470, 10, 351, 151))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("logo.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.buttonBox.raise_()
        self.connectButton.raise_()
        self.m_Status.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.textEdit_6.raise_()
        self.textEdit_8.raise_()
        self.textEdit_9.raise_()
        self.textEdit_10.raise_()
        self.textEdit_11.raise_()
        self.textEdit_12.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_2.raise_()
        self.powerDownButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Curtis Dyno BMS", None))
        self.connectButton.setText(_translate("Dialog", "Connect", None))
        self.label_6.setText(_translate("Dialog", "Pack Voltage", None))
        self.label_7.setText(_translate("Dialog", "P+ Voltage", None))
        self.label_8.setText(_translate("Dialog", "B+ Voltage", None))
        self.label_9.setText(_translate("Dialog", "Pack Current", None))
        self.label_10.setText(_translate("Dialog", "State of Charge", None))
        self.label.setText(_translate("Dialog", "Lithium Battery Pack", None))
        self.label_3.setText(_translate("Dialog", "Time Remaining :", None))
        self.label_11.setText(_translate("Dialog", "Min Cell Volts", None))
        self.label_12.setText(_translate("Dialog", "Cell Min Temp.", None))
        self.label_13.setText(_translate("Dialog", "Max Cell Volts", None))
        self.label_14.setText(_translate("Dialog", "Charger PWM", None))
        self.label_15.setText(_translate("Dialog", "Cell Max Temp.", None))
        self.label_2.setText(_translate("Dialog", "Version 1.1.0", None))
        self.powerDownButton.setText(_translate("Dialog", "Power Down", None))
        self.label_4.setText(_translate("Dialog", "Status", None))

