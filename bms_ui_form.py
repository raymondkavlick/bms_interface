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
        self.layoutWidget_2 = QtGui.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1270, 140, 281, 541))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textEdit_11 = QtGui.QTextEdit(self.layoutWidget_2)
        self.textEdit_11.setMinimumSize(QtCore.QSize(109, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.verticalLayout_5.addWidget(self.textEdit_11)
        self.textEdit_12 = QtGui.QTextEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.verticalLayout_5.addWidget(self.textEdit_12)
        self.textEdit_13 = QtGui.QTextEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_13.setFont(font)
        self.textEdit_13.setObjectName(_fromUtf8("textEdit_13"))
        self.verticalLayout_5.addWidget(self.textEdit_13)
        self.textEdit_14 = QtGui.QTextEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_14.setFont(font)
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.verticalLayout_5.addWidget(self.textEdit_14)
        self.textEdit_15 = QtGui.QTextEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_15.setFont(font)
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.verticalLayout_5.addWidget(self.textEdit_15)
        self.layoutWidget_3 = QtGui.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(901, 131, 361, 551))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.layoutWidget_3.setFont(font)
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_16 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_6.addWidget(self.label_18)
        self.label_19 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_6.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_6.addWidget(self.label_20)
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(880, 120, 691, 581))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 30, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(1090, 40, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
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
        self.textEdit_6.setGeometry(QtCore.QRect(170, 814, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_6.setAcceptDrops(False)
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
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
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
        self.label_10.setText(_translate("Dialog", "SoC", None))
        self.label_16.setText(_translate("Dialog", "Pack Voltage", None))
        self.label_17.setText(_translate("Dialog", "P+ Voltage", None))
        self.label_18.setText(_translate("Dialog", "B+ Voltage", None))
        self.label_19.setText(_translate("Dialog", "Pack Current", None))
        self.label_20.setText(_translate("Dialog", "SoC", None))
        self.label.setText(_translate("Dialog", "Pack # 1", None))
        self.label_2.setText(_translate("Dialog", "Pack # 2", None))
        self.label_3.setText(_translate("Dialog", "Time Remaining :", None))

