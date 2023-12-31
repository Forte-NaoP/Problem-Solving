#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
#include <iostream>
#include <set>
#include <cstdint>

using namespace std;

int people[51];
int party[51][51];

int find(int x) {
    if (x == people[x]) return x;
    return people[x] = find(people[x]);
}

void union_(int x, int y) {
    x = find(x);
    y = find(y);
    if (x != y) {
        x > y ? people[x] = people[y] : people[y] = people[x];
    }
    return;
}

int main() {
    int n, m;
    int t, p;
    scanf("%d%d", &n, &m);
    scanf("%d", &t);

    for (int i=1; i<=n; ++i) people[i] = i;

    for (int i=0; i<t; ++i){
        scanf("%d", &p);
        union_(p, 0);
    }

    for (int i=0; i<m; ++i) {
        int c, pp;
        scanf("%d", &c);
        scanf("%d", &p);
        party[i][++party[i][0]] = p;
        for (int j=0; j<c-1; ++j) {
            scanf("%d", &pp);
            party[i][++party[i][0]] = pp;
            union_(pp, p);
        }
    }

    int ans = m;
    for (int i=0; i<m; ++i) {
        for (int j=1; j<=party[i][0]; ++j) {
            if (find(people[party[i][j]]) == 0) {
                ans -= 1;
                break;
            }
        }
    }

    printf("%d\n", ans);
}