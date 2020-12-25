#!/usr/bin/env python3
##
## Daily and monthly trends of average cps rates. Refreshed every 15 minutes.
##

import matplotlib.pyplot as plt
import time
import csv
from datetime import datetime, date
import calendar
import matplotlib.dates as mdates
import os

fullpath = os.path.dirname(os.path.abspath(__file__)) + "/"

def doplot(x,y,title,tolu,date_formatter,xlabel,path):
	plotfile = fullpath + path

	plt.plot_date(x,y, linestyle="solid", linewidth=1.1, marker=",", color="orange")

	plt.title("Last update: " + tolu, fontsize=9, loc="center")
	plt.suptitle(title, ha="center")
	plt.xlabel(xlabel)
	plt.ylabel("Avg. counts per second")
	plt.grid()
	plt.ylim(min(y) - 3,max(y) + 3)

	plt.gca().xaxis.set_major_formatter(date_format)
	plt.gcf().autofmt_xdate()

	plt.savefig(plotfile)
	plt.close()

def dailypng():
        datestr = F"{time.strftime('%Y%m%d',time.localtime())}"
        filename = fullpath + "data/" + datestr + ".csv"

        x = []
        y = []

        with open(filename,newline="") as file:
                csvread = csv.reader(file, delimiter=',')
                for row in csvread:
                        dstring = datestr + row[0]
                        x.append(datetime.strptime(dstring,"%Y%m%d%H%M"))
                        y.append(float(row[1]))

        today = x[len(x)-1].strftime("%Y-%m-%d")
        tolu = x[len(x)-1].strftime("%H:%M") #time of last update

        doplot(x,y,"Average cps across the day (" + today + ")",tolu,mdates.DateFormatter("%H:%M"),"Time (HH:MM)","docs/images/daily.png")

def monthlypng():
	files = []

	year = datetime.now().year
	month = datetime.now().month
	num_days = calendar.monthrange(year, month)[1]
	days = [date(year, month, day) for day in range(1, num_days+1)]

	for day in days:
		files.append(day.strftime("%Y%m%d"))

	x = []
	y = []
	count = 0

	for daystr in files:
		filename = fullpath + "data/" + daystr + ".csv"
		try:
			with open(filename,newline="") as file:
				avg = 0
				mcount = 0

				csvread = csv.reader(file, delimiter=',')
				for row in csvread:
					avg += float(row[1])
					mcount += 1

				avg /= mcount
				x.append(datetime.strptime(daystr,"%Y%m%d"))
				y.append(round(avg,2))
			count += 1
		except:
			continue #just continue with the days that exist

	tolu = time.strftime('%Y-%m-%d',time.localtime()) #time of last update
	substring = "Daily average cps month of " + calendar.month_name[month] + " " + str(year)

	doplot(x,y,substring,tolu,mdates.DateFormatter("%d"),"Day Of Month","docs/images/monthly.png")
