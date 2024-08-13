def solution(k, tangerine):

    answer = 0
    
    fruit_count = {}
    for fruit in tangerine:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1
    
    cnts = list(fruit_count.values())
    cnts.sort(reverse=True)
    
    current_sum = 0
    for i in range(len(cnts)):
        current_sum += cnts[i]
        if current_sum >= k:
            answer = i + 1
            break
    
    return answer

    
    for tmp in set(tangerine):
        cnts.append(tangerine.count(tmp))
    cnts.sort(key=lambda x:-x)
    
    i = 0
    while i < len(cnts):
        if sum(cnts[0:i+1]) < k:
            i += 1
        else:
            answer = i+1
            break
            
    return answer