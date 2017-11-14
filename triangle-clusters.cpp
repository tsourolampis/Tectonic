#include <sys/time.h>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

#define FI first
#define SE second
#define X first
#define Y second
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef vector<int> VI;
typedef long double LD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

double getTime() {
	timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;
}

ifstream in_graph;
ifstream communities;
int n, k;

struct Edge {
    int u, v;
};

typedef pair<int, double> PID;

vector<Edge> edges;

vector< vector<PID> > e;
vector< vector<PID> > parent;

vector<int> p;

int gp(int x) {
    if (p[x] != x) {
        p[x] = gp(p[x]);
    }
    return p[x];
}

vector<int> height;

void dfs(int x, PID my_parent) {
    if (my_parent.ST != -1) {
        parent[x].PB(my_parent);
        /*int i = 0;
        while (i < parent[parent[x][i].ST].size()) {
            int w = min(parent[x][i].ND, parent[parent[x][i].ST][i].ND);
            parent[x].PB(MP(parent[parent[x][i].ST][i].ST, w));
            i += 1;
        }*/
    }
    for (const PID& p: e[x]) {
        if (p.first != my_parent.first) {
            height[p.first] = height[x] + 1;
            dfs(p.first, MP(x, p.second));
        }
    }
}

double min_encountered;

int lca(int x, int y) {
    while (height[x] > height[y]) {
        min_encountered = min(min_encountered, parent[x][0].ND);
        x = parent[x][0].ST;
    }
    while (height[y] > height[x]) {
        min_encountered = min(min_encountered, parent[y][0].ND);
        y = parent[y][0].ST;
    }
    while (height[x] > 1 && x != y) {
        min_encountered = min(min_encountered, parent[x][0].ND);
        x = parent[x][0].ST;
        min_encountered = min(min_encountered, parent[y][0].ND);
        y = parent[y][0].ST;
    }
    if (height[x] == 1 && x != y) {
        min_encountered = 0;
    }
    return x;
}

vector<int> cur;

vector< vector<int> > sons;

void get_cluster(int x, vector<int>& result) {
    result.PB(x);
    FORE (it, sons[x]) {
        get_cluster(*it, result);
    }
}

void print_cluster(int x) {
    vector<int> cluster;
    get_cluster(gp(x), cluster);
    FORE (it, cluster) {
        if (it != cluster.begin()) {
            cout << " ";
        }
        cout << *it;
    }
    cout << endl;
}

int main(int argc, char **argv) {
    in_graph.open(argv[1]);
    n = atoi(argv[2]);
    k = atoi(argv[3]);
    while (!in_graph.eof()) {
        Edge e;
        int weight;
        in_graph >> e.u >> e.v >> weight;
        if (weight < k) {
            continue;
        }
        if (in_graph.eof()) {
            break;
        }
        edges.PB(e);
    }
    in_graph.close();
    parent.resize(n);
    e.resize(n);
    p.resize(n);
    sons.resize(n);
    REP (i, n) {
        p[i] = i;
    }
    for (const Edge& ed : edges) {
        if (gp(ed.u) != gp(ed.v)) {
            sons[gp(ed.v)].PB(gp(ed.u));
            p[gp(ed.u)] = gp(ed.v);
        }
    }
    REP (i, n) {
        if (p[i] == i) {
            print_cluster(i);
        }
    }
}
