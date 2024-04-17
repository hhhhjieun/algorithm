import sys
input=sys.stdin.readline

N,M=map(int,input().split())
L=list(map(int,input().split()))

dp=[0]*(N+1)
for i in range(M):
    a,b,k=map(int,input().split())
    dp[a-1]+=k ; dp[b]-=k

for i in range(1,N+1):
    dp[i]+=dp[i-1]

for i in range(N):
    L[i]+=dp[i]

print(*L)