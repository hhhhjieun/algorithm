# 좋은수열

def choose(result, count):
    for i in range(1, count//2+1):
        if str(result)[count-i:] == str(result)[count-2*i:count-i]:
            return
    if count == N:
        print(result)
        exit(0)
    for i in range(1, 4):
        temp = result * 10 + i
        choose(temp, count+1)


N = int(input())
choose(0, 0)