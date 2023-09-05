class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = dict()
        c_count = dict()
        for a in arr:
            if count.get(a) is None:
                count[a] = 1
            else:
                count[a] += 1

        for key, val in count.items():
            if c_count.get(val) is None:
                c_count[val] = set([key])
            else:
                c_count[val].add(key)

        removed = 0
        i = 1
        while 0 < k and k >= i:
            if (c := c_count.get(i)) is not None:
                most = k // i
                if most > 0:
                    k -= min(most, len(c)) * i
                    removed += min(most, len(c))
                else:
                    break
            i += 1

        return sum(map(len, c_count.values())) - removed