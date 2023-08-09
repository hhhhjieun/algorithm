import sys

N = int(sys.stdin.readline())

# 빈 리스트(stack)
stack = []

for _ in range(N):
    command = list(sys.stdin.readline().split())

    # pop
    if command[0] == 'push':
        stack.append(command[1])
    # pop
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pops = stack.pop(-1)
            print(pops)
    # size
    elif command[0] == 'size':
        print(len(stack))
    # empty
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
