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

GPIO_Pin_PowerSave4 = 4
GPIO_Pin_PowerSave26 = 26

myPowerSave4 = SDL_Pi_GrovePowerSave.SDL_Pi_GrovePowerSave(GPIO_Pin_PowerSave4, True)
myPowerSave26 = SDL_Pi_GrovePowerSave.SDL_Pi_GrovePowerSave(GPIO_Pin_PowerSave26, True)
	
print "turning Pin %i off" % GPIO_Pin_PowerSave4
print "turning Pin %i off" % GPIO_Pin_PowerSave26
myPowerSave4.turnOffPowerSave()
myPowerSave26.turnOffPowerSave()



		
