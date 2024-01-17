#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <array>
#include <vector>
#include <cmath>

using namespace std;

#define MAX_H 16

struct Node {
    int depth;
    int parent[MAX_H];
    int sub_cnt;
    vector<int> child;

    Node() : depth(0), parent(), sub_cnt(0) {}
};

Node tree[10001];

int init_tree(int node, int parent, int depth) {
    tree[node].depth = depth;
    tree[node].parent[0] = parent;
    tree[node].sub_cnt = 0;

    for (int ch : tree[node].child) {
        tree[node].sub_cnt += init_tree(ch, node, depth + 1) + 1;
    }

    return tree[node].sub_cnt;
}

void log_parent(int n) {
    for (int j = 1; j < MAX_H; ++j) {
        for (int i = 1; i <= n; ++i) {
            tree[i].parent[j] = tree[tree[i].parent[j-1]].parent[j-1];
        }
    }
}

int find_lca(int a, int b) {
    if (tree[a].depth < tree[b].depth) swap(a, b);

    int diff = tree[a].depth - tree[b].depth;

    for (int i=0; i<MAX_H; ++i) {
        if (diff & (1 << i)) a = tree[a].parent[i];
    }

    if (a != b) {
        for (int i=MAX_H-1; i>=0; --i) {
            if (tree[a].parent[i] != tree[b].parent[i]) {
                a = tree[a].parent[i];
                b = tree[b].parent[i];
            }
        }
        a = tree[a].parent[0];
    }
    return a;
}

int main() {
    int T;
    scanf("%d", &T);
    int v, e, a, b;
    int p, d, bn = 0;
    for (int i=1; i<=T; ++i) {
        for (int j=0; j<=bn; ++j) tree[j].child.clear();
        scanf("%d%d%d%d", &v, &e, &a, &b);
        for (int j=0; j<e; ++j) {
            scanf("%d%d", &p, &d);
            tree[p].child.push_back(d);
        }
        
        init_tree(1, 0, 0);
        log_parent(v);
        int lca = find_lca(a, b);
        printf("#%d %d %d\n", i, lca, tree[lca].sub_cnt + 1);
        bn = v;
    }
}