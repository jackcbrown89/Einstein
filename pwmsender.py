import RPi.GPIO as GPIO
import sys
import time
import threading
import os, fcntl
import thread

print "hello!!"
red = 100
green = 100
blue = 100
change = 0

pipe_name = 'pipe'
path = 'pipe'
try:
    fifo = open(path, "r", 0)
    fd = fifo.fileno()
    flag = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, flag | os.O_NONBLOCK)

except OSError, e:
    print "Failed to create FIFO: %s" % e
    # exit here or something?

# pipe_actual = open(pipe_name, 'r')


def sendpwm(R, G, B):
    global red
    global blue
    global green
    global change
    if change == 1:
        #p1.stop()
        #p2.stop()
        #p3.stop()
        GPIO.cleanup()
        change = 0
    print "sendPWM"
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    
    p1 = GPIO.PWM(12, (red))
    print("red's good")
    p2 = GPIO.PWM(16, (green))
    print("green's good")
    p3 = GPIO.PWM(18, (blue))
    print("blue's good")
    p1.start(1)
    p2.start(1)
    p3.start(1)
    print "time sleep"
    time.sleep(1)


def getpipe():
    global red
    global blue
    global green
    global change
    print("GETPIPE pwmSENDER\n")
    # pipein = open(pipe_name, 'r')

    path = "pipe"
    # try:
        # fifo = open(path, "r", 0)
    # except OSError, e:
        # print "Failed to create ??: %s" % e
    # else:
    for line in fifo:
        print "Received: " + line + "\n",
        # if(line is not None):
        line = line.split(",")
        print "Split lines: "
        print line
        red = line[0]
        print(red)
        green = line[1]
        print(green)
        blue = line[2]
        print(blue)
        change = 1
        


def start():
    global red
    global blue
    global green
    global change
    print "beginning of start"
    while True:
        print "RED: " + str(red) + " GREEN: " + str(green) + " blue: " + str(blue)
        sendpwm(red, green, blue)
        getpipe()


start()
