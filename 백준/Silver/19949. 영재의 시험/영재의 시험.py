answer = list(map(int, input().split()))
case = 0
youngjae = [0]*10


def dfs(n):
    global case
    if n == 10:
        point = 0
        for i in range(10):
            if youngjae[i] == answer[i]:
                point += 1

            if i - point > 6:
                break

            if point >= 5:
                case += 1
                break
        return

    for i in range(1,6):
        if n >= 2 and youngjae[n-2] == youngjae[n-1] == i:
            continue
        youngjae[n] = i
        dfs(n+1)
        youngjae[n] = 0


dfs(0)
print(case)