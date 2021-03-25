# FABL-8-Open-Isothermal-Platform
<img align="right" src="https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Picture%202.png">

Publicly accessible details on how to build and operate a FABL-8 isothermal diagnostic device. The build instructions have been divided into an essential and optional section. The essential section details how to build just the control, heating, excitation and emission systems as well as a touchscreen interface - the bare minimum for an operating isothermal diagnostic platform. The optional section describes how we built a casing for the instrument, however this specific design was not mandatory for function and could be used as a guide as there is considerable flexibility.

## About
The FABL-8 is an open source, low cost and scalable diagnostic platform for the running and monitoring of loop mediated isothermal amplification (LAMP) reactions. 

## Publication
A publication detailing the FABL-8 and its diagnostic performance against commercial offerings is in progress.

## Page index
<img align="right" src="https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Picture%201.png">

- [Essential build](#essential-build)
  - [Electronic configuration](#electronic-configuration)  
    - [Circuit schematic](#circuit-schematic)
    - [Setting up the Raspberry pi](#Setting-up-the-Raspberry-pi)
  - [Heating block](#heating-block)
  - [Heating block stands](#heating-block-stands)
  - [3D printed parts](#3d-printed-parts)
    - [Magnet mount](#magnet-mount)
    - [Fixed photodiode mount](#fixed-photodiode-mount)
    - [Fixed LED mount ](#fixed-led-mount)
  - [Assembly](#sssembly)
    - [Block stands and magnet mount](#block-stands-and-magnet-mount)
    - [Excitation system](#excitation-system)
    - [Emission system](#emission-system)
- [Instrument case](#instrument-case)
  - [3D printed parts](#3d-printed-parts)
    - [Left screen mount](#left-screen-mount)
    - [Right screen mount](#right-screen-mount)
    - [Screen face plate](#screen-face-plate)
  - [Block mounting partition](#block-mounting-partition)
- [Instructions of use](#instructions-of-use)
- [Essential build parts list](#essential-build-parts-list)
- [Instrument case parts list](#Instrument-case-parts-list)
- [Script index](#script-index)


# Essential build
This section details how to build just the control, heating, excitation and emission systems as well as a touchscreen interface - the bare minimum for an operating isothermal platform. All required parts can be found in the [Essential build parts list](#essential-build-parts-list).

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

Return to [page index](#page-index).

### Power source
We used 19V 6.3A laptop power supply packs as power sources for the FABLE-8 units. Alternatively, a 12V power pack with at least 10A output (120W) would suffice. Using a different power supply may need cause a different heating effect and the PID parameters may need to be slightly adjusted. For more detail see the PID_SAFE.py script in the [script index](#script-index).

### Circuit schematic  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/FABL-8_schematic.png)

Return to [page index](#page-index).

### Setting up the Raspberry pi  

1. Use SDFormatter (https://www.sdcard.org/downloads/) to perform a quick format of a microSD card.  

2. Download the preconfigured image from this page named 'NEW-UNIT_19-03-21.img.gz'.
  
3. Use Raspberry Pi Imager (https://www.raspberrypi.org/software/) to write 'NEW-UNIT_19-03-21.img.gz' image to microSD card.  

Details of all scripts packaged into the image file can be found in the [Script index](#script-index).

Return to [page index](#page-index).

## Heating block
The heating block was made from solid aluminium  using a computer numerical control (CNC) machine. The lid plates and resistor retainer plates were made using a drill press. All 2.5mm holes in the heating block were tapped with metric 3mm (M3) threads.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Simple_block_with_threaded_holes.png)

The thermal breaker and temperature sensor are mounted on the rear of the heating block. The thermal breaker mounts using M3 bolts while the temperature sensor is retained using a small clip made from sheet metal that is secured under a thermal breaker mounting bolt head.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/thermal_breaker.png)

## Heating block stands
Stands were made from 1mm thick sheet metal. If sheet metal is difficult to source or work with, any kind of block mounting stand could be fabricated as long as it can withstand a constant 65oC.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/block_stands.png)

## 3D printed parts
All 3D printed parts were printed using black 1.75 PLA filament on a Creality3D Ender-3 3D printer modified with a BLTouch V2 automatic mechanical bed levelling device (https://www.antclabs.com/bltouch).  

### Magnet mount  
Retains two rare earth magnets in its upper cavity. The mount holds the magnets captive when the closed end of the cavity is facing away from the block.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Magnet_mount.png)

### Fixed photodiode mount  
Retains the eight photodiodes and is sandwiched between two 2mm thick block lid plates. The emission filter gel is mounted between the photodiodes and the lower block lid plate.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Fixed_photodiode_mount.png)  

### Fixed LED mount  
Retains the eight LEDs and clamps the excitation filter gel to the block.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Fixed_8-LED_mount.png)  

## Assembly

### Block stands and magnet mount
Two wire wound resistors are fitted into the cavity underneath the heating block and are secured in place using the two resistor retaining plates. The magnet mount is first attached to the block stand with two M5 bolts and nuts. The block is then mounted to the block stand by passing M3 bolts through the gaps in the magnet mounts. 
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Magnet_mount_anno.jpg)

### Excitation system
The eight excitation LEDs are pressed into the fixed LED mount. The excitation gel is sandwiched between the block and the fixed LED mount which is secured in place using M3 bolts, nuts, standoffs and two rear LED mount retainers.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Block_anno.jpg)

### Emission system
The eight photodiodes are fitted into the fixed photodiode mount (with light sensitive surface facing downward through holes) and individually secured with a small piece of sticky tape. The emission filter gels are then overlaid on the light sensitive side of the photodiode mount and secured with the metal lids on both sides using M3 bolts and nuts. Once both block stands are secured to the block, the entire assembly is mounted on a sheet of acrylic.
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/emission_anno.jpg)

Return to [page index](#page-index).

# Instrument case
The key requirements for a FABL-8 casing are firstly that the enclosure blocks out all environmental light and secondly that it provides a thermally insulating environment for the PID controlled heating block to reach and maintain a stable 65oC. Our implementation of the FABL-8 involved a robust briefcase style plastic box and inner acrylic partition that was used to mount the heating block. While this specific setup was ideal for transportation and storage, any casing configuration that meets the abovementioned requirements will suffice. Below we have detailed our case configuration which may be useful as a guide. All required parts can be found in the [Instrument case parts list](#Instrument-case-parts-list).

## 3D printed parts
All 3D printed parts were printed using black 1.75 PLA filament on a Creality3D Ender-3 3D printer modified with a BLTouch V2 automatic mechanical bed levelling device (https://www.antclabs.com/bltouch).  

### Left screen mount  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Left_screen_mount.png)  

### Right screen mount  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Right_Screen_mount.png)  

### Screen face plate  
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Screen_face_plate.png)  

## Block mounting partition
![Image description](https://github.com/abuultjens/FABL-8-Open-Isothermal-Platform/blob/main/Partition.png)  

Return to [page index](#page-index).


# Instructions of use  

* An Initial warmup period occurs upon powerup to stably raise the block temperature to 65oC. 

* Once at operation temperature a reaction can be run by preparing LAMP reagents and template in an OptiGene strip, cutting off the plastic wings on the terminal ends of the strip, removing the magnetic block lid, inserting the strip and replacing the magnetic lid. Specific care must be taken to ensure that all tube lids are firmly pressed closed prior to replacing the block lid.

* The operator then closes the main instrument case lid and uses the touchscreen interface to enter well information and initiate the run. During the run a plot of normalised florescence emission is displayed in real-time. 

* At the conclusion of the run the measurements are saved locally as well as wirelessly uploaded to a webserver via a hotspot hosted by a mobile device. The webserver calculates the derivative of the normalised emission timeseries to classify if the well was positive or negative as well as time to positive (TTP).

Return to [page index](#page-index).

## Essential build parts list
| Part: | Quantity: | Link: |
| --------------- | --------------- | --------------- |
| 12-stage Binary Counter CMOS IC 4040 | 1 | https://www.jaycar.com.au/4040-12-stage-binary-counter-cmos-ic/p/ZC4040 |
| 5M bolts and nuts | 1 | https://www.bunnings.com.au/zenith-m5-x-25mm-316-stainless-steel-round-head-bolt-and-nut-5-pack_p2310748 |
| Arduino Compatible 24V 5A MOS Driver Module | 3 | https://www.jaycar.com.au/arduino-compatible-24v-5a-mos-driver-module/p/XC4488 |
| Arduino Compatible 5V Relay Board | 1 | https://www.jaycar.com.au/arduino-compatible-5v-relay-board/p/XC4419 |
| Arduino Compatible DC Voltage Regulator 2A | 4 | https://www.auselectronicsdirect.com.au/dc-dc-voltage-step-down-converter-module-for-ardui?gclid=Cj0KCQjw3duCBhCAARIsAJeFyPXY0H_Z5v1TH_utRIlQ2Qi64cqLh3KEt3j74XoJ1cvceE0Bd_h9uLgaAl81EALw_wcB |
| Blue 5mm CREE LED 23500mcd Round Clear | 8 | https://www.jaycar.com.au/blue-5mm-cree-led-23500mcd-round-clear/p/ZD0291 |
| DC Power Connector Jack 5 A  2.5 mm  panel mount | 1 | https://au.element14.com/switchcraft-conxall/712a/dc-power-jack-2-5mm-12vdc-5a-solder/dp/1608729 |
| DC power supply 120W 12V | 1 | https://www.jaycar.com.au/12v-dc-10a-desktop-power-supply-2-1mm-dc-plug/p/MP3241 |
| Digital Temperature Sensor Module - DS18B20 | 1 | https://www.jaycar.com.au/digital-temperature-sensor-module/p/XC3700 |
| Emission filter gel: LEE filter 015 and 767 | 1 | http://www.leefilters.com |
| Excitation filter gel: LEE filter 126 | 1 | http://www.leefilters.com |
| HDMI cable 1.5m | 1 | https://www.jaycar.com.au/economy-hdmi-cable-1-5m/p/WV7913?pos=2&queryId=171ab68ba12a5e9c9169ce26e2ab1f60 |
| HDMI resistive touch interface 5inch screen 800x480  | 1 | https://www.jaycar.com.au/5-inch-touchscreen-with-hdmi-and-usb/p/XC9024 |
| Heat Shrink | 1 | https://www.jaycar.com.au/3-0mm-black-heatshrink-tubing/p/WH5532 |
| High current wire (meters) (red and black) | 1 | https://www.jaycar.com.au/black-heavy-duty-hook-up-wire-sold-per-metre/p/WH3041 |
| Low current wire (meters) (various colours) | 2 | https://www.jaycar.com.au/hook-up-wire-pack-2-metres/p/WH3025 |
| M3 bolts 25mm (pack of 25) | 1 | https://www.jaycar.com.au/m3-x-25mm-steel-screws-pk-25/p/HP0414 |
| M3 nuts (pack of 25) | 1 | https://www.jaycar.com.au/m3-steel-nuts-pk-25/p/HP0425 |
| M3 standoff (pack of 8) | 1 | https://www.jaycar.com.au/m3-x-10mm-tapped-metal-spacers-pk8/p/HP0900 |
| M3 washers (pack of 200) | 1 | https://www.jaycar.com.au/3mm-steel-flat-washers-pk-200/p/HP0431 |
| Photodiodes - TSL235R | 8 | https://www.sparkfun.com/products/9768 |
| Phototransistor Optocoupler 4N25/4N28  | 1 | https://www.jaycar.com.au/4n25-4n28-phototransistor-optocoupler/p/ZD1928 |
| Rare Earth Magnets diameter=10mm height=3mm (pack of four) | 1 | https://www.jaycar.com.au/rare-earth-magnet-small-pk-4/p/LM1622 |
| Raspberry Pi 3 Model B+ | 1 | https://www.jaycar.com.au/raspberry-pi-3b-single-board-computer/p/XC9001 |
| Resistor 56 ohm 1/4 Watt | 2 | https://www.jaycar.com.au/56-ohm-1-watt-carbon-film-resistors-pack-of-2/p/RR2544 |
| Single 8-channel Analogue Multiplexer CMOS IC 4051 | 2 | https://www.jaycar.com.au/4051-single-8-channel-analogue-multiplexer-cmos-ic/p/ZC4051 |
| Thermal breaker (80oc) | 1 | https://sinolec.co.uk/en/thermal-cut-out-bimetal-switches/1211447-thermal-cut-out-80c-nc.html |
| Wire Wound Resistor 10 Ohm 10 Watt  | 2 | https://www.jaycar.com.au/10-ohm-10-watt-wire-wound-resistor/p/RR3352 |

Return to [page index](#page-index).

## Instrument case parts list
| Part: | Quantity: | Link: |
| --------------- | --------------- | --------------- |
| Craftright 465 x 360 x 175mm Safe Case | 1 | https://www.bunnings.com.au/craftright-465-x-360-x-175mm-safe-case_p5810252 |
| Black acrylic sheet 6mm thick | 1 | https://www.amazon.com.au/SimbaLux-Acrylic-Plexiglass-Protective-Projects/dp/B07TVKHLP6 |
| IP67 Rated USB Socket - Type A | 1 | https://www.jaycar.com.au/ip67-rated-usb-socket-type-a/p/PS0782 |

Return to [page index](#page-index).

## Script index   
   
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
SCP outfiles to remote server and moves run files to local 'SAVE' dir. You will need to insert your own remote server login details in this script. If you don't want to use any remote server(s) then comment out the lines with `sshpass`
  
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

Return to [page index](#page-index).
