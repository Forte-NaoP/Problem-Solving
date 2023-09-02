class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        board = dict()
        for idx, alphabet in enumerate(alphabets):
            board[alphabet] = (idx//5, idx%5)
        
        cr, cc = 0, 0
        ans = ''
        bc = ''
        z = False
        for ch in target:
            nr, nc = board[ch]
            
            if bc != 'z' and ch =='z':
                nr -= 1
                z = True
            
            dr, dc = nr-cr, nc-cc

            if dr < 0:
                ans += 'U'*abs(dr)
            else:
                ans += 'D'*abs(dr)

            if dc < 0:
                ans += 'L'*abs(dc)
            else:
                ans += 'R'*abs(dc)
                
            if z:
                nr += 1
                ans += 'D'
                z = False
            
            ans += '!'
            cr, cc = nr, nc
            bc = ch
        return ans