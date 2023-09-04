class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        chunk_len = numRows * 2 - 2
        chunk_row_len = numRows - 1
        left_len = len(s) % chunk_len
        left_row_len = max(left_len - numRows, 0) + 1
        zigzag_len = chunk_row_len * (len(s) // chunk_len) + left_row_len
        zigzag = [['' for _ in range(numRows)] for _ in range(zigzag_len)]

        i, j = 0, 0
        rev = False
        for c in s:
            zigzag[i][j] = c
            if not rev:
                i, j = i, j + 1
                if j == numRows - 1:
                    rev = True
            else:
                i, j = i + 1, j - 1
                if j == 0:
                    rev = False

        answer = ''
        for i in range(numRows):
            for j in range(zigzag_len):
                if zigzag[j][i] != '':
                    answer += zigzag[j][i]

        return answer