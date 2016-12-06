#!env/bin/python
from pexpect import pxssh
from flask import Flask
import customutils.common
from modules import *
import json
import sys
ganpati_config = customutils.common.getconf('ganpati') 

# initialize flask
app = Flask(__name__)



# routes
@app.route('/')
def index():
        return "Ganpati"

@app.route('/hadoop')
def hadoop_summary():
	# get the cluster information
	cluster_config = customutils.common.getconf('cluster')
	hosts = cluster_config['hosts_info_temp']
	bigdata_user = cluster_config['bigdata_user']
	bigdata_password = cluster_config['bigdata_password']	
	hadoop_array = {}
	for host in hosts:
		#hadoop_array[host] = {}
		print host
		print host["ip"]
		modules = host['module']
		submodules = host['submodule']
		connection = customutils.common.connect(host["ip"],bigdata_user,bigdata_password)
		if connection is not None:
			for submodule in submodules:
				print "Submodule is  "+submodule
				hadoop_array[host["ip"]] = hadoop.analyze( connection , submodule)
	return json.dumps(hadoop_array);

# debug options
# command line will override config
if len(sys.argv) == 1:
	debugMode = ganpati_config['debug']
elif sys.argv[1] == "--debug":
	debugMode = "True"

# start the server
if debugMode == "True":
	app.run(debug=bool(ganpati_config['debug']), host=ganpati_config['serverHost'], port=ganpati_config['serverPort'])
else:
	app.run(debug=False, host=ganpati_config['serverHost'], port=ganpati_config['serverPort'])
