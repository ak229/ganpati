#!env/bin/python
from pexpect import pxssh
from flask import Flask
import customutils.common
from modules import *
import json
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
	hosts = cluster_config['hosts']
	bigdata_user = cluster_config['bigdata_user']
	bigdata_password = cluster_config['bigdata_password']	
	hadoop_array = {}
	for host in hosts:
		print "----" + host
		hadoop_array[host] = {}
		connection = customutils.common.connect(host,bigdata_user,bigdata_password)
		hadoop_array[host]['home_variable'] = hadoop.home_variable(connection)
		hadoop_array[host]['path'] = hadoop.env(connection)
	return json.dumps(hadoop_array);
# start the server
app.run(debug=ganpati_config['debug'], host=ganpati_config['serverHost'], port=ganpati_config['serverPort'])
