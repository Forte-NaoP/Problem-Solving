import sys
input = sys.stdin.readline

long, short, t = map(int, input().split())
if short > long:
    long, short = short, long
total_eat, total_drink = 0, t
long_cnt = 0

while t >= (long_eat := long * long_cnt):
    left_time = t - long_eat
    eat = long_cnt + left_time // short
    drink = left_time % short

    if (total_drink > drink) or (total_drink == drink and eat > total_eat):
        total_eat, total_drink = eat, drink

    long_cnt += 1

print(total_eat, total_drink)