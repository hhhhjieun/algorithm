'''
1 : N극 -> 밑으로
2 : S극 -> 위로
table : 100 x 100

풀이방법
: 행을 우선 탐색하면서 자석만 list로 모아서 1,2가 연속으로 나오면 교착상태
'''

T = 10

for test_case in range(1, T + 1):
    table_length = int(input())  # table 길이
    # table 초기 상태
    table = [list(map(int, input().split())) for _ in range(100)]
    deadlocking = 0  # 교착 상태

    # 행 우선 탐색
    for j in range(100):
        magnetic = []
        for i in range(100):
            if table[i][j] != 0:
                magnetic.append(table[i][j])

        for k in range(len(magnetic)-1):
            if magnetic[k] == 1 and magnetic[k+1] == 2:
                deadlocking += 1

    print(f'#{test_case} {deadlocking}')
