# TempTor_sensors
The temperature sensors code.
#Set of Files
  Files outside of Folders in repo are the pdfs of the assignments completed for this class
  Adafruit_MAX31855 folder has the source code used for the hardware to run the MAX31855 Thermocouple, this code was designed by Tony DiCola
     of Adafruit and was public use
  examples folder is the code written by Sutton Cowperthwaite and Maryjane Clark and the simpletest.py file which is was based off of.
  Temptor.py is this code we have written.

#Running code
  To run the code for the sensor make sure that the MAX31855 Thermocouple is correctly connected to the Raspberry pi. To propery connect the components connect
  the following wires as such:
  Pi 3.3V to MAX31855 Vin
  Pi GND to MAX31855 GND
  Pi GPIO 18 to MAX31855 DO
  Pi GPIO 24 to MAX31855 CS
  Pi GPIO 25 to MAX31855 CLK
  When the wiring is set up and the raspberry pi is set up run TempTor.py in the examples folder. Run in any process that will run python.
  When TempTor.py is running follow the onscreen instructions to set up the sensor. 
  Make sure to choice:
  -Temperature Units
  -Time interval between reading
  Once these are set up follow onscreen instructions and allow the sensor to run and send data to the server.
  Sensor is setup and ready to go.
  
  
