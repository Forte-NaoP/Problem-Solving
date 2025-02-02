#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <bitset>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int32_t T, n, m;
    cin >> T;

    for (int32_t t = 1; t <= T; ++t) {
        cin >> n >> m;
        int32_t mask = (1 << n) - 1;
        cout << "#" << t << " " << ((mask & m) == mask ? "ON" : "OFF") << "\n";
    }
}
