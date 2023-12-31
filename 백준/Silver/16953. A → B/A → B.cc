#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
#include <iostream>
#include <utility>
#include <cstdint>

using namespace std;

int64_t bfs(int64_t a, int64_t b) {
    queue<pair<int64_t, int64_t>> q;
    q.push(make_pair(a, 1));
    while (!q.empty()) {
        pair<int64_t, int64_t> p = q.front();
        q.pop();
        if(p.first == b) {
            return p.second;
        }
        
        if (p.first*2 <= b) {
            q.push(make_pair(p.first*2, p.second+1));
        }
        if (p.first*10+1 <= b) {
            q.push(make_pair(p.first*10+1, p.second+1));
        }
    }
    return -1;
}

int main() {
    int64_t a, b;
    
    map<int64_t, int64_t> s;
    scanf("%ld%ld", &a, &b);
    printf("%ld\n", bfs(a, b));
    
    return 0;
}