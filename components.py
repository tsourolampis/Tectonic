#!/usr/bin/python

import sys

sys.setrecursionlimit(1000000)

in_graph = open(sys.argv[1])
n = int(sys.argv[2])
out = open(sys.argv[3], 'w')

p = range(n)

def gp(x):
    global p
    if p[x] != x:
        p[x] = gp(p[x])
    return p[x]

import random
for line in in_graph:
    u, v, w = map(int, line.split())[:3]
    if w < 4:
        continue
    p[gp(u)] = gp(v)
in_graph.close()

t = [[] for i in range(n)]

for i in range(n):
    t[gp(i)].append(i)

cnt = 0
s2 = 0

for i in range(n):
    if not t[i]:
        continue
    cnt += 1
    if len(t[i]) > 1:
        s2 += 1
    out.write(' '.join(map(str, t[i])) + '\n')
out.close()

print 'Components:', cnt, ', non-singletons:', s2
