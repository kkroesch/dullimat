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

	
	
set_port(1, 1)
sleep(1)
set_port(2, 1)
sleep(1)
set_port(1, 0)
sleep(1)
set_port(2, 0)
sleep(2)

set_port(1, 1)
set_port(2, 1)
print get_status()
sleep(2)

set_port(1, 0)
set_port(2, 0)

print get_status()

sock.close()