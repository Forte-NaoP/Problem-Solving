class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st = []
        ans = []
        for i in range(len(heights) - 1, -1, -1):
            can_see = 0
            while st and st[-1] < heights[i]:
                st.pop()
                can_see += 1
            if st:
                can_see += 1
            st.append(heights[i])
            ans.append(can_see)
        ans.reverse()
        return ans