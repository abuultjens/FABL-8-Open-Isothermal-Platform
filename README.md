# FABL-8-Open-Isothermal-Platform
<img align="right" src="https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Picture%202.png">
Publicly accessible details on how to build and operate a FABL-8 isothermal diagnostic device. The build instructions have been divided into an essential and optional section. The essential section details how to build just the control, heating, excitation and emission systems as well as a touchscreen interface - the bare minimum for an operating isothermal platform. The optional section describes how we built a casing for the instrument, however this specific design was not mandatory for function and could be used as a guide as there is considerable flexibility.

## About
The FABL-8 is an open source, low cost and scalable diagnostic platform for the running of loop mediated isothermal amplification (LAMP) reactions. 

## Publication
A publication detailing the FABL-8 and its diagnostic performance against commercial offerings is in progress.

# Essential build

## Parts list
| Part: | Quantity: | Link: |
| --------------- | --------------- | --------------- |
| 12-stage Binary Counter CMOS IC 4040 | 1 | https://www.jaycar.com.au/4040-12-stage-binary-counter-cmos-ic/p/ZC4040 |
| Raspberry Pi 3 Model B+ | 1 | https://www.jaycar.com.au/raspberry-pi-3b-single-board-computer/p/XC9001 |
| Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |


## Electronic configuration
The circuit consists of five main systems:  
* __Voltage regulation__  
Provide individual step down 5V DC power supplies from the input 19V DC for the control, heater, excitation and emission systems. 
* __Control__  
Consists of a Raspberry pi that orchestrates the heater, excitation and emission systems. The control system uses a 12-stage binary counter to accurately  quantify the clock pulses from the emission system.  
* __Heater__  
Provides high current on/off switching of two 10W wire wound resistors that form the heating element. The heating system utilises a thermal breaker that acts as a failsafe to shutoff the heating element in the event of a control malfunction.
* __Excitation__  
Sequentially illuminates LEDs in an eight LED array using an 8-channel analogue multiplexer.
* __Emission__  
Sequentially reads clock pulses from light-to-frequency photodiodes in an eight photodiode array using an 8-channel analogue demultiplexer.    

### Circuit schematic  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/FABL-8_schematic.png)

### Setting up the Raspberry pi  

1. Use SDFormatter (https://www.sdcard.org/downloads/) to perform a quick format of a microSD card.  

2. Download the preconfigured image from this page named 'NEW-UNIT_19-03-21.img.gz'.
  
3. Use Raspberry Pi Imager (https://www.raspberrypi.org/software/) to write 'NEW-UNIT_19-03-21.img.gz' image to microSD card.  

## Heating block
The heating block was made from solid aluminium  using a computer numerical control (CNC) machine. The lid plates and resistor retainer plates were made using a drill press. All 2.5mm holes in the heating block were tapped with metric 3mm (M3) tap.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Simple_block_with_threaded_holes.png)

The thermal breaker and temperature sensor are mounted on the rear of the heating block. The thermal breaker mounts using M3 bolts while the temperature sensor is retained using a small clip made from sheet metal that is secured under a thermal breaker mounting bolt head.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/thermal_breaker.png)

## Heating block stands
Stands were made from 1mm thick sheet metal. If sheet metal is difficult to source or work with, any kind of block mounting stand could be fabricated as long as it can withstand a constant 65oC.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/block_stands.png)


## 3D printed parts
All 3D printed parts were printed using black 1.75 PLA filament on an Ender3 3D printer modified with a BLTouch V2 automatic mechanical bed levelling device (https://www.antclabs.com/bltouch).  

### Magnet mount  
This part retains two rare earth magnets in its upper cavity. The part holds the magnets captive when the closed end of the cavity is facing away from the block.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Magnet_mount.png)

### Fixed photodiode mount  
This part retains the eight photodiodes and is sandwiched between two 2mm thick block lid plates. The emission filter gel is mounted between the photodiodes and the lower block lid plate.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Fixed_photodiode_mount.png)  

### Fixed LED mount  
This part retains the eight LEDs and clamps the excitation filter gel to the block.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Fixed_8-LED_mount.png)  

## Assembly

### Block stands and magnet mount
Two wire wound resistors are fitted into the cavity underneath the heating block and secured in place using the two resistor retaining plates. The magnet mount is first attached to the block stand with two M5 bolts and nuts. The block is then mounted to the block stand by passing M3 bolts through the gaps in the magnet mounts. 
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Magnet_mount_anno.jpg)

### Excitation system
The eight excitation LEDs are pressed into the fixed LED mount. During assembly the excitation gel is sandwiched between the block and the fixed LED mount which is secured in place using M3 bolts, nuts, standoffs and the rear LED mount retainer.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Block_anno.jpg)

### Emission system
The eight photodiodes are fitted into the fixed photodiode mount (with light sensitive surface facing downward through holes) and individually secured with a small piece of sticky tape. The emission filter gels are then overlaid on the light sensitive side of the photodiode mount and secured with the metal lids on both sides using M3 bolts and nuts. Once both block stands are secured to the block, the stands are mounted on a sheet of acrylic.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/emission_anno.jpg)



   




# Instrument case
The key requirements for casing are that the enclosure blocks out all environmental light and secondly that it provides a thermally insulating environment for the PID to reach a stable 65oC. Our implementation of the FABL-8 involved a robust briefcase style plastic box and inner acrylic partition that was used to mount the heating block. While this specific setup was ideal for transportation and storage, any casing configuration that meets the abovementioned requirements will suffice. We have here detailed our case configuration which may be useful as a guide.

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

