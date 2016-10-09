import os, time, sys
pipe_name = 'pipe_test'

def child():
	# os.mkfifo("")
	path = "/pipe"
	os.mkfifo(path)

	fifo = open(path, "w")
	fifo.write(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
	fifo.close()
    # pipeout = os.open(pipe_name, os.O_WRONLY)
    # os.write(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
    # os.close()


child()    


# import os

# path = "/tmp/my_program.fifo"
# os.mkfifo(path)

# fifo = open(path, "w")
# fifo.close()