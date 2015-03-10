#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
import socket

#Global Variables
tempunit = 'C'
timeset= 0
Timeset= 0
hrs= 0
mins =0
secs= 0
addsecs = 0
addmins =0
addhrs =0 	


# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)


#Server Setup
def logtemp(temp,time):
	connection=sqlite3.connect(my_datbase_production)
	curs=connection.cursor()
	curs.execute("Insert into temps values(time('time'),(?))",(temp,))
	connection.commit()
	connection.close()


#Sutton Cowperthwaite & Maryjane Clark
# Loop printing measurements every second.
def Sensor (Unit , Time):
	print 'Press Ctrl-C to quit.'
	unitset= 0
	if Unit in ['C','c']:
		unitset = 0
		while True:
			temp = sensor.readTempC()
			internal = sensor.readInternalC()
			Temper=UnitChange(temp,unitset)
			Intern=UnitChange(internal,unitset)
			print 'Thermocouple Temperature: {0:0.3F}*C'.format(Temper)
			print 'Internal Temperature: {0:0.3F}*C'.format(Intern)
			time.sleep(Time)
	if Unit in ['K','k']:
		unitset =1
		while True:
			temp = sensor.readTempC()
			internal = sensor.readInternalC()
			Temper=UnitChange(temp,unitset)
			Intern=UnitChange(internal,unitset)
			print 'Thermocouple Temperature: {0:0.3F}*K'.format(Temper)
			print 'Internal Temperature: {0:0.3F}*k'.format(Intern)
			time.sleep(Time)
	if Unit in ['F','f']:
		unitset = 2
		while True:
			temp = sensor.readTempC()
			internal = sensor.readInternalC()
			Temper=UnitChange(temp,unitset)
			Intern=UnitChange(internal,unitset)
			print 'Thermocouple Temperature: {0:0.3F}*F'.format(Temper)
			print 'Internal Temperature: {0:0.3F}*F'.format(Intern)
			time.sleep(Time)
	Timeset += Time		
	logtemp(Temper,Timeset)				

#Sutton Cowperthwaite & Maryjane Clark code
#Change the temperature units
def UnitChange(c,setpt):
	if setpt == 0:
		return c
	elif setpt ==1:
		K= c-273.15
		return K
	elif setpt == 2:		
		F=(9/5)*c+32.0
		return F
	
#Introduction Script
#Sutton Cowperthwaite & Maryjane Clark



#Set Temperature units

while True:
	print 'What temperature units would you like to use?'
	print 'Type F for Fahrenheit'
	print 'Type C for Celsius'
	print 'Type K for Kelvin'
	tempunit = raw_input("Enter: ")
	if tempunit[0] in ['K','k','F','f','C','c',]:
		break
	else:
		print 'Wrong Input: Please try agian'
		print ' '
print ' '
print 'What time interval to do you want?'
#Set up time interval
while True:
	print 'Add Seconds?'
	print 'Add Minutes?'   
	print 'Add Hours?'
	timein= raw_input('Enter time interval you want to change: ')
	print ' '
	if timein[0] in ['S', 's']:
		addsecs= raw_input("How many seconds do you want to add to time interval? ")
	elif timein[0] in ['M','m']:
		addmins= raw_input("How many mins do you want to add to time interval? ")
	elif timein[0] in ['H', 'h']:
		addhrs= raw_input("How many hours do you want to add to time interval? ")
	else:
		print 'Wrong input'	
	print ' '	
	secs += int(float(addsecs))
	mins += int(float(addmins))
	hrs += int(float(addhrs))
	if secs >= 60:
		mins += secs // 60
		secs = secs % 60
	if mins >= 60:
		hrs += mins // 60
		mins = mins % 60					
	print 'Current Time Interval is {0} hours. {1} minutes, {2} seconds'.format(hrs, mins, secs)
	Addtime= raw_input('Are you satisfied with the time interval? (Y/N) ')
	if Addtime[0] in ['y', 'Y']:
		timeset= secs + 60 * mins + 3600 * hrs
		Sensor(tempunit[0],timeset);
		
		
		

