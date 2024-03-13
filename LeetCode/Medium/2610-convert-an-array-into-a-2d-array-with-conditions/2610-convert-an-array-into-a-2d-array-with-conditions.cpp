#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        int cnt_num[201] = {};

        for (int& num : nums) cnt_num[num]++;

        int max_group = *max_element(cnt_num + 1, cnt_num + 201);

        vector<vector<int>> ans(max_group);
        for (int i = 1; i < 201; ++i) {
            for (int j = 0; j < cnt_num[i]; ++j) {
                ans[j].push_back(i);
            }
        }

        return ans;
    }
};