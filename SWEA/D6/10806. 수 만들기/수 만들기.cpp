#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <cstdint>
#include <queue>

using namespace std;

int main() {

    int T;
    scanf("%d", &T);
    int n, k;
    int d[10];
    priority_queue<pair<int, int>> pq; 
    for (int i=1; i<=T; ++i) {
        
        scanf("%d", &n);
        for (int j=0; j<n; ++j) scanf("%d", d+j);
        scanf("%d", &k);

        pq.push(make_pair(0, k));

        while (pq.top().second != 0) {
            pair<int, int> cur = pq.top();
            pq.pop();
            for (int l=0; l<n; ++l) {
                pq.push(make_pair(-(-cur.first + cur.second % d[l]), cur.second / d[l]));
            }
            pq.push(make_pair(-(-cur.first + cur.second), 0));
        }

        printf("#%d %d\n", i, -pq.top().first);

        pq = priority_queue<pair<int, int>>();
    }
}