# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Nov 28 16:34:19 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(762, 333)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(762, 0))
        MainWindow.setMaximumSize(QtCore.QSize(762, 333))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TopLevelLayout = QtGui.QVBoxLayout()
        self.TopLevelLayout.setObjectName(_fromUtf8("TopLevelLayout"))
        self.inputFileSubLayout = QtGui.QHBoxLayout()
        self.inputFileSubLayout.setObjectName(_fromUtf8("inputFileSubLayout"))
        self.inputFileEdit = QtGui.QLineEdit(self.centralwidget)
        self.inputFileEdit.setEnabled(True)
        self.inputFileEdit.setReadOnly(True)
        self.inputFileEdit.setObjectName(_fromUtf8("inputFileEdit"))
        self.inputFileSubLayout.addWidget(self.inputFileEdit)
        self.selectInputFileButton = QtGui.QPushButton(self.centralwidget)
        self.selectInputFileButton.setObjectName(_fromUtf8("selectInputFileButton"))
        self.inputFileSubLayout.addWidget(self.selectInputFileButton)
        self.TopLevelLayout.addLayout(self.inputFileSubLayout)
        self.dialSubLayout = QtGui.QGridLayout()
        self.dialSubLayout.setObjectName(_fromUtf8("dialSubLayout"))
        self.doubleSpinBoxSeconds = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxSeconds.setMinimum(-1000.0)
        self.doubleSpinBoxSeconds.setMaximum(1000.0)
        self.doubleSpinBoxSeconds.setSingleStep(0.1)
        self.doubleSpinBoxSeconds.setObjectName(_fromUtf8("doubleSpinBoxSeconds"))
        self.dialSubLayout.addWidget(self.doubleSpinBoxSeconds, 1, 1, 1, 1)
        self.dialSeconds = QtGui.QDial(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        self.dialSeconds.setObjectName(_fromUtf8("dialSeconds"))
        self.dialSubLayout.addWidget(self.dialSeconds, 1, 0, 1, 1)
        self.dialSecondsLabel = QtGui.QLabel(self.centralwidget)
        self.dialSecondsLabel.setObjectName(_fromUtf8("dialSecondsLabel"))
        self.dialSubLayout.addWidget(self.dialSecondsLabel, 1, 2, 1, 1)
        self.TopLevelLayout.addLayout(self.dialSubLayout)
        self.outputFileSubLayout = QtGui.QHBoxLayout()
        self.outputFileSubLayout.setObjectName(_fromUtf8("outputFileSubLayout"))
        self.outputFileEdit = QtGui.QLineEdit(self.centralwidget)
        self.outputFileEdit.setObjectName(_fromUtf8("outputFileEdit"))
        self.outputFileSubLayout.addWidget(self.outputFileEdit)
        self.selectOutputFileButton = QtGui.QPushButton(self.centralwidget)
        self.selectOutputFileButton.setObjectName(_fromUtf8("selectOutputFileButton"))
        self.outputFileSubLayout.addWidget(self.selectOutputFileButton)
        self.TopLevelLayout.addLayout(self.outputFileSubLayout)
        self.generateOutputButton = QtGui.QPushButton(self.centralwidget)
        self.generateOutputButton.setObjectName(_fromUtf8("generateOutputButton"))
        self.TopLevelLayout.addWidget(self.generateOutputButton)
        self.verticalLayout.addLayout(self.TopLevelLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SRT time adjuster", None))
        self.selectInputFileButton.setText(_translate("MainWindow", "Select input file...", None))
        self.dialSecondsLabel.setText(_translate("MainWindow", "seconds", None))
        self.selectOutputFileButton.setText(_translate("MainWindow", "Select output file...", None))
        self.generateOutputButton.setText(_translate("MainWindow", "Generate output", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File...", None))
        self.actionOpen_File.setToolTip(_translate("MainWindow", "Open Srt File", None))

