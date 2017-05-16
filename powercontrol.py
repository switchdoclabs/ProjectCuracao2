#
#
# Power Control for Project Curacao2 
#
# SwitchDoc Labs
# May  2017
#
# Version 1.1


import  SDL_Pi_GrovePowerSave
import  SDL_Pi_GrovePowerDrive

import RPi.GPIO as GPIO
import time

import pclogging

# Check for user imports
try:
        import conflocal as config
except ImportError:
        import config


GPIO.setmode(GPIO.BCM)


PowerSave_GPIO_AirQuality = 4
PowerSave_GPIO_LoRa = 5
PowerSave_GPIO_OLED = 12
PowerDrive_GPIO_Fan = 26

USBPowerControl_Enable = 21
USBPowerControl_Control = 20
GPIO.setup(USBPowerControl_Enable, GPIO.OUT, initial=True)
GPIO.setup(USBPowerControl_Control, GPIO.OUT, initial=True)

myPowerSaveAirQuality = SDL_Pi_GrovePowerSave.SDL_Pi_GrovePowerSave(PowerSave_GPIO_AirQuality, True)
myPowerSaveLoRa = SDL_Pi_GrovePowerSave.SDL_Pi_GrovePowerSave(PowerSave_GPIO_LoRa, True)
myPowerSaveOLED = SDL_Pi_GrovePowerSave.SDL_Pi_GrovePowerSave(PowerSave_GPIO_OLED, True)
myPowerDriveFan = SDL_Pi_GrovePowerDrive.SDL_Pi_GrovePowerDrive(PowerDrive_GPIO_Fan, PowerDrive_GPIO_Fan, True, True)



def turnAllOn():

	# Air Quality Sensor Off
	myPowerSaveAirQuality.setPowerSave(True)
	config.AirQuality_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: AirQuality Turned: %s" % "ON")

	# LoRa Reciever On	
	myPowerSaveLoRa.setPowerSave(True)
	config.LORA_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: LoRa Turned: %s" % "ON") 


	# OLED Display On
	myPowerSaveOLED.setPowerSave(True)
	config.OLED_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: OLED Turned: %s" % "ON")

	# Fan Off
	myPowerDriveFan.setPowerDrive(1, True)
	config.Fan_Drive_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: Fan Turned: %s" % "ON")

	# turn on USBPowerControl Controlling WiFi Dongle

	GPIO.output(USBPowerControl_Enable, True)
	GPIO.output(USBPowerControl_Control, True)
	config.WiFi_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: WiFi Turned: %s" % "ON")



	print "Turn On All Power"


def initialPowerState():



	# Air Quality Sensor Off
	myPowerSaveAirQuality.setPowerSave(False)
	config.AirQuality_Power = False
   	pclogging.log(pclogging.INFO, __name__, "Power: AirQuality Turned: %s" % "OFF")

	# LoRa Reciever On	
	myPowerSaveLoRa.setPowerSave(True)
	config.LORA_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: LoRa Turned: %s" % "ON") 
	
	# OLED Display On
	myPowerSaveOLED.setPowerSave(True)
	config.OLED_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: OLED Turned: %s" % "ON")

	# Fan Off
	myPowerDriveFan.setPowerDrive(1, False)	
	config.Fan_Drive_Power = False
   	pclogging.log(pclogging.INFO, __name__, "Power: Fan Turned: %s" % "OFF")

	# turn on USBPowerControl Controlling WiFi Dongle

	GPIO.output(USBPowerControl_Enable, True)
	GPIO.output(USBPowerControl_Control, True)
	config.WiFi_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: WiFi Turned: %s" % "ON")



	print "Initial Power State Set"
	

def setOLEDDisplayPower(value):
	
	if (value == True):
		myPowerSaveOLED.setPowerSave(True)
		config.OLED_Power = True
   		pclogging.log(pclogging.INFO, __name__, "Power: OLED Turned: %s" % "ON")

	if (value == False):
		config.OLED_Power = False
		myPowerSaveOLED.setPowerSave(False)
   		pclogging.log(pclogging.INFO, __name__, "Power: OLED Turned: %s" % "OFF")

def setLoRaPower(value):
	
	if (value == True):
		myLoRaSaveOLED.setPowerSave(True)
		config.LORA_Power = True
   		pclogging.log(pclogging.INFO, __name__, "Power: LoRa Turned: %s" % "ON") 

	if (value == False):
		config.LORA_Power = False
		myPowerSaveLoRa.setPowerSave(False)
   		pclogging.log(pclogging.INFO, __name__, "Power: LoRa Turned: %s" % "OFF") 

def resetWXLink():
	
	print "reset the LoRa reciever"	

	# LoRa Reciever Off	
	myPowerSaveLoRa.setPowerSave(False)
	config.LORA_Power = False
   	pclogging.log(pclogging.INFO, __name__, "Power: LoRa Turned: %s" % "OFF") 
	time.sleep(5.0)
	myPowerSaveLoRa.setPowerSave(True)
	config.LORA_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: LoRa Turned: %s" % "ON") 


def setWiFiOn(reason):

	# turn on USBPowerControl Controlling WiFi Dongle

	GPIO.output(USBPowerControl_Enable, True)
	GPIO.output(USBPowerControl_Control, True)
	config.WiFi_Power = True
   	pclogging.log(pclogging.INFO, __name__, "Power: %s WiFi Turned: %s" % (reason,"ON"))


def setWiFiOff(reason):

        f = open("/home/pi/SDL_Pi_ProjectCuracao2/WIFISHUTOFF","r")
        command = f.read()
        f.close()
	command = command.replace("\n", "")
	print "command='%s'"% command
        if (command == "False"): 
   		pclogging.log(pclogging.INFO, __name__, "Power: %s WiFi !: %s DISABLED" % (reason,"OFF"))
                # Nothing to do
                return 


	# turn off USBPowerControl Controlling WiFi Dongle

	GPIO.output(USBPowerControl_Enable, True)
	GPIO.output(USBPowerControl_Control, False)
	config.WiFi_Power = False
   	pclogging.log(pclogging.INFO, __name__, "Power: %s WiFi Turned: %s" % (reason,"OFF"))
   	





