#!/usr/bin/python

import sys

lines = open(sys.argv[1])

sizes = dict()

for line in lines:
    n = len(line.split())
    if n not in sizes:
        sizes[n] = 0
    sizes[n] += 1

t = []
for x in sizes.iteritems():
    t.append(x)

t.sort()

for x, y in t:
    print x, y

lines.close()
