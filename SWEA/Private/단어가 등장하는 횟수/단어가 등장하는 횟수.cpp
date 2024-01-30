#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> get_pi(const string& s) {
    vector<int> pi(s.size(), 0);
    int begin = 1, matched = 0;

    while (begin + matched < s.size()) {
        if (s[begin+matched] == s[matched]) {
            matched += 1;
            pi[begin+matched-1] = matched;
        } else {
            if (matched == 0) begin += 1;
            else {
                begin += matched - pi[matched-1];
                matched = pi[matched-1];
            }
        }
    }
    return pi;
}

int kmp(const string& b, const string& s) {
    vector<int> pi = get_pi(s);
    vector<int> found;
    int begin = 0, matched = 0;

    while (begin + s.size() <= b.size()) {
        if (matched < s.size() && b[begin+matched] == s[matched]) {
            matched += 1;
            if (matched == s.size()) found.push_back(begin);
        } else {
            if (matched == 0) begin += 1;
            else {
                begin += matched - pi[matched-1];
                matched = pi[matched-1];
            }
        }
    }
    return found.size();
}

int main() {
    freopen("../../input.txt", "rt", stdin);

	int T;
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> T;
    cin.ignore();
    int h, w, n, m;
    string s;
    for (int i=1; i<=T; ++i) {
        cin >> h >> w >> n >> m;
        cin.ignore();
        vector<string> d, t;
        vector<vector<int>> pi;
        for (int j=0; j<h; ++j) {
            cin >> s;
            d.push_back(s);
        }
        for (int j=0; j<n; ++j) {
            cin >> s;
            t.push_back(s);
        }
    }
}