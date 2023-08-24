import sys

dwarfs = []
for _ in range(9):  # 아홉 난쟁이
    dwarf = int(sys.stdin.readline())
    dwarfs.append(dwarf)

n = 9
result = []  # 가능한 정답

# 부분집합
for i in range(1 << n):
    arr = []
    total = 0
    for j in range(n):
        if i & (1 << j):
            arr.append(dwarfs[j])
            total += dwarfs[j]

    # 일곱난장이의 키 합 = 100
    if len(arr) == 7:
        if total == 100:
            result.append(arr)

# 키를 오름차순

result[0].sort()

for num in result[0]:
    print(num)