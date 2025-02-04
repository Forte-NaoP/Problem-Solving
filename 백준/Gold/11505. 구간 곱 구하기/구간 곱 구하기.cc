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
#include <regex>
#include <set>

using namespace std;

const int64_t MOD = 1'000'000'007;

int32_t bit_ceil(int32_t val) {
    int32_t ret = 1;
    while (ret < val) ret <<= 1;
    return ret;
}

int32_t n, base;
int64_t tree[4'000'000];

void init(int32_t idx, int64_t val) {
    idx += base;
    tree[idx] = val;
    idx >>= 1;
    while (idx > 0) {
        tree[idx] = ((tree[idx * 2] % MOD) * (tree[idx * 2 + 1] % MOD)) % MOD;
        idx >>= 1;
    }
}

int64_t query(int32_t l, int32_t r, int32_t s, int32_t e, int32_t idx) {
    if (e < l || r < s) return 1;
    if (l <= s && e <= r) return tree[idx];

    int32_t mid = (s + e) / 2;
    return (query(l, r, s, mid, idx * 2) * query(l, r, mid + 1, e, idx * 2 + 1)) % MOD;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int32_t m, k;
    cin >> n >> m >> k;
    int32_t x;
    base = bit_ceil(n);
    for (int32_t i = 0; i < base * 2; ++i) tree[i] = 1;
    for (int32_t i = 0; i < n; ++i) {
        cin >> x;
        init(i, x);
    }

    int32_t t = m + k;
    int32_t a, b, c;
    for (int32_t i = 0; i < t; ++i) {
        cin >> a >> b >> c;
        if (a == 1) init(b - 1, c);
        else cout << query(b - 1, c - 1, 0, base - 1, 1) << "\n";
    }

}
