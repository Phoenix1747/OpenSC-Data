#!/usr/bin/env python3
##
## Täglicher Verlauf des avg cps values.
##

import matplotlib.pyplot as plt
import time
import csv
from datetime import datetime
import matplotlib.dates as mdates

datestr = F"{time.strftime('%Y%m%d',time.localtime())}"
filename = "data/" + datestr + ".csv"
plotfile = "docs/images/daily.png"

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

#plt.style.use("seaborn")

plt.plot_date(x,y, linestyle="solid", linewidth=1.1, marker=",", color="orange")

plt.title("Last update: " + tolu, fontsize=9, loc="center")
plt.suptitle("Average CPS across the day (" + today + ")", ha="center")
plt.xlabel("Time (HH:MM)")
plt.ylabel("Average CPS")
plt.grid()
#plt.ylim(10.0,20.0)

date_format = mdates.DateFormatter("%H:%M")
plt.gca().xaxis.set_major_formatter(date_format)
plt.gcf().autofmt_xdate()

plt.savefig(plotfile)

#plt.show()
