# 구간 곱 구하기
'''


'''
import sys
import math
sys.setrecursionlimit(10 ** 8)


def makeSegTree(idx, start, end):
    if start == end:  # 리프 노드
        seg[idx] = numbers[start]
        # print(seg)
        return seg[idx]

    mid = (start + end) // 2  # 몫 구하기

    left = makeSegTree(idx * 2, start, mid)
    right = makeSegTree(idx * 2 + 1, mid + 1, end)

    # 곱 계산
    seg[idx] = left * right % 1000000007

    return seg[idx]


def find(idx, start, end):
    # 찾으려는 범위가 겹치지 않을 때
    if c-1 < start or b-1 > end:
        return 1

    if b-1 <= start and end <= c-1:
        return seg[idx]

    # 구간이 겹치지 않는 경우
    mid = (start + end) // 2
    left = find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)

    return left * right % 1000000007


def update(idx, start, end, id, val):
    # 길이 1인 구간
    if start == end == id:
        seg[idx] = val
        return

    if id < start or end < id:
        return

    mid = (start + end) // 2
    # 왼쪽 업데이트
    update(idx * 2, start, mid, id, val)
    # 오른쪽 업데이트
    update(idx * 2 + 1, mid + 1, end, id, val)

    # 업데이트 된 자식노드를 통해 현재 노드 업데이트
    seg[idx] = seg[idx*2] * seg[idx*2+1] % 1000000007


N, M, K = map(int, sys.stdin.readline().split())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
# print(numbers)

# math.ceil 로 시간단축
seg = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))

makeSegTree(1, 0, N - 1)

for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    # a가 1인 경우 change, 2인 경우 구간의 곱
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        ans = find(1, 0, N-1)
        print(ans)
