import pylab as plt
import time
import threading
import random
import socket
from pylab import *


host = '0.0.0.0' 
port = 8888 
backlog = 5 
size = 1024 

dataX = []
dataY = []

# This just simulates reading from a socket.
def runSocket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host,port)) 
	s.listen(backlog)
	while 1: 
        	client, address = s.accept() 
        	cr = client.recv(size).split(",")   
        	print cr      
        	if cr:
           		dataX.append(cr[0])
           		dataY.append(cr[1])
           		#print cr
           		#print "\n" 	       	    
        
    	

if __name__ == '__main__':
	th = threading.Thread(target=runSocket)
	th.daemon = True
	th.start()
	fig = plt.figure()   
	plt.ylim(-2, 2)
	plt.xlim(-2, 2)
	plt.ion()
	plt.show()    
	while True:
        	print dataX
        	print dataY
        	print "\n"
        	l = plt.plot(dataX, dataY);
        	setp(l,linewidth=3,color="r",linestyle='-')
        	#plt.pause(1)
        	#ln.set_ydata([x[0] for x in data[len(data)-101:len(data)-1:])
        	plt.draw()

