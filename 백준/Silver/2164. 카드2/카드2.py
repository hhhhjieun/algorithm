import sys
from collections import deque
N = int(sys.stdin.readline())

card = deque([i for i in range(1, N+1)])

while len(card) != 1:
    # 버리기
    card.popleft()
    # 뒤로보내기
    if len(card) == 1:
        break
    else:
        card.append(card.popleft())

print(card[0])