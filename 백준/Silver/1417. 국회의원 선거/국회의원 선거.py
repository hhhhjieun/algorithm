import sys

N = int(sys.stdin.readline())  # 후보자 수
candidate = list(int(sys.stdin.readline()) for _ in range(N))

cnt = 0

if candidate[0] != max(candidate):
    while candidate[0] != max(candidate):
        for i in range(1, N):
            if candidate[i] == max(candidate):
                candidate[i] -= 1
                candidate[0] += 1
                cnt += 1
                break

    else:
        if candidate.count(max(candidate)) > 1:
            while candidate.count(max(candidate)) != 1:
                for i in range(1, N):
                    if candidate[i] == max(candidate):
                        candidate[i] -= 1
                        candidate[0] += 1
                        cnt += 1
                        break

else:
    if candidate.count(max(candidate)) > 1:
        while candidate.count(max(candidate)) != 1:
            for i in range(1, N):
                if candidate[i] == max(candidate):
                    candidate[i] -= 1
                    candidate[0] += 1
                    cnt += 1
                    break


print(cnt)