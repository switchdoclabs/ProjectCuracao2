
#
#
# configuration file - contains customization for exact system
# JCS 11/8/2013
#

# it is a good idea to copy this file into a file called "conflocal.py" and edit that instead of this one.  This file is wiped out if you update ProjectCuracao2.



mailUser = "yourusename"
mailPassword = "yourmailpassword"

notifyAddress ="you@example.com"

fromAddress = "yourfromaddress@example.com"

textnotifyAddress = "yourphonenumber@yourprovider"

#MySQL Logging and Password Information

enable_MySQL_Logging = True
MySQL_Password = "password"

# modify this IP to enable WLAN operating detection  - search for WLAN_check in ProjectCuracao2.py
enable_WLAN_Detection = True
PingableRouterAddress = "192.168.1.1"

# WeatherUnderground Station

WeatherUnderground_Present = False
WeatherUnderground_StationID = "KWXXXXX"
WeatherUnderground_StationKey = "YYYYYYY"



# for barometeric pressure - needed to calculate sealevel equivalent - set your weatherstation elevation here

BMP280_Altitude_Meters = 648.0

# device present global variables

Lightning_Mode = False
SolarPower_Mode = False

TCA9545_I2CMux_Present = False
SunAirPlus_Present = False
AS3935_Present = False
DS3231_Present = False
BMP280_Present = False
FRAM_Present = False
HTU21DF_Present = False
HDC1080_Present = False
AM2315_Present = False
ADS1015_Present = False
ADS1115_Present = False
OLED_Present = False
WXLink_Present = False
Sunlight_Present = False


# Power Save and Fan Drive Variables

Fan_Drive_Power = True
OLED_Power = True
LORA_Power = True
AirQuality_Power = True
WiFi_Power = True


# if the WXLink has stopped transmitting, == False
WXLink_Data_Fresh = False
WXLink_Data_Fresh_ID = 0
WXLInk_LastMessageID = 0

# 2 and 3 sensor
WXLinkLastMessageID_2 = 0
WXLinkLastMessageID_3 = 0

