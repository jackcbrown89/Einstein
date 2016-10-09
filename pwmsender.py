import RPi.GPIO as GPIO
import sys
import time, os
import threading
import os, fcntl
import thread

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

print "hello!!"
red = 100
green = 100
blue = 100

def sendpwm(R, G, B):
    print "sendPWM"
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
    print "time sleep"
    time.sleep(1)


def getpipe():
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
        green = line[1]
        blue = line[2]
        


def start():
    print "beginning of start"
    while True:
        print "RED: " + str(red) + " GREEN: " + str(green) + " blue: " + str(blue)
        sendpwm(red, green, blue)

        getpipe()



# thread.start_new_thread(getpipe())


# sendpwm(100, 100, 100)
start()
#sendpwm(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))