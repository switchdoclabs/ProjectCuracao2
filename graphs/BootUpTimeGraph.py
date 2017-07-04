
# BootUpTimeGraph.py
# filename: BootUpTimeGraph.py
# Version 1.0 06/03/17
# Version 1.4 03/30/15
#
# contains event routines for data collection
#
#

import sys
import time
import RPi.GPIO as GPIO

import gc
import datetime

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

from matplotlib import pyplot
from matplotlib import dates

import pylab

import MySQLdb as mdb

# Check for user imports
try:
        import conflocal as config
except ImportError:
        import config

def  BootUpTimeGraph(source,days,delay):


	
	print("BootUpTimeGraph source:%s days:%s delay:%i" % (source,days,delay))
	print("sleeping :",delay)
	time.sleep(delay)
	print("BootUpTimeGraph running now")
	
        # blink GPIO LED when it's run
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, True)
        time.sleep(0.2)
        GPIO.output(18, False)

	# now we have get the data, stuff it in the graph 

	try:
		print("trying database")
    		db = mdb.connect('localhost', 'root', config.MySQL_Password, 'ProjectCuracao2');

    		cursor = db.cursor()

		query = "SELECT CONVERT_TZ(TimeStamp, '+00:00', '-04:00'), Message, HOUR(CONVERT_TZ(TimeStamp, '+00:00', '-04:00')), MINUTE(TimeStamp), SECOND(TimeStamp)  FROM systemlog WHERE  (now() - interval %i hour < TimeStamp" % (days*24) + ") AND Message LIKE 'ProjectCuracao2 Startup Version%' AND TimeStamp > '2017-06-18 00:00:00'"
		print query
		cursor.execute(query)
		result = cursor.fetchall()

		t = []
		s = []
		u = []
		v = []
		#x = []
		
		for record in result:
  			t.append(record[0])

			mysql_time = record[0]

			print mysql_time
			hours  = record[2] 
			print hours
			minutes  = record[3] 
			print minutes
			seconds =  record[4]
			print seconds

			numSeconds = hours * 3600 + minutes * 60 + seconds
			numSeconds  = numSeconds / 3600.0
			print numSeconds
  			s.append(numSeconds)
		fig = pyplot.figure()


		print ("count of t=",len(t))
		#print (t)
		if (len(t) == 0):
			return
		#dts = map(datetime.datetime.fromtimestamp, t)
		#print dts
		#fds = dates.date2num(t) # converted
		# matplotlib date format object
		hfmt = dates.DateFormatter('%m/%d-%H')

		fig.set_facecolor('white')
		ax = fig.add_subplot(111,axisbg = 'white')
		#ax.vlines(fds, -200.0, 1000.0,colors='w')

		ax.xaxis.set_major_locator(dates.HourLocator(interval=48))
		ax.xaxis.set_major_formatter(hfmt)
		ax.set_ylim(bottom = -200.0)
		pyplot.xticks(rotation='vertical')
		pyplot.subplots_adjust(bottom=.3)
		pylab.plot(t, s, color='r',label="BootUp Time",linestyle="-",marker="^")
		pylab.xlabel("Time")
		pylab.ylabel("Hour of Day")
		pylab.legend(loc='upper left')

		pylab.axis([min(t), max(t), 0, 24])
		pylab.figtext(.5, .05, ("ProjectCuracao2 BootUp Time Last %i Days" % days),fontsize=18,ha='center')
		pyplot.setp( ax.xaxis.get_majorticklabels(), rotation=70)

		pylab.grid(True)

		pyplot.show()
		try:
			pyplot.savefig("/home/pi/RasPiConnectServer/static/BootUpTimeGraph.png",facecolor=fig.get_facecolor())	
		except:
			pyplot.savefig("/home/pi/SDL_Pi_ProjectCuracao2/static/BootUpTimeGraph.png",facecolor=fig.get_facecolor())	


	except mdb.Error, e:
  
    		print "Error %d: %s" % (e.args[0],e.args[1])
    
	finally:    

		cursor.close()       	 
        	db.close()

		del cursor
		del db

		fig.clf()
		pyplot.close()
		pylab.close()
		del t, s, u, v
		gc.collect()
		print("BootUpTimeGraph finished now")
