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

priority_queue<int> lq;
priority_queue<int, vector<int>, greater<int>> rq;

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, x;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (lq.size() == rq.size()) {
            if (!rq.empty() && rq.top() < x) {
                lq.push(rq.top());
                rq.pop();
                rq.push(x);
            } else {
                lq.push(x);
            }
        } else {
            if (lq.top() > x) {
                rq.push(lq.top());
                lq.pop();
                lq.push(x);
            } else {
                rq.push(x);
            }
        }
        cout << lq.top() << "\n";
    }

}