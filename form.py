# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(244, 799)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.soundProgress = QtGui.QProgressBar(self.centralwidget)
        self.soundProgress.setGeometry(QtCore.QRect(10, 174, 225, 23))
        self.soundProgress.setProperty("value", 0)
        self.soundProgress.setTextVisible(True)
        self.soundProgress.setInvertedAppearance(False)
        self.soundProgress.setObjectName(_fromUtf8("soundProgress"))
        self.openValue = QtGui.QLabel(self.centralwidget)
        self.openValue.setGeometry(QtCore.QRect(215, 215, 50, 13))
        self.openValue.setObjectName(_fromUtf8("openValue"))
        self.open12Value = QtGui.QLabel(self.centralwidget)
        self.open12Value.setGeometry(QtCore.QRect(215, 245, 46, 13))
        self.open12Value.setObjectName(_fromUtf8("open12Value"))
        self.minValue = QtGui.QLineEdit(self.centralwidget)
        self.minValue.setGeometry(QtCore.QRect(24, 301, 51, 20))
        self.minValue.setObjectName(_fromUtf8("minValue"))
        self.sredValue = QtGui.QLineEdit(self.centralwidget)
        self.sredValue.setGeometry(QtCore.QRect(94, 301, 51, 20))
        self.sredValue.setObjectName(_fromUtf8("sredValue"))
        self.maxValue = QtGui.QLineEdit(self.centralwidget)
        self.maxValue.setGeometry(QtCore.QRect(164, 301, 51, 20))
        self.maxValue.setObjectName(_fromUtf8("maxValue"))
        self.mouthCheck = QtGui.QCheckBox(self.centralwidget)
        self.mouthCheck.setGeometry(QtCore.QRect(24, 152, 70, 17))
        self.mouthCheck.setObjectName(_fromUtf8("mouthCheck"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 323, 21, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 323, 20, 10))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 201, 91))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.colorLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.colorLayout.setObjectName(_fromUtf8("colorLayout"))
        self.openSlider = QtGui.QSlider(self.centralwidget)
        self.openSlider.setGeometry(QtCore.QRect(10, 214, 191, 20))
        self.openSlider.setMaximum(100)
        self.openSlider.setSliderPosition(60)
        self.openSlider.setOrientation(QtCore.Qt.Horizontal)
        self.openSlider.setObjectName(_fromUtf8("openSlider"))
        self.open12Slider = QtGui.QSlider(self.centralwidget)
        self.open12Slider.setGeometry(QtCore.QRect(10, 244, 191, 20))
        self.open12Slider.setSliderPosition(45)
        self.open12Slider.setOrientation(QtCore.Qt.Horizontal)
        self.open12Slider.setObjectName(_fromUtf8("open12Slider"))
        self.sevoPosSlider = QtGui.QSlider(self.centralwidget)
        self.sevoPosSlider.setGeometry(QtCore.QRect(40, 363, 151, 20))
        self.sevoPosSlider.setMaximum(180)
        self.sevoPosSlider.setProperty("value", 85)
        self.sevoPosSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sevoPosSlider.setInvertedAppearance(False)
        self.sevoPosSlider.setInvertedControls(False)
        self.sevoPosSlider.setObjectName(_fromUtf8("sevoPosSlider"))
        self.posValue = QtGui.QLabel(self.centralwidget)
        self.posValue.setGeometry(QtCore.QRect(200, 359, 60, 20))
        self.posValue.setObjectName(_fromUtf8("posValue"))
        self.headTreckerChack = QtGui.QCheckBox(self.centralwidget)
        self.headTreckerChack.setGeometry(QtCore.QRect(24, 430, 70, 17))
        self.headTreckerChack.setChecked(True)
        self.headTreckerChack.setObjectName(_fromUtf8("headTreckerChack"))
        self.minXSlider = QtGui.QSlider(self.centralwidget)
        self.minXSlider.setGeometry(QtCore.QRect(40, 481, 151, 20))
        self.minXSlider.setMaximum(180)
        self.minXSlider.setProperty("value", 10)
        self.minXSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minXSlider.setObjectName(_fromUtf8("minXSlider"))
        self.maxXSlider = QtGui.QSlider(self.centralwidget)
        self.maxXSlider.setGeometry(QtCore.QRect(40, 511, 151, 20))
        self.maxXSlider.setMaximum(180)
        self.maxXSlider.setProperty("value", 70)
        self.maxXSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxXSlider.setObjectName(_fromUtf8("maxXSlider"))
        self.portBox = QtGui.QComboBox(self.centralwidget)
        self.portBox.setGeometry(QtCore.QRect(13, 10, 71, 22))
        self.portBox.setObjectName(_fromUtf8("portBox"))
        self.speedPortBox = QtGui.QComboBox(self.centralwidget)
        self.speedPortBox.setGeometry(QtCore.QRect(163, 10, 71, 22))
        self.speedPortBox.setObjectName(_fromUtf8("speedPortBox"))
        self.minXValue = QtGui.QLineEdit(self.centralwidget)
        self.minXValue.setGeometry(QtCore.QRect(200, 477, 31, 20))
        self.minXValue.setObjectName(_fromUtf8("minXValue"))
        self.maxXValue = QtGui.QLineEdit(self.centralwidget)
        self.maxXValue.setGeometry(QtCore.QRect(200, 509, 30, 20))
        self.maxXValue.setObjectName(_fromUtf8("maxXValue"))
        self.delayValue = QtGui.QLabel(self.centralwidget)
        self.delayValue.setGeometry(QtCore.QRect(200, 390, 60, 20))
        self.delayValue.setObjectName(_fromUtf8("delayValue"))
        self.delaySlider = QtGui.QSlider(self.centralwidget)
        self.delaySlider.setGeometry(QtCore.QRect(40, 393, 151, 20))
        self.delaySlider.setMaximum(200)
        self.delaySlider.setSingleStep(5)
        self.delaySlider.setProperty("value", 0)
        self.delaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.delaySlider.setInvertedAppearance(False)
        self.delaySlider.setInvertedControls(False)
        self.delaySlider.setObjectName(_fromUtf8("delaySlider"))
        self.minYValue = QtGui.QLineEdit(self.centralwidget)
        self.minYValue.setGeometry(QtCore.QRect(200, 565, 31, 20))
        self.minYValue.setObjectName(_fromUtf8("minYValue"))
        self.minYSlider = QtGui.QSlider(self.centralwidget)
        self.minYSlider.setGeometry(QtCore.QRect(40, 569, 151, 20))
        self.minYSlider.setMaximum(180)
        self.minYSlider.setProperty("value", 60)
        self.minYSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minYSlider.setObjectName(_fromUtf8("minYSlider"))
        self.maxYValue = QtGui.QLineEdit(self.centralwidget)
        self.maxYValue.setGeometry(QtCore.QRect(200, 597, 30, 20))
        self.maxYValue.setObjectName(_fromUtf8("maxYValue"))
        self.maxYSlider = QtGui.QSlider(self.centralwidget)
        self.maxYSlider.setGeometry(QtCore.QRect(40, 599, 151, 20))
        self.maxYSlider.setMaximum(180)
        self.maxYSlider.setProperty("value", 150)
        self.maxYSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxYSlider.setObjectName(_fromUtf8("maxYSlider"))
        self.reverseYChack = QtGui.QCheckBox(self.centralwidget)
        self.reverseYChack.setGeometry(QtCore.QRect(157, 539, 70, 17))
        self.reverseYChack.setChecked(False)
        self.reverseYChack.setObjectName(_fromUtf8("reverseYChack"))
        self.reverseXChack = QtGui.QCheckBox(self.centralwidget)
        self.reverseXChack.setGeometry(QtCore.QRect(158, 453, 70, 17))
        self.reverseXChack.setChecked(True)
        self.reverseXChack.setObjectName(_fromUtf8("reverseXChack"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 484, 31, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 515, 31, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 572, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 603, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 455, 61, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 540, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(206, 200, 46, 13))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(198, 227, 46, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 363, 31, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 394, 31, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.closeSlider = QtGui.QSlider(self.centralwidget)
        self.closeSlider.setGeometry(QtCore.QRect(10, 272, 191, 20))
        self.closeSlider.setSliderPosition(2)
        self.closeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.closeSlider.setObjectName(_fromUtf8("closeSlider"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(205, 259, 46, 13))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.closeValue = QtGui.QLabel(self.centralwidget)
        self.closeValue.setGeometry(QtCore.QRect(215, 273, 46, 13))
        self.closeValue.setObjectName(_fromUtf8("closeValue"))
        self.gainBox = QtGui.QSpinBox(self.centralwidget)
        self.gainBox.setGeometry(QtCore.QRect(194, 146, 42, 22))
        self.gainBox.setMinimum(1)
        self.gainBox.setMaximum(10)
        self.gainBox.setObjectName(_fromUtf8("gainBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(164, 150, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.xHeadSlider = QtGui.QSlider(self.centralwidget)
        self.xHeadSlider.setGeometry(QtCore.QRect(30, 630, 160, 19))
        self.xHeadSlider.setStyleSheet(_fromUtf8(""))
        self.xHeadSlider.setMaximum(180)
        self.xHeadSlider.setProperty("value", 90)
        self.xHeadSlider.setOrientation(QtCore.Qt.Horizontal)
        self.xHeadSlider.setObjectName(_fromUtf8("xHeadSlider"))
        self.yHeadSlider = QtGui.QSlider(self.centralwidget)
        self.yHeadSlider.setGeometry(QtCore.QRect(30, 660, 160, 19))
        self.yHeadSlider.setMaximum(180)
        self.yHeadSlider.setPageStep(10)
        self.yHeadSlider.setProperty("value", 90)
        self.yHeadSlider.setOrientation(QtCore.Qt.Horizontal)
        self.yHeadSlider.setObjectName(_fromUtf8("yHeadSlider"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 632, 46, 13))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 663, 46, 13))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.yHeadValue = QtGui.QLabel(self.centralwidget)
        self.yHeadValue.setGeometry(QtCore.QRect(210, 660, 40, 13))
        self.yHeadValue.setObjectName(_fromUtf8("yHeadValue"))
        self.xHeadValue = QtGui.QLabel(self.centralwidget)
        self.xHeadValue.setGeometry(QtCore.QRect(210, 629, 40, 13))
        self.xHeadValue.setObjectName(_fromUtf8("xHeadValue"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 130, 260, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-10, 30, 260, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(6, 730, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(6, 750, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.micStat = QtGui.QLabel(self.centralwidget)
        self.micStat.setGeometry(QtCore.QRect(76, 730, 161, 16))
        self.micStat.setObjectName(_fromUtf8("micStat"))
        self.arduinoStat = QtGui.QLabel(self.centralwidget)
        self.arduinoStat.setGeometry(QtCore.QRect(76, 750, 161, 16))
        self.arduinoStat.setObjectName(_fromUtf8("arduinoStat"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(-10, 413, 260, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(-10, 720, 260, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 694, 31, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.delaySliderHead = QtGui.QSlider(self.centralwidget)
        self.delaySliderHead.setGeometry(QtCore.QRect(40, 693, 151, 20))
        self.delaySliderHead.setMaximum(200)
        self.delaySliderHead.setSingleStep(5)
        self.delaySliderHead.setProperty("value", 0)
        self.delaySliderHead.setOrientation(QtCore.Qt.Horizontal)
        self.delaySliderHead.setInvertedAppearance(False)
        self.delaySliderHead.setInvertedControls(False)
        self.delaySliderHead.setObjectName(_fromUtf8("delaySliderHead"))
        self.delayValueHead = QtGui.QLabel(self.centralwidget)
        self.delayValueHead.setGeometry(QtCore.QRect(200, 690, 60, 20))
        self.delayValueHead.setObjectName(_fromUtf8("delayValueHead"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(93, 10, 61, 23))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 340, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tempValue = QtGui.QLabel(self.centralwidget)
        self.tempValue.setGeometry(QtCore.QRect(150, 340, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempValue.setFont(font)
        self.tempValue.setObjectName(_fromUtf8("tempValue"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.soundProgress.setFormat(_translate("MainWindow", "%p", None))
        self.openValue.setText(_translate("MainWindow", "60", None))
        self.open12Value.setText(_translate("MainWindow", "45", None))
        self.minValue.setText(_translate("MainWindow", "85", None))
        self.sredValue.setText(_translate("MainWindow", "135", None))
        self.maxValue.setText(_translate("MainWindow", "180", None))
        self.mouthCheck.setText(_translate("MainWindow", "Mouth", None))
        self.label_3.setText(_translate("MainWindow", "Min", None))
        self.label_4.setText(_translate("MainWindow", "Max", None))
        self.posValue.setText(_translate("MainWindow", "85", None))
        self.headTreckerChack.setText(_translate("MainWindow", "HeadTreker", None))
        self.minXValue.setText(_translate("MainWindow", "10", None))
        self.maxXValue.setText(_translate("MainWindow", "70", None))
        self.delayValue.setText(_translate("MainWindow", "0 ms", None))
        self.minYValue.setText(_translate("MainWindow", "60", None))
        self.maxYValue.setText(_translate("MainWindow", "150", None))
        self.reverseYChack.setText(_translate("MainWindow", "Reverse", None))
        self.reverseXChack.setText(_translate("MainWindow", "Reverse", None))
        self.label_7.setText(_translate("MainWindow", "Min", None))
        self.label_8.setText(_translate("MainWindow", "Max", None))
        self.label_9.setText(_translate("MainWindow", "Min", None))
        self.label_10.setText(_translate("MainWindow", "Max", None))
        self.label_11.setText(_translate("MainWindow", "X position", None))
        self.label_12.setText(_translate("MainWindow", "Y position", None))
        self.label_13.setText(_translate("MainWindow", "Open", None))
        self.label_14.setText(_translate("MainWindow", "Open 1/2", None))
        self.label_15.setText(_translate("MainWindow", "Pos", None))
        self.label_16.setText(_translate("MainWindow", "Delay", None))
        self.label_17.setText(_translate("MainWindow", "Close", None))
        self.closeValue.setText(_translate("MainWindow", "2", None))
        self.label.setText(_translate("MainWindow", "Gain:", None))
        self.label_18.setText(_translate("MainWindow", "X:", None))
        self.label_19.setText(_translate("MainWindow", "Y:", None))
        self.yHeadValue.setText(_translate("MainWindow", "90", None))
        self.xHeadValue.setText(_translate("MainWindow", "90", None))
        self.label_2.setText(_translate("MainWindow", "Microphone:", None))
        self.label_5.setText(_translate("MainWindow", "Arduino:", None))
        self.micStat.setText(_translate("MainWindow", "...", None))
        self.arduinoStat.setText(_translate("MainWindow", "...", None))
        self.label_20.setText(_translate("MainWindow", "Delay", None))
        self.delayValueHead.setText(_translate("MainWindow", "0 ms", None))
        self.label_6.setText(_translate("MainWindow", "Temperature:", None))
        self.tempValue.setText(_translate("MainWindow", "xx", None))

