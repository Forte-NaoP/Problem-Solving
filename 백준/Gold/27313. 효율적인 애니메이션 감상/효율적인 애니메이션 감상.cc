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

int n, m, k;

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int x;
    cin >> n >> m >> k;
    vector<int> anime;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x <= m) anime.push_back(x);
    }
    sort(anime.begin(), anime.end());

    int lo = 0, hi = anime.size() - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int64_t t = 0;
        for (int i = mid; i >= 0; i -= k) {
            t += anime[i];
        }
        if (t <= m) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    cout << lo << '\n';
}

// f(x): x까지 볼 때 M시간 이하로 가능한가?

