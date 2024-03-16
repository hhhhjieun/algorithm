# 2251번: 물통
a,b,c = map(int,input().split())

ans = []

from collections import deque

q = deque()
q.append([0,0,c])
check = [[0] * 201 for i in range(201)]
ans = [0 for i in range(201)]

def bfs():
    while q:
        x,y,z = q.popleft()

        if check[x][y] == 1: # 이미 했었떤 조합이면 pass
            continue

        check[x][y] = 1 # flag용도

        if x == 0: # 문제에서 요구한 조건
            ans[z] = 1

        # A->B
        if x+y > b: # a->b로 옮기는데 b에서 넘쳐남
            q.append([x+y-b,b,z])
        else: # a->b로 옮기는데 b를 다 못채움
            q.append([0,x+y,z])
        
        # A->C
        if x+z > c: # A->C로 옮기는데 C에서 넘쳐남
            q.append([x+z-c,y,c])
        else: # A->C로 옮기는데 C를 다 못채움
            q.append([0,y,x+z])

        # B->C    
        if y+z > c: # B->C로 옮기는데 C에서 넘쳐남
            q.append([x,y+z-c,c])
        else: # B->C로 옮기는데 C를 다 못채움
            q.append([x,0,y+z])

        # B->A
        if y+x > a: # B->A로 옮기는데 A에서 넘쳐남
            q.append([a,y+x-a,z])
        else: # B->A로 옮기는데 A를 다 못채움
            q.append([y+x,0,z])

        # C->A
        if z+x > a: # C->A로 옮기는데 A에서 넘쳐남
            q.append([a,y,z+x-a])
        else: # C->A로 옮기는데 A를 다 못채움
            q.append([x+z,y,0])

        # C->B
        if z+y > b: # C->B로 옮기는데 B에서 넘쳐남
            q.append([x,b,z+y-b])
        else: # C->B로 옮기는데 B를 다 못채움
            q.append([x,z+y,0])

bfs()
for i in range(201):
    if ans[i]:
        print(i,end=' ')