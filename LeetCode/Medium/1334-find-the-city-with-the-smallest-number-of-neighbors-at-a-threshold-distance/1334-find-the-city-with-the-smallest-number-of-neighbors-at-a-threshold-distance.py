from collections import defaultdict

INF = 1 << 31

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [defaultdict(int) for _ in range(n)]
        min_neighbor, city_num = 999, -1
        
        for f, t, w in edges:
            graph[f][t] = w
            graph[t][f] = w

        dist = [[0 if i == j else INF if graph[i][j] == 0 else graph[i][j] for j in range(n)] for i in range(n)]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt < min_neighbor:
                min_neighbor, city_num = cnt, i
            elif cnt == min_neighbor:
                city_num = max(i, city_num)
    
        return city_num