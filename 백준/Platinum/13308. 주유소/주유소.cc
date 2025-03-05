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

using namespace std;

struct Edge {
    int from, to, dist;
};

int cityCharge[2500];
vector<Edge> graph[2500];
int n, m;

struct Node {
    int charge, now, cost;
};

struct NodeCmp {
    bool operator()(const Node& a, const Node& b) {
        return a.cost > b.cost;
    }
};

int minCharge[2500];
int minCost[2500];
priority_queue<Node, vector<Node>, NodeCmp> pq;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> cityCharge[i];
    }

    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        u -= 1; v -= 1;
        graph[u].push_back({u, v, c});
        graph[v].push_back({v, u, c});
    }

    fill(minCost, minCost + 2500, INT32_MAX);
    memcpy(minCharge, cityCharge, sizeof(cityCharge));

    minCost[0] = 0;
    pq.push({minCharge[0], 0, 0});

    while (!pq.empty()) {
        Node cur = pq.top();
        pq.pop();

        if (cur.now == n - 1) {
            pq = {};
            cout << cur.cost;
            break;
        }

        if (minCharge[cur.now] <= cur.charge && minCost[cur.now] < cur.cost) continue;
        minCharge[cur.now] = min(minCharge[cur.now], cur.charge);

        for (Edge& e: graph[cur.now]) {
            int nxtCost = cur.cost + cur.charge * e.dist;
            if (minCharge[e.to] <= cur.charge && minCost[e.to] < nxtCost) continue;
            if (minCost[e.to] > nxtCost) minCost[e.to] = nxtCost;
            pq.push({min(minCharge[e.to], cur.charge), e.to, nxtCost});
        }
    }
}