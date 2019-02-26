import sys
from PyQt4 import QtGui
import mainwindow

from dialstate import DialState
from srtstreamer import SrtStreamer
from datetime import timedelta

"""
An application that reads an SRT file 
( https://en.wikipedia.org/wiki/SubRip#SubRip_text_file_format )
with content like this...

1041
01:37:25,000 --> 01:37:30,000
Traduction : Attila0375
http://attilaswebsite.free.fr

... into an array of subtitle data sets,  
and can adjust all timestamps in that dataset bu a given delta
and write the data back out as another SRT file.

This is my first attempt at writing a python UI using Qt, let's see how it works out!
"""


# note to self: pyuic4 mainwindow.ui > mainwindow.py
class Main(QtGui.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.dialState = DialState(self.ui.dialSeconds, self.ui.doubleSpinBoxSeconds)

        self.ui.selectInputFileButton.clicked.connect(self.showSelectInputFileDialog)
        self.ui.actionOpen_File.triggered.connect(self.showSelectInputFileDialog)
        self.ui.selectOutputFileButton.clicked.connect(self.showSelectOutputFileDialog)
        self.ui.generateOutputButton.clicked.connect(self.processFiles)

    def showSelectInputFileDialog(self):
        fpath = QtGui.QFileDialog.getOpenFileName(self, 'Open SRT file', '/home',
                                                  'SRT files (*.srt *.SRT)')  # '*.srt *.SRT;; Text files (*.txt)')
        self.ui.inputFileEdit.setText(fpath)

    def showSelectOutputFileDialog(self):
        fpath = QtGui.QFileDialog.getSaveFileName(self, 'Select file to save to', '/home/output.srt',
                                                  'SRT file (*.srt)')
        self.ui.outputFileEdit.setText(fpath)

    def getInputFilePath(self):
        return self.ui.inputFileEdit.text()

    def getOutputFilePath(self):
        return self.ui.outputFileEdit.text()

    def getDelta(self):
        return timedelta(seconds=self.dialState.getActualSecondsValue())

    def processFiles(self):
        streamer = SrtStreamer(self.getInputFilePath(), self.getOutputFilePath(), self.getDelta())
        streamer.streamConvert()
        msgBox = QtGui.QMessageBox.information(self, "Success",
                                               "The converted output has been saved to " + self.getOutputFilePath(),
                                               "OK")


def main():
    app = QtGui.QApplication(sys.argv)

    my_mainWindow = Main()
    my_mainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
