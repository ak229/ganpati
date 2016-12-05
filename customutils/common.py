from pexpect import pxssh
import os
import json
def getconf( name ):
	# initialize parameters
	with open(os.getcwd()+'/config/'+name+'.json') as config_file:
    		config = json.load(config_file)
	return config
def connect( ip, username, password ):
        s = pxssh.pxssh()
        s.login(ip, username, password)
        return s	
