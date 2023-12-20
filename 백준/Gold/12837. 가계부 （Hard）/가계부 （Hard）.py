# 가계부

import sys
sys.setrecursionlimit(10 ** 8)


def find(idx, start, end, left, right):
    # 범위 포함 안되는 경우
    if left > end or right < start:
        return 0

    # 포함
    if left <= start and right >= end:
        return seg[idx]

    mid = (start + end) // 2
    l = find(idx * 2, start, mid, left, right)
    r = find(idx * 2 + 1, mid + 1, end, left, right)

    return l + r


def update(idx, start, end, id, val):

    if id < start or end < id:
        return

    if start == end:
        seg[idx] += val
        return

    mid = (start + end) // 2
    # 왼쪽 업데이트
    update(idx * 2, start, mid, id, val)
    # 오른쪽 업데이트
    update(idx * 2 + 1, mid + 1, end, id, val)

    # 업데이트 된 자식노드를 통해 현재 노드 업데이트
    seg[idx] = seg[idx*2] + seg[idx*2+1]


N, Q = map(int, sys.stdin.readline().split())

seg = [0] * (4 * N)

for _ in range(Q):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(find(1, 0, N-1, b-1, c-1))

