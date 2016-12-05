# Ganpati
A tool to make troubleshooting Hadoop installations easy.

## What is this tool for 
The main aim of this tool is to help with :

- **Monitor Failing services for all tools on all nodes**
- Look at the whole cluster in one look and see what nodes have problems -- example services x number of services were supposed to be on for tool A, but some or all are not 'on' on one of the nodes.
- Ports x were supposed to be used for service a on this node but is free -- this is a problem.

- See all configuration related to a tool for all the nodes.
- Run port communication test from each node to the other nodes (only ports that the tools on this machine would use)


## Start it
To get this to work : 
`source env/bin/activate`

Run the application: 
`python ssh.py`


