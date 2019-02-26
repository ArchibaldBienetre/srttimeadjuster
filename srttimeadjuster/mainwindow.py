# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 333)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(762, 0))
        MainWindow.setMaximumSize(QtCore.QSize(762, 333))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopLevelLayout = QtWidgets.QVBoxLayout()
        self.TopLevelLayout.setObjectName("TopLevelLayout")
        self.inputFileSubLayout = QtWidgets.QHBoxLayout()
        self.inputFileSubLayout.setObjectName("inputFileSubLayout")
        self.inputFileEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFileEdit.setEnabled(True)
        self.inputFileEdit.setReadOnly(True)
        self.inputFileEdit.setObjectName("inputFileEdit")
        self.inputFileSubLayout.addWidget(self.inputFileEdit)
        self.selectInputFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectInputFileButton.setObjectName("selectInputFileButton")
        self.inputFileSubLayout.addWidget(self.selectInputFileButton)
        self.TopLevelLayout.addLayout(self.inputFileSubLayout)
        self.dialSubLayout = QtWidgets.QGridLayout()
        self.dialSubLayout.setObjectName("dialSubLayout")
        self.doubleSpinBoxSeconds = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxSeconds.setMinimum(-1000.0)
        self.doubleSpinBoxSeconds.setMaximum(1000.0)
        self.doubleSpinBoxSeconds.setSingleStep(0.1)
        self.doubleSpinBoxSeconds.setObjectName("doubleSpinBoxSeconds")
        self.dialSubLayout.addWidget(self.doubleSpinBoxSeconds, 1, 1, 1, 1)
        self.dialSeconds = QtWidgets.QDial(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialSeconds.sizePolicy().hasHeightForWidth())
        self.dialSeconds.setSizePolicy(sizePolicy)
        self.dialSeconds.setMinimumSize(QtCore.QSize(243, 100))
        self.dialSeconds.setMinimum(-1000)
        self.dialSeconds.setMaximum(1000)
        self.dialSeconds.setProperty("value", 0)
        self.dialSeconds.setSliderPosition(0)
        self.dialSeconds.setWrapping(True)
        self.dialSeconds.setNotchTarget(100.0)
        self.dialSeconds.setNotchesVisible(True)
        self.dialSeconds.setObjectName("dialSeconds")
        self.dialSubLayout.addWidget(self.dialSeconds, 1, 0, 1, 1)
        self.dialSecondsLabel = QtWidgets.QLabel(self.centralwidget)
        self.dialSecondsLabel.setObjectName("dialSecondsLabel")
        self.dialSubLayout.addWidget(self.dialSecondsLabel, 1, 2, 1, 1)
        self.TopLevelLayout.addLayout(self.dialSubLayout)
        self.outputFileSubLayout = QtWidgets.QHBoxLayout()
        self.outputFileSubLayout.setObjectName("outputFileSubLayout")
        self.outputFileEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFileEdit.setObjectName("outputFileEdit")
        self.outputFileSubLayout.addWidget(self.outputFileEdit)
        self.selectOutputFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectOutputFileButton.setObjectName("selectOutputFileButton")
        self.outputFileSubLayout.addWidget(self.selectOutputFileButton)
        self.TopLevelLayout.addLayout(self.outputFileSubLayout)
        self.generateOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateOutputButton.setObjectName("generateOutputButton")
        self.TopLevelLayout.addWidget(self.generateOutputButton)
        self.verticalLayout.addLayout(self.TopLevelLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        # START change to generated code
        # self.actionQuit.activated.connect(MainWindow.close)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        # END change to generated code

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SRT time adjuster"))
        self.selectInputFileButton.setText(_translate("MainWindow", "Select input file..."))
        self.dialSecondsLabel.setText(_translate("MainWindow", "seconds"))
        self.selectOutputFileButton.setText(_translate("MainWindow", "Select output file..."))
        self.generateOutputButton.setText(_translate("MainWindow", "Generate output"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))
        self.actionOpen_File.setToolTip(_translate("MainWindow", "Open Srt File"))

