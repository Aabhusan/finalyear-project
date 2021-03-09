#!/usr/bin/python36

import socket
import subprocess as sp


s = socket.socket()
ip="192.168.43.222"
port= 4444
s.bind((ip , port))
s.listen(5)


while True:
	conn , addr = s.accept()
	data = conn.recv(20)
	data_decode =  data.decode() #byte data is converted through decode only.
	

	if int(data_decode)==1:
		cmd=sp.getoutput("ansible-playbook /root/Desktop/webserver.yml")
		print("successfully configured webserver")

	elif int(data_decode)==2:
		cmd=sp.getoutput("ansible-playbook /root/Desktop/docker.yml")
		print("successfully execute")

	elif int(data_decode)==3:
		cmd=sp.getoutput("python36 /root/Desktop/automate_hadoop.py")
		print("executing hadoop cluster")

	else:
		cmd="option not supported"
	
	cmd_byte=cmd.encode() #convert into byte
	conn.send(cmd_byte) # send to client




