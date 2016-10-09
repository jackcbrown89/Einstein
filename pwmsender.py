import RPi.GPIO as GPIO
import os, time, sys
pipe_name = 'pipe_test'

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

def parent():
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time())

sendpwm(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))