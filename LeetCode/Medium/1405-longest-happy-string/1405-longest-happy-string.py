import heapq

push = heapq.heappush
pop = heapq.heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        pq = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heapq.heapify(pq)

        while True:
            max_cnt = pop(pq)
            
            if len(ans) > 1 and ans[-2:] == max_cnt[1] * 2:
                tmp = max_cnt
                max_cnt = pop(pq)
                push(pq, tmp)

            if max_cnt[0] == 0:
                break

            ans += max_cnt[1]
            max_cnt[0] += 1

            push(pq, max_cnt)

        return ans