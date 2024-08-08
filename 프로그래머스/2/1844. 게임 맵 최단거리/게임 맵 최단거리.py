from collections import deque 

def findway(start_x, start_y , maps):
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    q = deque([(start_y, start_x, 1)])
    visited = set([(start_y, start_x)])
    
    n, m = len(maps), len(maps[0])
    
    while q:
        i, j, dist = q.popleft()
        
        if i == n - 1 and j == m - 1:
            return dist
        
        for d in range(4):
            ni, nj = i + dy[d], j + dx[d]
            
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and  (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((ni, nj, dist + 1))
                
    return -1


def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])

    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        answer = -1
        
    else:    
        # bfs
        answer = findway(0, 0, maps)

    return answer

