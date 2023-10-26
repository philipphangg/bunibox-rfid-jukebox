#!/usr/bin/env python3

# Joystick:
# Joystick up "ABS_Y_0" "functionCallVolU"
# Joystick down "ABS_Y_255" "functionCallVolD"
# Joystick left "ABS_X_0" ""
# Joystick right "ABS_X_255" ""
# Butoons from left to right:
# "BTN_TOP2" "functionCallPlayerPrev"
# "BTN_THUMB2" "functionCallPlayerNext"
# "BTN_TOP" "functionCallPlayerPause"
# "BTN_TOP2" "functionCallPlayerPrev"
# "BTN_THUMB"
# "BTN_JOYSTICK (BTN_TRIGGER)"


import sys

sys.path.append(".") # This command should be before imports of components

import logging
from evdev import categorize, ecodes, KeyEvent, InputDevice
from components.gpio_control.function_calls import phoniebox_function_calls

device = InputDevice('/dev/input/event1')
logger = logging.getLogger(__name__)

try:
    function_calls = phoniebox_function_calls()
    for event in device.read_loop():

        # ABS_Z code=2 scip
        if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Z:
            pass

        # ABS_Y code=1 value=0 -> volume up
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Y and event.value == 0:
            try:
                getattr(function_calls, 'functionCallVolU')()
            except:
                logger.warning(
                    "Function functionCallVolU not found in function_calls.py event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Y and event.value == 0")

        # ABS_Y code=1 value=255 -> volume down
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Y and event.value == 255:
            try:
                getattr(function_calls, 'functionCallVolD')()
            except:
                logger.warning(
                    "Function functionCallVolD not found in function_calls.py; event.type == ecodes.EV_ABS and event.code == ecodes.ABS_Y and event.value == 255")

        # ABS_X code=0 value=0 -> ?
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X and event.value == 0:
            pass
             # try:
             #     getattr(function_calls, 'functionCallPlayerSeekBack')()
             # except:
             #     logger.warning(
             #         "Function functionCallPlayerSeekBack not found in function_calls.py; event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X and event.value == 0")

        # ABS_X code=0 value=255 -> ?
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X and event.value == 255:
            pass
            # try:
            #     getattr(function_calls, 'functionCallPlayerSeekFwd')()
            # except:
            #     logger.warning(
            #         "Function functionCallPlayerSeekFwd not found in function_calls.py; event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X and event.value == 255")

        # BTN_TOP2 code=292 value=1 (key down) -> player priv
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP2 and event.value == 1:
            try:
                getattr(function_calls, 'functionCallPlayerPrev')()
            except:
                logger.warning(
                    "Function functionCallPlayerPrev not found in function_calls.py; event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP2 and event.value == 1")

        # BTN_THUMB2 code=290 value=1 (key down) -> player next
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_THUMB2 and event.value == 1:
            try:
                getattr(function_calls, 'functionCallPlayerNext')()
            except:
                logger.warning(
                    "Function functionCallPlayerNext not found in function_calls.py; event.type == ecodes.EV_KEY and event.code == ecodes.BTN_THUMB2 and event.value == 1")

        # BTN_TOP code=291 value=1 (key down) -> player pause/play
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP and event.value == 1:
            try:
                getattr(function_calls, 'functionCallPlayerPause')()
            except:
                logger.warning(
                    "Function functionCallPlayerPause not found in function_calls.py; event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP and event.value == 1")

        # BTN_THUMB code=289 value=1 (key down) -> ?
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_THUMB and event.value == 1:
            pass
            # try:
            #     getattr(function_calls, 'functionCallPlayerRandomCard')()
            # except:
            #     logger.warning(
            #         "Function functionCallPlayerRandomCard not found in function_calls.py; event.type == ecodes.EV_KEY and event.code == ecodes.BTN_THUMB and event.value == 1")


        # BTN_JOYSTICK (BTN_TRIGGER) code=289 value=1 (key down) -> ?
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP and event.value == 1:
            pass
            # try:
            #     getattr(function_calls, 'functionCallPlayerRandomFolder')()
            # except:
            #     logger.warning(
            #         "Function functionCallPlayerRandomFolder not found in function_calls.py; event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOP and event.value == 1")


except:
    logger.error("An error with Buttons USB Encoder occurred.")
