#
#
# SDL_Pi_GrovePowerSave example
# Raspberry Pi Driver for the SwitchDoc Labs GrovePowerSave 
#
# SwitchDoc Labs
# April  2017
#
# Version 1.1

# assumes device is plugged into GPIO Pin 26 (D26 of Pi2Grover board)

import  SDL_Pi_GrovePowerSave
import time

GPIO_Pin_PowerSave = 4

myPowerSave = SDL_Pi_GrovePowerSave.SDL_Pi_GrovePowerSave(GPIO_Pin_PowerSave, True)
	
print "turning Pin %i off" % GPIO_Pin_PowerSave
myPowerSave.setPowerSave(False)

time.sleep(60)

myPowerSave.setPowerSave(True)

print "turning Pin %i on" % GPIO_Pin_PowerSave


		
