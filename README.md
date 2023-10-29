# BuniBox

RFID Kids Audio Jukebox Project with USB Arcade Buttons and Joystick for Volume Control, Based on Volumio (+ old version with Phoniebox). If you come across this repository, feel free to use it. However, please examine the code thoroughly before implementing it, as not everything is universally applicable and may not fit your specific environment.

The project was initially started with Phoniebox in 2021. In 2022, Spotify disabled a deprecated API and made it mandatory to use the Spotify Playback API. As a result, support for most open-source audio projects was broken. Subsequently, a new software solution was sought, and Volumio was chosen for the project.

The advantages of using Volumio for this project include Spotify support and a well-documented API. The installation process is also more straightforward. Using Volumio's API, you can easily create an RFID kids' jukebox. RFID and arcade buttons are implemented as Python services/daemons, as they existed from the initial Phoniebox implementation. Additionally, Volumio's plugin system allows for the possibility of implementing a plugin ;)


## How It Works

Whenever a new and unknown RFID card is placed on the reader, a Volumio playlist is automatically created with a combined name that includes "RFID-" as a prefix along with the card code (e.g. RFID-7334897777). When a known RFID card is placed on the reader, the associated playlist is played. Since the card code is printed on the RFID cards, finding the corresponding playlists is easy. To add music, podcasts, internet radio stations, or any other content to the playlists, Volumio's GUI is utilized.

## Software documentation

The main software documentation/HowTo of the RFID kids audio jukebox based on Volumio can be found in the folder [volumio/](volumio/README.md). 
The old software documentation/HowTo of the RFID kids audio jukebox based on Phoniebox is under [phoniebox/](phoniebox/README.md)

## Hardware

This section serves as documentation for building an RFID kids' audio jukebox. Here's a list of hardware components used:

Hardware list:
- Raspberry Pi 4
- PIMORONI OnOff Shim
- LED Arcade DIY Kit Parts, including USB Encoder, PC Ellipse & Oval Stil Bat Joystick, and 5 V LED Arcade Buttons (available on Amazon)
- Neuftech USB RFID Reader ID Card Reader for EM4100
- HiFiBerry MiniAmp
- VISATON F 8 SC speakers
- USB mini disco lights
- An assortment of small parts ;)

![BuniBox outside](img/bunibox_outside.jpg?raw=true "Title")
![BuniBox inside](img/bunibox_inside.jpg?raw=true "Title")





