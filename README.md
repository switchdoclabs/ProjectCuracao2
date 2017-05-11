ProjectCuracao2 Libraries and Example for Raspberry Pi Solar Powered Weather Station

Supports SwitchDoc Labs WeatherRack WeatherBoard (WeatherPiArduino V2 and above)

Version 3.0 

http://www.switchdoc.com/

March 9, 2017 - Forked from GroveWeatherPi Version 2.8 





-----------------
Install this for smbus:

sudo apt-get install python-smbus

If using the Grove Sunlight Sensor do this:

git clone https://github.com/adafruit/Adafruit_Python_PureIO.git<BR>
cd Adafruit_Python_PureIO<BR>
sudo python setup.py install<BR>

Other installations required for AM2315:

sudo apt-get install python-pip

sudo apt-get install libi2c-dev

sudo pip install tentacle_pi

#Installing apscheduler

sudo pip install --upgrade setuptools pip <BR>

sudo pip install setuptools --upgrade  <BR>
sudo pip install apscheduler <BR>


----------------
Note some configurations of Raspberry Pi software requres the following:
----------------
<pre>
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
</pre>
SwitchDocLabs Documentation for WeatherRack/WeatherPiArduino under products on: store.switchdoc.com

Read the ProjectCuracao2 Instructable on instructables.com for more software installation instructions 

or

Read the tutorial on ProjectCuracao2 on http://www.switchdoc.com/2016/08/tutorial-part-1-building-a-solar-powered-raspberry-pi-weather-station-groveweatherpi/
for more software installation instructions.

-----------
setup your configuration variables in config.py!
-----------

--------
Add SQL instructions
----------

Use phpmyadmin or sql command lines to add the included SQL file to your MySQL databases.<BR>
Note:  If the database has been updated, run the example below to update your database.   The current contents will not be lost.


example:   mysql -u root -p ProjectCuracao2< ProjectCuracao2.sql

user:  root

password: password

Obviously with these credentials, don't connect port 3306 to the Internet.   Change them if you aren't sure.

NOTE:

If you have a WXLink wireless transmitter installed, the software assumes you have connected your AM2315 outdoor temp/humidity sensor to the WXLink.  If you put another AM2315 on your local system, it will use those values instead of the WXLink values

----------

----------


