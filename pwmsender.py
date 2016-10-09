import RPi.GPIO as GPIO
import sys
import time, os
import threading
import os, fcntl
import thread

pipe_name = 'pipe_test'
# pipe_actual = open(pipe_name, 'r')

fcntl.fcntl(pipe_actual, fcntl.F_SETFL, os.O_NONBLOCK)

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

    time.sleep(1)


def getpipe():
    print("GETPIPE pwmSENDER")
    # pipein = open(pipe_name, 'r')

    # line = pipe_actual.readline()


    path = "pipe"
    try:
        fifo = open(path, "r", 0)
    except OSError, e:
        print "Failed to create FIFO: %s" % e
    else:
        for line in fifo:
            print "Received: " + line,
            # if(line is not None):
            line = line.split(",")
            red = line[0]
            green = line[1]
            blue = line[2]
        fifo.close()



def start():
    while True:
        sendpwm(red, green, blue)
        getpipe()



# thread.start_new_thread(getpipe())


# sendpwm(100, 100, 100)
start()
#sendpwm(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))