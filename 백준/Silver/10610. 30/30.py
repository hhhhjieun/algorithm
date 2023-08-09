N = list(input())

# 0이 없다면 30의 배수가 될 수 없음
if '0' not in N:
    print('-1')

else:
    # 각 자리수의 합이 3의 배수가 아닐 때,
    total = 0
    for i in range(len(N)):
        total += int(N[i])
    if total % 3 != 0:
        print('-1')

    # 각 자리수의 합이 3의 배수일 때, 내림차순
    else:
        N.sort(reverse=True)
        result = ''.join(N)
        print(result)