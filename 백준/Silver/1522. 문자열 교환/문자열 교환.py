# 문자열 교환
'''
문자열은 원형 -> 처음과 끝은 서로 인접
원형리스트 처럼 만들기
b 개수만큼 잘라서 그 안에 a 몇개 있는가
최소일때 찾기
'''
import sys

s = sys.stdin.readline().strip()
n = len(s)
b_cnt = s.count('b')


s += s[0:n-1]
cnt = 999999

for j in range(n):
    a_check = s[j:(j+b_cnt)]
    a_cnt = a_check.count('a')
    cnt = min(cnt, a_cnt)

print(cnt)
