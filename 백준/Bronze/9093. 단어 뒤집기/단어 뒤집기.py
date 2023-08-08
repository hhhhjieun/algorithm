T = int(input())

for test_case in range(T):
    sen = list(input().split())

    for i in range(len(sen)):
        test = ''
        for j in range(len(sen[i])):

            test = sen[i][j] + test
        print(test, end=' ')