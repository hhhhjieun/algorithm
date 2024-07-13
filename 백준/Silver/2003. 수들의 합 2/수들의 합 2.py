import sys

N, M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))
lst.append(0)
ans = 0

start = 0
end = 1

total = lst[0]
while start <= end and end <= N:
    if total < M:
        total += lst[end]
        end += 1
    elif total > M:
        total -= lst[start]
        start += 1
    else:
        ans += 1
        total += lst[end]
        end += 1

print(ans)