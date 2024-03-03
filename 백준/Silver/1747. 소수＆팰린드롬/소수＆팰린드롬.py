# 소수 & 팰린드롬
import sys
import math


# 소수 판별(에라토스테네스의 체)
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


# 팰린드롬
def Palin(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


N = int(sys.stdin.readline())

while True:
    if isPrime(N) and Palin(N):
        print(N)
        break

    N += 1