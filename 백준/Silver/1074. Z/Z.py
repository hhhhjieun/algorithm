import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

i = 0
ans = 0
while i < N:
    if r >= 2 ** (N - i - 1) and c >= 2 ** (N - 1 - i):
        ans += 3 * (4 ** (N - i - 1))
    elif r >= 2 ** (N - i - 1) and c < 2 ** (N - 1 - i):
        ans += 2 * (4 ** (N - i - 1))
    elif r < 2 ** (N - i - 1) and c >= 2 ** (N - 1 - i):
        ans += 4 ** (N - i - 1)
    r = r % (2 ** (N - i - 1))
    c = c % (2 ** (N - i - 1))
    i += 1
print(ans)