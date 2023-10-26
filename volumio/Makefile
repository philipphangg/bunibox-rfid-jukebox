APP_NAME := bunibanibox
SSH_TARGET := volumio@bunibanibox.local

.PHONY:

## git-crypt ##
decrypt:
	git-crypt unlock ~/git-crypt-${APP_NAME}.private

## sync scripts ##
sync-scripts:
	scp scripts/* ${SSH_TARGET}:scripts/

sync-audio:
	scp -r ../audio/* ${SSH_TARGET}:/data/INTERNAL
	ssh ${SSH_TARGET} sudo chmod -R 755 /data/INTERNAL/*

copy-arcade-buttons-usb-encoder:
	scp bunibox/arcade_buttons_usb_encoder.py ${SSH_TARGET}:bunibox/arcade_buttons_usb_encoder.py

copy-rfid-card-usb-encoder:
	scp bunibox/rfid_card_usb_encoder.py ${SSH_TARGET}:bunibox/rfid_card_usb_encoder.py

copy-usb-encoders:
	scp -r bunibox ${SSH_TARGET}:
	ssh ${SSH_TARGET} chmod +x bunibox/setup-usb-encoders.sh

measure-wlan:
	ssh ${SSH_TARGET} sudo iw dev wlan0 scan | grep -B7 'SSID: Netzgier'

backup-playlists:
	mkdir playlist/$(shell date +%Y%d%m)
	scp -r ${SSH_TARGET}:/data/playlist playlist/$(shell date +%Y%d%m)

copy-startup-sound:
	scp -r startup-song/startup.wav ${SSH_TARGET}:/volumio/app/startup.wav
