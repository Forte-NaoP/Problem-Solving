#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

const int32_t MAX_H = 17;

int32_t N;
vector<int32_t> graph[100'001];
int32_t parent[100'001][MAX_H];
int32_t depth[100'001];
vector<int32_t> order;

void init_tree(int root) {
    deque<int> q;
    depth[root] = 1;
    parent[root][0] = 0;
    q.push_back(root);

    while (!q.empty()) {
        int node = q.front();
        q.pop_front();
        order.push_back(node);

        for (int ch: graph[node]) {
            if (ch == parent[node][0]) continue;
            depth[ch] = depth[node] + 1;
            parent[ch][0] = node;
            q.push_back(ch);
        }
    }
}

void search_parent() {
    for (int32_t j = 1; j < MAX_H; ++j) {
        for (int32_t i = 1; i <= N; ++i) {
            parent[i][j] = parent[parent[i][j - 1]][j - 1];
        }
    }
}

int32_t find_lca(int32_t a, int32_t b) {
    if(depth[a] < depth[b]) swap(a, b);

    int32_t d_a = depth[a], d_b = depth[b];

    int diff = depth[a] - depth[b];

    for (int i=0; i<MAX_H; ++i) {
        if (diff & (1 << i)) a = parent[a][i];
    }

    if (a != b) {
        for (int i=MAX_H-1; i>=0; --i) {
            if (parent[a][i] != parent[b][i]) {
                a = parent[a][i];
                b = parent[b][i];
            }
        }
        a = parent[a][0];
    }
    return d_b + d_a - depth[a] * 2;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int32_t T, p;
    cin >> T;

    for (int32_t i = 1; i <= T; ++i) {
        cin >> N;
        for (int32_t j = 0; j <= N; ++j) {
            graph[j].clear();
        }
        memset(depth, 0, sizeof(int32_t) * 100'001);
        memset(parent, 0, sizeof(int32_t) * 100'001 * MAX_H);
        order.clear();
        for (int32_t j = 2; j <= N; ++j) {
            cin >> p;
            graph[p].push_back(j);
            graph[j].push_back(p);
        }

        init_tree(1);
        search_parent();
        int64_t ans = 0;
        for (int i = 0; i < N - 1; ++i) {
            ans += find_lca(order[i], order[i + 1]);
        }
        cout << "#" << i << " " << ans << "\n";
    }
}