#!/usr/bin/env python
import requests
import sys

def count_backends(hostname, iterations):
    nodes = {}
    for i in range(0, int(iterations)):
        r = requests.get('http://' + hostname)
        if not r.content in nodes:
            nodes[r.content] = 0
        nodes[r.content] += 1
    for node in sorted(nodes.keys()):
        print node, nodes[node]


if __name__ == '__main__':
    count_backends(sys.argv[1], sys.argv[2])
