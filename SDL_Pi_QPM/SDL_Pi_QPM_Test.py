#!/usr/bin/env python
#
#
# Test case for QPM
# SDL_Pi_QPM Library for Rasbperry PI
#
# SwitchDoc Labs, August 2015
#

# imports

import sys
import time
import datetime
import random 
import SDL_Pi_QPM

# Main Program

print ""
print "Test SDL_Pi_QPM Version 1.0 - SwitchDoc Labs"
print ""
print "Sample uses 0x21 I2C Address"
print "Cycles through all the four loadswitches"
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""


filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

QuadPower = SDL_Pi_QPM.SDL_Pi_QPM()
print "-----------------"
# enable all four channels
  

# Enable Channels
QuadPower.enablePowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO0, QuadPower.QuadPower_ENABLE)  
QuadPower.enablePowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO1, QuadPower.QuadPower_ENABLE)
QuadPower.enablePowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO2, QuadPower.QuadPower_ENABLE)
QuadPower.enablePowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO3, QuadPower.QuadPower_ENABLE)

QuadPower.setDirectionGPIOChannel(QuadPower.QuadPower_REG_IO7, QuadPower.QuadPower_OUTPUT)
value = QuadPower.readGPIO()
print("------>>>> Initial GPIO Value =",value)

# turn on I07 too
QuadPower.writeGPIO(0x80)

while True:


    
    print("----------------")
    # turn on I07 too
    QuadPower.writeGPIO(0x80)
    print("Turn on LSW0")
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO0, QuadPower.QuadPower_ON)
    time.sleep(3)
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO0, QuadPower.QuadPower_OFF)
    print("Turn on LSW1")
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO1, QuadPower.QuadPower_ON)
    time.sleep(3)
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO1, QuadPower.QuadPower_OFF)
    print("Turn on LSW2")
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO2, QuadPower.QuadPower_ON)
    time.sleep(3);
    
    # turn off I07 too
    QuadPower.writeGPIO(0x00)
    
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO2, QuadPower.QuadPower_OFF)
    print("Turn on LSW3")
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO3, QuadPower.QuadPower_ON)
    time.sleep(3)
    QuadPower.setPowerChannel(QuadPower.QuadPower_POWER_CHANNEL_IO3, QuadPower.QuadPower_OFF)
  
