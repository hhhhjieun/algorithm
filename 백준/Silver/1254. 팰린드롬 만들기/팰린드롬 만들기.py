# 팰린드롬 만들기
import sys
arr = sys.stdin.readline().strip()

n = len(arr)
pallin_idx = 0

def reverse(i):
    reverse_arr = ''
    for i in range(n-1, i-1, -1):
        reverse_arr += arr[i]

    return reverse_arr

for i in range(n):

    if arr[i:] == reverse(i):
        pallin_idx = i
        break

ans = n + pallin_idx
print(ans)
