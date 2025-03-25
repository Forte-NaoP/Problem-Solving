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

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

struct node {
    int x, y, d, m, t;
};

deque<node> dq;
bool visit[500][500][2][10];
int maze[500][500];
int n, m;

node next_node(const node& cur, int x, int y) {
    int nd = cur.d, nm = cur.m, nt = cur.t;
    nm += 1;
    if (nm == m) {
        nt += 1;
        nm = 0;
    }

    if (nt == 2) {
        nd += 1;
        nt = 0;
    }

    return {x, y, nd, nm, nt};
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int x;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> maze[i][j];
        }
    }

    node ans = {-1, -1, -1, -1, -1};

    visit[0][0][0][0] = true;
    dq.push_back({0, 0, 1, 0, 0});

    while (!dq.empty()) {
        node cur = dq.front();
        dq.pop_front();

        if (cur.x == n - 1 && cur.y == n - 1) {
            ans = cur;
            break;
        }

        for (int i = 0; i < 4; ++i) {
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            node nxt = next_node(cur, nx, ny);
            if (visit[nx][ny][nxt.t][nxt.m]) continue;
            if (maze[nx][ny] == 0) {
                visit[nx][ny][nxt.t][nxt.m] = true;
                dq.push_back(nxt);
            } else {
                if (cur.t == 1) {
                    while (
                        !(nx < 0 || nx >= n || ny < 0 || ny >= n) &&
                        maze[nx][ny] == 1
                    ) {
                        nx += dx[i];
                        ny += dy[i];
                    }
                    if (!(nx < 0 || nx >= n || ny < 0 || ny >= n)) {
                        visit[nx][ny][nxt.t][nxt.m] = true;
                        nxt.x = nx;
                        nxt.y = ny;
                        dq.push_back(nxt);
                    }
                }
            }
        }
    }

    if (ans.d == -1) {
        cout << -1 << '\n';
    } else {
        cout << ans.d << ' ' << (ans.t == 0 ? "sun" : "moon") << '\n';
    }
}
