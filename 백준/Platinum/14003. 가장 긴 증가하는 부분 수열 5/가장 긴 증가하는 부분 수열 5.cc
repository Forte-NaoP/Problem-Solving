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

int32_t n;
int32_t arr[1'000'000];
int32_t lis_end;
int32_t lis[1'000'000];
int32_t lis_idx[1'000'000];

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for (int32_t i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    lis[lis_end++] = arr[0];
    lis_idx[0] = lis_end;

    for (int32_t i = 1; i < n; ++i) {
        int32_t pos = lower_bound(lis, lis + lis_end, arr[i]) - lis;
        if (pos == lis_end) {
            lis[lis_end++] = arr[i];
            lis_idx[i] = lis_end;
        } else {
            lis[pos] = arr[i];
            lis_idx[i] = pos + 1;
        }
    }

    cout << lis_end << "\n";
    deque<int32_t> q;
    for (int32_t i = n - 1; i >= 0; --i) {
        if (lis_idx[i] == lis_end) {
            q.push_front(arr[i]);
            lis_end -= 1;
        }
    }
    
    for (int32_t cur: q) cout << cur << " ";
}
