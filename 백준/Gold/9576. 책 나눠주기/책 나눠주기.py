import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    books = [True] * (N + 1)
    result = 0
    students = []

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        students.append((a, b))

    students.sort(key=lambda x : x[1])

    for student in students:
        for i in range(student[0], student[1] + 1):
            if books[i]:
                books[i] = False
                result += 1
                break

    print(result)

