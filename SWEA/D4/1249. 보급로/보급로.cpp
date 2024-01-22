#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <cmath>

using namespace std;

int n;
int arr[100][100];
int cost[100][100];

void recover() {
    priority_queue<pair<int, pair<int, int>>> pq;

    cost[0][0] = 0;
    pq.push(make_pair(0, make_pair(0, 0)));

    while (!pq.empty()) {
        auto cur = pq.top();
        int c = -cur.first;
        int x = cur.second.first, y = cur.second.second;
        pq.pop();
        
        if (c > cost[x][y]) continue;

        if (x > 0) {
            if (arr[x-1][y] + c < cost[x-1][y]) {
                cost[x-1][y] = arr[x-1][y] + c;
                pq.push(make_pair(-cost[x-1][y], make_pair(x-1, y)));
            }
        }   
        if (y > 0) {
            if (arr[x][y-1] + c < cost[x][y-1]) {
                cost[x][y-1] = arr[x][y-1] + c;
                pq.push(make_pair(-cost[x][y-1], make_pair(x, y-1)));
            }
        }
        if (x < n - 1) {
            if (arr[x+1][y] + c < cost[x+1][y]) {
                cost[x+1][y] = arr[x+1][y] + c;
                pq.push(make_pair(-cost[x+1][y], make_pair(x+1, y)));
            }
        }
        if (y < n - 1) {
            if (arr[x][y+1] + c < cost[x][y+1]) {
                cost[x][y+1] = arr[x][y+1] + c;
                pq.push(make_pair(-cost[x][y+1], make_pair(x, y+1)));
            }
        }
    }
}

int main() {

	int T;
    char c;
    scanf("%d", &T);

    for (int i=1; i<=T; ++i) {
        scanf("%d", &n);

        fill(&cost[0][0], &cost[99][100], INT32_MAX);

        for (int j=0; j<n; ++j) {
            for (int k=0; k<n; ++k) {
                scanf(" %c", &c);
                arr[j][k] = c - '0';
            }
        }

        recover();

        printf("#%d %d\n", i, cost[n-1][n-1]);
    }
}