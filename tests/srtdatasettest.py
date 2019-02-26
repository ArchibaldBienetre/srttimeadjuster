import unittest
from srttimeadjuster.srtdataset import SrtDataSet
from datetime import timedelta


class SrtDataSetTest(unittest.TestCase):
    def testParseDataSetFromString(self):
        """simple test that SrtDataSet can parse a data set"""
        self.assertTrue(True)

    def test(self):
        """manual test - just printing a conversion result"""
        testData = SrtDataSet.fromLines(
            "1041\n01:37:25,200 --> 01:37:30,700\nTraduction : Attila0375\nhttp://attilaswebsite.free.fr".split("\n"))
        print(testData.toString())
        testData.applyDelta(timedelta(seconds=-5))
        print(testData.toString())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
