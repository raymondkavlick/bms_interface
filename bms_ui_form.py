# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bms_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(1615, 885)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(1260, 830, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(980, 790, 151, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.m_Status = QtGui.QTextEdit(Dialog)
        self.m_Status.setGeometry(QtCore.QRect(1140, 790, 241, 61))
        self.m_Status.setAcceptDrops(False)
        self.m_Status.setReadOnly(True)
        self.m_Status.setAcceptRichText(False)
        self.m_Status.setObjectName(_fromUtf8("m_Status"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 140, 361, 541))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
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
        self.layoutWidget1.setGeometry(QtCore.QRect(41, 131, 361, 551))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
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
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 120, 771, 581))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 30, 501, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 820, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_6 = QtGui.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(170, 830, 111, 41))
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
        self.textEdit_6.setStyleSheet(_fromUtf8("background: rgb(250, 243, 255)"))
        self.textEdit_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setAcceptRichText(False)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.buttonBox.raise_()
        self.pushButton.raise_()
        self.m_Status.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.textEdit_6.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "BMS Interface", None))
        self.pushButton.setText(_translate("Dialog", "Connect", None))
        self.label_6.setText(_translate("Dialog", "Pack Voltage", None))
        self.label_7.setText(_translate("Dialog", "P+ Voltage", None))
        self.label_8.setText(_translate("Dialog", "B+ Voltage", None))
        self.label_9.setText(_translate("Dialog", "Pack Current", None))
        self.label_10.setText(_translate("Dialog", "State of Charge", None))
        self.label.setText(_translate("Dialog", "Lithium Battery Pack", None))
        self.label_3.setText(_translate("Dialog", "Time Remaining :", None))

