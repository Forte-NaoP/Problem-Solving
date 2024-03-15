#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstdint>

using namespace std;

struct node {
    int left;
    int right;
};

node tree[200001];
int64_t ans;

void dfs(int nid, int64_t k) {
    if (tree[nid].left == -1 && tree[nid].right == -1) {
        ans = nid;
        return;
    }

    if (tree[nid].left == -1) {
        dfs(tree[nid].right, k);
    } else if (tree[nid].right == -1) {
        dfs(tree[nid].left, k);
    } else {
        if (k % 2 == 0) {
            dfs(tree[nid].right, k / 2);
        } else {
            dfs(tree[nid].left, k / 2 + 1);
        }
    }
}

int main () {
    int n, l, r;
    int64_t k;
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i) {
        scanf("%d%d", &l, &r);
        tree[i] = {l, r};
    }

    scanf("%ld", &k);
    dfs(1, k);
    printf("%ld\n", ans);
}