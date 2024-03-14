#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <queue>
#include <string>
#include <cstdint>

using namespace std;

struct h {
    int64_t l;
    int16_t r;
};

bool operator<(const h& a, const h& b) {
    return a.l != b.l ? a.l < b.l : a.r < b.r;
}

h encode(char s[16]) {
    h _h = {0, 0};
    int i;
    for (i = 0; s[i]; ++i) {
        char x = s[i] - 'a' + 1;
        if (i < 12) {
            _h.l <<= 5;
            _h.l += x;
        } else {
            _h.r <<= 5;
            _h.r += x;
        }
    }

    if (i <= 12) {
        _h.l <<= (5 * (12 - i));
    } else {
        _h.r <<= (5 * (15 - i));
    }

    return _h;
}

string decode(h _h) {
    string s;
    while (_h.r != 0) {
        if ((_h.r & 31) != 0) s += (_h.r & 31) + 'a' - 1;
        _h.r >>= 5;
    }
    while (_h.l != 0) {
        if ((_h.l & 31) != 0) s += (_h.l & 31) + 'a' - 1;
        _h.l >>= 5;
    }
    reverse(s.begin(), s.end());
    return s;
}

int n;
vector<int> toward[400001];
map<h, int> item_id;
h item[400001];
int indegree[400001];
int item_cnt = 1;

struct cmp {
    bool operator()(const int a, const int b){
        return item[a].l != item[b].l ? !(item[a].l < item[b].l) : !(item[a].r < item[b].r);
    }
};

void tsort() {
    priority_queue<int, vector<int>, cmp> pq;
    vector<h> v;
    for (int i = 1; i < item_cnt; ++i) {
        if (indegree[i] == 0) pq.push(i);
    }

    while (true) {
        vector<int> buf;

        while (!pq.empty()) {
            int top = pq.top();
            v.push_back(item[top]);
            pq.pop();
            for (auto x : toward[top]) {
                indegree[x] -= 1;
                if (indegree[x] == 0) {
                    buf.push_back(x);
                }
            }
        }

        if (buf.size() == 0) break;
        for (int x : buf) pq.push(x);
    }

    if (v.size() == 0 || v.size() != item_cnt - 1) {
        printf("-1\n");
    } else {
        for (auto x : v) {
            string s = decode(x);
            printf("%s\n", s.c_str());
        }
    }

}

int main () {
    scanf("%d", &n);
    char a[16], b[16];

    for (int i = 0; i < n; ++i) {
        scanf(" %s", a);
        scanf(" %s", b);

        h ha = encode(a);
        h hb = encode(b);

        if (item_id[ha] == 0) {
            item_id[ha] = item_cnt;
            item[item_cnt] = ha;
            item_cnt += 1;
        }
        if (item_id[hb] == 0) {
            item_id[hb] = item_cnt;
            item[item_cnt] = hb;
            item_cnt += 1;
        }

        toward[item_id[ha]].push_back(item_id[hb]);
        indegree[item_id[hb]] += 1;
    }
    tsort();
}