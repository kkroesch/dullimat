from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from devices.models import Device
from django.conf import settings
from socket import *

def main(request):
	master = settings.MASTER_DEVICE
	sock = socket()
	sock.connect((settings.MASTER_DEVICE, settings.DEVICE_PORT))
	length = sock.send("getstatus \r\n")
	status = sock.recv(length + 2)
	length = sock.send("getadc 1\r\n")
	temperature = int(sock.recv(length + 2)) / 10.0
	sock.close()

	return render_to_response('index.html', {
		'master': master,
		'status': status,
		'temperature': temperature,
	})
	
def index(request):
	device_list = Device.objects.all()
	return render_to_response('devices/index.html', {'device_list': device_list})

def switch(request, device_id):
	dev = get_object_or_404(Device, pk=device_id)
	if (dev.status == '1'):
		dev.status = 0
	else:
		dev.status = 1
	dev.save()
	
	sock = socket()
	sock.connect((settings.MASTER_DEVICE, settings.DEVICE_PORT))
	# TODO: sock.connect((dev.host, port)) # Instead of master device
	sock.send("setport %i.%i" % (dev.channel, dev.status))
	answer = sock.recv(1024)
	sock.close()
	
	message = "Switching device %s." % device_id
	device_list = Device.objects.all()
	return render_to_response('devices/index.html', {'device_list': device_list})
