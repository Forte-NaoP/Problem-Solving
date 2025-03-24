#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <cstdint>

using namespace std;

int64_t minTree[400001];
int64_t maxTree[400001];
int64_t arr[100001];
int32_t base, n;

void update(int32_t idx, int64_t val) {
    idx += base;
    minTree[idx] = val;
    maxTree[idx] = val;
    
    idx >>= 1;
    while (idx > 0) {
        minTree[idx] = min(minTree[idx << 1], minTree[idx << 1 | 1]);
        maxTree[idx] = max(maxTree[idx << 1], maxTree[idx << 1 | 1]);
        idx >>= 1;
    }
}

void init() {
    base = 1;
    while (base < n) base <<= 1;
    for (int i = 0; i < n; ++i) {
        update(i, arr[i]);
    }
}

int64_t query_min(int32_t l, int32_t r, int32_t s, int32_t e, int32_t node) {
    if (r < s || e < l) return INT64_MAX;
    if (l <= s && e <= r) return minTree[node];

    int32_t mid = (s + e) / 2;
    return min(query_min(l, r, s, mid, node << 1), query_min(l, r, mid + 1, e, node << 1 | 1));
}

int64_t query_max(int32_t l, int32_t r, int32_t s, int32_t e, int32_t node) {
    if (r < s || e < l) return INT64_MIN;
    if (l <= s && e <= r) return maxTree[node];

    int32_t mid = (s + e) / 2;
    return max(query_max(l, r, s, mid, node << 1), query_max(l, r, mid + 1, e, node << 1 | 1));
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    fill(minTree, minTree + 400001, INT64_MAX);
    fill(maxTree, maxTree + 400001, INT64_MIN);

    int32_t m, a, b;
    cin >> n >> m;
    for (int32_t i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    init();
    for (int i = 0; i < m; ++i) {
        cin >> a >> b;
        if (a > b) swap(a, b);
        cout << query_min(a - 1, b - 1, 0, base - 1, 1) << ' ' << query_max(a - 1, b - 1, 0, base - 1, 1) << '\n';
    }
}
