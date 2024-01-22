#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

	int T, n, m;
    cin >> T;
    vector<string> a, b;
    for (int i=1; i<=T; ++i) {
        cin >> n >> m;
        cin.ignore();
        string line, word;

        a.clear();
        b.clear();

        getline(cin, line);
        istringstream iss(line);
        while (iss >> word) a.push_back(word);
        sort(a.begin(), a.end());

        getline(cin, line);
        iss = istringstream(line);
        while (iss >> word) b.push_back(word);
        sort(b.begin(), b.end());

        vector<string> v(a.size() + b.size());
        auto iter = set_intersection(a.begin(), a.end(), b.begin(), b.end(), v.begin());
        cout << '#' << i << ' ' << iter - v.begin() << '\n';
    }
}