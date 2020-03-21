![license](https://img.shields.io/github/license/hhk7734/Odroid.GPIO)
![pypi](https://img.shields.io/pypi/v/Odroid.GPIO)
![language](https://img.shields.io/github/languages/top/hhk7734/Odroid.GPIO)

# Odroid.GPIO

## Installation

```shell
sudo apt update \
&& sudo apt install -y python3 python3-dev python3-pip \
    odroid-wiringpi libwiringpi-dev
```

```bash
python3 -m pip install -U --user pip Odroid.GPIO
```

## Blink example

```python
import Odroid.GPIO as GPIO
# You can also use 'import RPi.GPIO as GPIO'.
import time

'''
GPIO.BCM == GPIO.SOC
GPIO.BOARD
GPIO.WIRINGPI
'''
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)

while True:
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(13, GPIO.LOW)
    time.sleep(1)
```

## Changelog

Ref: CHANGELOG
