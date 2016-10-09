import RPi.GPIO as GPIO
import sys
import time
import asyncio
from rx import Observable


async def sendpwm(R, G, B):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    
    p1 = GPIO.PWM(12, R)
    p2 = GPIO.PWM(16, G)
    p3 = GPIO.PWM(18, B)
    p1.start(1)
    p2.start(1)
    p3.start(1)

def outsideloop:


sendpwm(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))