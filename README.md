# FABL-8-build  
Details of how to build a FABL-8 isothermal diagnostic unit  

# Parts list
| Part: | Quantity: | Link: |
| --------------- | --------------- | --------------- |
| 12-stage Binary Counter CMOS IC 4040 | Row 1 Column 2 | Row 1 Column 3 |
| Row 2 Column 1 | Row 2 Column 2 | Row 2 Column 3 |
| Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |


# Circuit schematic
![Image description](https://github.com/abuultjens/FABL-8-build/blob/main/FABL-8_schematic.png)

# CNC aluminum heating block


# 3D printed parts
All parts were printed on an Ender3 modified with a BL touch using 1.75 PLA filament.  
magnet mount  
fixed photodiode mount  
fixed LED mount  
left screen mount  
right screen mount  
screen face plate  

# Instrument case



# Setting up Raspberry pi  
Used SDFormatter version 4.0 to perform a quick format of a 16GB microSD card.  
https://www.sdcard.org/downloads/  
  
Used Raspberry Pi Imager version 1.3 to write 'NEW-UNIT_19-03-21.img.gz' image to microSD card.  
https://www.raspberrypi.org/software/  
   
* startup-script.sh  
script that runs on startup and initiates the app and ....

* script-replacer.sh  
this replaces RBP script with newer script(s) from a dir on the MDU server  

* UPDATE-CONFIRM.sh  
uploads a log file confirming if the updated script(s) have been uploaded to the RBP  

* python3 APP_v2.py  
this is the main app. This script runs:
MAC_ADDRESS.sh 
This script makes:
APP_v2_log.csv 

#### APP_v2.py starts:  

* MAC_ADDRESS.sh  
makes a file callled NEW_MAC_ADDRESS.csv or OLD_MAC_ADDRESS.csv  

* PID_SAFE.sh  
get the set temp and runs PID_SAFE.py  

* PID_SAFE.py  
PID control 

* SCP.sh
SCP outfiles to remote server  
  
* KILL_PID.sh  
gets PID process ID and kills it  

* RESTART.sh  
kills python, sets all GPIO off and restarts app  

* blink.py  
sets GPIO pins off  

* KILL_PYTHON.sh  
kills python and sets all GPIO off  

* stepper_SW_colour-sensor_MICROSTEP_CAL.py  
steps through all eight wells and read photodiodes  



# Instructions of use  

* An Initial warmup period occurs upon powerup to stably raise the block temperature to 65oC. 

* Once at operation temperature a reaction can be run by preparing LAMP reagents and template in an OptiGene strip, cutting off the plastic wings on the terminal ends of the strip, removing the magnetic block lid, inserting the strip and replacing the magnetic lid. 

* The operator then closes the main instrument lid and uses the touchscreen interface to enter well information and initiate the run. During the run a plot of normalised florescence emission is displayed in real-time. 

* At the conclusion of the run the measurements are wirelessly uploaded to a webserver via a hotspot hosted by a mobile device. The webserver calculates the derivative of the normalised emission timeseries to classify if the well was positive or negative as well as time to positive (TTP).




