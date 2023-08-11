import sys

memo = [0] * 10001

N = int(sys.stdin.readline())

memo[1] = 1
for i in range(2, N+1):
    if memo[i]:
        continue
    # 규칙이 i의 값은 i-2의 2배 와 i-1의 합
    memo[i] = memo[i-2] + memo[i-1]


print(memo[N])