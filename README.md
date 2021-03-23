# FABL-8-Open-Isothermal-Platform
Publically accessible details on how to build and opperate a FABL-8 isothermal diagnostic device. The build instructions have been divided into an essential and optional section. The essential section details how to build just the control, heating, excitation and emission systems as well as a touchscreen interface - the bare minimum for an operating isothemal platform. The optional section describes how we built a casing for the instriment, however this specific design was not manditory for function and could be used as a guid as there is considerable flexibility. 

![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Picture%202.png)


# Essential build

## Parts list
| Part: | Quantity: | Link: |
| --------------- | --------------- | --------------- |
| 12-stage Binary Counter CMOS IC 4040 | 1 | https://www.jaycar.com.au/4040-12-stage-binary-counter-cmos-ic/p/ZC4040 |
| Raspberry Pi 3 Model B+ | 1 | https://www.jaycar.com.au/raspberry-pi-3b-single-board-computer/p/XC9001 |
| Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |


## Electronic configuration
The circuit consists of five main elements:  
* __Voltage regulators__  
Provide individual step down 5V DC power supplies from the input 19V DC for the control, heater, excitation and emission systems. 
* __Control system__  
Consists of a Raspberry pi that orchestrates the heater, excitation and emission systems. The control system uses a 12-stage binary counter to accuratly quantify the clock pulses from the emission system.  
* __Heater system__  
Provides high current on/off switching of two 10W wire wound resistors that form the heating elememnt. The heating system utelises a thermal breaker that acts as a failsafe to shutoff the heating element in the event of a control  malfunction.
* __Excitation system__  
Sequentially illuminates LEDs in an eight LED array using an 8-channel analogue multiplexer.
* __Emission system__  
Sequentially reads clock pulses from light-to-frequency photodiodes in an eight photodiode array using an 8-channel analogue demultiplexer.    

### Circuit schematic  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/FABL-8_schematic.png)

## Heating block
The heating block was made from aluminum using a computer numerical control (CNC) machine. The lid plates and resistor retainer plates were made using a drill press. All 2.5mm holes in the heating block were tapped with metric 3mm (M3) tap.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Simple_block_with_threaded_holes.png)

The thermal breaker and temperature sensor are mounted on the rear of the heating block. The thermal breaker mounts using M3 bolts while the tempreature sensor is retained using a small clip made from sheet metal that is secured under a thermal breaker mounting bolt head.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/thermal_breaker.png)

## Heating block stands
Stands were made from 1mm thick sheet metal. If sheet metal is difficult to source or work with, any kind of block mounting stand could be fabricated as long as it can withstand a constant 65oC.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/block_stands.png)


## 3D printed parts
All 3D printed parts were printed using black 1.75 PLA filament on an Ender3 3D printer modified with a BLTouch V2 automatic mechanical bed levelling device (https://www.antclabs.com/bltouch).  

### magnet mount  
This part retains two rare earth magnets in its upper cavity. The part holds the magnets captive when the colsed end of the cavity is facing away from the block.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Magnet_mount.png)

### fixed photodiode mount  
This part retains the eight photodiodes and is sandwched between two 2mm thich block lid plates. The emission filter gel is mounted inbetween this part ad the lower block lid plate.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Fixed_photodiode_mount.png)  

### fixed LED mount  
This part retains the eight LEDs and clamps the excitation filter gel to the block.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Fixed_8-LED_mount.png)  

# Setting up the Raspberry pi  


1. Use SDFormatter (https://www.sdcard.org/downloads/) to perform a quick format of a 16GB microSD card.  

2. Download the preconfigured image from this page named 'NEW-UNIT_19-03-21.img.gz'.
  
3. Use Raspberry Pi Imager (https://www.raspberrypi.org/software/) to write 'NEW-UNIT_19-03-21.img.gz' image to microSD card.  

   
## Scripts:   
   
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



# Instrument case

## Parts list
| Part: | Quantity: | Link: |
| --------------- | --------------- | --------------- |
| 12-stage Binary Counter CMOS IC 4040 | 1 | https://www.jaycar.com.au/4040-12-stage-binary-counter-cmos-ic/p/ZC4040 |
| Raspberry Pi 3 Model B+ | 1 | https://www.jaycar.com.au/raspberry-pi-3b-single-board-computer/p/XC9001 |
| Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |

## 3D printed parts
All parts were printed on an Ender3 modified with a BL touch using black 1.75 PLA filament.  

### left screen mount  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Left_screen_mount.png)  

### right screen mount  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Right_Screen_mount.png)  

### screen face plate  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Screen_face_plate.png)  

## Block mounting partition
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Partition.png)  




# Instructions of use  

* An Initial warmup period occurs upon powerup to stably raise the block temperature to 65oC. 

* Once at operation temperature a reaction can be run by preparing LAMP reagents and template in an OptiGene strip, cutting off the plastic wings on the terminal ends of the strip, removing the magnetic block lid, inserting the strip and replacing the magnetic lid. 

* The operator then closes the main instrument lid and uses the touchscreen interface to enter well information and initiate the run. During the run a plot of normalised florescence emission is displayed in real-time. 

* At the conclusion of the run the measurements are wirelessly uploaded to a webserver via a hotspot hosted by a mobile device. The webserver calculates the derivative of the normalised emission timeseries to classify if the well was positive or negative as well as time to positive (TTP).




