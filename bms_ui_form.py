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
        Dialog.resize(475, 644)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 600, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 530, 151, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.m_Status = QtGui.QTextEdit(Dialog)
        self.m_Status.setGeometry(QtCore.QRect(200, 530, 241, 61))
        self.m_Status.setAcceptDrops(False)
        self.m_Status.setReadOnly(True)
        self.m_Status.setAcceptRichText(False)
        self.m_Status.setObjectName(_fromUtf8("m_Status"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(241, 128, 201, 81))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(241, 215, 201, 81))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(241, 302, 201, 81))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(241, 389, 201, 81))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(80, 40, 131, 431))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(241, 41, 201, 81))
        self.textEdit.setMinimumSize(QtCore.QSize(109, 0))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.buttonBox.raise_()
        self.pushButton.raise_()
        self.m_Status.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.textEdit_4.raise_()
        self.textEdit_5.raise_()
        self.textEdit.raise_()
        self.textEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "BMS Interface", None))
        self.pushButton.setText(_translate("Dialog", "Connect", None))
        self.label_6.setText(_translate("Dialog", "Pack Voltage", None))
        self.label_7.setText(_translate("Dialog", "P+ Voltage", None))
        self.label_8.setText(_translate("Dialog", "B+ Voltage", None))
        self.label_9.setText(_translate("Dialog", "Pack Current", None))
        self.label_10.setText(_translate("Dialog", "SoC", None))

