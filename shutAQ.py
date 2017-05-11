

import sys
sys.path.append('./SDL_Pi_GrovePowerSave')
sys.path.append('./SDL_Pi_GrovePowerDrive')

import powercontrol



powercontrol.myPowerDriveFan.turnOffPowerDrive(1) 
powercontrol.myPowerSaveAirQuality.turnOffPowerSave() 

print "Fan and AirQuality Turned Off"

