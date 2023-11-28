import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())

tmp = [input().strip() for _ in range(n)]
s = [input().strip() for _ in range(m)]

dic = {}

for x in tmp:
    for i in range(1, len(x) + 1) : dic[x[:i]] = 1

cnt = 0
for i in s:
    try:
        cnt += dic[i]
    except:
        pass

print(cnt)