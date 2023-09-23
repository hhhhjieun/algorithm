# N과 M(9)
import sys


def recur(cnt, arr):
    global result

    if cnt == M:
        print(*arr)

    if cnt >= M:
        return

    use_number = []
    for w in range(N):
        if path[w] == 0 and numbers[w] not in use_number:
            path[w] = 1
            arr.append(numbers[w])
            use_number.append(numbers[w])
            recur(cnt + 1, arr)
            path[w] = 0
            arr.pop()


N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

path = [0] * N
result = []
recur(0, [])
