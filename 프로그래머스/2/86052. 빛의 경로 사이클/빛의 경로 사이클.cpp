#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

vector<int> dir[26];
int graph[500][500];
int visit[500][500][4];
int visit_id;
int n, m;

int dfs(int id, int x, int y, int d, int len) {
    if (visit[x][y][d] == id) {
        return len;
    }
    
    visit[x][y][d] = id;
    int nx = (x + dx[d]) % n;
    int ny = (y + dy[d]) % m;
    if (nx < 0) nx += n;
    if (ny < 0) ny += m;

    int nd = dir[graph[nx][ny]][d];
    
    return dfs(id, nx, ny, nd, len + 1);
}

vector<int> solution(vector<string> grid) {
    dir['S' - 'A'] = {0, 1, 2, 3};
    dir['L' - 'A'] = {3, 0, 1, 2};
    dir['R' - 'A'] = {1, 2, 3, 0};
    
    n = grid.size();
    m = grid[0].size();
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            graph[i][j] = grid[i][j] - 'A';
        }
    }

    vector<int> answer;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int d = 0; d < 4; ++d) {
                if (visit[i][j][d] == 0) {
                    answer.push_back(dfs(++visit_id, i, j, d, 0));
                }
            }
        }
    }
    
    sort(answer.begin(), answer.end());
    
    return answer;
}