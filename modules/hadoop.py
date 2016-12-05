from customutils import *
def home_variable( connection ):
	# check if hadoop_home is set
	# if hadoop_home is set, return true
	# else return 1
	hadoop_home = connection.sendline('echo $HADOOP_HOME')
	connection.prompt()
	return connection.before.splitlines()[1]

def env( connection ):
	# check if hadoop_home is in the path
	# if hadoop_home is in the path, return true
	# else return 2
        hadoop_home = connection.sendline('echo $PATH')
        connection.prompt()
        return connection.before.splitlines()[1]

def services():
	# return the services that are running
	# e.g. namenode, secondary namenode, data note, resource manager etc.
	
	return True

def cluster_config():
	# check if the clusterid of the data and namenode directory is same
	return True
