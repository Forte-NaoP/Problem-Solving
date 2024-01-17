#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

#define MAX_LEN 400000

struct heap {
    int *v;
    int cnt;
    bool is_max;

    heap() {
        v = (int *)malloc(sizeof(int)*MAX_LEN+4);
    }

    void init(bool m) { 
        cnt = 0; 
        is_max = m;
    }

    int& operator[] (int index) {
        if (index < 0 || index > cnt) throw out_of_range("Index out of range");
        return v[index];
    }

    int size() {
        return cnt;
    }

    int top() {
        return v[1];
    }

    bool empty() {
        return cnt == 0;
    }

    void push(int x) {
        if (cnt >= MAX_LEN) throw out_of_range("heap is full");
        v[++cnt] = x;

        int cur = cnt;
        int parent = cnt / 2;

        while (cur > 1 && cmp(v[cur], v[parent])) {
            swap(v[cur], v[parent]);
            cur = parent;
            parent /= 2;
        }
    }

    int pop() {
        if (cnt < 1) return -1; 
        int mv = v[1];
        swap(v[cnt--], v[1]);
        int cur = 1, child;

        while (true) {
            child = cur * 2;
            if (child > cnt) break;
            if (child+1 <= cnt && cmp(v[child+1], v[child])) child += 1;
            if (!cmp(v[child], v[cur])) break;
            swap(v[cur], v[child]);
            cur = child;
        }

        return mv;
    }

    bool cmp(int& a, int& b) {
        return is_max ? a > b : a < b;
    }
};

int main() {

    heap maxheap, minheap;
    int T;
    scanf("%d", &T);
    int n, x, y, sum, median;
    for (int i=1; i<=T; ++i) {
        maxheap.init(true);
        minheap.init(false);
        sum = 0;
        
        scanf("%d%d", &n, &median);
        maxheap.push(median);
        minheap.push(median);

        for (int j=0; j<n; ++j) {
            scanf("%d%d", &x, &y);
            
            maxheap.top() > x ? maxheap.push(x) : minheap.push(x);
            maxheap.top() > y ? maxheap.push(y) : minheap.push(y);

            if (maxheap.size() > minheap.size()) {
                maxheap.pop();
                minheap.push(maxheap.top());
            } else if (minheap.size() > maxheap.size()) {
                minheap.pop();
                maxheap.push(minheap.top());
            }
            sum = (sum + maxheap.top()) % 20171109;
        }
        printf("#%d %d\n", i, sum);
    }
}