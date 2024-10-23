import sys
from typing import List

input = sys.stdin.readline

def encode(s):
    val = 0
    for c in s:
        val <<= 5
        val += ord(c) - ord('A') + 1
    return val

def decode(val):
    s = []
    while val > 0:
        s.append(chr((val & 31) + ord('A') - 1))
        val >>= 5
    s.reverse()
    return ''.join(s)

class Node:
    def __init__(self):
        self.link: List[Node, None] = [None for _ in range(26)]
        self.end = False

    def insert(self, s: int):
        if not s:
            self.end = True
            return
        idx = (s & 31) - 1
        if not self.link[idx]:
            self.link[idx] = Node()
        self.link[idx].insert(s >> 5)
    
    def find(self, s: int):
        if not s:
            return True if self.end else False
        idx = (s & 31) - 1
        if not self.link[idx]:
            return False
        return self.link[idx].find(s >> 5)

trie = Node()
for _ in range(int(input())):
    trie.insert(encode(input().strip()))

diff = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
score = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}

def dfs(x, y, word, depth):
    global longest_word, lword_len, max_score
    visited[x][y] = True
    word = (word << 5) + ord(board[x][y]) - ord('A') + 1

    if depth != 0 and word not in chk:
        if trie.find(word):
            chk.add(word)
            max_score += score[depth]
            if lword_len < depth:
                longest_word = word
                lword_len = depth
            elif lword_len == depth:
                longest_word = min(longest_word, word)

    if depth == 8:
        word >>= 5
        visited[x][y] = False
        return
    
    for dx, dy in diff:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 4) or not (0 <= ny < 4):
            continue
        if visited[nx][ny]:
            continue
        dfs(nx, ny, word, depth + 1)

    word >>= 5
    visited[x][y] = False

input()
for _ in range(int(input())):
    board = [list(input().strip()) for _ in range(4)]
    input()
    visited = [[False for _ in range(4)] for _ in range(4)]
    chk = set()
    longest_word, lword_len, max_score = 0, 0, 0
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, 1)
    print(max_score, decode(longest_word), len(chk))