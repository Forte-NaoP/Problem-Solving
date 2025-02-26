#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <stdexcept>
#include <string>
#include <numeric>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <bits/extc++.h>

using namespace std;
using namespace __gnu_pbds;

using ordered_set = tree<int, null_type, greater<int>, rb_tree_tag, tree_order_statistics_node_update>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T, n, k;
    char c;
    deque<int> q;
    ordered_set s;

    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        q.clear();
        s.clear();

        cin >> n >> k;
        int size = n / 4;
        for (int i = 0; i < n; ++i) {
            cin >> c;
            if (c < 'A') q.push_back(c - '0');
            else q.push_back(c - 'A' + 10);
        }

        for (int r = 0; r < n; ++r) {
            for (int i = 0; i < n; i += size) {
                int val = 0;
                for (int j = 0; j < size; ++j) {
                    val <<= 4;
                    val += q[i + j];
                }
                s.insert(val);
            }
            q.push_front(q.back());
            q.pop_back();
        }
        cout << "#" << tc << " " << *s.find_by_order(k - 1) << "\n";
    }
}