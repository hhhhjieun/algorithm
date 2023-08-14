import sys

N = int(sys.stdin.readline())

T = []  # 시간
A = []  # 점수
scores = 0

for i in range(N):
    task = list(map(int, sys.stdin.readline().split()))

    if task[0] == 1:
        A.append(task[1])
        T.append(task[2])

    if T:
        time = T.pop()
        score = A.pop()
        time -= 1
        if time == 0:
            scores += score
        else:
            T.append(time)
            A.append(score)

print(scores)