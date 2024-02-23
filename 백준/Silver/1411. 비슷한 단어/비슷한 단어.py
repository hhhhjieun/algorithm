# 비슷한 단어
import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        word1, word2 = words[i], words[j]

        check1 = [0] * 26
        check2 = [0] * 26

        n = len(word1)
        tmp = True

        for k in range(n):
            alphabet1 = ord(word1[k]) - ord('a')
            alphabet2 = ord(word2[k]) - ord('a')

            if check1[alphabet1] == 0 and check2[alphabet2] == 0:
                check1[alphabet1] = word2[k]
                check2[alphabet2] = word1[k]
            elif check1[alphabet1] != word2[k]:
                tmp = False
                break

        if tmp:
            cnt += 1

print(cnt)
