#!/usr/bin/python

import sys
from collections import defaultdict

threshold = int(sys.argv[1])
data = open(sys.argv[2])
out_graph = open(sys.argv[3], 'w')
out_communities = open(sys.argv[4], 'w')

t = defaultdict(list)
v = []

for line in data:
    line = line[:-1]
    line = line.split(',')
    t[line[0]].append(len(v))
    v.append(line[1:])

for l in t.values():
    out_communities.write(' '.join(map(str, l)) + '\n')

n = len(v)

deleted = []
for j in range(len(v[0])):
    for i in range(n):
        if v[i][j] == '?':
            deleted.append(j)
            break

for j in deleted[::-1]:
    for i in range(n):
        v[i] = v[i][:j] + v[i][j+1:]

for i in range(n):
    for j in range(i+1, n):
        dist = 0
        for k in range(len(v[i])):
            if v[i][k] != v[j][k]:
                dist += 1
                if dist > threshold:
                    break
        if dist <= threshold:
            out_graph.write(str(i) + ' ' + str(j) + '\n')

out_graph.close()
out_communities.close()

