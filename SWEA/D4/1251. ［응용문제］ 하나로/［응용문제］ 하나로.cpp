#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstdint>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAX_H 16

struct city {
    int x, y, idx;
    city() {}
    city(int x, int y, int idx) : x(x), y(y), idx(idx) {}
};

struct road {
    city a, b;
    double cost;

    road(city a, city b, double rate) {
        this->a = a;
        this->b = b;
        cost = rate * (double)(pow(abs(a.x-b.x), 2) + pow(abs(a.y-b.y), 2));
    }
};

vector<city> vertex;
vector<road> edge;

int parent[1001];
int u_rank[1001];

int find(city& x) {
    if (x.idx == parent[x.idx]) return x.idx;
    return parent[x.idx] = find(vertex[parent[x.idx]]);
}

void joint(city& x, city& y) {
    x = vertex[find(x)];
    y = vertex[find(y)];

    if (x.idx == y.idx) return;
    if (u_rank[x.idx] >= u_rank[y.idx]) swap(x, y);
    parent[x.idx] = y.idx;
    if (u_rank[x.idx] == u_rank[y.idx]) u_rank[y.idx] = u_rank[x.idx] + 1; 
}

void init(int n) {
    vertex.clear();
    vertex.push_back(city());
    edge.clear();
    for (int j=1; j<=n; ++j) {
        parent[j] = j;
        u_rank[j] = 0;
    }
}

bool cmp(road& a, road& b) {
    return a.cost < b.cost;
}

int main() {
    int T;
    scanf("%d", &T);
    vertex.reserve(1001);
    edge.reserve(1000001);
    
    int n, m;
    int a, b;
    double rate;
    double total_cost;

    for (int i=1; i<=T; ++i) {
        scanf("%d", &n);
        init(n);
        total_cost = 0;
        for (int j=1; j<=n; ++j) {
            scanf("%d", &a);
            vertex.push_back(city{a, 0, j});
        }
        for (int j=1; j<=n; ++j) {
            scanf("%d", &b);
            vertex[j].y = b;
        }
        scanf("%lf", &rate);

        for (int j=1; j<=n; ++j) {
            for (int k=j; k<=n; ++k) {
                edge.push_back(road(vertex[j], vertex[k], rate));
            }
        }

        sort(edge.begin(), edge.end(), cmp);

        int cnt = 0;
        for (int j=0; j<n, cnt<n-1; ++j) {
            if (find(edge[j].a) != find(edge[j].b)) {
                cnt += 1;
                joint(edge[j].a, edge[j].b);
                total_cost += edge[j].cost;
            }
        }

        printf("#%d %.0lf\n", i, total_cost);
    }
}

