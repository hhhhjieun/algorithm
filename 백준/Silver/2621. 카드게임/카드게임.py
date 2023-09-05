import sys

cards = [list(sys.stdin.readline().split()) for _ in range(5)]

colors = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
nums_li = []
nums = set()
for card in cards:
    colors[card[0]] += 1
    nums.add(int(card[1]))
    nums_li.append(int(card[1]))

scores = []
score = 0
# 색 확인(5장이 같을 때만 존재)
flag = True
for color in colors:
    if colors[color] == 5:
        flag = True
        # 숫자가 연속적
        result = True
        nums_li.sort()
        for i in range(1, 5):
            if nums_li[i] == nums_li[i-1] + 1:
                continue
            else:
                result = False
                break
        if result is True:
            score = 0
            score += (900 + max(nums_li))
            scores.append(score)
        # 아닌경우
        else:
            score = 0
            score += (600 + max(nums_li))
            scores.append(score)
            break

    else:
        flag = False

# 숫자 확인
num_li = list(nums)
num_li.sort()

# 5장일 경우
if len(num_li) == 5:
    seq = True
    for i in range(1, 5):
        if num_li[i] == num_li[i-1] + 1:
            seq = True
        else:
            seq = False
            break
    if seq is True:
        score = 0
        score += (500 + max(num_li))
        scores.append(score)
    else:
        score = 0
        score += (100 + max(num_li))
        scores.append(score)

elif len(num_li) == 2:
    score = 0
    # 4장,1장일 경우
    if nums_li.count(num_li[0]) == 4:
        score += (800 + num_li[0])
    elif nums_li.count(num_li[1]) == 4:
        score += (800 + num_li[1])
    # 3장, 2장일 경우
    elif nums_li.count(num_li[0]) == 3 and nums_li.count(num_li[1]) == 2:
        score += (num_li[0] * 10 + 700 + num_li[1])
    elif nums_li.count(num_li[1]) == 3 and nums_li.count(num_li[0]) == 2:
        score += (num_li[1] * 10 + 700 + num_li[0])

    scores.append(score)

elif len(num_li) == 3:
    score = 0
    # 3장, 1장, 1장
    if nums_li.count(num_li[0]) == 3:
        score += (400 +num_li[0])
    elif nums_li.count(num_li[1]) == 3:
        score += (400 +num_li[1])
    elif nums_li.count(num_li[2]) == 3:
        score += (400 +num_li[2])

    # 2장, 2장
    elif nums_li.count(num_li[0]) == 2 and nums_li.count(num_li[1]) == 2:
        score += (max(num_li[0], num_li[1]) * 10 + 300 + min(num_li[0], num_li[1]))
    elif nums_li.count(num_li[0]) == 2 and nums_li.count(num_li[2]) == 2:
        score += (max(num_li[0], num_li[2]) * 10 + 300 + min(num_li[0], num_li[2]))
    elif nums_li.count(num_li[1]) == 2 and nums_li.count(num_li[2]) == 2:
        score += (max(num_li[1], num_li[2]) * 10 + 300 + min(num_li[1], num_li[2]))

    scores.append(score)

elif len(num_li) == 4:
    if nums_li.count(num_li[0]) == 2:
        score += (200 + num_li[0])
    elif nums_li.count(num_li[1]) == 2:
        score += (200 + num_li[1])
    elif nums_li.count(num_li[2]) == 2:
        score += (200 + num_li[2])
    elif nums_li.count(num_li[3]) == 2:
        score += (200 + num_li[3])
    scores.append(score)


print(max(scores))
