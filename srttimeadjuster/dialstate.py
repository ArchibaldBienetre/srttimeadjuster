from PyQt5 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


# TODO make this into an own QDial subclass named "RollingDial" or something
class DialState:
    dialScaling = 100.0

    def __init__(self, dial, spinbox):
        self.dial = dial
        self.spinbox = spinbox
        dial.valueChanged.connect(self.updateFromDial)

        # should not register on valueChanged, or setting it when the dial is changed would trigger it to be set again...?
        spinbox.valueChanged.connect(self.updateFromSpinbox)
        # spinbox.editingFinished.connect(self.updateFromSpinbox)

        # custom instance variables...
        # ... cached old dial value
        self.oldDialValue = dial.value()
        # ... accumulated full turns time adjustment
        self.fullTurns = 0.0

        # custom constants...
        # ... adjustment per full turn
        self.adjustmentPerTurn = dial.maximum() - dial.minimum()
        # ... boundary to lower quarter of dial
        self.lowerQuarterBoundary = dial.minimum() + (self.adjustmentPerTurn / 4.0)
        # ... boundary to upper quarter of dial
        self.upperQuarterBoundary = dial.maximum() - (self.adjustmentPerTurn / 4.0)

        self.actualValue = (self.oldDialValue + self.adjustmentPerTurn * self.fullTurns) / DialState.dialScaling

    def isInLowestQuarterOfDial(self, num):
        return self.lowerQuarterBoundary > num

    def isInHighestQuarterOfDial(self, num):
        return self.upperQuarterBoundary < num

    def updateFromDial(self):
        # ignore when the dial position is set from the spin box
        if not self.dial.isSliderDown:
            return

        # if this completes a full circle, keep adding / subtracting
        tempValue = self.dial.value()
        if (self.isInLowestQuarterOfDial(tempValue) and self.isInHighestQuarterOfDial(self.oldDialValue)):
            self.fullTurns += 1
        elif (self.isInHighestQuarterOfDial(tempValue) and self.isInLowestQuarterOfDial(self.oldDialValue)):
            self.fullTurns -= 1

        self.oldDialValue = tempValue
        self.actualValue = (tempValue + self.adjustmentPerTurn * self.fullTurns) / DialState.dialScaling
        self.spinbox.setValue(self.actualValue)

    def spinboxClicked(self):
        pass

    def updateFromSpinbox(self):
        self.actualValue = self.spinbox.value()

        tempValue = self.actualValue * DialState.dialScaling

        self.fullTurns = (tempValue - self.dial.minimum()) // self.adjustmentPerTurn

        self.oldDialValue = tempValue - (self.adjustmentPerTurn * self.fullTurns)

        self.dial.setValue(self.oldDialValue)

    def getActualSecondsValue(self):
        return self.actualValue
