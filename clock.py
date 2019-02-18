#!/usr/bin/python
from Tkinter import *
from time import localtime,strftime
from datetime import datetime,timedelta
import math

class clock:

	def updateClock(self):
		# show clock
		self.timeStr.set(strftime("%I:%M %p", localtime()))

		# show countdown timer
		if datetime.now() > self.target:
			delta = datetime.now() - self.target
			t = delta.seconds / 60
			if t == 1:
				word = " minute "
			else:
				word = " minutes "
			self.countStr.set(str(t)+word+"past end time")
			self.status.config(fg="red")
			self.time.config(fg="#CCCCCC")
		else:
			delta = self.target - datetime.now()
			if delta.seconds < self.show:
				t = int(math.ceil(delta.seconds / 60.0))
				if t == 1:
					word = " minute "
				else:
					word = " minutes "
				self.countStr.set(str(t)+word+"remaining")


		# schedule update
		self.root.update()
		self.root.after(2000, self.updateClock)

	def __init__(self, countdown):
		self.root = Tk()

		self.root.configure(background="black")
		self.root.title("Test Countdown Clock")
		self.timeStr  = StringVar()
		self.countStr = StringVar()
		self.show     = countdown[1]
		self.target   = datetime.now() + timedelta(seconds=countdown[0])
		
		self.time = Label(self.root, textvariable=self.timeStr, 
			font="Arial 300 bold", fg="white", background="black")
		self.time.pack()
		self.status = Label(self.root, textvariable=self.countStr, 
			font="Arial 80 bold", fg="white", background="black")
		self.status.pack()
		self.updateClock()
		self.root.mainloop()

if __name__ == "__main__":
	duration = datetime(2019, 2, 18, 11, 51, 00)-datetime.now()
	countdown=(duration.seconds, 30*60)
	clock(countdown)
