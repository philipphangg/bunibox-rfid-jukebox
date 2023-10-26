#!/usr/bin/env bash

chmod +x arcade_buttons_usb_encoder.py

printf "\nStart arcade-buttons-usb-encoder service...\n"
cp -v arcade-buttons-usb-encoder.service /etc/systemd/system/arcade-buttons-usb-encoder.service
systemctl start arcade-buttons-usb-encoder.service
systemctl enable arcade-buttons-usb-encoder.service


chmod +x rfid_card_usb_encoder.py

printf "\nStart rfid-card-usb-encoder service...\n"
cp -v rfid-card-usb-encoder.service /etc/systemd/system/rfid-card-usb-encoder.service
systemctl start rfid-card-usb-encoder.service
systemctl enable rfid-card-usb-encoder.service
