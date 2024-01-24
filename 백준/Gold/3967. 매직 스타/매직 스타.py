# 매직스타
def check(star):
    if (ord(star[0][4]) - ord('A') + 1) + (ord(star[1][3]) - ord('A') + 1) + (ord(star[2][2]) - ord('A') + 1) + (
            ord(star[3][1]) - ord('A') + 1) != 26:
        return False
    if (ord(star[0][4]) - ord('A') + 1) + (ord(star[1][5]) - ord('A') + 1) + (ord(star[2][6]) - ord('A') + 1) + (
            ord(star[3][7]) - ord('A') + 1) != 26:
        return False
    if (ord(star[1][1]) - ord('A') + 1) + (ord(star[1][3]) - ord('A') + 1) + (ord(star[1][5]) - ord('A') + 1) + (
            ord(star[1][7]) - ord('A') + 1) != 26:
        return False
    if (ord(star[3][1]) - ord('A') + 1) + (ord(star[3][3]) - ord('A') + 1) + (ord(star[3][5]) - ord('A') + 1) + (
            ord(star[3][7]) - ord('A') + 1) != 26:
        return False
    if (ord(star[4][4]) - ord('A') + 1) + (ord(star[3][3]) - ord('A') + 1) + (ord(star[2][2]) - ord('A') + 1) + (
            ord(star[1][1]) - ord('A') + 1) != 26:
        return False
    if (ord(star[4][4]) - ord('A') + 1) + (ord(star[3][5]) - ord('A') + 1) + (ord(star[2][6]) - ord('A') + 1) + (
            ord(star[1][7]) - ord('A') + 1) != 26:
        return False

    return True


def DFS(idx, n, star, visited, v, cnt):
    if n == cnt:
        if check(star):
            for row in star:
                print(''.join(row))
            exit(0)

    for i in range(12):
        if visited[i]:
            continue
        visited[i] = True
        star[v[idx][0]][v[idx][1]] = chr(i + ord('A'))
        DFS(idx + 1, n + 1, star, visited, v, cnt)
        star[v[idx][0]][v[idx][1]] = 'x'
        visited[i] = False



star = [[' '] * 9 for _ in range(5)]
visited = [False] * 13
cnt = 0
# x 위치 저장
v = []

for i in range(5):
    row = input()
    for j in range(9):
        star[i][j] = row[j]

        if 'A' <= star[i][j] <= 'L':
            visited[ord(star[i][j]) - ord('A')] = True
        elif star[i][j] == 'x':
            v.append((i, j))
            cnt += 1

DFS(0, 0, star, visited, v, cnt)
