# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(990, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hF_indicator = QtWidgets.QFrame(self.centralwidget)
        self.hF_indicator.setEnabled(True)
        self.hF_indicator.setObjectName("hF_indicator")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.hF_indicator)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(0, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.hF_indicator)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setEnabled(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_Xpos = QtWidgets.QLabel(self.frame)
        self.label_Xpos.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Xpos.setFont(font)
        self.label_Xpos.setObjectName("label_Xpos")
        self.horizontalLayout_5.addWidget(self.label_Xpos)
        self.label_Ypos = QtWidgets.QLabel(self.frame)
        self.label_Ypos.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Ypos.setFont(font)
        self.label_Ypos.setObjectName("label_Ypos")
        self.horizontalLayout_5.addWidget(self.label_Ypos)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.hF_indicator)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_sigX = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_sigX.setFont(font)
        self.label_sigX.setObjectName("label_sigX")
        self.horizontalLayout_6.addWidget(self.label_sigX)
        self.label_sigY = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_sigY.setFont(font)
        self.label_sigY.setObjectName("label_sigY")
        self.horizontalLayout_6.addWidget(self.label_sigY)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.hF_indicator)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.graphicsView.setRubberBandSelectionMode(QtCore.Qt.ContainsItemShape)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.hV_zoom = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hV_zoom.sizePolicy().hasHeightForWidth())
        self.hV_zoom.setSizePolicy(sizePolicy)
        self.hV_zoom.setObjectName("hV_zoom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.hV_zoom)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_FitInView = QtWidgets.QPushButton(self.hV_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FitInView.sizePolicy().hasHeightForWidth())
        self.pushButton_FitInView.setSizePolicy(sizePolicy)
        self.pushButton_FitInView.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_FitInView.setMaximumSize(QtCore.QSize(60, 16777215))
        icon = QtGui.QIcon.fromTheme("0")
        self.pushButton_FitInView.setIcon(icon)
        self.pushButton_FitInView.setObjectName("pushButton_FitInView")
        self.horizontalLayout_2.addWidget(self.pushButton_FitInView)
        self.pushButton_zoomIn = QtWidgets.QPushButton(self.hV_zoom)
        self.pushButton_zoomIn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_zoomIn.setObjectName("pushButton_zoomIn")
        self.horizontalLayout_2.addWidget(self.pushButton_zoomIn)
        self.pushButton_zoomOut = QtWidgets.QPushButton(self.hV_zoom)
        self.pushButton_zoomOut.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_zoomOut.setObjectName("pushButton_zoomOut")
        self.horizontalLayout_2.addWidget(self.pushButton_zoomOut)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_saveConfig = QtWidgets.QPushButton(self.hV_zoom)
        self.pushButton_saveConfig.setObjectName("pushButton_saveConfig")
        self.horizontalLayout_2.addWidget(self.pushButton_saveConfig)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.hV_zoom)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.spinBox_Xmin = QtWidgets.QSpinBox(self.hV_zoom)
        self.spinBox_Xmin.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_Xmin.setMaximum(1000)
        self.spinBox_Xmin.setObjectName("spinBox_Xmin")
        self.horizontalLayout_2.addWidget(self.spinBox_Xmin)
        self.spinBox_Xmax = QtWidgets.QSpinBox(self.hV_zoom)
        self.spinBox_Xmax.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_Xmax.setMaximum(9999)
        self.spinBox_Xmax.setProperty("value", 9999)
        self.spinBox_Xmax.setObjectName("spinBox_Xmax")
        self.horizontalLayout_2.addWidget(self.spinBox_Xmax)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.hV_zoom)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.spinBox_Ymin = QtWidgets.QSpinBox(self.hV_zoom)
        self.spinBox_Ymin.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_Ymin.setMaximum(1000)
        self.spinBox_Ymin.setSingleStep(1)
        self.spinBox_Ymin.setObjectName("spinBox_Ymin")
        self.horizontalLayout_2.addWidget(self.spinBox_Ymin)
        self.spinBox_Ymax = QtWidgets.QSpinBox(self.hV_zoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_Ymax.sizePolicy().hasHeightForWidth())
        self.spinBox_Ymax.setSizePolicy(sizePolicy)
        self.spinBox_Ymax.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_Ymax.setMaximum(9999)
        self.spinBox_Ymax.setProperty("value", 9999)
        self.spinBox_Ymax.setObjectName("spinBox_Ymax")
        self.horizontalLayout_2.addWidget(self.spinBox_Ymax)
        self.verticalLayout_2.addWidget(self.hV_zoom)
        spacerItem6 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox_cameras = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_cameras.setObjectName("comboBox_cameras")
        self.verticalLayout.addWidget(self.comboBox_cameras)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_turnOn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_turnOn.setEnabled(False)
        self.pushButton_turnOn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_turnOn.setObjectName("pushButton_turnOn")
        self.horizontalLayout.addWidget(self.pushButton_turnOn)
        self.pushButton_turnOff = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_turnOff.setEnabled(False)
        self.pushButton_turnOff.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_turnOff.setObjectName("pushButton_turnOff")
        self.horizontalLayout.addWidget(self.pushButton_turnOff)
        self.pushButton_refreshList = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refreshList.setObjectName("pushButton_refreshList")
        self.horizontalLayout.addWidget(self.pushButton_refreshList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.vF_control = QtWidgets.QFrame(self.centralwidget)
        self.vF_control.setEnabled(True)
        self.vF_control.setObjectName("vF_control")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.vF_control)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.toolBox = QtWidgets.QToolBox(self.vF_control)
        self.toolBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 248, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.spinBox_Exp = QtWidgets.QSpinBox(self.page)
        self.spinBox_Exp.setObjectName("spinBox_Exp")
        self.verticalLayout_3.addWidget(self.spinBox_Exp)
        self.label_MinMaxExp = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_MinMaxExp.setFont(font)
        self.label_MinMaxExp.setObjectName("label_MinMaxExp")
        self.verticalLayout_3.addWidget(self.label_MinMaxExp)
        self.line_3 = QtWidgets.QFrame(self.page)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_3.addWidget(self.doubleSpinBox)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 248, 201))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox = QtWidgets.QComboBox(self.page_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_9.addWidget(self.comboBox)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem9)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_9.addWidget(self.comboBox_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_avg = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_avg.setObjectName("checkBox_avg")
        self.verticalLayout_6.addWidget(self.checkBox_avg)
        self.frame_avg = QtWidgets.QFrame(self.page_3)
        self.frame_avg.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_avg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_avg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_avg.setObjectName("frame_avg")
        self.formLayout = QtWidgets.QFormLayout(self.frame_avg)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.frame_avg)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox_avg_frames = QtWidgets.QSpinBox(self.frame_avg)
        self.spinBox_avg_frames.setMinimum(1)
        self.spinBox_avg_frames.setMaximum(50)
        self.spinBox_avg_frames.setProperty("value", 1)
        self.spinBox_avg_frames.setObjectName("spinBox_avg_frames")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_avg_frames)
        self.label_8 = QtWidgets.QLabel(self.frame_avg)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBox_avg_delay = QtWidgets.QSpinBox(self.frame_avg)
        self.spinBox_avg_delay.setMaximum(1000)
        self.spinBox_avg_delay.setObjectName("spinBox_avg_delay")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_avg_delay)
        self.verticalLayout_6.addWidget(self.frame_avg)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout_8.addWidget(self.toolBox)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem12)
        self.checkBox_profile = QtWidgets.QCheckBox(self.vF_control)
        self.checkBox_profile.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_profile.setFont(font)
        self.checkBox_profile.setObjectName("checkBox_profile")
        self.verticalLayout_8.addWidget(self.checkBox_profile)
        self.checkBox_pos_size = QtWidgets.QCheckBox(self.vF_control)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_pos_size.setFont(font)
        self.checkBox_pos_size.setObjectName("checkBox_pos_size")
        self.verticalLayout_8.addWidget(self.checkBox_pos_size)
        self.checkBox_send_pos = QtWidgets.QCheckBox(self.vF_control)
        self.checkBox_send_pos.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_send_pos.setFont(font)
        self.checkBox_send_pos.setObjectName("checkBox_send_pos")
        self.verticalLayout_8.addWidget(self.checkBox_send_pos)
        self.label_overexposed = QtWidgets.QLabel(self.vF_control)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_overexposed.setFont(font)
        self.label_overexposed.setTextFormat(QtCore.Qt.AutoText)
        self.label_overexposed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_overexposed.setWordWrap(False)
        self.label_overexposed.setObjectName("label_overexposed")
        self.verticalLayout_8.addWidget(self.label_overexposed)
        self.pushButton_saveImage = QtWidgets.QPushButton(self.vF_control)
        self.pushButton_saveImage.setEnabled(True)
        self.pushButton_saveImage.setStatusTip("")
        self.pushButton_saveImage.setWhatsThis("")
        self.pushButton_saveImage.setObjectName("pushButton_saveImage")
        self.verticalLayout_8.addWidget(self.pushButton_saveImage)
        self.verticalLayout.addWidget(self.vF_control)
        spacerItem13 = QtWidgets.QSpacerItem(250, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlliedVision viewer"))
        self.label_3.setText(_translate("MainWindow", "Положение [мм]"))
        self.label_Xpos.setText(_translate("MainWindow", "X:"))
        self.label_Ypos.setText(_translate("MainWindow", "Y:"))
        self.label_4.setText(_translate("MainWindow", "Размер [мм]"))
        self.label_sigX.setText(_translate("MainWindow", "sigX:"))
        self.label_sigY.setText(_translate("MainWindow", "sigY:"))
        self.pushButton_FitInView.setText(_translate("MainWindow", "FitInView"))
        self.pushButton_zoomIn.setText(_translate("MainWindow", "+"))
        self.pushButton_zoomOut.setText(_translate("MainWindow", "-"))
        self.pushButton_saveConfig.setText(_translate("MainWindow", "Сохранить настройки"))
        self.label_5.setText(_translate("MainWindow", "X: "))
        self.label_6.setText(_translate("MainWindow", "Y: "))
        self.label.setText(_translate("MainWindow", "Выбор камеры"))
        self.pushButton_turnOn.setText(_translate("MainWindow", "ВКЛ"))
        self.pushButton_turnOff.setText(_translate("MainWindow", "ВЫКЛ"))
        self.pushButton_refreshList.setText(_translate("MainWindow", "Обновить"))
        self.label_2.setText(_translate("MainWindow", "Выдержка, мкс"))
        self.label_MinMaxExp.setText(_translate("MainWindow", "Min = , Max = "))
        self.label_9.setText(_translate("MainWindow", "Gain, dB"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Экспозиция и усиление"))
        self.label_10.setText(_translate("MainWindow", "Источник"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Синхронизация"))
        self.checkBox_avg.setText(_translate("MainWindow", "Усреднение по нескольким кадрам"))
        self.label_7.setText(_translate("MainWindow", "Количество кадров"))
        self.label_8.setText(_translate("MainWindow", "Доп. задержка, мс"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Усреднение и фон"))
        self.checkBox_profile.setText(_translate("MainWindow", "Показать профиль"))
        self.checkBox_pos_size.setText(_translate("MainWindow", "Измерение размеров и положения"))
        self.checkBox_send_pos.setText(_translate("MainWindow", "Запустить сервер EPICS"))
        self.label_overexposed.setText(_translate("MainWindow", "Пересвеченные пиксели!"))
        self.pushButton_saveImage.setText(_translate("MainWindow", "Сохранить изображение"))

