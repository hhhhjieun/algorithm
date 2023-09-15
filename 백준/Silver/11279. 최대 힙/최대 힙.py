import sys

N = int(sys.stdin.readline())
heap = [0]*100001
last = 0


def heap_add(last):
    c = last
    p = c// 2
    if p < 1:
        return
    else:
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            heap_add(p)


def heap_del(p):
    c = p*2
    if c > last:
        return
    else:
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            heap_del(c)


for i in range(N):
    X = int(sys.stdin.readline())
    if X:
        last += 1
        heap[last] = X
        heap_add(last)

    else:
        print(heap[1])
        if last:
            heap[1] = 0
            heap[1], heap[last] = heap[last], heap[1]
            last -= 1
            p = 1
            heap_del(p)