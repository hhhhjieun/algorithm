import sys
input = sys.stdin.readline


def draw_star(n, row, col, li):
    if n == 0:
        li[row][col] = '*'
    else:
        size = 5 ** (n - 1)
        # 1
        draw_star(n - 1, row, col + size * 2, li)
        # 2
        draw_star(n - 1, row + size, col + size * 2, li)
        # 3
        draw_star(n - 1, row + size * 2, col, li)
        draw_star(n - 1, row + size * 2, col + size, li)
        draw_star(n - 1, row + size * 2, col + size * 2, li)
        draw_star(n - 1, row + size * 2, col + size * 3, li)
        draw_star(n - 1, row + size * 2, col + size * 4, li)
        # 4
        draw_star(n - 1, row + size * 3, col + size, li)
        draw_star(n - 1, row + size * 3, col + size * 2, li)
        draw_star(n - 1, row + size * 3, col + size * 3, li)
        # 5
        draw_star(n - 1, row + size * 4, col + size, li)
        draw_star(n - 1, row + size * 4, col + size * 3, li)


N = int(input())

if N == 0:
    print('*')
else:
    size = 5 ** N
    star_matrix = [[' ' for _ in range(size)] for _ in range(size)]
    draw_star(N, 0, 0, star_matrix)

    for row in star_matrix:
        print(''.join(row))