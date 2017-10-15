#!/usr/bin/env python


"""
PanTilt.py
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





# Check for user imports
try:
        import conflocal as config
except ImportError:
        import config


import sendemail

import pclogging


batteryVoltage =0
batteryCurrent =0
solarVoltage  =0
solarCurrent =0

def setTiltServo(pwm,value):
        servoMin = 150  # Min pulse length out of 4096
        servoMax = 620  # Max pulse length out of 4096
        pwm.setPWM(14,0, value)

        '''
	degrees = -degrees+90
        servoPerDegree= (servoMax - servoMin)/180.0
        if ((degrees > -45) and (degrees < 135)):
                pwm.setPWM(14,0, int((degrees+45)*servoPerDegree+servoMin))
	'''


def setPanServo(pwm,value):
        servoMin = 100  # Min pulse length out of 4096
        servoMax = 500  # Max pulse length out of 4096
        pwm.setPWM(15,0, int(value))

        '''
	servoPerDegree= (servoMax - servoMin)/270.0
        degrees = -degrees
        if ((degrees > -135) and (degrees < 135)):
                value = ((degrees+135)*servoPerDegree+servoMin)
                pwm.setPWM(15,0, int(value))
	'''




def shutOffPanTilt(pwm):
        pwm.softwareReset()



"""
        for x in range(-45,135):
                setTiltServo(x)
                time.sleep(0.1)

        for x in range(-135,135):
                setPanServo(x)
                time.sleep(0.1)

        shutOffServo()
        print "servo off"
        time.sleep(20)
"""


# Camera stuff

def takeSinglePicture(camera, pwm, pan, tilt, name ):



        setTiltServo(pwm, tilt)
	time.sleep(1.0)
        setPanServo(pwm, pan)

	time.sleep(1.0)
        camera.capture(name)

        shutOffPanTilt(pwm)



def  takeRaspiStill(source, pwm, pan, tilt):


        setTiltServo(pwm, tilt)
	time.sleep(1.0)
        setPanServo(pwm, pan)
	time.sleep(1.0)


        try:
	         f = open("/home/pi/SDL_Pi_ProjectCuracao2/state/exposure.txt", "r")
	         tempString = f.read()
	         f.close()
	         lowername = tempString

        except IOError as e:
		 lowername = "auto"

	#lowername = "auto"
	#filename = "/home/pi/RasPiConnectServer/static/picameraraw.jpg" 
	filename = "/home/pi/SDL_Pi_ProjectCuracao2/static/picameraraw.jpg" 
	filenameout = "/home/pi/SDL_Pi_ProjectCuracao2/static/picamera.jpg" 
	exposuremode = lowername
	# take picture
	print "taking picture"
	#cameracommand = "raspistill -o " + filename + " -rot 180 -t 750 -ex " + exposuremode
	cameracommand = "raspistill -o " + filename + " -t 750 -ex " + exposuremode
	print cameracommand
	output = subprocess.check_output (cameracommand,shell=True, stderr=subprocess.STDOUT )
	output = subprocess.check_output("convert '"+ filename + "' -pointsize 72 -fill white -gravity SouthWest -annotate +50+100 'ProjectCuracao2 %[exif:DateTimeOriginal]' '" + filenameout +"'", shell=True, stderr=subprocess.STDOUT)

	pclogging.log(pclogging.INFO, __name__, source )
        shutOffPanTilt(pwm)

	print "finished taking picture"
	return lowername


def takeAndSendPicture(source, pwm, pan, tilt ):
	
	#try:
       	exposure = takeRaspiStill(source,pwm, pan, tilt)
		
       	bodyText =  "\n" + "BV=%0.2fV/BC=%0.2fmA/SV=%0.2fV/SC=%0.2fmA/%s" % (batteryVoltage, batteryCurrent, solarVoltage, solarCurrent,exposure)

	sendemail.sendEmail("TestPicture", bodyText, "Project Curacao2 Picture \n", config.notifyAddress,  config.fromAddress, "static/picamera.jpg")
	#except:
       	#print "Camera Failed"

	return
