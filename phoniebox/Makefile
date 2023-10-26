APP_NAME := bunibanibox

.PHONY:

## sync scripts ##
sync-scripts:
	scp scripts/* pi@bunibanibox:scripts/

sync-audio:
	scp -r audio/* pi@bunibanibox:RPi-Jukebox-RFID/shared/audiofolders/

sync-buttons-usb-encoder:
	scp buttons_usb_encoder/setup-buttons-usb-encoder.sh pi@bunibanibox:RPi-Jukebox-RFID/components/controls/buttons_usb_encoder/setup-buttons-usb-encoder.sh
	scp buttons_usb_encoder/buttons_usb_encoder.py pi@bunibanibox:RPi-Jukebox-RFID/components/controls/buttons_usb_encoder/buttons_usb_encoder.py
