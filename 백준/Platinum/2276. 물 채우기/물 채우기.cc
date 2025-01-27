#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>

using namespace std;

struct Node {
    int x, y, h;

    bool operator<(const Node& other) const {
        return h > other.h;
    }
};

priority_queue<Node> pq;

int r, c;
int bowl[300][300];
int visit[300][300];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> c >> r;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> bowl[i][j];
            if (i == 0 || i == r - 1 || j == 0 || j == c - 1) {
                pq.push({i, j, bowl[i][j]});
                visit[i][j] = true;
            }
        }
    }

    int64_t filled = 0;
    while (!pq.empty()) {
        Node cur = pq.top();
        pq.pop();

        for (int i = 0; i < 4; ++i) {
            int nx = cur.x + dx[i], ny = cur.y + dy[i];

            if (nx < 0 || nx == r || ny < 0 || ny == c) continue;
            if (visit[nx][ny]) continue;

            visit[nx][ny] = true;

            if (bowl[nx][ny] > cur.h) {
                pq.push({nx, ny, bowl[nx][ny]});
            } else {
                filled += cur.h - bowl[nx][ny];
                pq.push({nx, ny, cur.h});
            }
        }
    }

    cout << filled << "\n";
}