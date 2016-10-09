import os, time, sys
pipe_name = 'pipe_test'

def child():
    pipeout = os.open(pipe_name, os.O_WRONLY)
    os.write(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
    os.close()


child()    
