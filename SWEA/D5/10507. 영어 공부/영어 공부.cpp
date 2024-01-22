#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <array>
#include <vector>
#include <cmath>

using namespace std;

int study[200001];
int play[200001];
int n, p;

int main() {
	int T;
    scanf("%d", &T);

    for (int i=1; i<=T; ++i) {
        int ans = 0, can_rank;
        scanf("%d%d", &n, &p);
        scanf("%d", &study[0]);
        play[0] = 0;
        for (int j=1; j<n; ++j) {
            scanf("%d", &study[j]);
            play[j] = study[j] - study[j-1] + play[j-1] - 1;
        }

        for (int j=0; j<n; ++j) {
            int lo = j, hi = n-1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                int hp = play[mid] - play[j];
                int mp = max(p - hp, 0);

                if (hp > p) hi = mid - 1;
                else {
                    lo = mid + 1;
                    can_rank = study[mid] - study[j] + 1 + mp;
                }
            }
            ans = max(ans, can_rank);
        }

        printf("#%d %d\n", i, ans);
    }
}