# Tectonic: Scalable Motif-Aware Community Detection

This repository contains some software used in   [Scalable Motif-Aware Graph Clustering](https://arxiv.org/abs/1606.06235).  You can find the project web page [here](https://tsourakakis.com/tectonic/).


### Authors 

- [Charalampos E. Tsourakakis](https://tsourakakis.com/) 
- [Jakub Pachocki](https://scholar.harvard.edu/meret/home)
- [Michael Mitzemacher](http://www.eecs.harvard.edu/~michaelm/) 

## Usage 

Our code takes as input a graph, and the ground-truth communities, check files _com-amazon.ungraph.txt_ and _com-amazon.top5000.cmty.txt_ to see the input format. 

1. Run from a terminal _python_ relabel-graph.py com-amazon.ungraph.txt com-amazon.top5000.cmty.txt amazon.mace amazon.communities.
2. Download and compile [MACE](http://research.nii.ac.jp/~uno/code/mace.html).
3. Run _./mace_ C -l 3 -u 3 amazon.mace amazon.triangles  
4. Run _python_ mace-to-list.py amazon.mace amazon.edges 
5. For some stats, run _python_ community-stats.py amazon.edges amazon.communities amazon.edges.stats and _python_ community-stats.py amazon.triangles amazon.communities amazon.triangles.stats
6. Compile the file triangle_clusters.cpp g++ -std=c++11 -o triangle_clusters triangle-clusters.cpp
7. Run ./triangle_clusters amazon.triangles numbers_of_nodes (334858 for amazon) threshold_value > amazon_clusters.txt
8. Quick heuristic evaluation python grade-clusters.py amazon.communities amazon_clusters.txt output.txt
