N = int(input())
cmd = [input() for _ in range(N)]

# 출력할 패턴
pattern = ''
if N == 1:
    print(cmd[0])
else:
    for j in range(len(cmd[0])):
        result = True
        for i in range(N - 1):
            if cmd[i][j] == cmd[i + 1][j]:
                continue
            else:
                result = False
                break

        if result is True:
            pattern += cmd[i][j]
        else:
            pattern += '?'

    print(pattern)