# 0만들기
import sys
import copy


def zero(arr, n):
    if len(arr) == n:
        ans.append(copy.deepcopy(arr))
        return

    arr.append(' ')
    zero(arr, n)
    arr.pop()

    arr.append('+')
    zero(arr, n)
    arr.pop()

    arr.append('-')
    zero(arr, n)
    arr.pop()


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    ans = []
    zero([], N - 1)

    nums = [i for i in range(1, N + 1)]

    for result in ans:
        tmp = ''
        for i in range(N - 1):
            tmp += str(nums[i]) + result[i]

        tmp +=  str(nums[-1])
        if eval(tmp.replace(' ', '')) == 0:
            print(tmp)
    print()
