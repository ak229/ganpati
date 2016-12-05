#!env/bin/python

from pexpect import pxssh
from flask import Flask


def make_connection( ip ):
	s = pxssh.pxssh()
	hostname = ip
	username = 'root'
	password = 'redhat'
	s.login(hostname, username, password)
	return s


#k = s.sendline ('ps aux | grep kafka')
# s.sendline('source /etc/environment')


def check_kafka( conn ):
	conn.sendline('ps aux | grep zookeeper | grep -v "grep" | wc -l')

	conn.prompt()

	print conn.before



def check_hdd( conn ):
	conn.sendline('df')
	conn.prompt()

	return conn.before
	

def check_stuff( ip ):

	#print "Connecting"
	k = make_connection( ip )

	#print "checking kafka"
	#check_kafka( k )

	#print "checking df"
	conn.sendline("echo $PATH");
	return conn.before
	#return check_hdd( k )


# print "Checking on 0.3"
# check_stuff('172.17.0.3')

# print "Checking on local"
# check_stuff("localhost")


app = Flask(__name__)

@app.route('/')
def index():
    return check_stuff('172.17.0.3')
#eturn "hello World"

if __name__ == '__main__':
    app.run(debug=True, host='172.17.0.2', port=80)





