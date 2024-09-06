import sys
input = sys.stdin.readline

txt = "WelcomeToSMUPC"
n = int(input())
print(txt[(n - 1) % 14])