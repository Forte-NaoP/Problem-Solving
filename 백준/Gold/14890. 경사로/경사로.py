import sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
used = [[False for _ in range(n)] for _ in range(n)]

ans = 0
def check():
    global ans
    for i in range(n):
        st = 0
        cross = True
        while st < n:
            j = st
            h = road[i][j]
            streak = 0
            while j < n and h == road[i][j]:
                j += 1
                streak += 1
            
            if j == n: # 모든 높이가 같음
                break
                
            if abs(h - road[i][j]) > 1: # 높이가 2 이상 차이나면 경사로를 놓을 수 없음
                cross = False
                break

            if h < road[i][j]: #높이가 높아졌고
                if streak < m or any(used[i][j - m:j]): # 경사로의 길이보다 짧거나 사용중이면 건너지 못함
                    cross = False
                    break
                used[i][j - m:j] = [True] * m # 경사로 놓기
            else: # 높이가 낮아졌으면
                k = j
                streak = 0
                # 낮은 부분이 얼마나 평탄한지 확인
                while k < n and streak < m and road[i][k] == road[i][j]:
                    k += 1
                    streak += 1
                if streak < m or any(used[i][j:k]): # 경사로의 길이보다 짧거나 사용중이면 건너지 못함
                    cross = False
                    break
                used[i][j:j + m] = [True] * m 
            
            st = j
            
        if cross:
            ans += 1

        # 한 줄 확인 후에 초기화
        used[i] = [False for _ in range(n)]

check()
# 행, 열 뒤집어서 함수 재활용
for i in range(n):
    for j in range(i):
        road[i][j], road[j][i] = road[j][i], road[i][j]
check()
print(ans)