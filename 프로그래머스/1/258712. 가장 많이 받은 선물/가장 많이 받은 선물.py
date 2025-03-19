from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    rec = defaultdict(lambda : defaultdict(int))
    g_score = defaultdict(int)
    r_score = defaultdict(int)
    for a, b in map(str.split, gifts):
        rec[a][b] += 1
        g_score[a] += 1
        r_score[b] += 1
        
    get = defaultdict(int)
    for a, b in combinations(friends, 2):
        if rec[a][b] > rec[b][a]:
            get[a] += 1
        elif rec[b][a] > rec[a][b]:
            get[b] += 1
        else:
            if g_score[a] - r_score[a] > g_score[b] - r_score[b]:
                get[a] += 1
            elif g_score[a] - r_score[a] < g_score[b] - r_score[b]:
                get[b] += 1
    
    if get:
        return max(get.values())
    else:
        return 0