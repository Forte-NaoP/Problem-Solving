#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int dist[20001];
vector<pair<int, int>> graph[20001];

int main () {
    fill(dist, dist+20001, INT32_MAX);

    int v, e;
    scanf("%d%d", &v, &e);
    
    int k;
    scanf("%d", &k);

    for (int i = 0; i < e; ++i) {
        int _u, _v, _w;
        scanf("%d%d%d", &_u, &_v, &_w);
        graph[_u].push_back({_v, _w});
    }

    priority_queue<pair<int, int>> pq;
    dist[k] = 0;
    pq.push({0, k});

    while (!pq.empty()) {
        auto [cost, cur] = pq.top();
        pq.pop();
        cost = -cost;

        for (auto nxt : graph[cur]) {
            if (dist[nxt.first] <= cost + nxt.second) continue;
            dist[nxt.first] = cost + nxt.second;
            pq.push({-(cost + nxt.second), nxt.first});
        }
    }

    for (int i = 1; i <= v; ++i) {
        dist[i] == INT32_MAX ? printf("INF\n") : printf("%d\n", dist[i]);
    }
}