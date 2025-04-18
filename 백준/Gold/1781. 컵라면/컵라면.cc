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

using namespace std;

struct Problem {
    int deadline, reward;

    Problem(int d, int r): deadline(d), reward(r) {}
};

struct Problem_Priority {
    bool operator()(const Problem& a, const Problem& b) const {
        return a.reward <= b.reward;
    }
};

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<Problem> problems;
    priority_queue<Problem, vector<Problem>, Problem_Priority> pq;

    int n, d, r;
    cin >> n;
    problems.reserve(n);

    for (int i = 0; i < n; ++i) {
        cin >> d >> r;
        problems.emplace_back(d, r);
    }

    sort(problems.begin(), problems.end(), [](const Problem& a, const Problem& b) {
        return a.deadline > b.deadline;
    });

    int idx = 0;
    int deadline = problems[0].deadline;
    vector<Problem> solved(n + 1, {0, 0});

    while (deadline > 0) {
        while (idx < n && problems[idx].deadline >= deadline) {
            pq.push(problems[idx++]);
        }
        if (!pq.empty()) {
            solved[deadline] = pq.top();
            pq.pop();
        } else {
            solved[deadline] = {deadline, 0};
        }
        deadline -= 1;
    }

    int ans = 0;
    for (Problem& p: solved) {
        ans += p.reward;
    }

    cout << ans << '\n';
}


