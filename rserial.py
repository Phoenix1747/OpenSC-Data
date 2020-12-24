#!/usr/bin/env python3
##
## Regularly gets the serial output value of the OpenSC, saves data and does other stuff
##

import serial
import time
import csv
import os
import pnggen #must be same directory!

ser = serial.Serial("/dev/ttyACM0", 2000000)
ser.flushInput()

fullpath = os.path.dirname(os.path.abspath(__file__)) + "/"

indexfile = fullpath + "docs/index.html"

while True:
	#try:
		ser_bytes = ser.readline()

		filename = fullpath + "data/" + time.strftime('%Y%m%d',time.localtime()) + ".csv"
		timestr = time.strftime('%H%M',time.localtime())

		data = float(ser_bytes.decode("utf-8"))

		with open(filename,"a",newline="") as file:
			writer = csv.writer(file, delimiter=",")
			writer.writerow([timestr,data])

		pnggen.dailypng() #generate pngs for webpage
		pnggen.monthlypng()

		indexrepl = {
			"$current" : str(data),
			"$lastup" : time.strftime("%Y-%m-%d, %H:%M",time.localtime())
			} #holds all values to be replaced in web

		with open(indexfile + ".orig", "r") as file:
			content = file.read() #read whole file to string
			for key in indexrepl: #replace all values
				content = content.replace(key, indexrepl[key])
			with open(indexfile, "w") as f: #save file with new values
				f.write(content)
	#except:
	#	continue
