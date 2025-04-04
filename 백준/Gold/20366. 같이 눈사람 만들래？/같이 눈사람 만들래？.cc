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

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, x;
    vector<int> snow;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        snow.push_back(x);
    }

    int ans = INT32_MAX;
    sort(snow.begin(), snow.end());
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int sum = snow[i] + snow[j];
            int st = i + 1, ed = n - 1;
            while (st < ed) {
                if (st == i || st == j) {
                    st += 1;
                    continue;
                }

                if (ed == i || ed == j) {
                    ed -= 1;
                    continue;
                }

                int target = snow[st] + snow[ed];
                ans = min(ans, abs(target - sum));

                if (target > sum) {
                    ed -= 1;
                } else if (target < sum) {
                    st += 1;
                } else {
                    break;
                }
            }
        }
    }
    cout << ans << '\n';
}
