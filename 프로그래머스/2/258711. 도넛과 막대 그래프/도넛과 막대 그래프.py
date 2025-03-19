from collections import defaultdict

def solution(edges):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    node = set()
    
    for a, b in edges:
        indegree[b] += 1
        outdegree[a] += 1
        node.add(a)
        node.add(b)
        
    answer = [0, 0, 0, 0]

    for i in list(node):
        if indegree[i] == 0 and outdegree[i] >= 2:
            answer[0] = i
        elif indegree[i] > 0 and outdegree[i] == 0:
            answer[2] += 1
        elif indegree[i] >= 2 and outdegree[i] >= 2:
            answer[3] += 1
    
    answer[1] = outdegree[answer[0]] - (answer[2] + answer[3])
        
    return answer