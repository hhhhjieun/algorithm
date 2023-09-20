N = int(input())
arr = list(map(int,input().split()))
max_e = 0
def energy(N, E):
    global max_e
    if N == 2:
        if max_e < E:
            max_e = E
        return

    for i in range(1,N-1):
        en = arr[i-1]*arr[i+1]
        n = arr.pop(i)
        energy(N-1, E+en)
        arr.insert(i,n)

energy(N, 0)
print(max_e)