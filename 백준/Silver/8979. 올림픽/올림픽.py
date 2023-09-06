N, country = map(int, input().split())
arr = []
for _ in range(N):
    num, gold, silver, bronze = map(int, input().split())
    arr.append([gold, silver, bronze])
    if num == country:
        me = [gold, silver, bronze]

arr.sort(reverse=True)

for i in range(N):
    if arr[i] == me:
        rank = i+1
        break

print(rank)