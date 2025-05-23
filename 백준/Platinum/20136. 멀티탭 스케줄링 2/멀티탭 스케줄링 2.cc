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

deque<int> dq[500001];

struct node {
    int appear, x;
};

struct pq_cmp {
    bool operator()(const node& a, const node& b) {
        return a.appear < b.appear;
    }
};

priority_queue<node, vector<node>, pq_cmp> pq;
bool plugged[500001];

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> seq;
    int x;
    int ans = 0;
    for (int i = 0; i < k; ++i) {
        cin >> x;
        dq[x].push_back(i);
        seq.push_back(x);
    }

    for (int j: seq) {
        dq[j].push_back(1000000);
    }

    int used = 0;
    for (int i = 0; i < k; ++i) {
        while (!pq.empty() && pq.top().appear != dq[pq.top().x].front()) pq.pop();
        x = seq[i];
        auto& curDeque = dq[x];

        if (plugged[x]) {
            curDeque.pop_front();
            pq.push({curDeque.front(), x});
            continue;
        }

        if (used < n) {
            curDeque.pop_front();
            pq.push({curDeque.front(), x});
            plugged[x] = true;
            used += 1;
        } else {
            ans += 1;
            node rm = pq.top();
            pq.pop();
            plugged[rm.x] = false;

            curDeque.pop_front();
            pq.push({curDeque.front(), x});
            plugged[x] = true;
        }
    }

    cout << ans;
}
