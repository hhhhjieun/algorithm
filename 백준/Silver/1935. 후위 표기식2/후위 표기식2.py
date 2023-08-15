import sys
N = int(sys.stdin.readline())

cal = list(sys.stdin.readline().strip())

# 피연산자 값 받기
alpha = [0] * N

for i in range(N):
    alpha[i] = int(sys.stdin.readline())

# 계산
stack = []

for char in cal:
    if char not in '+-*/':
        stack.append(alpha[ord(char)-ord('A')])

    elif char in '+-*/':
        n2 = stack.pop()
        n1 = stack.pop()

        if char == '+':
            result = n1 + n2

        elif char == '-':
            result = n1 - n2

        elif char == '*':
            result = n1 * n2

        else:
            result = n1 / n2

        stack.append(result)

ans = stack.pop()
print("{:.2f}".format(ans))