#include <set>
#include <cstdint>

using namespace std;

class Solution {
public:
    int flipLights(int n, int presses) {

        int button[4] = {7, 3, 5, 4};
        set<uint8_t> comb[4];
        comb[0].insert(7);

        presses = min(presses, 3);
        n = min(n, 3);

        for (int i = 1; i <= presses; ++i) {
            for (int j = 0; j < 4; ++j) {
                for (auto x : comb[i - 1]) {
                    comb[i].insert(x ^ button[j]);
                }
            } 
        }    

        set<uint8_t> ans;
        for (auto x : comb[presses]) {
            ans.insert(x >> (3 - n));
        }
        return ans.size();
    }
};