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
    '''
    Set up numbering mode to use for channels.
    BOARD    - Use Raspberry Pi board numbers.
    BCM      - Use SOC GPIO 00..nn numbers.
    SOC      - Use SOC GPIO 00..nn numbers.
    WIRINGPI - Use wiringPi pin numbers.
    '''
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
    '''
    Get numbering mode used for channel numbers.
    Returns BOARD, BCM, SOC, WIRINGPI or None
    '''
    return _gpio_mode


def setup(channels, direction, pull_up_down=PUD_OFF, initial=None):
    '''
    Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control.
    channel        - A pin number depending on which mode is set.
    direction      - IN or OUT
    [pull_up_down] - PUD_OFF (default), PUD_UP or PUD_DOWN
    [initial]      - Initial value for an output channel"
    '''
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
    '''
    Clean up by resetting all GPIO channels that have been used by this program to INPUT
            with no pullup/pulldown and no event detection.
    [channel] - individual channel or list/tuple of channels to clean up.
            Default - clean every channel that has been used.
    '''
    _warning_unsupported_func()


def input(pin):
    '''
    Input from a GPIO channel.  Returns HIGH=1=True or LOW=0=False.
    channel - A pin number depending on which mode is set.
    '''
    return digitalRead(pin)


def output(pin, status):
    '''
    Output to a GPIO channel or list of channels.
    channel - A pin number depending on which mode is set.
    value   - 0/1 or False/True or LOW/HIGH.
    '''
    digitalWrite(pin, status)


def event_detected(channel):
    '''
    Returns True if an edge has occurred on a given GPIO.
            You need to enable edge detection using add_event_detect() first.
    channel - A pin number depending on which mode is set.
    '''
    _warning_unsupported_func()


def add_event_callback(channel, callback):
    '''
    Add a callback for an event already defined using add_event_detect().
    channel      - A pin number depending on which mode is set.
    callback     - A callback function.
    '''
    _warning_unsupported_func()


def add_event_detect(channel, edge, callback=None, bouncetime=None):
    '''
    Enable edge detection events for a particular GPIO channel.
    channel      - A pin number depending on which mode is set.
    edge         - RISING, FALLING or BOTH.
    [callback]   - A callback function for the event (optional).
    [bouncetime] - Switch bounce timeout in ms for callback.
    '''
    _warning_unsupported_func()


def remove_event_detect(channel):
    '''
    Remove edge detection for a particular GPIO channel.
    channel - A pin number depending on which mode is set.
    '''
    _warning_unsupported_func()


def wait_for_edge(channel, edge, bouncetime=None, timeout=None):
    '''
    Wait for an edge.  Returns the channel number or None on timeout.
    channel      - A pin number depending on which mode is set.
    edge         - RISING, FALLING or BOTH.
    [bouncetime] - Time allowed between calls to allow for switchbounce.
    [timeout]    - Timeout in ms.
    '''
    _warning_unsupported_func()


def gpio_function(channel):
    '''
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI).
    channel - A pin number depending on which mode is set.
    '''
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
        '''
        Start software PWM.
        duty_cycle_percent - the duty cycle (0.0 to 100.0).
        '''
        _warning_unsupported_func()

    def ChangeFrequency(self, frequency_hz):
        '''
        Change the frequency.
        frequency_hz - frequency in Hz (freq > 1.0).
        '''
        _warning_unsupported_func()

    def ChangeDutyCycle(self, duty_cycle_percent):
        '''
        Change the duty cycle.
        duty_cycle_percent - between 0.0 and 100.0.
        '''
        _warning_unsupported_func()

    def stop(self):
        '''
        Stop software PWM.
        '''
        _warning_unsupported_func()

    def _reconfigure(self, frequency_hz, duty_cycle_percent, start=False):
        _warning_unsupported_func()

def setwarnings(enable)
    '''
    Enable or disable warning messages.
    '''
    _warning_unsupported_func()
