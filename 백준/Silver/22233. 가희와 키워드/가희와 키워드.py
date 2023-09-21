import sys   
input = sys.stdin.readline  



N, M = map(int, input().split())  
cnt = 0  
words = dict()  
for i in range(N):  
    words[input().rstrip()] = 1  
    cnt += 1  

for i in range(M):  
    using = [*map(str, input().rstrip().split(','))]  
    for j in using:  
        if words.get(j):  
            cnt -= 1  
            del words[j]  
    print(cnt)