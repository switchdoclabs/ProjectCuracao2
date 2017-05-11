
import sys
import time

sys.path.append('./SDL_Pi_SSD1306')
sys.path.append('./Adafruit_Python_SSD1306')
sys.path.append('./RTC_SDL_DS3231')
sys.path.append('./Adafruit_Python_BMP')
sys.path.append('./Adafruit_Python_GPIO')
sys.path.append('./SDL_Pi_WeatherRack')
sys.path.append('./SDL_Pi_FRAM')
sys.path.append('./RaspberryPi-AS3935/RPi_AS3935')
sys.path.append('./SDL_Pi_INA3221')
sys.path.append('./SDL_Pi_TCA9545')
sys.path.append('./SDL_Pi_SI1145')
sys.path.append('./graphs')
sys.path.append('./SDL_Pi_HDC1000')
sys.path.append('./SDL_Pi_GrovePowerSave')
sys.path.append('./SDL_Pi_GrovePowerDrive')
sys.path.append('./Adafruit_PWM_Servo_Driver')



import powercontrol






powercontrol.setWiFiOff("Testing Off")

time.sleep (10.0)

powercontrol.setWiFiOn("Testing On")

