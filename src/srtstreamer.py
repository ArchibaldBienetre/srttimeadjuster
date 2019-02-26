from srtdataset import SrtDataSet

from datetime import timedelta
import re


# def test():
# streamer = SrtStreamer("/home/hoo/Desktop/lesrivierespourpres-1cd (modified).srt",  "/home/hoo/Desktop/testSrtOut.srt",  timedelta(seconds=-5))
# streamer.streamConvert()

class SrtStreamer:
    """ simple class to read from an SRT file, convert the time stamps in it  by a given delta, and write to an output location"""

    def __init__(self, inputFilePath, outputFilePath, delta):
        self.inputFile = open(inputFilePath, 'r')
        self.outputFile = open(outputFilePath, 'w')
        self.delta = delta

    def streamConvert(self):
        buffer = []
        for line in self.inputFile:
            if (re.match('^\s*$', line)):
                ds = SrtDataSet.fromLines(buffer)
                ds.applyDelta(self.delta)
                self.outputFile.write(ds.toString())
                buffer = []
            else:
                buffer.append(line.strip())
        self.inputFile.close()
        self.outputFile.close()

# test()
