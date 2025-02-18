#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int N, M;
unordered_map<int, vector<int>> graph, reverse_graph;

int dfs(int node, unordered_map<int, vector<int>>& g, vector<bool>& visited) {
    visited[node] = true;
    int count = 0;

    for (int next : g[node]) {
        if (!visited[next]) {
            count += dfs(next, g, visited) + 1;
        }
    }
    return count;
}

int main() {
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);      
        reverse_graph[b].push_back(a); 
    }

    int result = 0;
    for (int i = 1; i <= N; i++) {
        vector<bool> visited1(N + 1, false);
        int smaller_count = dfs(i, graph, visited1); 

        vector<bool> visited2(N + 1, false);
        int taller_count = dfs(i, reverse_graph, visited2);

        if (smaller_count + taller_count == N - 1) result++;
    }

    cout << result << "\n";
    return 0;
}