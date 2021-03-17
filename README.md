# FABL-8-build  
Details of how to build a FABL-8 isothermal diagnostic unit  

# obtained Raspbery pi OS (32-bit) from:
https://www.raspberrypi.org/software/
Released 11-01-21

# log in using home wifi:  
ssh pi@10.0.0.12  

#PW:  
Plenty_Gorge  

## starts with  
sh startup-script.sh  

## startup-script.sh starts:  
## this replaces RBP script with newer script(s) from a dir on the MDU server  
sh script-replacer.sh  
## this is the main app  
python3 APP_v2.py  

## APP_v2.py starts:  
## makes a file callled NEW_MAC_ADDRESS.csv or OLD_MAC_ADDRESS.csv  
MAC_ADDRESS.sh  
## same as before  
script-replacer.sh  
## makes log file  
APP_v2_log.csv  
## uploads a log file confirming if the updated script(s) have been uploaded to the RBP  
UPDATE-CONFIRM.sh  
## get the set temp and runs PID_SAFE.py  
PID_SAFE.sh  
## PID control  
PID_SAFE.py  
## SCP outfiles to remote server  
SCP.sh  
## gets PID process ID and kills it  
KILL_PID.sh  
## kills python, sets all GPIO off and restarts app  
RESTART.sh  
## sets GPIO pins off  
blink.py  
## kills python and sets all GPIO off  
KILL_PYTHON.sh  
## steps through all eight wells and read photodiodes  
stepper_SW_colour-sensor_MICROSTEP_CAL.py  









