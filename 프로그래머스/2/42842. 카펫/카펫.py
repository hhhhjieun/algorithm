
def solution(brown, yellow):
    answer = []
    
    w = 0
    h = 0
    
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            tmp_w, tmp_h = yellow//i, i
            
            tmp = (tmp_w + 2) * 2 + (tmp_h * 2)
            if tmp == brown:
                w, h = tmp_w + 2, tmp_h + 2
            else:
                continue
    
    answer = [w, h]
            
    return answer