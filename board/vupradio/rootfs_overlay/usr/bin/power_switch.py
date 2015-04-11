#!/usr/bin/env python

#this is the GPIO pin connected to the lead on switch labeled OUT
GPIOpin1=23

#this is the GPIO pin connected to the lead on switch labeled IN
GPIOpin2=24

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIOpin1, GPIO.IN)
GPIO.setup(GPIOpin2, GPIO.OUT)
GPIO.output(GPIOpin2, GPIO.HIGH)

import os, time
while True:
  GPIO.wait_for_edge(GPIOpin1, GPIO.RISING)
  time.sleep(1)
  if GPIO.input(GPIOpin1):
    print("rising edge on GPIO {} detected. Shutting down".format(GPIOpin1))
    break

os.system("poweroff")
