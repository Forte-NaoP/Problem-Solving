#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string input, bomb;
    cin >> input >> bomb;

    int count = 0;
    vector<char> ans;

    for (char c : input) {
        ans.push_back(c);
        if (ans.size() >= bomb.size()) {
            bool matched = true;
            for (int i = ans.size() - bomb.size(), j = 0; i < ans.size(); ++i, ++j) {
                if (ans[i] != bomb[j]) {
                    matched = false;
                    break;
                }
            }
            if (matched) {
                for (int i = 0; i < bomb.size(); ++i) ans.pop_back();
            }
        }
    }
    
    if (ans.empty()) {
        cout << "FRULA" << '\n';
        return 0;
    }

    cout << string(ans.begin(), ans.end()) << '\n';
}
