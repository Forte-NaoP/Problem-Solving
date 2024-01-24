#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

struct Node {
    Node* child[26] = {};
    bool leaf = false;
    int cnt[26] = {};

    bool insert(const char* key) {
        bool result = true;
        if (*key == '\0') {
            if (leaf) result = false;
            leaf = true;
        } else {
            int idx = *key - 'a';
            if (child[idx] == nullptr) child[idx] = new Node();
            result = child[idx]->insert(key + 1);
            if (result) cnt[idx] += 1;
        }
        return result;
    }

    Node* find(const char* key) {
        if (*key == '\0') return this;
        int idx = *key - 'a'; 
        if (child[idx] == nullptr) return nullptr;
        return child[idx]->find(key + 1);
    }

    bool find_k(int& k, char* ans, int idx) {
        if (leaf) {
            if (--k == 0) {
                ans[idx] = '\0';
                return true;
            }
        }

        for (int i=0; i<26; ++i) {
            if (child[i] != nullptr) {
                if (k > cnt[i]) k -= cnt[i];
                else {
                    ans[idx] = i + 'a';
                    if (child[i]->find_k(k, ans, idx + 1)) return true;
                }
            }
        }
        return false;
    }

    void printAll(const std::string& prefix = "") {
        if (leaf) {
            cout << prefix << endl;
        }
        for (int i = 0; i < 26; ++i) {
            if (child[i] != nullptr) {
                child[i]->printAll(prefix + char(i + 'a'));
            }
        }
    }
};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
	int T;
    cin >> T;
    cin.ignore();
    string s;
    int k;
    char cstr[401];
    for (int i=1; i<=T; ++i) {
        cin >> k;
        cin.ignore();
        cin >> s;
        strcpy(cstr, s.c_str());

        Node root;
        for (int j=0; j<s.size(); ++j) {
            for (int l=j; l<s.size(); ++l) {
                char c = cstr[l+1];
                cstr[l+1] = '\0';
                root.insert(cstr+j);
                // cout << "insert: " << cstr+j << '\n'; 
                cstr[l+1] = c;
            }
        }
        
        if(root.find_k(k, cstr, 0)) cout << '#' << i << ' ' << cstr << '\n';
        else cout << '#' << i << " none" << '\n';
    }
}