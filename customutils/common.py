from pexpect import pxssh
import os
import json
from collections import defaultdict
def getconf( name ):
	# initialize parameters
	with open(os.getcwd()+'/config/'+name+'.json') as config_file:
    		config = json.load(config_file)
	return config

def connect( ip, username, password ):
       	try: 
		s = pxssh.pxssh()
        	s.login(ip, username, password)
        	return s
	except pxssh.ExceptionPxssh as e:
		print "Could not reach host --- " + ip

def execute( connection, command ):
	connection.sendline(command)
        connection.prompt()
	return connection.before.splitlines()[1:]
