from socket import *
from time import sleep

host = 'io.kroesch.ch'
port = 50290
sock = socket()
sock.connect((host, port))


def set_port(channel, value) :
	global sock
	sock.send("setport %i.%i" % (channel, value))
	answer = sock.recv(1024)
	return answer

def get_status() :
	global sock
	sock.send('getstatus')
	answer = sock.recv(1024)
	return answer

	
while (1):	
	set_port(1, 1)
	sleep(4)
	set_port(1, 0)
	set_port(2, 1)
	sleep(1)
	set_port(2, 0)
	set_port(3, 1)
	sleep(4)
	set_port(2, 1)
	sleep(1)
	set_port(3, 0)
	set_port(2, 0)

sock.close()