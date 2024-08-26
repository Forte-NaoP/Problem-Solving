import sys
input = sys.stdin.readline

bee = input().strip()
letter = [False for _ in range(26)]
for b in bee:
    letter[ord(b) - ord('a')] = True
n = int(input())

for _ in range(n):
    word = input().strip()
    if len(word) < 4:
        continue
    
    if all(letter[ord(w) - ord('a')] for w in word) and bee[0] in word:
        print(word)