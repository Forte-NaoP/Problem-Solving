#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <array>
#include <vector>
#include <cmath>

using namespace std;

int64_t candy[100];

int main() {
	int T;
    scanf("%d", &T);
    int n;
    int64_t m, ans;
    for (int i=1; i<=T; ++i) {
        int64_t max_candy = 0;
        ans = 0;
        scanf("%d%ld", &n, &m);
        for (int j=0; j<n; ++j) {
            scanf("%ld", &candy[j]);
            max_candy = max(max_candy, candy[j]);
        }

        int64_t ideal_num = max_candy;
        int64_t lo = 1, hi = ideal_num;
        int64_t mid;

        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            int64_t num_per_bag = 0;

            for (int j=0; j<n; ++j) num_per_bag += candy[j] / mid;

            if (num_per_bag < m) hi = mid - 1;
            else {
                ans = mid;
                lo = mid + 1;
            }
        }

        printf("#%d %ld\n", i, ans);
    }
}