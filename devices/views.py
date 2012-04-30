from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from devices.models import Device
from socket import *

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
	sock.connect(('io.kroesch.ch', 50290))
	# TODO: sock.connect((dev.host, port))
	sock.send("setport %i.%i" % (dev.channel, dev.status))
	answer = sock.recv(1024)
	sock.close()
	
	message = "Switching device %s." % device_id
	device_list = Device.objects.all()
	return render_to_response('devices/index.html', {'device_list': device_list})
