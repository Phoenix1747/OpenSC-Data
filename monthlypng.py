#!/usr/bin/env python3
##
## Monatlicher Verlauf des täglichen cps Durchschnitts.
##

import matplotlib.pyplot as plt
import time
import csv
from datetime import datetime, date
#from datetime import date
import calendar
import matplotlib.dates as mdates
import os

files = []

fullpath = os.path.dirname(os.path.abspath(__file__)) + "/"

year = datetime.now().year
month = datetime.now().month
num_days = calendar.monthrange(year, month)[1]
days = [date(year, month, day) for day in range(1, num_days+1)]

for day in days:
	files.append(day.strftime("%Y%m%d"))

plotfile = fullpath + "docs/images/monthly.png" #str(year) + str(month) + ".png"

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
		continue
		#just continue with the days that exist

tolu = time.strftime('%Y-%m-%d',time.localtime()) #time of last update
substring = "Daily average CPS month of " + calendar.month_name[month] + " " + str(year)

#plt.style.use("seaborn")

plt.plot_date(x,y, linestyle="solid", linewidth=1.1, marker=",", color="orange")

plt.title("Last update: " + tolu, fontsize=9, loc="center")
plt.suptitle(substring, ha="center")
plt.xlabel("Day Of Month")
plt.ylabel("Average CPS")
plt.grid()
#plt.ylim(10.0,20.0)

date_format = mdates.DateFormatter("%d")
plt.gca().xaxis.set_major_formatter(date_format)
plt.gcf().autofmt_xdate()

plt.savefig(plotfile)

#plt.show()
