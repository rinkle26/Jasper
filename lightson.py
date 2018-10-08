import RPi.GPIO as GPIO
import re

WORDS = ["LIGHT","LIGHTS","ON"]

def handle(text, mic, profile):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.LOW)
    print "lights on"

def isValid(text):
    return bool(re.search(r'\blights on|light on|on\b', text, re.IGNORECASE))
