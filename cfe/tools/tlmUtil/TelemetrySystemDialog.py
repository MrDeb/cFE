# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelemetrySystemDialog.ui'
#
# Created: Sun Feb 23 07:11:43 2014
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TelemetrySystemDialog(object):
    def setupUi(self, TelemetrySystemDialog):
        TelemetrySystemDialog.setObjectName("TelemetrySystemDialog")
        TelemetrySystemDialog.resize(584, 642)
        self.buttonBox = QtGui.QDialogButtonBox(TelemetrySystemDialog)
        self.buttonBox.setGeometry(QtCore.QRect(440, 40, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(TelemetrySystemDialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 201, 17))
        self.label.setObjectName("label")
        self.scrollArea = QtGui.QScrollArea(TelemetrySystemDialog)
        self.scrollArea.setGeometry(QtCore.QRect(30, 140, 541, 461))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setBaseSize(QtCore.QSize(0, 800))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 521, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_0 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_0.setGeometry(QtCore.QRect(400, 40, 101, 27))
        self.pushButton_0.setObjectName("pushButton_0")
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(200, 10, 71, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(290, 10, 91, 17))
        self.label_5.setObjectName("label_5")
        self.SubsysBrowser_0 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_0.setGeometry(QtCore.QRect(30, 40, 141, 31))
        self.SubsysBrowser_0.setObjectName("SubsysBrowser_0")
        self.pktidBrowser_0 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_0.setGeometry(QtCore.QRect(190, 40, 81, 31))
        self.pktidBrowser_0.setObjectName("pktidBrowser_0")
        self.countBrowser_0 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_0.setGeometry(QtCore.QRect(290, 40, 91, 31))
        self.countBrowser_0.setObjectName("countBrowser_0")
        self.SubsysBrowser_1 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_1.setGeometry(QtCore.QRect(30, 80, 141, 31))
        self.SubsysBrowser_1.setObjectName("SubsysBrowser_1")
        self.SubsysBrowser_2 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_2.setGeometry(QtCore.QRect(30, 120, 141, 31))
        self.SubsysBrowser_2.setObjectName("SubsysBrowser_2")
        self.SubsysBrowser_3 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_3.setGeometry(QtCore.QRect(30, 160, 141, 31))
        self.SubsysBrowser_3.setObjectName("SubsysBrowser_3")
        self.SubsysBrowser_4 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_4.setGeometry(QtCore.QRect(30, 200, 141, 31))
        self.SubsysBrowser_4.setObjectName("SubsysBrowser_4")
        self.SubsysBrowser_5 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_5.setGeometry(QtCore.QRect(30, 240, 141, 31))
        self.SubsysBrowser_5.setObjectName("SubsysBrowser_5")
        self.SubsysBrowser_6 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_6.setGeometry(QtCore.QRect(30, 280, 141, 31))
        self.SubsysBrowser_6.setObjectName("SubsysBrowser_6")
        self.SubsysBrowser_7 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_7.setGeometry(QtCore.QRect(30, 320, 141, 31))
        self.SubsysBrowser_7.setObjectName("SubsysBrowser_7")
        self.SubsysBrowser_8 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_8.setGeometry(QtCore.QRect(30, 360, 141, 31))
        self.SubsysBrowser_8.setObjectName("SubsysBrowser_8")
        self.SubsysBrowser_9 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_9.setGeometry(QtCore.QRect(30, 400, 141, 31))
        self.SubsysBrowser_9.setObjectName("SubsysBrowser_9")
        self.SubsysBrowser_10 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_10.setGeometry(QtCore.QRect(30, 440, 141, 31))
        self.SubsysBrowser_10.setObjectName("SubsysBrowser_10")
        self.SubsysBrowser_11 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_11.setGeometry(QtCore.QRect(30, 480, 141, 31))
        self.SubsysBrowser_11.setObjectName("SubsysBrowser_11")
        self.SubsysBrowser_12 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_12.setGeometry(QtCore.QRect(30, 520, 141, 31))
        self.SubsysBrowser_12.setObjectName("SubsysBrowser_12")
        self.SubsysBrowser_13 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_13.setGeometry(QtCore.QRect(30, 560, 141, 31))
        self.SubsysBrowser_13.setObjectName("SubsysBrowser_13")
        self.SubsysBrowser_14 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_14.setGeometry(QtCore.QRect(30, 600, 141, 31))
        self.SubsysBrowser_14.setObjectName("SubsysBrowser_14")
        self.SubsysBrowser_15 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_15.setGeometry(QtCore.QRect(30, 640, 141, 31))
        self.SubsysBrowser_15.setObjectName("SubsysBrowser_15")
        self.SubsysBrowser_16 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_16.setGeometry(QtCore.QRect(30, 680, 141, 31))
        self.SubsysBrowser_16.setObjectName("SubsysBrowser_16")
        self.SubsysBrowser_17 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_17.setGeometry(QtCore.QRect(30, 720, 141, 31))
        self.SubsysBrowser_17.setObjectName("SubsysBrowser_17")
        self.SubsysBrowser_18 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_18.setGeometry(QtCore.QRect(30, 760, 141, 31))
        self.SubsysBrowser_18.setObjectName("SubsysBrowser_18")
        self.SubsysBrowser_19 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_19.setGeometry(QtCore.QRect(30, 800, 141, 31))
        self.SubsysBrowser_19.setObjectName("SubsysBrowser_19")
        self.SubsysBrowser_20 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.SubsysBrowser_20.setGeometry(QtCore.QRect(30, 840, 141, 31))
        self.SubsysBrowser_20.setObjectName("SubsysBrowser_20")
        self.pktidBrowser_1 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_1.setGeometry(QtCore.QRect(190, 80, 81, 31))
        self.pktidBrowser_1.setObjectName("pktidBrowser_1")
        self.pktidBrowser_2 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_2.setGeometry(QtCore.QRect(190, 120, 81, 31))
        self.pktidBrowser_2.setObjectName("pktidBrowser_2")
        self.pktidBrowser_3 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_3.setGeometry(QtCore.QRect(190, 160, 81, 31))
        self.pktidBrowser_3.setObjectName("pktidBrowser_3")
        self.pktidBrowser_4 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_4.setGeometry(QtCore.QRect(190, 200, 81, 31))
        self.pktidBrowser_4.setObjectName("pktidBrowser_4")
        self.pktidBrowser_5 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_5.setGeometry(QtCore.QRect(190, 240, 81, 31))
        self.pktidBrowser_5.setObjectName("pktidBrowser_5")
        self.pktidBrowser_6 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_6.setGeometry(QtCore.QRect(190, 280, 81, 31))
        self.pktidBrowser_6.setObjectName("pktidBrowser_6")
        self.pktidBrowser_7 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_7.setGeometry(QtCore.QRect(190, 320, 81, 31))
        self.pktidBrowser_7.setObjectName("pktidBrowser_7")
        self.pktidBrowser_8 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_8.setGeometry(QtCore.QRect(190, 360, 81, 31))
        self.pktidBrowser_8.setObjectName("pktidBrowser_8")
        self.pktidBrowser_9 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_9.setGeometry(QtCore.QRect(190, 400, 81, 31))
        self.pktidBrowser_9.setObjectName("pktidBrowser_9")
        self.pktidBrowser_10 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_10.setGeometry(QtCore.QRect(190, 440, 81, 31))
        self.pktidBrowser_10.setObjectName("pktidBrowser_10")
        self.pktidBrowser_11 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_11.setGeometry(QtCore.QRect(190, 480, 81, 31))
        self.pktidBrowser_11.setObjectName("pktidBrowser_11")
        self.pktidBrowser_12 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_12.setGeometry(QtCore.QRect(190, 520, 81, 31))
        self.pktidBrowser_12.setObjectName("pktidBrowser_12")
        self.pktidBrowser_13 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_13.setGeometry(QtCore.QRect(190, 560, 81, 31))
        self.pktidBrowser_13.setObjectName("pktidBrowser_13")
        self.pktidBrowser_14 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_14.setGeometry(QtCore.QRect(190, 600, 81, 31))
        self.pktidBrowser_14.setObjectName("pktidBrowser_14")
        self.pktidBrowser_15 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_15.setGeometry(QtCore.QRect(190, 640, 81, 31))
        self.pktidBrowser_15.setObjectName("pktidBrowser_15")
        self.pktidBrowser_16 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_16.setGeometry(QtCore.QRect(190, 680, 81, 31))
        self.pktidBrowser_16.setObjectName("pktidBrowser_16")
        self.pktidBrowser_17 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_17.setGeometry(QtCore.QRect(190, 720, 81, 31))
        self.pktidBrowser_17.setObjectName("pktidBrowser_17")
        self.pktidBrowser_18 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_18.setGeometry(QtCore.QRect(190, 760, 81, 31))
        self.pktidBrowser_18.setObjectName("pktidBrowser_18")
        self.pktidBrowser_19 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_19.setGeometry(QtCore.QRect(190, 800, 81, 31))
        self.pktidBrowser_19.setObjectName("pktidBrowser_19")
        self.pktidBrowser_20 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.pktidBrowser_20.setGeometry(QtCore.QRect(190, 840, 81, 31))
        self.pktidBrowser_20.setObjectName("pktidBrowser_20")
        self.countBrowser_1 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_1.setGeometry(QtCore.QRect(290, 80, 91, 31))
        self.countBrowser_1.setObjectName("countBrowser_1")
        self.countBrowser_2 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_2.setGeometry(QtCore.QRect(290, 120, 91, 31))
        self.countBrowser_2.setObjectName("countBrowser_2")
        self.countBrowser_3 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_3.setGeometry(QtCore.QRect(290, 160, 91, 31))
        self.countBrowser_3.setObjectName("countBrowser_3")
        self.countBrowser_4 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_4.setGeometry(QtCore.QRect(290, 200, 91, 31))
        self.countBrowser_4.setObjectName("countBrowser_4")
        self.countBrowser_5 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_5.setGeometry(QtCore.QRect(290, 240, 91, 31))
        self.countBrowser_5.setObjectName("countBrowser_5")
        self.countBrowser_6 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_6.setGeometry(QtCore.QRect(290, 280, 91, 31))
        self.countBrowser_6.setObjectName("countBrowser_6")
        self.countBrowser_7 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_7.setGeometry(QtCore.QRect(290, 320, 91, 31))
        self.countBrowser_7.setObjectName("countBrowser_7")
        self.countBrowser_8 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_8.setGeometry(QtCore.QRect(290, 360, 91, 31))
        self.countBrowser_8.setObjectName("countBrowser_8")
        self.countBrowser_9 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_9.setGeometry(QtCore.QRect(290, 400, 91, 31))
        self.countBrowser_9.setObjectName("countBrowser_9")
        self.countBrowser_10 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_10.setGeometry(QtCore.QRect(290, 440, 91, 31))
        self.countBrowser_10.setObjectName("countBrowser_10")
        self.countBrowser_11 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_11.setGeometry(QtCore.QRect(290, 480, 91, 31))
        self.countBrowser_11.setObjectName("countBrowser_11")
        self.countBrowser_12 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_12.setGeometry(QtCore.QRect(290, 520, 91, 31))
        self.countBrowser_12.setObjectName("countBrowser_12")
        self.countBrowser_13 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_13.setGeometry(QtCore.QRect(290, 560, 91, 31))
        self.countBrowser_13.setObjectName("countBrowser_13")
        self.countBrowser_14 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_14.setGeometry(QtCore.QRect(290, 600, 91, 31))
        self.countBrowser_14.setObjectName("countBrowser_14")
        self.countBrowser_15 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_15.setGeometry(QtCore.QRect(290, 640, 91, 31))
        self.countBrowser_15.setObjectName("countBrowser_15")
        self.countBrowser_16 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_16.setGeometry(QtCore.QRect(290, 680, 91, 31))
        self.countBrowser_16.setObjectName("countBrowser_16")
        self.countBrowser_17 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_17.setGeometry(QtCore.QRect(290, 720, 91, 31))
        self.countBrowser_17.setObjectName("countBrowser_17")
        self.countBrowser_18 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_18.setGeometry(QtCore.QRect(290, 760, 91, 31))
        self.countBrowser_18.setObjectName("countBrowser_18")
        self.countBrowser_19 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_19.setGeometry(QtCore.QRect(290, 800, 91, 31))
        self.countBrowser_19.setObjectName("countBrowser_19")
        self.countBrowser_20 = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.countBrowser_20.setGeometry(QtCore.QRect(290, 840, 91, 31))
        self.countBrowser_20.setObjectName("countBrowser_20")
        self.pushButton_1 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_1.setGeometry(QtCore.QRect(400, 80, 101, 27))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 120, 101, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 160, 101, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 200, 101, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 240, 101, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 280, 101, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 320, 101, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 360, 101, 27))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 400, 101, 27))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setGeometry(QtCore.QRect(400, 440, 101, 27))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 480, 101, 27))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 520, 101, 27))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setGeometry(QtCore.QRect(400, 560, 101, 27))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setGeometry(QtCore.QRect(400, 600, 101, 27))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setGeometry(QtCore.QRect(400, 640, 101, 27))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_16.setGeometry(QtCore.QRect(400, 680, 101, 27))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_17.setGeometry(QtCore.QRect(400, 720, 101, 27))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_18.setGeometry(QtCore.QRect(400, 760, 101, 27))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_19.setGeometry(QtCore.QRect(400, 800, 101, 27))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_20.setGeometry(QtCore.QRect(400, 840, 101, 27))
        self.pushButton_20.setObjectName("pushButton_20")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtGui.QLabel(TelemetrySystemDialog)
        self.label_2.setGeometry(QtCore.QRect(220, 110, 111, 17))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtGui.QLabel(TelemetrySystemDialog)
        self.label_6.setGeometry(QtCore.QRect(110, 50, 121, 17))
        self.label_6.setObjectName("label_6")
        self.sequenceCount = QtGui.QTextBrowser(TelemetrySystemDialog)
        self.sequenceCount.setGeometry(QtCore.QRect(250, 40, 131, 31))
        self.sequenceCount.setObjectName("sequenceCount")

        self.retranslateUi(TelemetrySystemDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TelemetrySystemDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TelemetrySystemDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TelemetrySystemDialog)

    def retranslateUi(self, TelemetrySystemDialog):
        TelemetrySystemDialog.setWindowTitle(QtGui.QApplication.translate("TelemetrySystemDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "cFE/CFS Subsystem Telemetry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_0.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Subsystem/Page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Packet ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Packet Count", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_1.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_19.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_20.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Display Page", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Available Pages", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("TelemetrySystemDialog", "Packets Received", None, QtGui.QApplication.UnicodeUTF8))
