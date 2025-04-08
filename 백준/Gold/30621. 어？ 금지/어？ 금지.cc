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

using namespace std;

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    int64_t x;
    cin >> n;
    vector<int64_t> t(n, 0), b(n, 0), dp(n, 0);

    for (int64_t& v: t) cin >> v;
    for (int64_t& v: b) cin >> v;

    cin >> dp[0];
    for (int i = 1; i < n; ++i) {
        cin >> x;
        int prev = lower_bound(t.begin(), t.begin() + i, t[i] - b[i]) - t.begin();

        dp[i] = max(dp[i - 1], x);
        if (prev > 0) dp[i] = max(dp[i], dp[prev - 1] + x);
    }

    cout << dp[n - 1] << '\n';
}
