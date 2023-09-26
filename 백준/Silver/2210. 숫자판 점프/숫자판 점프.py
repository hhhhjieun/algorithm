arr = [list(map(str, input().split())) for _ in range(5)]
size = 6
jump_num = set()


def jump(x, i,j, cnt):
    if cnt == size:
        jump_num.add(x)
        return

    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni <5 and 0<= nj <5:
            jump(x + str(arr[ni][nj]),ni,nj, cnt+1)

for i in range(5):
    for j in range(5):
        x = arr[i][j]
        jump(x, i, j, 1)

print(len(jump_num))