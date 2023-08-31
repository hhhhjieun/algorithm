
import sys
from collections import deque


def plus_A(s1):
    s1.append('A')
    return s1


def plus_B_reverse(s2):
    s2.append('B')
    s2.reverse()
    return s2


S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())
result = 0

q = deque()
q.append(T)

while q:
    t = q.popleft()

    for i in range(1, 3):
        if i == 1:
            t1 = t[:]
            if len(t1) >= 1:
                if t1[0] == 'B':
                    t1.reverse()
                    t1.pop()
                    q.append(t1)
                    if t1 == S:
                        result = 1
                        break
        else:
            t2 = t[:]
            if len(t2) >= 1:
                if t2[-1] == 'A':
                    t2.pop()
                    q.append(t2)
                    if t2 == S:
                        result = 1
                        break



print(result)