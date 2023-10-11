# 괄호 추가하기

import sys

def cal():
    stack =[]
    idx = 0
    while idx < len(arr):
        if arr[idx] == '(':
            idx += 1
            tmp = arr[idx:idx+3]
            stack.append(str(eval(str(''.join(tmp)))))
            idx += 4
        else:
            stack.append(arr[idx])
            idx += 1

    stack2 = []
    j = 0
    while j < len(stack):
        stack2.append(stack[j])
        if len(stack2) == 3:
            tmp = str(eval(str(''.join(stack2))))
            stack2.clear()
            stack2.append(tmp)
        j += 1
    return stack2[0]


def calcul(cnt, k):
    global max_ans
    max_ans = max(max_ans, int(cnt))
    if visited.count(False) < 2:
        return

    for i in range(k, len(arr)):
        if not visited[i] and i != len(arr) - 2 and i != len(arr) - 1:
            visited[i] = True
            if i + 3 < len(arr):
                visited[i + 2] = True
            # 괄호 넣기
            arr.insert(i + 3, ')')
            arr.insert(i, '(')
            # 괄호 visited 넣기
            visited.insert(i + 3, True)
            visited.insert(i, True)
            calcul(cal(), i)
            # pop
            visited.pop(i + 4)
            visited.pop(i)
            arr.pop(i + 4)
            arr.pop(i)
            visited[i] = False
            if i + 3 < len(arr):
                visited[i + 2] = False


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip())
# print(N, arr)
visited = [False] * N
for i in range(1, N, 2):
    visited[i] = True

max_ans = -99999999999999
calcul(-99999999999, 0)

if N == 1:
    print(arr[0])
else:
    print(max_ans)
