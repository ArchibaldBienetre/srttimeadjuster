
import unittest 
import sys
from ..src.srtdataset import SrtDataSet
from datetime import timedelta

# run with this command: 
#  ~/projects $ python -m srttimeadjuster.tests.srtdatasettest


class SrtDataSetTest(unittest.TestCase):
	def testParseDataSetFromString(self):
		"""simple test that SrtDataSet can parse a data set"""
		self.assertTrue(True)
		
	def test(self):
		"""blah"""
		#testData = SrtDataSet(1041, datetime.time(1, 37, 25, 200000),  datetime.time(1,  37,  30,  700000),  "Traduction : Attila0375\nhttp://attilaswebsite.free.fr" )
		#print (testData.toString())
		testData = SrtDataSet.fromLines("1041\n01:37:25,200 --> 01:37:30,700\nTraduction : Attila0375\nhttp://attilaswebsite.free.fr".split("\n"))
		print (testData.toString())
		testData.applyDelta(timedelta(seconds=-5))
		print (testData.toString())
	

#t = SrtDataSetTest()
#t.test()


def main():
    unittest.main()

if __name__ == '__main__':
    main()
