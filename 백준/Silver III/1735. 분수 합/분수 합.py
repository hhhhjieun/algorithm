# 분수 합
import sys
import math

A1, B1 = map(int, sys.stdin.readline().split())
A2, B2 = map(int, sys.stdin.readline().split())

N = math.gcd((A1 * B2 + B1 * A2), B1 * B2)

print((A1 * B2 + B1 * A2) // N, (B1 * B2) // N)


