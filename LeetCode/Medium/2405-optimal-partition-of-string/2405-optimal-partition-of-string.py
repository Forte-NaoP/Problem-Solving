class Solution:
    def partitionString(self, s: str) -> int:
        ans = []
        cnt = [0 for _ in range(26)]
        st, ed = 0, 0

        while ed < len(s):
            if cnt[ord(s[ed]) - ord('a')] != 0:
                ans.append(s[st:ed])
                cnt = [0 for _ in range(26)]
                st = ed
            else:
                cnt[ord(s[ed]) - ord('a')] += 1
                ed += 1
        ans.append(s[st:ed])
        return len(ans)