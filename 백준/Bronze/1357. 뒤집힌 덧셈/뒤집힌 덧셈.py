# 뒤집힌 덧셈
X, Y = map(str, input().split())

Rev_X = ''
for i in X:
    Rev_X = i + Rev_X

Rev_Y = ''
for j in Y:
    Rev_Y = j + Rev_Y

result = int(Rev_X) + int(Rev_Y)

ans = ''
for k in str(result):
    ans = k + ans

print(int(ans))