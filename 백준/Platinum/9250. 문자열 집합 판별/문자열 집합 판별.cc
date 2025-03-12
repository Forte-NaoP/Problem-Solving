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

struct TrieNode {
    TrieNode* children[26];
    TrieNode* failLink;
    bool isEnd;

    TrieNode(): isEnd(false), failLink(nullptr) {
        for (int i = 0; i < 26; i++) children[i] = nullptr;
    }
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() { root = new TrieNode(); }

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->children[index]) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->isEnd = true;
    }

    void failure() {
        deque<TrieNode*> q;

        if (root)
            q.push_back(root);

        while (!q.empty()) {
            TrieNode* node = q.front();
            q.pop_front();

            for (int i = 0; i < 26; ++i) {
                TrieNode* child = node->children[i];
                if (!child) continue;
                if (node == root) {
                    child->failLink = root;
                } else {
                    TrieNode* parent = node->failLink;
                    while (parent != root && !parent->children[i]) {
                        parent = parent->failLink;
                    }
                    if (parent->children[i]) {
                        parent = parent->children[i];
                    }
                    child->failLink = parent;
                }

                if (child->failLink->isEnd) {
                    child->isEnd = true;
                }

                q.push_back(child);
            }
        }
    }

    bool search(const string& word) {
        TrieNode* node = root;
        for (char c: word) {
            int index = c - 'a';
            while (node != root && !node->children[index]) {
                node = node->failLink;
            }
            if (node->children[index]) {
                node = node->children[index];
            }
            if (node->isEnd) {
                return true;
            }
        }
        return false;
    }

    ~Trie() {
        deleteNode(root);
    }

private:
    void deleteNode(TrieNode* node) {
        if (!node) return;
        for (int i = 0; i < 26; i++) {
            deleteNode(node->children[i]);
        }
        delete node;
    }
};

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    Trie trie = Trie();

    int n, q;
    string s;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> s;
        trie.insert(s);
    }
    trie.failure();
    cin >> q;
    for (int i = 0; i < q; ++i) {
        cin >> s;
        if (trie.search(s)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}

