from customutils import *
def analyze( connection, submodule = "" ):

	# get all the info required
	host = {}
	host['submodule'] = submodule
	host = info( connection , host )

	host = runTests( host )

	return host

def info( connection , host ):
        host['home_variable'] = home_variable ( connection )
        host['path'] = path ( connection )
        host['services'] = services ( connection )
	return host

def runTests( host ):
	# if submodule is hadoop_standalone
        # namenode should match
        # secondary namenode should match
        # datanode should match
	host['tests'] = {}

	if host['submodule'] == "hadoop_standalone":
        	if "NameNode" not in host['services']:
			host['tests']['namenode_running'] = False
                	print "NameNode not Running..."

        	if "SecondaryNameNode" not in host['services']:
			host['tests']['secondarynamenode_running'] = False
                	print "Secondary NameNode not Running..."

        	if "DataNode" not in host['services']:
			host['tests']['datanode_running'] = False
                	print "DataNode not Running..."


        # if submodule is hadoop_cluster_server
        # atleast one should be working
        # if namenode is present, data node should not be present

	return host	

def home_variable( connection ):
	# check if hadoop_home is set
	# if hadoop_home is set, return true
	# else return 1
	print common.execute( connection, 'ls')
	return common.execute(connection,'echo $HADOOP_HOME')[0]

def path( connection ):
	# check if hadoop_home is in the path
	# if hadoop_home is in the path, return true
	# else return 2
        return common.execute(connection,'echo $PATH')[0]

def services( connection ):
	# return the services that are running
	# e.g. namenode, secondary namenode, data note, resource manager etc.
	
	return common.execute(connection,"jps |  awk '{print $2}' | grep -v \"Jps\"")

def cluster_config():
	# check if the clusterid of the data and namenode directory is same
	return True
