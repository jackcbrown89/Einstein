import os, tempfile
import time, sys

tmpdir = ""
filename = os.path.join(tmpdir, 'pipe')
print "filename: " + filename
try:
    os.mkfifo(filename)
except IOError, e:
    print "Failed to create FIFO: %s" % e
fifo = open(filename, 'w')
    # write stuff to fifo
fifo.write(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
print "wrote \t" + sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3]
# print >> fifo, "hello"
fifo.close()
# os.remove(filename)





# import os, time, sys
# import errno

# pipe_name = 'pipe_test'

# def child():
# 	# os.mkfifo("")
# 	path = "/pipe"
# 	# try
# 		# os.mkfifo(path)
# 	print "path: "
# 	print path
# 	fifo = open(path, "w")
# 	print fifo
# 	fifo.write(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
# 	fifo.close()
#     # pipeout = os.open(pipe_name, os.O_WRONLY)
#     # os.write(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
#     # os.close()


# child()    


# import os

# path = "/tmp/my_program.fifo"
# os.mkfifo(path)

# fifo = open(path, "w")
# fifo.close()