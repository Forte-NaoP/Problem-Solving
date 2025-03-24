#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <numeric>
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;


int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    int s, t;
    vector<pair<int, int>> lecture;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < n; ++i) {
        cin >> s >> t;
        lecture.push_back({s, t});
    }

    sort(lecture.begin(), lecture.end());

    for (auto& lect: lecture) {
        pq.push(lect.second);
        if (pq.top() <= lect.first) pq.pop();
    }

    cout << pq.size() << '\n';
}
