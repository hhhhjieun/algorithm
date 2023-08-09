S = input()

n = len(S)
# 생성된 부분 문자열을 넣을 빈 세트
test_set = set()

# 부분 문자열의 길이는 1부터 len(S)까지
for i in range(n+1):
    for j in range(i, n+1):
        test_set.add(S[i:j])


# 세트 개수
result = len(list(test_set))
print(result-1)