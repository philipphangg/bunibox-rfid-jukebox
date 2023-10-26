#!/usr/bin/env python3

import evdev


device = evdev.InputDevice('/dev/input/event1')
print(device)

# leiser: ABS_Y code=1 value=255
# lauter: ABS_Y code=1 value=0
# rechts: ABS_X code=0 value=255
# links: ABS_X code=0 value=0
# "BTN_TOP2"
# "BTN_THUMB2" "functionCallPlayerNext"
# "BTN_TOP" "functionCallPlayerPause"
# "BTN_TOP2" "functionCallPlayerPrev"
# "BTN_THUMB"
# "BTN_JOYSTICK (BTN_TRIGGER)"

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_X:
            print(evdev.categorize(event))
            print(event.code)
            print(event.value)

        if event.code == evdev.ecodes.ABS_Y:
            print(evdev.categorize(event))
            print(event.code)
            print(event.value)

    if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))
            print(event.code)
            print(event.value)

