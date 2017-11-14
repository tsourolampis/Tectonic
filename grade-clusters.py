#!/usr/bin/python

import sys

communities = open(sys.argv[1])
clusters = open(sys.argv[2])
out = open(sys.argv[3], 'w')

n = int(communities.readline())

cluster_no = [-1] * n
cluster_size = []


for line in clusters:
    cluster = map(int, line.split())
    for i in cluster:
        cluster_no[i] = len(cluster_size)
    cluster_size.append(len(cluster))

clusters.close()
print(cluster_no)
print(cluster_size)

inside = [0] * len(cluster_size)

total_precision = 0.0
total_recall = 0.0
exact = 0
cnt = 0

for line in communities:
    community = map(int, line.split())
    for i in community:
        if cluster_no[i] == -1:
            continue
        inside[cluster_no[i]] += 1
    hits = 0
    csize = 1
    for i in community:
        if cluster_no[i] == -1:
            continue
        if inside[cluster_no[i]] > hits:
            hits = inside[cluster_no[i]]
            csize = cluster_size[cluster_no[i]]
    for i in community:
        if cluster_no[i] == -1:
            continue
        inside[cluster_no[i]] = 0
    precision = hits / float(csize)
    recall = hits / float(len(community))
    total_precision += precision
    total_recall += recall
    cnt += 1
    if precision == 1.0 and recall == 1.0:
        exact += 1
    out.write('{0:d} {1:.5f} {2:.5f}\n'.format(len(community), precision, recall))

communities.close()
out.close()

#print 'Exact matches: ' + str(exact)
#print 'Precision: {0:.5f} Recall: {1:.5f}'.format(total_precision / float(cnt), total_recall / float(cnt))
print '{0:.5f} {1:.5f}'.format(total_precision / float(cnt), total_recall / float(cnt))


