class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        board = dict()
        for idx, alphabet in enumerate(alphabets):
            board[alphabet] = (idx//5, idx%5)
        
        cr, cc = 0, 0
        ans = ''
        z = False
        for ch in target:
            nr, nc = board[ch]
            dr, dc = nr-cr, nc-cc
            
            if ch == 'z':
                if dc < 0:
                    ans += 'L'*abs(dc)
                else:
                    ans += 'R'*abs(dc)
            
                if dr < 0:
                    ans += 'U'*abs(dr)
                else:
                    ans += 'D'*abs(dr)
            else:
                if dr < 0:
                    ans += 'U'*abs(dr)
                else:
                    ans += 'D'*abs(dr)
                    
                if dc < 0:
                    ans += 'L'*abs(dc)
                else:
                    ans += 'R'*abs(dc)
            
            ans += '!'
            cr, cc = nr, nc
        return ans