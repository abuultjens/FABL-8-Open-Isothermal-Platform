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
  
#### starts with  
sh startup-script.sh  

#### startup-script.sh starts:  
#### this replaces RBP script with newer script(s) from a dir on the MDU server  
sh script-replacer.sh  
#### this is the main app  
python3 APP_v2.py  

#### APP_v2.py starts:  
#### makes a file callled NEW_MAC_ADDRESS.csv or OLD_MAC_ADDRESS.csv  
MAC_ADDRESS.sh  
#### same as before  
script-replacer.sh  
#### makes log file  
APP_v2_log.csv  
#### uploads a log file confirming if the updated script(s) have been uploaded to the RBP  
UPDATE-CONFIRM.sh  
#### get the set temp and runs PID_SAFE.py  
PID_SAFE.sh  
#### PID control  
PID_SAFE.py  
#### SCP outfiles to remote server  
SCP.sh  
#### gets PID process ID and kills it  
KILL_PID.sh  
#### kills python, sets all GPIO off and restarts app  
RESTART.sh  
#### sets GPIO pins off  
blink.py  
#### kills python and sets all GPIO off  
KILL_PYTHON.sh  
#### steps through all eight wells and read photodiodes  
stepper_SW_colour-sensor_MICROSTEP_CAL.py  



# Instructions of use  





