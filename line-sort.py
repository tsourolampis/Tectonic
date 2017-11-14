#!/usr/bin/python

import sys

t = []

in_file = open(sys.argv[1])

for line in in_file:
    t.append(sorted(map(int, line.split())))

in_file.close()

out_file = open(sys.argv[1], 'w')

for line in t:
    out_file.write(' '.join(map(str, line)) + '\n')

out_file.close()
