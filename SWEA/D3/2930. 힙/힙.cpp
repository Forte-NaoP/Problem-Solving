#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

struct heap {
    int v[100001];
    int size;

    heap() : size(0) {}
    void init() { size = 0; }
    int& operator[] (int index) {
        if (index < 0 || index >= size) throw out_of_range("Index out of range");
        return v[index];
    }

    void push(int x) {
        if (size >= 100000) throw out_of_range("heap is full");
        v[++size] = x;

        int cur = size;
        int parent = size / 2;

        while (cur > 1 && v[cur] > v[parent]) {
            swap(v[cur], v[parent]);
            cur = parent;
            parent /= 2;
        }
    }

    int pop() {
        if (size < 1) return -1; 
        int mv = v[1];
        swap(v[size--], v[1]);
        int cur = 1, child;

        while (true) {
            child = cur * 2;
            if (child > size) break;
            if (child+1 <= size && v[child+1] > v[child]) child += 1;
            if (v[child] <= v[cur]) break;
            swap(v[cur], v[child]);
            cur = child;
        }

        return mv;
    }
};

heap h;

int main() {

    int T;
    scanf("%d", &T);
    int op, x;
    int n;
    for (int i=1; i<=T; ++i) {
        h.init();
        printf("#%d ", i);
        scanf("%d", &n);
        for(int j=0; j<n; ++j) {
            scanf("%d", &op);
            
            if (op == 1) {
                scanf("%d", &x); 
                h.push(x);
            } else {
                printf("%d ", h.pop());
            }
        }
        printf("\n");
    }
}