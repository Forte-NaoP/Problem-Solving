#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>

using namespace std;

#define MAX_H 16

int parent[101];
int u_rank[101];

int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

void joint(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;
    if (u_rank[x] >= u_rank[y]) swap(x, y);
    parent[x] = y;
    if (u_rank[x] == u_rank[y]) u_rank[y] = u_rank[x] + 1; 
}

int main() {

    int T;
    scanf("%d", &T);
    int n, m;
    int a, b;
    for (int i=1; i<=T; ++i) {
        scanf("%d%d", &n, &m);
        for (int j=1; j<=n; ++j) {
            parent[j] = j;
            u_rank[j] = 0;
        }
        for (int j=0; j<m; ++j) {
            scanf("%d%d", &a, &b);
            joint(a, b);
        }

        for (int j=1; j<=n; ++j) find(j);
        set<int> s(parent+1, parent+n+1);
        printf("#%d %lu\n", i, s.size());
    }
}

