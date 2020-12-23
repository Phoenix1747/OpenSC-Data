#!/usr/bin/env python

import serial
import time
import csv
import os

ser = serial.Serial("/dev/ttyACM0", 2000000)
ser.flushInput()

while True:
	try:
		ser_bytes = ser.readline()

		filename = "data/" + time.strftime('%Y%m%d',time.localtime()) + ".csv"
		timestr = time.strftime('%H%M',time.localtime())

		data = float(ser_bytes.decode("utf-8"))

		with open(filename,"a",newline="") as file:
			writer = csv.writer(file, delimiter=",")
			writer.writerow([timestr,data])

		os.system("python3 dailypng.py &")
		os.system("python3 monthlypng.py &")
	except:
		continue

