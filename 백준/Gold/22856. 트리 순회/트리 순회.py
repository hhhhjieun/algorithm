import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(n + 1)]
cnt = 0
ans = 0
finish = 0

for i in range(n):
    root, left, right = list(map(int, sys.stdin.readline().rstrip().split()))
    if left == -1: left = 0
    if right == -1: right = 0
    tree[root].append(left)
    tree[root].append(right)

def max_right(node):
    global finish
    if tree[node][0]: max_right(tree[node][0])
    finish = node
    if tree[node][1]: max_right(tree[node][1])

def inorder(node):
    global cnt
    global ans
    if node == finish:
        ans = cnt
    if tree[node][0]:
        cnt += 1
        inorder(tree[node][0])
        cnt += 1
        if node == finish:
            ans = cnt
    if tree[node][1]:
        cnt += 1
        inorder(tree[node][1])
        cnt += 1

max_right(1)
inorder(1)
print(ans)