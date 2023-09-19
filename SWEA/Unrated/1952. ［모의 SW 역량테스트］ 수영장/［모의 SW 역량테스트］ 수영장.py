def swim(month, money):
    global min_v
    if min_v <= money:
        return

    if month > 12:
        if min_v > money:
            min_v = money

    else:
        swim(month+1, money+d*schedule[month-1])
        swim(month+1, money+m)
        swim(month+3, money+q)

T = int(input())
for tc in range(1, T+1):
    d, m, q, y = map(int,input().split())
    schedule = list(map(int, input().split()))

    min_v = y
    swim(1,0)
    print(f'#{tc} {min_v}')