# 겹치는 건 싫어
import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = end = 0

num_dict = {}
max_cnt = 0

while end != n:
    if arr[end] not in num_dict:
        num_dict[arr[end]] = 1
        end += 1
    else:
        num_dict[arr[end]] += 1

        if num_dict[arr[end]] > k:
            tmp = end - start
            max_cnt = max(max_cnt, tmp)

            while arr[start] != arr[end]:
                num_dict[arr[start]] -= 1
                start += 1
                
            num_dict[arr[start]] -= 1
            start += 1

        end += 1

ans = end - start
max_cnt = max(max_cnt, ans)

print(max_cnt)