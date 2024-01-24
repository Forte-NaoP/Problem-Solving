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

    void insert(const char* key) {
        if (*key == '\0') leaf = true;
        else {
            int idx = *key - 'a';
            if (child[idx] == nullptr) child[idx] = new Node();
            child[idx]->insert(key + 1);
            cnt[idx] += 1;
        }
    }

    Node* find(const char* key) {
        if (*key == '\0') return this;
        int idx = *key - 'a'; 
        if (child[idx] == nullptr) return nullptr;
        return child[idx]->find(key + 1);
    }

    string find_k(int k) {
        if (leaf) return string();
        int n = 0, i = 0;
        while (i < 26 && n + cnt[i] < k) {
            n += cnt[i];
            i += 1;
        }
        string s;
        s.push_back(i + 'a');
        s += child[i]->find_k(k - n);
        return s;
    }

    void printAll(const std::string& prefix = "") {
        if (leaf) {
            std::cout << prefix << std::endl;
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
    for (int i=1; i<=T; ++i) {
        cin >> k;
        cin.ignore();
        cin >> s;
        const char * sp = s.c_str();

        Node root;
        for (int j=s.size()-1; j>=0; --j) {
            root.insert(sp + j);
        }

        cout << '#' << i << ' ' << root.find_k(k) << endl;
    }
}