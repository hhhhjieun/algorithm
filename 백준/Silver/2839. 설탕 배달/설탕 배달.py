import sys

N = int(sys.stdin.readline())

# 5kg 최대개수
max_n5 = N // 5

n5 = 0
n3 = 0
result = True
# 최대개수 부터 내림차순으로 나머지가 3으로 나눠지면 그만
for i in range(max_n5, -1, -1):
    if (N - (5*i)) % 3 == 0:
        n5 = i
        n3 = (N - (5*i)) // 3
        result = True
        break
    else:
        result = False

if result is True:
    total = n3 + n5
    print(total)
else:
    print(-1)