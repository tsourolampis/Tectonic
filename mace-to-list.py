#!/usr/bin/python

import sys

graph = open(sys.argv[1])
out_graph = open(sys.argv[2], 'w')

u = 0
for line in graph:
    for v in map(int, line.split()):
        out_graph.write(str(u) + ' ' + str(v) + '\n')
    u += 1
graph.close()
out_graph.close()

