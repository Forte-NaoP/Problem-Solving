#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

struct Node {
    int value;
    string path;
};

int rotateL(int num) {
    int last = num / 1000;
    int rest = num % 1000;

    return rest * 10 + last;
}

int rotateR(int num) {
    int last = num % 10;
    int rest = num / 10;

    if (num < 10) return num * 1000;

    return last * 1000 + rest;
}

void bfs(int num, int password) {
    queue<Node> q;
    vector<bool> visited(10000, false);
    q.push({ num, "" });
    visited[num] = true;

    while (!q.empty()) {
        Node now = q.front();
        q.pop();

        if (now.value == password) {
            cout << now.path << endl;
        }

        int double_now = (now.value * 2) % 10000;
        if (!visited[double_now]) {
            visited[double_now] = true;
            q.push({ double_now, now.path + "D" });
        }

        int minus_num = (now.value == 0) ? 9999 : now.value - 1;
        if (!visited[minus_num]) {
            visited[minus_num] = true;
            q.push({ minus_num, now.path + "S" });
        }

        int L_num = rotateL(now.value);
        if (!visited[L_num]) {
            visited[L_num] = true;
            q.push({ L_num, now.path + "L" });
        }

        int R_num = rotateR(now.value);
        if (!visited[R_num]) {
            visited[R_num] = true;
            q.push({ R_num, now.path + "R" });
        }
    }
}

int main() {
    int N; cin >> N;
    for (int idx = 0; idx < N; idx++) {
        int start, end; cin >> start >> end;
        bfs(start, end);
    }
}