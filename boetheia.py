#!/usr/bin/env python3
import RPi.GPIO as GPIO
from os import system
from time import sleep


class boetheia(object):
    """
    Plays a sound if calling
    """

    def __init__(self):
        """
        Init method
        """
        # Settings
        self.isLed = True
        self.ledPin = 17
        self.ldrPin = 4
        self.delay = 0.5

        # GPIO mode to BCM
        GPIO.setmode(GPIO.BCM)
        # LED
        if self.isLed == True:
            GPIO.setup(self.ledPin, GPIO.OUT)
            GPIO.output(self.ledPin, GPIO.HIGH)
        # LDR Sensor
        GPIO.setup(self.ldrPin, GPIO.IN)

        try:
            while True:
                if self.lightSensor() == False:
                    self.action()
                sleep(self.delay)
        except:
            if self.isLed == True:
                GPIO.output(self.ledPin, GPIO.LOW)

    def lightSensor(self):
        """
        Returns state of light sensor
        """
        return GPIO.input(self.ldrPin)

    def action(self):
        """
        Action to be run when laser is detected
        """
        system("mpg123 /home/pi/boetheia/sound.mp3")


Boetheia = boetheia()
