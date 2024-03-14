#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <queue>
#include <cmath>

using namespace std;

struct p {
    int x, y, d;
};

int dist(const p& a, const p& b) {
    return abs(a.x - b.x) + abs(a.y - b.y);
}

bool operator<(const p& a, const p& b) {
    if (a.d != b.d) return a.d < b.d;
    return a.x != b.x ? a.x < b.x : a.y < b.y;
}

int n;
int sea[20][20];
int visit[20][20];

vector<p> dv = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
p q[400];

p cur;
p cand;
int big = 2, ate;
constexpr int never_reach = 999;

void bfs(int lv) {
    int s = 0, e = 0;

    cur.d = 0;
    q[e++] = cur;
    visit[cur.x][cur.y]++;

    while (s < e) {
        p now = q[s++];
        if (now.d >= cand.d) break;
        for (auto d : dv) {
            p nxt = {now.x + d.x, now.y + d.y, now.d + 1};
            if (nxt.x < 0 || nxt.x >= n || nxt.y < 0 || nxt.y >= n || sea[nxt.x][nxt.y] > big) continue;
            if (visit[nxt.x][nxt.y] != lv) {
                visit[nxt.x][nxt.y] = lv;
                q[e++] = nxt;
                if (sea[nxt.x][nxt.y] != 0 && sea[nxt.x][nxt.y] < big && nxt < cand) cand = nxt;
            }
        }
    }
}

int main () {
    scanf("%d", &n);

    int x;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%d", &x);
            if (x == 9) {
                cur = {i, j};
                sea[i][j] = 0;
            } else {
                sea[i][j] = x;
            }
        }
    }
    
    int ans = 0;
    int lv = 1;
    while (true) {
        cand = {99, 99, never_reach};
        bfs(lv++);
        if (cand.d == never_reach) break;
        sea[cand.x][cand.y] = 0;
        ate++;
        if (ate == big) {
            big++;
            ate = 0;
        }
        ans += cand.d;
        cur = cand;
    }

    printf("%d\n", ans);
}