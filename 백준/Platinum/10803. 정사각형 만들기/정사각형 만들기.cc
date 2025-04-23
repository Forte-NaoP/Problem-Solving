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
#include <stack>

using namespace std;

int paper[10001][101];
int n, m;

int recursive(int x, int y) {
    if (x % y == 0) return x / y;
    
    int& ret = paper[x][y];
    if (ret != 0) return ret;

    ret = x * y;
    if (x >= y * 3) {
        ret = min(ret, recursive(x - y, y) + 1);
    } else {
        for (int i = 1; i <= x / 2; ++i) {
            ret = min(ret, recursive(x - i, y) + recursive(i, y));
        }
    
        for (int i = 1; i <= y / 2; ++i) {
            ret = min(ret, recursive(x, y - i) + recursive(x, i));
        }
    }
    
    return ret;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    for (int i = 1; i <= n; ++i) paper[i][1] = i;
    for (int i = 1; i <= m; ++i) paper[1][i] = i;
    for (int i = 1; i < 101; ++i) paper[i][i] = 1;

    cout << recursive(n, m) << '\n';
}