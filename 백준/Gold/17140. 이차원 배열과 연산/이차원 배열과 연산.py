import sys
import heapq

input = sys.stdin.readline

MAX_VAL = 100

r, c, k = map(int, input().split())
max_row, max_col = 3, 3
arr = [[0 for _ in range(MAX_VAL + 1)] for _ in range(MAX_VAL + 1)]
for i in range(max_row):
    arr[i][:max_col] = list(map(int, input().split()))

row_cnt = [[0 for _ in range(MAX_VAL + 1)] for _ in range(MAX_VAL + 1)]
col_cnt = [[0 for _ in range(MAX_VAL + 1)] for _ in range(MAX_VAL + 1)]

for i in range(max_row):
    for j in range(max_col):
        row_cnt[i][arr[i][j]] += 1
        col_cnt[j][arr[i][j]] += 1

heap = []
hpush = heapq.heappush
hpop = heapq.heappop

def row_op():
    global max_row, max_col, heap
    for row_idx in range(max_row):
        for val in range(1, MAX_VAL + 1):
            if row_cnt[row_idx][val] != 0:
                hpush(heap, (row_cnt[row_idx][val], val))
                row_cnt[row_idx][val] = 0
        
        col_idx = 0
        while heap and col_idx < MAX_VAL:
            cnt, val = hpop(heap)

            col_cnt[col_idx][arr[row_idx][col_idx]] -= 1
            col_cnt[col_idx + 1][arr[row_idx][col_idx + 1]] -= 1

            arr[row_idx][col_idx] = val
            arr[row_idx][col_idx + 1] = cnt

            col_cnt[col_idx][arr[row_idx][col_idx]] += 1
            col_cnt[col_idx + 1][arr[row_idx][col_idx + 1]] += 1

            row_cnt[row_idx][val] += 1
            row_cnt[row_idx][cnt] += 1

            col_idx += 2

        max_col = max(col_idx, max_col)
        while col_idx < MAX_VAL:
            col_cnt[col_idx][arr[row_idx][col_idx]] -= 1
            arr[row_idx][col_idx] = 0
            col_idx += 1
        heap = []
    
def col_op():
    global max_row, max_col, heap
    for col_idx in range(max_col):
        for val in range(1, MAX_VAL + 1):
            if col_cnt[col_idx][val] != 0:
                hpush(heap, (col_cnt[col_idx][val], val))
                col_cnt[col_idx][val] = 0

        row_idx = 0
        while heap and row_idx < MAX_VAL:
            cnt, val = hpop(heap)

            row_cnt[row_idx][arr[row_idx][col_idx]] -= 1
            row_cnt[row_idx + 1][arr[row_idx + 1][col_idx]] -= 1

            arr[row_idx][col_idx] = val
            arr[row_idx + 1][col_idx] = cnt

            row_cnt[row_idx][arr[row_idx][col_idx]] += 1
            row_cnt[row_idx + 1][arr[row_idx + 1][col_idx]] += 1

            col_cnt[col_idx][val] += 1
            col_cnt[col_idx][cnt] += 1
            
            row_idx += 2

        max_row = max(row_idx, max_row)
        while row_idx < MAX_VAL:
            row_cnt[row_idx][arr[row_idx][col_idx]] -= 1
            arr[row_idx][col_idx] = 0
            row_idx += 1
        
        heap = []  

sec = 0
while arr[r - 1][c - 1] != k and sec < MAX_VAL + 1:
    if max_row >= max_col:
        row_op()
    else:
        col_op()

    sec += 1

if sec == MAX_VAL + 1:
    sec = -1
print(sec)
