# 백준 11727, 2 x n 타일링 2

tiled = {1:1, 2:3}
def tiling(n):
    if n in tiled:
        return tiled[n]

    tiled[n] = tiling(n-1) + 2 * tiling(n-2)
    return tiled[n]

if __name__ == "__main__":
    n = int(input())

    result = tiling(n) % 10007

    print(result)