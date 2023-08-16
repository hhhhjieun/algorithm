import sys
cal = sys.stdin.readline().strip()

stack = [0] * len(cal)
postfix = ''
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

top = -1

for token in cal:
    if token not in '+-*/()':
        postfix += token

    else:
        # ')' 일때, '(' 까지 pop()
        if token == ')':
            while stack[top] != '(':
                postfix += stack[top]
                top -= 1
            top -= 1

        # 우선 순위가 높은 경우
        elif top == -1 or isp[stack[top]] < icp[token]:
            top += 1  # push
            stack[top] = token

        # 낮은 경우
        elif isp[stack[top]] >= icp[token]:
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1  # pop
            top += 1
            stack[top] = token

while top > -1:
    postfix += stack[top]
    top -= 1

print(postfix)