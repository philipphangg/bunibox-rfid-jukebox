#!/usr/bin/env python2

import sys
import time
from socketIO_client import SocketIO
from systemd import journal
from evdev import categorize, ecodes, KeyEvent, InputDevice

# device = InputDevice('/dev/input/event0')
device = InputDevice('/dev/input/by-id/usb-16c0_27db-event-kbd')
keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
rfidTag = ''
sio = SocketIO('localhost', 3000)
enterKeyLastEvent = time.time()
enterKeyDelay = 3

try:
    for event in device.read_loop():
        if event.type == 1 and event.value == 1:
            if ecodes.KEY[event.code] != 'KEY_ENTER':
                rfidTag += keys[event.code]
            else:
                if enterKeyLastEvent > (time.time() - enterKeyDelay):
                    journal.send("RFID USB Encoder: Skipping emit while locked")
                    rfidTag = ''
                else:
                    enterKeyLastEvent = time.time()
                    playlistName = 'RFID-' + rfidTag
                    rfidTag = ''
                    journal.send("RFID USB Encoder starts playlist " + playlistName )
                    sio.emit('createPlaylist', {"name": playlistName})
                    time.sleep(0.2)
                    sio.emit('playPlaylist', {"name": playlistName})

except:
    journal.send("RFID USB Encoder: ERROR processing input")

