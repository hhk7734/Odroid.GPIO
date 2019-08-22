# Odroid.GPIO

## Installation

```bash
$ sudo apt install -y python3-pip &&\
  python3 -m pip install -U pip setuptools
```

```bash
$ python3 -m pip install -U Odroid.GPIO
```

## Example

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

print("  BOARD ")
print("  1 |  2")
print("  3 |  4")
print("  5 |  6")
print("  7 |  8")
print("  9 | 10")
print(" 11 | 12")
print(" 13 | 14")
print(" 15 | 16")
print(" 17 | 18")
print(" 19 | 20")
print(" 21 | 22")
print(" 23 | 24")
print(" 25 | 26")
print(" 27 | 28")
print(" 29 | 30")
print(" 31 | 32")
print(" 33 | 34")
print(" 35 | 36")
print(" 37 | 38")
print(" 39 | 40")

GPIO.setup(35, GPIO.OUT)

while True:
    GPIO.output(35, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(35, GPIO.LOW)
    time.sleep(1)
```
