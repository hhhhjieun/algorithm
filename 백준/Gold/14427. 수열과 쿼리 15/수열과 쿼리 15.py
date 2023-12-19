# 수열과 쿼리 15

import sys
import math
sys.setrecursionlimit(10 ** 8)


def makeSegTree(idx, start, end):
    if start == end:  # 리프 노드
        seg[idx] = numbers[start]
        # print(seg)
        return seg[idx]

    mid = (start + end) // 2

    left = makeSegTree(idx * 2, start, mid)
    right = makeSegTree(idx * 2 + 1, mid + 1, end)

    seg[idx] = min(left, right)

    return seg[idx]


def find(idx, start, end):

    if start > end:
        return

    elif start == end:
        seg[idx] = numbers[start]
        return numbers[start]

    mid = (start + end) // 2
    left = find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)

    return min(left, right)


def update(idx, start, end, id, val):

    if start > end:
        return 1000000000

    elif start == end:
        if start == id:
            seg[idx] = val
            return val
        else:
            return seg[idx]

    if id < start or end < id:
        return

    mid = (start + end) // 2
    # 왼쪽 업데이트
    update(idx * 2, start, mid, id, val)
    # 오른쪽 업데이트
    update(idx * 2 + 1, mid + 1, end, id, val)

    # 업데이트 된 자식노드를 통해 현재 노드 업데이트
    seg[idx] = min(seg[idx*2], seg[idx*2+1])


def find_idx(idx, val, start, end):
    global result
    if seg[idx] == None or seg[idx] != val or result != None:
        return

    if start == end and seg[idx] == val:
        result = start
        return

    mid = (start + end) // 2
    find_idx(idx * 2, val, start, mid)
    find_idx(idx * 2 + 1, val, mid + 1, end)


N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().strip().split()))
# print(numbers)

# math.ceil 로 시간단축
seg = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))

makeSegTree(1, 0, N - 1)

M = int(sys.stdin.readline())
for _ in range(M):
    q = list(map(int, sys.stdin.readline().split()))
    # print(q)
    if q[0] == 1:
        update(1, 0, N-1, q[1]-1, q[2])
    else:
        result = None
        find_idx(1, seg[1], 0, N-1)
        print(result + 1)

