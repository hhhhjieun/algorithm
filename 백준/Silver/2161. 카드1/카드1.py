import sys

N = int(sys.stdin.readline())

Q = [i for i in range(1, N+1)]

result = []

while Q:
    result.append(str(Q.pop(0)))
    if len(Q) != 0:
        Q.append(str(Q.pop(0)))
    else:
        break


ans = ' '.join(result)
print(ans)