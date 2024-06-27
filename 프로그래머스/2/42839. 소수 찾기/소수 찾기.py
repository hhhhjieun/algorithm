from itertools import permutations

def solution(numbers):
    answer = 0
    
    ans = set()

    for i in range(1, len(numbers)+1):
        for number in list(permutations(numbers, i)):
            tmp = ''
            for j in range(len(number)):
                tmp += number[j]
            ans.add(int(tmp))

    
    for num in ans:
        if is_prime(num):
            answer += 1
            
    
    return answer

def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
        
    return True
