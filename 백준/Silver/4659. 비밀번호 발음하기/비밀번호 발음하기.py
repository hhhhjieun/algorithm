# 비밀번호 발음하기
'''
모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
'''
import sys

def condition1(pw):
    cnt = 0
    if 'a' in pw:
        cnt += 1
    if 'e' in pw:
        cnt += 1
    if 'i' in pw:
        cnt += 1
    if 'o' in pw:
        cnt += 1
    if 'u' in pw:
        cnt += 1
    return cnt

def condition2(pw):
    n = len(pw)
    result2 = True
    if n >= 3:
        for i in range(n-2):
            # 모음 3개
            if pw[i] in 'aeiou' and pw[i+1] in 'aeiou'and pw[i+2] in 'aeiou':
                result2 = False

            # 자음 3개
            if pw[i] not in 'aeiou' and pw[i+1] not in 'aeiou'and pw[i+2] not in 'aeiou':
                result2 = False

    return result2

def condition3(pw):
    n = len(pw)
    result3 = True
    if n >= 2:
        for i in range(n-1):
            if pw[i] == pw[i+1]:
                if pw[i] == 'e' or pw[i] == 'o':
                    continue
                else:
                    result3 = False
                    break
    return result3




while True:
    pw = sys.stdin.readline().strip()

    if pw == 'end':
        break

    ans = True

    # 모음(a,e,i,o,u) 하나를 반드시 포함
    result1 = condition1(pw)
    if result1 < 1:
        ans = False

    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    result2 = condition2(pw)
    if result2 is False:
        ans = False

    # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    result3 = condition3(pw)
    if result3 is False:
        ans = False

    if ans is True:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')