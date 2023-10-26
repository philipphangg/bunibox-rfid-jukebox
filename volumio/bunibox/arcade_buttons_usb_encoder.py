#!/usr/bin/env python2

# Joystick:
# Joystick up "ABS_Y_0" "sio.emit('volume', '+')"
# Joystick down "ABS_Y_255" "sio.emit('volume', '-')"
# Joystick left "ABS_X_0" ""
# Joystick right "ABS_X_255" ""
# Butoons from left to right:
# "BTN_TOP2" "io.emit('prev', '')"
# "BTN_THUMB2" "io.emit('next', '')"
# "BTN_TOP" "io.emit('toggle', '')"
# "BTN_THUMB"
# "BTN_JOYSTICK (BTN_TRIGGER)"


import sys
from socketIO_client import SocketIO
from systemd import journal
from evdev import categorize, ecodes, KeyEvent, InputDevice

device = InputDevice('/dev/input/event1')
sio = SocketIO('localhost', 3000)

try:
    for event in device.read_loop():

        # ABS_Z code=2 scip
        if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Z:
            pass

        # ABS_Y code=1 value=0 -> volume up
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Y and event.value == 0:
                sio.emit('volume', '+')

        # ABS_Y code=1 value=255 -> volume down
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Y and event.value == 255:
                sio.emit('volume', '-')

        # ABS_X code=0 value=0 -> ?
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X and event.value == 0:
            pass

        # ABS_X code=0 value=255 -> ?
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X and event.value == 255:
            pass

        # BTN_TOP2 code=292 value=1 (key down) -> player prev
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP2 and event.value == 1:
                sio.emit('prev', '')

        # BTN_THUMB2 code=290 value=1 (key down) -> player next
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_THUMB2 and event.value == 1:
                sio.emit('next', '')

        # BTN_TOP code=291 value=1 (key down) -> player pause/play
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP and event.value == 1:
                sio.emit('toggle', '')

        # BTN_THUMB code=289 value=1 (key down) -> ?
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_THUMB and event.value == 1:
            pass

        # BTN_JOYSTICK (BTN_TRIGGER) code=289 value=1 (key down) -> ?
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP and event.value == 1:
            pass

except:
    journal.send("An error with Arcade Buttons USB Encoder occurred.")
