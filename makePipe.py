import os, tempfile

tmpdir = "/"
filename = os.path.join(tmpdir, 'pipe')
print filename
try:
    os.mkfifo(filename)
except OSError, e:
    print "Failed to create FIFO: %s" % e
else:
    fifo = open(filename, os.O_WRONLY)
    # write stuff to fifo
    print >> fifo, "hello"
    fifo.close()
    os.remove(filename)
    os.rmdir(tmpdir)





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