#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

const int32_t all_chk = (1 << 10) - 1;

void mark(int32_t val, int32_t& chk) {
    while (val > 0) {
        chk |= (1 << (val % 10));
        val /= 10;
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int32_t T, n;
    cin >> T;

    for (int32_t t = 1; t <= T; ++t) {
        cin >> n;
        int32_t chk = 0, val = n;
        while (chk != all_chk) {
            mark(val, chk);
            val += n;
        }
        cout << "#" << t << " " << val - n << "\n";
    }
}