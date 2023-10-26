# BuniBox with Phoniebox

BuniBox based on Phoniebox software from 2022. As Phoniebox may have changed, things can be different today.  

## Usefull links

- https://github.com/MiczFlor/RPi-Jukebox-RFID
- https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm 
- https://koboldimkopf.wordpress.com/2020/01/10/tutorial-phoniebox/
- https://splittscheid.de/phoniebox-bauanleitung-toniebox-alternative/#ftoc-installation-software
- https://mopidy.com/ext/spotify/#authentication
- https://www.hifiberry.com/hifiberryos/



## Installation

### Base installation
Phoniebox needs Debian Buster. Install Image with Raspberry Pi Imager in headless mode.
See:
- https://github.com/MiczFlor/RPi-Jukebox-RFID/wiki/INSTALL-stretch
- https://www.pragmaticlinux.com/2021/08/raspberry-pi-headless-setup-with-the-raspberry-pi-imager/

1.) Download and install Raspberry Pi Imager
- https://www.raspberrypi.com/software/

2.) Download Debian Buster Image
- https://downloads.raspberrypi.org/raspios_oldstable_lite_armhf/images/raspios_oldstable_lite_armhf-2021-12-02/

3.) Open Imager and go to "Choose Image" -> "Custom". Select Image

4.) Select SD-Card as Storage

5.) Open Settings. If not Present hit "CTRL"+"SHIFT"+"x"
- Set hostname: bunibanibox.local
- Set username and password
- Configure Wifi
- Set local settings
- Skip first-run wizard

6.) Startup Raspberry Pi and connect `ssh pi@bunibanibox`. Update `sudo apt update && sudo apt upgrade`.
Reboot `sudo reboot` and after reboot cleanup `sudo apt autoremove`


### HifiBerry MiniAmp 
- https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/
- https://splittscheid.de/phoniebox-bauanleitung-toniebox-alternative/#ftoc-installation-software

1.) `sudo vi /boot/config.txt` -> `# dtparam=audio=on` + `dtoverlay=hifiberry-dac` + `dtoverlay=vc4-fkms-v3d,audio=off`
2.) `sudo vi /etc/asound.conf`
pcm.hifiberry {
    type softvol
    slave.pcm "plughw:0"
    control.name "Master"
    control.card 0
}
pcm.!default {
    type plug
    slave.pcm "hifiberry"
}

3.) `sudo reboot` and test with `aplay -l` and `speaker-test -D hifiberry -c 2`.
Sound could be played with `aplay -vvv audio/agnes_obel-falling_catching.wav`

4.) To reduce system audio volume run `alsamixer`

### Pimoroni OnOff Shim
- https://shop.pimoroni.com/products/onoff-shim
- https://github.com/pimoroni/clean-shutdown
- Install with `curl https://get.pimoroni.com/onoffshim | bash`
- Config lives under `vi /etc/cleanshutd.conf`. Changes to config need a restart of the deamon `sudo service cleanshutd restart`
To enable shutdown sound add `/usr/bin/mpg123 /home/pi/RPi-Jukebox-RFID/shared/shutdownsound.mp3` after `if shutdown_trigger; then`


### Phoniebox installation  ##

- https://github.com/MiczFlor/RPi-Jukebox-RFID/wiki/INSTALL-stretch#one-line-install-command
Master:
`cd; rm buster-install-*; wget https://raw.githubusercontent.com/MiczFlor/RPi-Jukebox-RFID/master/scripts/installscripts/buster-install-default.sh; chmod +x buster-install-default.sh; ./buster-install-default.sh`
Develop:
`cd; rm buster-install-*; wget https://raw.githubusercontent.com/MiczFlor/RPi-Jukebox-RFID/develop/scripts/installscripts/buster-install-default.sh; chmod +x buster-install-default.sh; GIT_BRANCH=develop bash ./buster-install-default.sh`
1.) Do you want to use interactive installation „Y“
2.) Do you want to configure your WiFi? [Y/n] n
3.) Use Headphone as iFace? [Y/n] n -> „Master“
4.) Do you want to enable Spotify? [Y/n] y
* Spotify-Mopidy Auth: https://mopidy.com/ext/spotify/#authentication
5.) Do you want to configure MPD? [Y/n] n
6.) Do you want to use the default location? [Y/n] y (/home/pi/RPi-Jukebox-RFID/shared/audiofolders)
7.) Do you want to activate the GPIO-Control-Service? [Y/n] n
8.) Start first part of installation with „Y“.
9.) Have you connected your RFID reader? „Y“, Please select the RFID reader you want to use: „1“ (Neuftech Reader) + "1" „HID 16c0:27db Keyboard“.
10.) Question after boot „n“



### Arcade Buttons ##
- https://github.com/MiczFlor/RPi-Jukebox-RFID/tree/develop/components/controls/buttons_usb_encoder

1.) `make sync-buttons-usb-encoder`
2.) `cd RPi-Jukebox-RFID/`
3.) `bash components/controls/buttons_usb_encoder/setup-buttons-usb-encoder.sh`
4.) `sudo reboot`


### Faster boot times ##

#### Deactivate MTA (Message Transfer Agend) for mails `sudo update-rc.d exim4 remove`

#### sudo vi /boot/config.txt tweaks
````
# Disables loading Bluetooth
dtoverlay=disable-bt
# Boot Delay Time
boot_delay=0
# the rainbow splash screen will not be shown on boot
disable_splash=1
# Initial Turbo in seconds; max. 60 seconds
initial_turbo=20
````

#### sudo vi sudo vi /etc/dhcpcd.conf
```
noarp
ipv4only
noipv6
```

## Backup ##
`sudo dd if=/dev/sdd | gzip -c >~/Cloud9/Documents/BuniBox/image_uncompressed/bunibaniboxback.img.gz`
`gzip -dc ~/Cloud9/Documents/BuniBox/image_uncompressed/bunibaniboxback.img.gz | dd of=/dev/sdd`
