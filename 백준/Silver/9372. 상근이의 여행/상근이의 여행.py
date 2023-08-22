'''
비행기 노선이 2개씩 밖에 없어
결국 모든 국가를 여행하려면 N-1번 타야함
'''
import sys

T = int(sys.stdin.readline())

for test_case in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())  # N : 국가의 수, M : 비행기 종류
    flights = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    print(N-1)