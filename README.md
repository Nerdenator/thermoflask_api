# Thermoflask
Thermoflask is a simple web server that polls your Raspberry Pi for its CPU clockspeed and temperature and returns the data in a JSON format for use in your application. It is written in Python using the Flask web framework. 

## Requirements
As of this writing, Thermoflask has only been tested to work on Raspberry Pi SBCs running Raspberry Pi OS 10.8. It is likely that it will work on future versions of the OS. Installation on a Python 3 interpreter is required; 3.8+ is recommended.