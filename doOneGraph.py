#
# calculate all graphs
#
# SwitchDoc Labs March 30, 2015

import sys
sys.path.append('/home/pi/SDL_Pi_ProjectCuracao2/graphs')

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Check for user imports
try:
        import conflocal as config
except ImportError:
        import config


import BootUpTimeGraph
import TemperatureHumidityGraph 
import PowerCurrentGraph 
import PowerVoltageGraph 
import BarometerLightningGraph 

def doAllGraphs():

	if (config.enable_MySQL_Logging == True):	

		#BarometerLightningGraph.BarometerLightningGraph('test', 10, 0)
		#TemperatureHumidityGraph.TemperatureHumidityGraph('test', 10, 0)
		#PowerCurrentGraph.PowerCurrentGraph('test', 10, 0)
		#PowerVoltageGraph.PowerVoltageGraph('test', 10, 0)
		BootUpTimeGraph.BootUpTimeGraph('test', 365, 0)




doAllGraphs()
