#!/usr/bin/python

import sys

in_triangles = open(sys.argv[1])
in_edges = open(sys.argv[2])
out_graph = open(sys.argv[3], 'w')
out_mixed = open(sys.argv[4], 'w')
n = int(sys.argv[5])

edges = [[] for _ in range(n)]

for line in in_triangles:
    t = list(map(int, line.split()))
    t.sort()
    edges[t[0]].append(t[1])
    edges[t[0]].append(t[2])
    edges[t[1]].append(t[2])
in_triangles.close()

for line in in_edges:
    t = list(map(int, line.split()))
    t.sort()
    edges[t[0]].append(t[1])
in_edges.close()

for u in range(n):
    edges[u].sort()
    weight = 0
    for i in range(len(edges[u])):
        weight += 1
        if i == len(edges[u]) - 1 or edges[u][i + 1] != edges[u][i]:
            if weight > 1:
                out_graph.write(' '.join(map(str, [u, edges[u][i], weight - 1])) + '\n')
            out_mixed.write(' '.join(map(str, [u, edges[u][i], weight])) + '\n')
            weight = 0
out_graph.close()
out_mixed.close()
