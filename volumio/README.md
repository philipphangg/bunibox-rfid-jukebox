# BuniBaniBox

- RFID kids jukebox based on Volumio

## Usefull links

- https://volumio.com/en/get-started/
- https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm 
- https://www.hifiberry.com/hifiberryos/
- https://github.com/Heiss/volumio_websocket/blob/master/volumio_websocket/websocket.py
- https://pypi.org/project/python-socketio/
- https://github.com/volumio/Volumio2/blob/master/app/plugins/user_interface/websocket/index.js
- https://community.volumio.org/t/websocket-home-automation/4255/2

## Installation

### Volumio base installation

See:
- https://volumio.com/en/get-started/
- https://www.pragmaticlinux.com/2021/08/raspberry-pi-headless-setup-with-the-raspberry-pi-imager/

1.) Download and install Raspberry Pi Imager
- https://www.raspberrypi.com/software/

2.) Download Volumio image and extract Zip file
- https://volumio.com/en/get-started/

3.) Open Imager and go to "Choose Image" -> "Custom". Select Image

4.) Select SD-Card as Storage

5.) Startup Raspberry Pi and connect to wlan (disable cable network before) "volumio" with password "volumio2"

6.) Configure device:
- Login: no
- Device name: bunibanibox (http://bunibanibox.local)
- Setup Wifi

7.) Reboot and open http://bunibanibox.local for further settings

### SSH

- Open http://bunibanibox.local/dev/ and enable ssh.
- `ssh volumio@bunibanibox.local` volumio default password: volumio

### HifiBerry MiniAmp 
- Seems to work out of the box. Try to reboot if it doesn't.
- https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/
- https://splittscheid.de/phoniebox-bauanleitung-toniebox-alternative/#ftoc-installation-software

### Pimoroni OnOff Shim
- https://shop.pimoroni.com/products/onoff-shim
- https://github.com/pimoroni/clean-shutdown
- Install with `curl https://get.pimoroni.com/onoffshim | bash`
- Config lives under `vi /etc/cleanshutd.conf`. Changes to config need a restart of the deamon `sudo service cleanshutd restart`


### USB encoders for Arcade Buttons and RFID reader
1.) USB encoders for Arcade-Buttons and RFID need socket.io to communicate with Volumio backend
Install socket.io client for Python with `sudo apt install python-socketio-client python-evdev python-systemd`

2.) Change input device in [rfid_card_usb_encoder.py](bunibox/rfid_card_usb_encoder.py) and [arcade_buttons_usb_encoder.py](bunibox/arcade_buttons_usb_encoder.py)
3.) Copy encoder directory with make `copy-usb-encoders`

4.) SSH to bunibox `ssh volumio@bunibanibox.local` and then `cd bunibox` . 
Install encoders with `sudo ./setup-usb-encoders.sh

5.) If encoders change reload sysctl deamon `systemctl daemon-reload`


## Misc ##
curl -X POST volumio.local/api/v1/replaceAndPlay --header "Content-Type: application/json" -d '{"uri": "INTERNAL://the_kiffness/num_num_cat.mp3","service": "mpd","title": "autostartup song","artist": "null","album": "null","type": "song","tracknumber": 0,"duration": 115,"trackType": "mp3"}'
scp -r ../audio/the_kiffness/Beautiful_Day.mp3 volumio@bunibanibox.local:/data/INTERNAL/the_kiffness/

## Backup ##
`sudo dd if=/dev/sdd | gzip -c >~/Documents/BuniBox/image_uncompressed/bunibaniboxback.img.gz`
`gzip -dc ~/Documents/BuniBox/image_uncompressed/bunibaniboxback.img.gz | dd of=/dev/sdd`

