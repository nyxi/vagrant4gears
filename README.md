## Vagrant cluster
A simple example of a Vagrant cluster containing a load balancer node and an arbitrary number of application server nodes. The cluster uses the private network functionality of Vagrant with the load balancer on IP 192.168.77.201 and the application servers on 201+N.

### Load balancer
Debian + nginx in round robin setup listening on port 81, forwarding requests to the application servers.

### Application servers
Debian + nginx with static page containing only the node's name.

## RR test
```
# pip install -r requirements.txt
$ python countbackends.py 192.168.77.201:81 100
node1 33
node2 34
node3 33
```
