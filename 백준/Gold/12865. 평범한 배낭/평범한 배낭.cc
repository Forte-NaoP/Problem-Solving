#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int dp[101][100001];
int w[101], v[101];

int main () {
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; ++i) {
        scanf("%d%d", w + i, v + i);
    }
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            if (j < w[i]) dp[i][j] = dp[i - 1][j];
            else dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]);
        }
    }

    printf("%d\n", dp[n][k]);
}