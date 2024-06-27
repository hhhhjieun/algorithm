def solution(sizes):
    answer = 0
    
    for size in sizes:
        size.sort()
    
    w = 0 
    h = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] > w:
            w = sizes[i][0]
        
        if sizes[i][1] > h:
            h = sizes[i][1]

    answer = w * h
    
    return answer

