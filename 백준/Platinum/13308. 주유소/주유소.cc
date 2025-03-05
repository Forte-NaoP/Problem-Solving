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
    int to;
    int64_t dist;
};

struct Node{
    int city;
    int minCharge;
    int64_t cost;
};
 
struct NodeCmp{
    bool operator()(Node &a, Node &b){
        return a.cost > b.cost;
    }
};
 
int N, M;
int charge[2501];
int64_t cost[2501][2501];
vector<Edge> graph[2501];
 
void dijkstra(){
    priority_queue<Node, vector<Node>, NodeCmp> pq;
    pq.push({1, charge[1], 0});
    cost[1][charge[1]] = 0;
    
    while(!pq.empty()){
        int cur = pq.top().city;
        int curCharge = pq.top().minCharge;
        int64_t curCost = pq.top().cost;

        pq.pop();

        if (cost[cur][curCharge] < curCost) continue;
        
        if(cur == N){
            cout << curCost << "\n";
            return;
        }
        
        for (Edge& e: graph[cur]) {
            int64_t nxtCost = curCost + e.dist * curCharge;
            int nxtCharge = min(curCharge, charge[e.to]);

            if (cost[e.to][nxtCharge] > nxtCost) {
                pq.push({e.to, nxtCharge, nxtCost});
                cost[e.to][nxtCharge] = nxtCost;
            }
            
        }
    }
}
 

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> M;
    for(int i = 1; i <= N; i++){
        cin >> charge[i];
    }

    int u, v, c;
    for(int i = 0; i < M; i++){
        cin >> u >> v >> c;
        graph[u].push_back({v, c});
        graph[v].push_back({u, c});
    }

    fill(cost[1], cost[N + 1], INT64_MAX);
    dijkstra();
}