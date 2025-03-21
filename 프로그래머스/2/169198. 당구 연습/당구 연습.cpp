#include <string>
#include <vector>

using namespace std;

int max_x, max_y;

int reflect(int x, int y, int a, int b) {
    int ub = 2 * max_y - b;
    int ra = 2 * max_x - a;
    int db = -b;
    int la = -a;
    
    int u = (x - a) * (x - a) + (y - ub) * (y - ub);
    int r = (x - ra) * (x - ra) + (y - b) * (y - b);
    int d = (x - a) * (x - a) + (y - db) * (y - db);
    int l = (x - la) * (x - la) + (y - b) * (y - b);

    int ret = 1e9;
    
    if (x == a) {
        if (y < b) u = 1e9;
        else d = 1e9;
    }
    
    if (y == b) {
        if (x < a) r = 1e9;
        else l = 1e9;
    }
    
    ret = min(min(u, d), min(l, r));
    return ret;
}

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    max_x = m;
    max_y = n;
    vector<int> answer;
    for (auto& ball: balls) {
        answer.push_back(reflect(startX, startY, ball[0], ball[1]));
    }
    
    return answer;
}