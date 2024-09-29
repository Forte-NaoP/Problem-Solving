import sys

input = sys.stdin.readline

n, k, d = map(int, input().split())
student = []
skill = []
any_know = [0 for _ in range(31)]

for i in range(n):
    a, b = map(int, input().split())
    skill.append((b, i))
    student.append(list(map(int, input().split())))

max_E = 0
skill.sort()
st, ed = 0, 0

while ed < n:
    for algo in student[skill[ed][1]]:
        any_know[algo] += 1
    ed += 1
    while st < ed and skill[ed - 1][0] - skill[st][0] > d:
        for algo in student[skill[st][1]]:
            any_know[algo] -= 1
        st += 1
    num = ed - st
    e = (31 - any_know.count(0) - any_know.count(num)) * num
    max_E = max(max_E, e)
    
print(max_E)