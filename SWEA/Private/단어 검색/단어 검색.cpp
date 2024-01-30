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
    int leaf = 0;
    int cnt[26] = {};

    ~Node() {
        for (int i = 0; i < 26; ++i) {
            if (child[i]) {
                delete child[i];
            }
        }
    }

    int insert(const char* key, const bool allow_dup = false) {
        int result = 0;
        if (*key == '\0') {
            if (leaf == 0 || allow_dup) leaf += 1;
            result = leaf;
        } else {
            int idx = *key - 'a';
            if (child[idx] == nullptr) child[idx] = new Node();
            result = child[idx]->insert(key + 1, allow_dup);
            if (result > 0) cnt[idx] += 1;
        }
        return result;
    }

    Node* find(const char* key) {
        if (*key == '\0') return this;
        int idx = *key - 'a'; 
        if (child[idx] == nullptr) return nullptr;
        return child[idx]->find(key + 1);
    }

    int find_cnt(const char* key) {
        if (*key == '\0') return leaf;

        int idx = *key == '?' ? 0 : *key - 'a';
        int end = *key == '?' ? 26 : idx + 1;
        int r = 0;
        for (; idx<end; ++idx) {
            if (child[idx] != nullptr) {
                int tr = child[idx]->find_cnt(key + 1);
                r += tr;
            } 
        }
        return r;
    }

    int remove(const char* key) {
        int r = 0;
        if (*key == '\0') {
            r = leaf;
            leaf = 0;
            return r;
        } else {
            int idx = *key == '?' ? 0 : *key - 'a';
            int end = *key == '?' ? 26 : idx + 1;
            for (; idx<end; ++idx) {
                if (child[idx] != nullptr) {
                    int tr = child[idx]->remove(key + 1);
                    r += tr;
                    cnt[idx] -= tr;
                } 
            }
        }
        return r;
    }
};

Node *root;

void init() {
    if (root != nullptr) delete root;
    root = new Node();
	return;
}

int add(char str[]) {
    return root->insert(str, true);
}

int remove(char str[]) {
    int result = root->remove(str);
	return result;
}

int search(char str[]) {
	return root->find_cnt(str);
}