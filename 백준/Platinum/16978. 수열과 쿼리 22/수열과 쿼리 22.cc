#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <vector>

using namespace std;

int64_t tree[400'000];
int64_t lazy[400'000];

void propagate(int s, int e, int node) {
    if (lazy[node] != 0) {
        tree[node] += (e - s + 1) * lazy[node];
        if (s != e) {
            lazy[node << 1] += lazy[node];
            lazy[node << 1 | 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update(int val, int l, int r, int s, int e, int node) {
    // propagate(s, e, node);
    if (r < s || e < l) return;
    if (l <= s && e <= r) {
        tree[node] += (e - s + 1) * val;
        if (s != e) {
            lazy[node << 1] += val;
            lazy[node << 1 | 1] += val;
        }
        return;
    }
    int mid = (s + e) / 2;
    update(val, l, r, s, mid, node << 1);
    update(val, l, r, mid + 1, e, node << 1 | 1);
    tree[node] = tree[node << 1] + tree[node << 1 | 1];
}

int64_t query(int l, int r, int s, int e, int node) {
    // propagate(s, e, node);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree[node];
    int mid = (s + e) / 2;
    return query(l, r, s, mid, node << 1) + query(l, r, mid + 1, e, node << 1 | 1);
}

struct Param {
    int l, r, v;
    int t;
    int idx;

    Param(int l, int r, int v, int t, int idx): l(l), r(r), v(v), t(t), idx(idx) {}

    bool operator<(const Param& other) {
        if (v == other.v) return t < other.t;
        return v < other.v;
    }
};

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int n, a;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a;
        update(a, i, i, 0, n - 1, 1);
    }

    int m, q, x, y, z;
    int q1_idx = 0;
    vector<Param> q_v;
    cin >> m;
    for (int i = 0; i < m; ++i) {
        cin >> q;
        if (q == 1) {
            cin >> x >> y;
            q_v.push_back(Param(x - 1, y, ++q1_idx, 0, i));
        } else {
            cin >> z >> x >> y;
            q_v.push_back(Param(x - 1, y - 1, z, 1, i));
        }
    }
    sort(q_v.begin(), q_v.end());
    // for (auto& qq : q_v) {
    //     cout << qq.t << " " << qq.v << " " << qq.l << " " << qq.r << "\n";
    // }
    vector<pair<int, int64_t>> result;
    for (auto& q_p : q_v) {
        if (q_p.t == 1) {
            result.push_back({q_p.idx, query(q_p.l, q_p.r, 0, n - 1, 1)});
        } else {
            int64_t val = query(q_p.l, q_p.l, 0, n - 1, 1);
            update(q_p.r - val, q_p.l, q_p.l, 0, n - 1, 1);
        }
    }
    sort(result.begin(), result.end());
    for (auto& res : result) {
        cout << res.second << "\n";
    }
}