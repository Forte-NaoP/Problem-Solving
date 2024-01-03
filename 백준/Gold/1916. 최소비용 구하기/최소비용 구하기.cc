#include <cstdint>
#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

#define INF 2147483647

int dist[1001];
priority_queue<pair<int, int>> q;
vector<pair<int, int>> bus[1001];

int main() {
    int n, m;
    scanf("%d%d", &n, &m);

    for (register int i=0; i<=n; ++i) {
        dist[i] = INF;
    }

    int s, t, d;
    for (register int i=0; i<m; ++i) {
        scanf("%d%d%d", &s, &t, &d);
        bus[s].push_back({d, t});
    }

    scanf("%d%d", &s, &t);
    dist[s] = 0;
    q.push({0, s});

    while (!q.empty()) {
        int current_dist = -q.top().first;
        int current = q.top().second;
        q.pop();

        if (dist[current] < current_dist) continue;

        for (register int i=0; i<bus[current].size(); ++i) {
            int next_dist = bus[current][i].first + current_dist;
            int next = bus[current][i].second;

            if (dist[next] > next_dist) {
                dist[next] = next_dist;
                q.push({-next_dist, next});
            }
        }
    }

    printf("%d\n", dist[t]);
}