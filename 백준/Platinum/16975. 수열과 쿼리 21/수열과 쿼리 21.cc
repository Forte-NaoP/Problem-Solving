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
    propagate(s, e, node);
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
    propagate(s, e, node);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree[node];
    int mid = (s + e) / 2;
    return query(l, r, s, mid, node << 1) + query(l, r, mid + 1, e, node << 1 | 1);
}

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
    cin >> m;
    for (int i = 0; i < m; ++i) {
        cin >> q;
        if (q == 1) {
            cin >> x >> y >> z;
            update(z, x - 1, y - 1, 0, n - 1, 1);
        } else {
            cin >> x;
            cout << query(x - 1, x - 1, 0, n - 1, 1) << "\n";
        }
    }
}