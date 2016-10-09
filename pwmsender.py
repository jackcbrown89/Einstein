import RPi.GPIO as GPIO
import sys
import time, os
import threading
import os, fcntl
import thread

pipe_name = 'pipe_test'

fcntl.fcntl(pipe_name, fcntl.F_SETFL, os.O_NONBLOCK)

red = 100
green = 100
blue = 100

def sendpwm(R, G, B):
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

    time.wait(1)


def getpipe():
    print("Hello")
    pipein = open(pipe_name, 'r')
    line = pipein.readline()
    if(line is not None):
        line = line.split(",")
        red = line[0]
        green = line[1]
        blue = line[2]


def start():
    while True:
        sendpwm(red, green, blue)
        getpipe()



# thread.start_new_thread(getpipe())


# sendpwm(100, 100, 100)
start()
#sendpwm(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))