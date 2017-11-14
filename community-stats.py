#!/usr/bin/python

import sys

graph = open(sys.argv[1])
communities = open(sys.argv[2])
out = open(sys.argv[3], 'w')

n = int(communities.readline())
m = 0

t = [[] for i in range(n)]

com_size = []

for line in communities:
    l = map(int, line.split())
    for i in l:
        t[i].append(m)
    com_size.append(len(l))
    m += 1

communities.close()

sz = len(graph.readline().split())
graph.seek(0)

cnt = [0] * m
got = [[0] * sz for i in range(m)]

z = 0
for line in graph:
    l = map(int, line.split())
    for i in l:
        for j in t[i]:
            cnt[j] += 1
    for i in l:
        for j in t[i]:
            if cnt[j] != 0:
                got[j][cnt[j] - 1] += 1
                cnt[j] = 0
graph.close()

for i in range(m):
    out.write(' '.join(map(str, [com_size[i]] + got[i])) + '\n')
out.close()
