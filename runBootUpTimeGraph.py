
#
# calculate all graphs
#
# SwitchDoc Labs March 30, 2015

import sys
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)


import BootUpTimeGraph 


BootUpTimeGraph.BootUpTimeGraph('test', 10, 0)

