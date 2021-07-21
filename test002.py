# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test001.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pic_ui_rc

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1133, 809)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(80, 550, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.checkBox.setFont(font)
        self.checkBox.setMouseTracking(True)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setStatusTip("")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 720, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(880, 410, 72, 39))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.checkBox_weather1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_weather1.setGeometry(QtCore.QRect(320, 640, 61, 31))
        self.checkBox_weather1.setStyleSheet("image: url(:/LR/sun.png);")
        self.checkBox_weather1.setText("")
        self.checkBox_weather1.setObjectName("checkBox_weather1")
        self.checkBox_weather2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_weather2.setGeometry(QtCore.QRect(377, 644, 61, 21))
        self.checkBox_weather2.setStyleSheet("image: url(:/LR/cloud.png);")
        self.checkBox_weather2.setText("")
        self.checkBox_weather2.setObjectName("checkBox_weather2")
        self.checkBox_weather3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_weather3.setGeometry(QtCore.QRect(434, 644, 51, 21))
        self.checkBox_weather3.setStyleSheet("image: url(:/LR/rain.png);")
        self.checkBox_weather3.setText("")
        self.checkBox_weather3.setObjectName("checkBox_weather3")
        self.checkBox_wind1_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_wind1_5.setGeometry(QtCore.QRect(490, 644, 51, 21))
        self.checkBox_wind1_5.setStyleSheet("image: url(:/LR/flash.png);")
        self.checkBox_wind1_5.setText("")
        self.checkBox_wind1_5.setObjectName("checkBox_wind1_5")

        self.checkBox_weather1.stateChanged.connect(self.changeCheck5)
        self.checkBox_weather2.stateChanged.connect(self.changeCheck6)
        self.checkBox_weather3.stateChanged.connect(self.changeCheck7)
        self.checkBox_wind1_5.stateChanged.connect(self.changeCheck8)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 490, 81, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setTabletTracking(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(400, 730, 281, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton.move(100,100)

        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 10, 651, 441))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget2)
        self.graphicsView.setEnabled(False)
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.graphicsView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.graphicsView.setStyleSheet("border-image: url(:/LR/LinearSVR.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(850, 320, 106, 22))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(770, 50, 282, 241))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(780, 450, 271, 191))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.layoutWidget4)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(50)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setPageStep(9)
        self.horizontalSlider_2.setProperty("value", 10)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget4)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setProperty("value", 25)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(330, 510, 201, 18))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_wind1 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_wind1.setObjectName("checkBox_wind1")
        self.horizontalLayout_4.addWidget(self.checkBox_wind1)
        self.checkBox_wind2 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_wind2.setObjectName("checkBox_wind2")
        self.horizontalLayout_4.addWidget(self.checkBox_wind2)
        self.checkBox_wind3 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_wind3.setObjectName("checkBox_wind3")
        self.horizontalLayout_4.addWidget(self.checkBox_wind3)
        self.checkBox_wind4 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_wind4.setObjectName("checkBox_wind4")

        self.checkBox_wind1.stateChanged.connect(self.changeCheck1)
        self.checkBox_wind2.stateChanged.connect(self.changeCheck2)
        self.checkBox_wind3.stateChanged.connect(self.changeCheck3)
        self.checkBox_wind4.stateChanged.connect(self.changeCheck4)




        self.horizontalLayout_4.addWidget(self.checkBox_wind4)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(330, 560, 201, 51))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.layoutWidget6)
        self.horizontalSlider_3.setMaximum(12)
        self.horizontalSlider_3.setProperty("value", 12)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_5.addWidget(self.horizontalSlider_3)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_3.setNum)
        self.pushButton_3.clicked['bool'].connect(MainWindow.close)
        self.calendarWidget.clicked['QDate'].connect(self.dateEdit.setDate)
        self.dateEdit.dateChanged['QDate'].connect(self.calendarWidget.setSelectedDate)
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_11.setNum)
        self.checkBox.clicked['bool'].connect(self.label_6.setHidden)
        self.checkBox.clicked['bool'].connect(self.label_7.setHidden)
        self.checkBox.clicked['bool'].connect(self.label_5.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_wind1.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_wind2.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_wind3.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_wind4.setHidden)
        self.checkBox.clicked['bool'].connect(self.horizontalSlider_3.setHidden)
        self.checkBox.clicked['bool'].connect(self.label_11.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_weather1.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_weather2.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_weather3.setHidden)
        self.checkBox.clicked['bool'].connect(self.checkBox_wind1_5.setHidden)
        self.checkBox.clicked['bool'].connect(self.label_12.setHidden)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_click_messBox)
        MainWindow.setTabOrder(self.checkBox, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.horizontalSlider_2)
        MainWindow.setTabOrder(self.horizontalSlider_2, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.calendarWidget)

    def  changeCheck1(self):
        if self.checkBox_wind1.checkState() == Qt.Checked:
            self.checkBox_wind2.setChecked(False)
            self.checkBox_wind3.setChecked(False)
            self.checkBox_wind4.setChecked(False)
    def  changeCheck2(self):
        if self.checkBox_wind2.checkState() == Qt.Checked:
            self.checkBox_wind1.setChecked(False)
            self.checkBox_wind3.setChecked(False)
            self.checkBox_wind4.setChecked(False)
    def  changeCheck3(self):
        if self.checkBox_wind3.checkState() == Qt.Checked:
            self.checkBox_wind1.setChecked(False)
            self.checkBox_wind2.setChecked(False)
            self.checkBox_wind4.setChecked(False)
    def  changeCheck4(self):
        if self.checkBox_wind4.checkState() == Qt.Checked:
            self.checkBox_wind1.setChecked(False)
            self.checkBox_wind2.setChecked(False)
            self.checkBox_wind3.setChecked(False)
    def  changeCheck5(self):
        if self.checkBox_weather1.checkState() == Qt.Checked:
            self.checkBox_weather2.setChecked(False)
            self.checkBox_weather3.setChecked(False)
            self.checkBox_wind1_5.setChecked(False)
    def  changeCheck6(self):
        if self.checkBox_weather2.checkState() == Qt.Checked:
            self.checkBox_weather1.setChecked(False)
            self.checkBox_weather3.setChecked(False)
            self.checkBox_wind1_5.setChecked(False)
    def  changeCheck7(self):
        if self.checkBox_weather3.checkState() == Qt.Checked:
            self.checkBox_weather1.setChecked(False)
            self.checkBox_weather2.setChecked(False)
            self.checkBox_wind1_5.setChecked(False)
    def  changeCheck8(self):
        if self.checkBox_wind1_5.checkState() == Qt.Checked:
            self.checkBox_weather1.setChecked(False)
            self.checkBox_weather2.setChecked(False)
            self.checkBox_weather3.setChecked(False)

    def on_click_messBox(self):
        import matplotlib.pyplot as plt
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        import pandas as pd

        from sklearn.svm import LinearSVR
        data = pd.read_csv('./data_new.csv', encoding='gbk')
        import random
        minweather=self.horizontalSlider_2.value()
        maxweather=self.horizontalSlider.value()
        print('最高温',maxweather)
        print('最低温',minweather)

        weathers=[self.checkBox_weather1.isChecked(),self.checkBox_weather2.isChecked(),
               self.checkBox_weather3.isChecked(),self.checkBox_wind1_5.isChecked()]
        print('测试weathers true',weathers.index(True))

        weathernum=weathers.index(True)+1

        print('weathers',weathers)
        winds=[self.checkBox_wind1.isChecked(),self.checkBox_wind2.isChecked(),
               self.checkBox_wind3.isChecked(),self.checkBox_wind4.isChecked()]
        print('winds',winds)
        windnum=winds.index(True)+1

        windstrong = self.horizontalSlider_3.value()
        print('风力',windstrong)


        datemonth=self.dateEdit.date().month()
        print('datemonth',datemonth)
        dateday=self.dateEdit.date().day()
        print('dateday', dateday)

        # 获取到的界面数据

        testxxx=[]
        testxxx.append(weathernum)  # 天气
        testxxx.append(windnum)     #风向
        testxxx.append(windstrong)  # 风力
        testxxx.append(minweather)  # 最低气温
        testxxx.append(maxweather)  # 最高气温
        testxxx.append(datemonth)  # 月
        testxxx.append(dateday)  # 日
        print('test_xxx',testxxx)

        x_train = data.iloc[:200, 1:]
        x_test = data.iloc[200:, 1:]
        y_train = data.iloc[:200, :1]
        y_test = data.iloc[200:, :1]

        clf = LinearSVR(C=1)
        clf.fit(x_train, y_train)

        y_pred = clf.predict([testxxx])

        print('y_pred',y_pred)
        stry = str(y_pred.tolist()[0])

        messBox = QMessageBox()
        messBox.setStyleSheet(
            "QLabel{"
            "min-width: 200px;"
            "min-height: 100px;"
            "}"
        )
        messBox.setWindowTitle(u'预测电荷值为')
        messBox.setText(stry)
        messBox.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "其他因素关闭"))
        self.pushButton_3.setText(_translate("MainWindow", "关闭实验"))
        self.label_10.setText(_translate("MainWindow", "温度设置"))
        self.label_6.setText(_translate("MainWindow", "风向"))
        self.label_7.setText(_translate("MainWindow", "风力"))
        self.label_5.setText(_translate("MainWindow", "天气"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "初始化"))
        self.label_8.setText(_translate("MainWindow", "电荷预测曲线图"))
        self.label_9.setText(_translate("MainWindow", "时间选择"))
        self.label_4.setText(_translate("MainWindow", "最低气温"))
        self.label_3.setText(_translate("MainWindow", "0~50"))
        self.label_2.setText(_translate("MainWindow", "最高气温"))
        self.label.setText(_translate("MainWindow", "0~50"))
        self.checkBox_wind1.setText(_translate("MainWindow", "东"))
        self.checkBox_wind2.setText(_translate("MainWindow", "西"))
        self.checkBox_wind3.setText(_translate("MainWindow", "南"))
        self.checkBox_wind4.setText(_translate("MainWindow", "北"))
        self.label_11.setText(_translate("MainWindow", "0~12"))
        self.label_12.setText(_translate("MainWindow", "级"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
