'''
MIT License

Copyright (c) 2012-2017 Ben Croston <ben@croston.org>
Copyright (c) 2019 Hyeonki Hong <hhk7734@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from Odroid._GPIO import *
import sys

VERSION = "0.0.2"

BOARD = 10
BCM = 11
SOC = 100
WIRINGPI = 101

PUD_OFF = 0
PUD_DOWN = 1
PUD_UP = 2

LOW = 0
HIGH = 1

RISING = 1
FALLING = 2
BOTH = 3

UNKNOWN = -1
OUT = 1
IN = 0

_IN_PULL_OFF = IN
_IN_PULL_UP = 2
_IN_PULL_DOWN = 3

_gpio_mode = None


def _warning_unsupported_func():
    func_name = str(sys._getframe(1).f_code.co_name)
    print("'{}' function is not yet supported.".format(func_name))


def setmode(mode):
    global _gpio_mode

    # if _gpio_mode and mode != _gpio_mode:
    #     raise ValueError("A different mode has already been set!")

    _gpio_mode = mode

    if mode == BOARD:
        wiringPiSetupPhys()
    elif (mode == BCM) or (mode == SOC):
        wiringPiSetupGpio()
    elif (mode == WIRINGPI):
        wiringPiSetup()
    else:
        print("'mode' parameter in setupmode() was set to unsupported parameter.")
        sys.exit(1)


def getmode():
    return _gpio_mode


def setup(channels, direction, pull_up_down=PUD_OFF, initial=None):
    if type(channels) is not list:
        channels = [channels]

    if initial is not None:
        # todo
        print(
            "'initial' parameter in setup() is not yet supported. Set to 'None' or not set.")
    else:
        if direction == OUT:
            for i in channels:
                pinMode(i, OUT)
        elif direction == IN:
            if pull_up_down == PUD_OFF:
                direction = _IN_PULL_OFF
            elif pull_up_down == PUD_DOWN:
                direction = _IN_PULL_DOWN
            elif pull_up_down == PUD_UP:
                direction = _IN_PULL_UP

            for i in channels:
                pinMode(i, direction)


def cleanup(channel=None):
    _warning_unsupported_func()


def input(pin):
    return digitalRead(pin)


def output(pin, status):
    digitalWrite(pin, status)


def event_detected(channel):
    _warning_unsupported_func()


def add_event_callback(channel, callback):
    _warning_unsupported_func()


def add_event_detect(channel, edge, callback=None, bouncetime=None):
    _warning_unsupported_func()


def remove_event_detect(channel):
    _warning_unsupported_func()


def wait_for_edge(channel, edge, bouncetime=None, timeout=None):
    _warning_unsupported_func()


def gpio_function(channel):
    _warning_unsupported_func()


def add_edge_detect(gpio, edge, bouncetime):
    _warning_unsupported_func()


def remove_edge_detect(gpio):
    _warning_unsupported_func()


def add_edge_callback(gpio, callback):
    _warning_unsupported_func()


def edge_event_detected(gpio):
    _warning_unsupported_func()


def gpio_event_added(gpio):
    _warning_unsupported_func()


def blocking_wait_for_edge(gpio, edge, bouncetime, timeout):
    _warning_unsupported_func()


def event_cleanup(gpio=None):
    _warning_unsupported_func()


class PWM(object):
    def __init__(self, channel, frequency_hz):
        _warning_unsupported_func()

    def __del__(self):
        _warning_unsupported_func()

    def start(self, duty_cycle_percent):
        _warning_unsupported_func()

    def ChangeFrequency(self, frequency_hz):
        _warning_unsupported_func()

    def ChangeDutyCycle(self, duty_cycle_percent):
        _warning_unsupported_func()

    def stop(self):
        _warning_unsupported_func()

    def _reconfigure(self, frequency_hz, duty_cycle_percent, start=False):
        _warning_unsupported_func()
