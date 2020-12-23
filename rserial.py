#!/usr/bin/env python

import serial
import time
import csv
import os

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

		os.system("python3 " + fullpath + "dailypng.py &")
		os.system("python3 " + fullpath +  "monthlypng.py &")

		with open(indexfile+".orig","r") as file:
			content = file.read()
			content.replace("$current", data)
	#except:
	#	continue
