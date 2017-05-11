#!/usr/bin/env python


"""
testServoCamera.py
JCS 08/17/2015 Version 1.0
"""


from datetime import datetime, timedelta
import sys
import time
import serial

import sys
import time
import datetime
import random
import subprocess


sys.path.append('./Adafruit_PWM_Servo_Driver')

#/*=========================================================================*/

# Main Program

print ""
print "Test Servo and Camera Version 1.0 - SwitchDoc Labs"
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()



from Adafruit_PWM_Servo_Driver import PWM





# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x50)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x50, debug=True)





def setTiltServo(degrees):
        servoMin = 150  # Min pulse length out of 4096
        servoMax = 600  # Max pulse length out of 4096

        degrees = -degrees+90
        servoPerDegree= (servoMax - servoMin)/180.0
        if ((degrees >= -45) and (degrees <= 135)):
		value = int((degrees+45)*servoPerDegree+servoMin)
		print "tilt degrees, value=%x, %x", (degrees, value)
                pwm.setPWM(14,0, int((degrees+45)*servoPerDegree+servoMin))


def setPanServo(degrees):
        servoMin = 150  # Min pulse length out of 4096
        servoMax = 600  # Max pulse length out of 4096

        servoPerDegree= (servoMax - servoMin)/270.0
        degrees = -degrees
        if ((degrees >= -135) and (degrees <= 135)):
                value = ((degrees+135)*servoPerDegree+servoMin)
		print "pan degrees, value=%x, %x", (degrees, value)
                pwm.setPWM(14,0, int(value))



def shutOffServo():
        pwm.softwareReset()

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


'''
while (True):

        for x in range(-45,135,10):
                #time.sleep(1.0)
                time.sleep(0.1)

        for x in range(-135,135,10):
                setPanServo(x)
                time.sleep(1.0)

        shutOffServo()
        print "servo off"
        time.sleep(20)
'''

pwm.setPWM(14,0,550)
time.sleep(5.0)
pwm.setPWM(15,0,300)
time.sleep(5.0)
'''
for x in range(100,500,10):
                pwm.setPWM(15,0, x)
                time.sleep(0.3)
'''
shutOffServo()

'''
while (True):

        for x in range(150,620,10):
                pwm.setPWM(14,0, x)
		print x
                time.sleep(0.3)

        
	for x in range(100,500,10):
                pwm.setPWM(15,0, x)
                time.sleep(0.3)

        #shutOffServo()
        #print "servo off"
        time.sleep(20)
'''


