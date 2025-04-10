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

int n, m, ed;
int dx[] = {-1, -1, 1, 1};
int dy[] = {-1, 1, -1, 1};

int dist[252525];
int visit[252525];

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    char c;
    cin >> n >> m;
    vector<vector<pair<int, int>>> circuit((n + 1) * (m + 1));
    fill(dist, dist + 252525, INT32_MAX);
    ed = (n + 1) * (m + 1) - 1;

    int v0, v1, v2, v3;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> c;
            v0 = i * (m + 1) + j;
            v1 = v0 + 1;
            v2 = v1 + m;
            v3 = v2 + 1;
            if (c == '\\') {
                circuit[v0].push_back({v3, 0});
                circuit[v3].push_back({v0, 0});
                circuit[v1].push_back({v2, 1});
                circuit[v2].push_back({v1, 1});
            } else {
                circuit[v0].push_back({v3, 1});
                circuit[v3].push_back({v0, 1});
                circuit[v1].push_back({v2, 0});
                circuit[v2].push_back({v1, 0});
            }
        }
    }

    // for (int i = 0; i < circuit.size(); ++i) {
    //     cout << i << ": ";
    //     for (auto& nxt: circuit[i]) {
    //         cout << "(" << nxt.first << ", " << nxt.second << "), ";
    //     }
    //     cout << '\n';
    // }

    int ans = INT32_MAX;
    deque<pair<int, int>> dq;
    visit[0] = true;
    dist[0] = 0;
    dq.push_back({0, 0});

    while (!dq.empty()) {
        auto cur = dq.front();
        dq.pop_front();

        if (cur.first == ed) {
            ans = cur.second;
            break;
        }

        for (auto& nxt: circuit[cur.first]) {
            if (!visit[nxt.first] && dist[nxt.first] > cur.second + nxt.second) {
                dist[nxt.first] = cur.second + nxt.second;
                if (nxt.second == 0) {
                    dq.push_front({nxt.first, dist[nxt.first]});
                } else {
                    dq.push_back({nxt.first, dist[nxt.first]});
                }
            }
        }
    }

    if (ans == INT32_MAX) cout << "NO SOLUTION\n";
    else cout << ans << '\n';

}


