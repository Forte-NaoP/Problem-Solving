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

using namespace std;

int64_t dp[111];


int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 1; i <= N; ++i) {
        dp[i] = dp[i - 1] + 1;
        for (int j = 3; j < i; ++j) {
            dp[i] = max(dp[i], dp[i - j] * (j - 1));
        }
    }

    cout << dp[N];

}

