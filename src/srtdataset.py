
from datetime import timedelta

import datetime
import time

	
#Simple class to encapsulate an SRT data set like this:
# 
#1041
#01:37:25,200 --> 01:37:30,700
#Traduction : Attila0375
#http://attilaswebsite.free.fr
#    Note to self: https://docs.python.org/3/library/datetime.html
class SrtDataSet:
	"""Single SRT dataset"""
	
	def __init__(self, index,  timeDeltaFrom,  timeDeltaTo, text):
		self.index = index
		self.timeDeltaFrom = timeDeltaFrom
		self.timeDeltaTo = timeDeltaTo
		self.text = text
		
	@classmethod
	def fromLines(cls,  lines):
		index = int(lines[0])
		tempTimes = lines[1].strip().split(" --> ")
		tempTimeFrom = time.strptime(tempTimes[0], "%H:%M:%S,%f")
		tempTimeTo = time.strptime(tempTimes[1], "%H:%M:%S,%f")
		# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
		timeDeltaFrom = timedelta(0,  tempTimeFrom.tm_sec,  0,  int(tempTimes[0].split(",")[1]),  tempTimeFrom.tm_min,  tempTimeFrom.tm_hour,  0)
		timeDeltaTo =   timedelta(0,  tempTimeTo.tm_sec, 0,  int(tempTimes[1].split(",")[1]),  tempTimeTo.tm_min,  tempTimeTo.tm_hour,  0)
		text = "\n".join(lines[2:])
		return cls(index,  timeDeltaFrom,  timeDeltaTo,  text)
		
		
	def applyDelta(self,  delta):
		self.timeDeltaFrom = self.timeDeltaFrom + delta
		self.timeDeltaTo = self.timeDeltaTo + delta
	
	def timeToString(self,  time):
		return "{:%H:%M:%S,}{:03d}".format(time,  time.microseconds / 1000)
		
	def  deltaToString(self,  delta):
		h = delta.seconds // 3600
		m = (delta.seconds % 3600) // 60
		s = delta.seconds % 60
		ms = delta.microseconds // 1000
#        print(delta.seconds)
#        print("{:02d}".format(h))
#        print("{:02d}".format(m))
#        print("{:02d}".format(s))
#        print("{:03d}".format(ms))
		return "{:02d}:{:02d}:{:02d},{:03d}".format(h,  m,  s,  ms)
		
	def toString(self):
		return "{:d}\n{} --> {}\n{}\n\n".format(self.index, self.deltaToString(self.timeDeltaFrom), self.deltaToString(self.timeDeltaTo), self.text)
#        return "{:d}\n{:%H:%M:%S,}{:03d} --> {:%H:%M:%S,}{:03d}\n{}"\
#        return "{}\n{:%H:%M:%S},000 --> {:%H:%M:%S},000\n{}".format(self.index, self.timeFrom,  self.timeTo, self.text)
#        return str(self.index) +"\n" + self.timeFrom.strftime(format) + " --> " + self.timeFrom.strftime(format) + "\n" + self.text + "\n"

