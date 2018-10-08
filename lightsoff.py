import RPi.GPIO as GPIO
import re

WORDS = ["LIGHT","LIGHTS","OFF"]

def handle(text, mic, profile):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.HIGH)
    print "lights off"

def isValid(text):
    return bool(re.search(r'\blights off|light off|off\b', text, re.IGNORECASE))
