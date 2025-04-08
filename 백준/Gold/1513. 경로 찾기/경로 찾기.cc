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

struct node {
    int x, y, last, cnt;
};

int n, m, c;
int city[51][51];
int dp[51][51][51][51];

void run() {
    dp[1][1][city[1][1]][city[1][1] > 0 ? 1 : 0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (i == 1 && j == 1) continue;
            if (city[i][j] > 0) {
                for (int k = 1; k <= c; ++k) {
                    for (int l = 0; l < city[i][j]; ++l) {
                        dp[i][j][city[i][j]][k] += dp[i - 1][j][l][k - 1];
                        dp[i][j][city[i][j]][k] += dp[i][j - 1][l][k - 1];
                        dp[i][j][city[i][j]][k] %= 1'000'007;
                    }
                }
            } else {
                for (int k = 0; k <= c; ++k) {
                    for (int l = 0; l <= c; ++l) {
                        dp[i][j][l][k] += dp[i - 1][j][l][k];
                        dp[i][j][l][k] += dp[i][j - 1][l][k];
                        dp[i][j][l][k] %= 1'000'007;
                    }
                }
            }
        }
    }

    for (int i = 0; i <= c; ++i) {
        int ans = 0;
        for (int j = 0; j <= c; ++j) {
            ans += dp[n][m][j][i];
            ans %= 1'000'007;
        }
        cout << ans << ' ';
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m >> c;
    int x, y;
    for (int i = 1; i <= c; ++i) {
        cin >> x >> y;
        city[x][y] = i;
    }

    run();
}
