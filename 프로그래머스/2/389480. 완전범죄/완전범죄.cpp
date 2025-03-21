#include <string>
#include <vector>

using namespace std;

bool dp[41][121][121];

int solution(vector<vector<int>> info, int n, int m) {
    dp[0][0][0] = true;
    
    for (int i = 0; i < info.size(); ++i) {
        for (int j = 0; j <= n; ++j) {
            for (int k = 0; k <= m; ++k) {
                if (dp[i][j][k]) {
                    if (j + info[i][0] < n) {
                        dp[i + 1][j + info[i][0]][k] = true;
                    }
                    if (k + info[i][1] < m) {
                        dp[i + 1][j][k + info[i][1]] = true;
                    }
                }
            }
        }
    }
    
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            if (dp[info.size()][i][j]) {
                return i;
            }
        }
    }
    
    return -1;
}