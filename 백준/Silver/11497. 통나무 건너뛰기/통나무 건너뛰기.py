from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    arr = deque(arr)

    queue = deque()
    while arr:
        a = arr.popleft()
        if arr:
            b = arr.popleft()

            queue.appendleft(a)
            queue.append(b)
        else:
            queue.appendleft(a)

    max_difficulty = 0
    for i in range(N):
        difficulty = abs(queue[i] - queue[i-1])

        if max_difficulty < difficulty:
            max_difficulty = difficulty

    print(max_difficulty)