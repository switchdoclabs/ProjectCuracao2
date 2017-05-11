#!/usr/bin/env python
#   SDL_Arduino_QuadPower Library
#   SDL_Arduino_QuadPower.py Raspberry Pi Drivers
#   Version 1.1
#   SwitchDoc Labs   August 3, 2015


import smbus
from datetime import datetime

class SDL_Pi_QPM():

	################
	# QuadPower Code
	################
	#I2C ADDRESS/BITS
	#   -----------------------------------------------------------------------
	QuadPower_ADDRESS                         =    (0x21)    # 0x21 (Addr=VDD)
	
	#=========================================================================
	
	#=========================================================================
	#    REGISTERS (R/W)
	#    -----------------------------------------------------------------------
	
	QuadPower_REGDATA_ADDR                   =    (0x00) # RegData
	QuadPower_REGDIR_ADDR                    =    (0x01) # Direction
	QuadPower_REGPULLUP_ADDR                 =    (0x02) # Pullups
	QuadPower_REGPULLDOWN_ADDR               =    (0x03) # Pulldowns
  	 
	QuadPower_INTERRUPTMASK_ADDR             =    (0x05) # Interrupt Mask
	QuadPower_SENSEHIGH_ADDR                 =    (0x06) # Interrupt direction 7-4
	QuadPower_SENSELOW_ADDR                  =    (0x07) # Interrupt direction 3-0
  	 
	QuadPower_INTERRUPTSOURCE_ADDR           =    (0x08) # Interrupt Source 
	QuadPower_EVENTSTATUS_ADDR               =    (0x09) # Event Status of I/Os
  	 
	QuadPower_REGPLDMODE_ADDR                =    (0x10) # PLD Mode  
	QuadPower_REGPLDPLDTABLE0_ADDR           =    (0x11) # PLD Truth Table 
	QuadPower_REGPLDPLDTABLE1_ADDR           =    (0x12) # PLD Truth Table  
	QuadPower_REGPLDPLDTABLE2_ADDR           =    (0x13) # PLD Truth Table  
	QuadPower_REGPLDPLDTABLE3_ADDR           =    (0x14) # PLD Truth Table  
	QuadPower_REGPLDPLDTABLE4_ADDR           =    (0x15) # PLD Truth Table  
	 
	QuadPower_REGADVANCED_ADDR               =    (0xAB) # Advanced Settings
  	 
	
  	 
	#---------------------------------------------------------------------
	QuadPower_CONFIG_RESET                    =    (0x8000)  # Reset Bit
		
	QuadPower_REG_IO7                     =    (0x80)  # Channel IO7 
	QuadPower_REG_IO6                     =    (0x40)  # Channel IO6 
	QuadPower_REG_IO5                     =    (0x20)  # Channel IO5 
	QuadPower_REG_IO4                     =    (0x10)  # Channel IO4 
  	QuadPower_POWER_CHANNEL_IO3  =                   (0x08)  # Power Channel IO3
   	QuadPower_POWER_CHANNEL_IO2  =                   (0x04)  # Power Channel IO2
   	QuadPower_POWER_CHANNEL_IO1  =                   (0x02)  # Power Channel IO1
   	QuadPower_POWER_CHANNEL_IO0  =                   (0x01)  # Power Channel IO0
    
	QuadPower_INPUT                       =    (0x01)  # 0 means input
	QuadPower_OUTPUT                      =    (0x00)  # 1 means output
  	 
	QuadPower_OFF                         =    (0x00)  # 0 means off
	QuadPower_ON                          =    (0x01)  # 1 means on
  	
    	QuadPower_DISABLE                     =   (0x01)  # 0 means off
    	QuadPower_ENABLE                      =   (0x00)  # 1 means on 
   	
	QuadPower_REG_SENS_NONE              =    (0x0)  # None - Interrupt Edge Sensitivity
	QuadPower_REG_SENS_RISING            =    (0x1)  # Rising - Interrupt Edge Sensitivity
	QuadPower_REG_SENS_FALLING           =    (0x2)  # Falling - Interrupt Edge Sensitivity
	QuadPower_REG_SENS_BOTH              =    (0x3)  # None - Interrupt Edge Sensitivity
	
    


	def __init__(self, twi=1, addr=QuadPower_ADDRESS):
		self._bus = smbus.SMBus(twi)
		self._QuadPower_i2caddr = addr
		
		# variables
    		self._QuadPower_direction = 0xFF
        	self._QuadPower_pullup = 0
        	self._QuadPower_pulldown = 0
		self._QuadPower_interruptmask = 0
    
    
   		self.wireWriteRegister(self.QuadPower_REGDIR_ADDR, self._QuadPower_direction);
    

    		self.writeGPIO(0)

			

	def readGPIO(self):
		value = self.wireReadRegister(self.QuadPower_REGDATA_ADDR)
		return value

	def writeGPIO(self, value):
		# only writes to upper 4 bits!
    		currentValue = self.wireReadRegister(self.QuadPower_REGDATA_ADDR)
    
    		newvalue = (currentValue & 0x0F) | (value & 0xF0)
		self.wireWriteRegister(self.QuadPower_REGDATA_ADDR, newvalue )

		return 


  	def setDirectionGPIOChannel(self, channel, direction):
   

		#    protect power lines from setting
    
    		channel = channel & 0xF0 

    		if (direction == self.QuadPower_INPUT):
        		value = self._QuadPower_direction | channel
        
        
    		else:
        		# assume output
        		value = self._QuadPower_direction & ((~channel) &0xFF) 
        
    
   		self._QuadPower_direction = value
    
    		self.wireWriteRegister(self.QuadPower_REGDIR_ADDR, value)
    
    		# print("GPIO Direction=",value)
    
    		return self._QuadPower_direction



  	
	def setPullupGPIOChannel(self, channel, state):
    
		if (state == self.QuadPower_OFF):
        		value = self._QuadPower_pullup & ((~channel) &0xFF) 
    		else:
        		# assume output
        		value = self._QuadPower_pullup | channel
        
    
    
    		self._QuadPower_pullup = value;
    		self.wireWriteRegister(self.QuadPower_REGPULLUP_ADDR, value);
    		#print("GPIO Pullup=",value)
    
    		return self._QuadPower_pullup;


  	def setPulldownGPIOChannel(self, channel, state):  

    
   		if (state == self.QuadPower_OFF):
        		value = self._QuadPower_pulldown & ((~channel) &0xFF) 
    		else:
        		# assume output
        		value = self._QuadPower_pulldown | channel
        
    
   		self._QuadPower_pulldown = value;
    		self.wireWriteRegister(self.QuadPower_REGPULLDOWN_ADDR, value)
    		#print("GPIO Pulldown=",value)
    
    		return self._QuadPower_pulldown;

  	def setInterruptMaskGPIOChannel(self, channel, state):
    		
		if (state == self.QuadPower_OFF):
        		value = self._QuadPower_interruptmask & ((~channel) &0xFF) 
    		else:
        		# assume output
        		value = self._QuadPower_interruptmask | channel
        
    
    
    		self._QuadPower_interruptmask = value
    		self.wireWriteRegister(self.QuadPower_INTERRUPTMASK_ADDR, value)
    		#print("GPIO Interrupt Mask=",value)
    
    		return self._QuadPower_interruptmask;

	# power management

	def enablePowerChannel(self, channel, enable):
    
    		if (enable == self.QuadPower_DISABLE):
       			value = self._QuadPower_DIREction | channel
        
        
    		else:
        		# assume output
        		value = self._QuadPower_direction & ((~channel) &0xFF) 
        
    
    		self._QuadPower_direction = value;
    
    		self.wireWriteRegister(self.QuadPower_REGDIR_ADDR, value);
		#print ("ePC value= %x ") % value
    		return self._QuadPower_direction;


	def setPowerChannel(self, channel, state):

    
    		value =  self.readGPIO()
    		if (state == self.QuadPower_ON):
    		
        		value = value | channel
        
    		else:
        		value = value & ((~channel) &0xFF)
    
		#print ("sPC value= %x ") % value
    		self.wireWriteRegister(self.QuadPower_REGDATA_ADDR, value)

		return

	# end of power management


 	def wireWriteRegister(self, reg, value):

        	#print "addr =0x%x register = 0x%x data = 0x%x " % (self._QuadPower_i2caddr, reg, value)
		self._bus.write_byte_data(self._QuadPower_i2caddr, reg, value)

    
	def wireReadRegister(self, reg ):

		returndata = self._bus.read_byte_data(self._QuadPower_i2caddr, reg)
        	#print "addr = 0x%x data = 0x%x %i returndata = 0x%x " % (self._QuadPower_i2caddr, reg, reg, returndata)
        	return returndata

