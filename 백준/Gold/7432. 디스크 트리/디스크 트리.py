# 디스크 트리
'''
트라이
insert, 구조 보여줄 수 있는 함수 구현

'''
import sys


# Trie 구조 구현
class Node():
    def __init__(self, key):
        self.key = key
        # 자식을 딕셔너리 형태로 가지고 있고, 자식의 이름이 key 역할을 함
        self.children = dict()


class Trie():
    def __init__(self):
        self.head = Node(None)

    # 추가
    def insert(self, string):
        curr_node = self.head

        for char in string:
            # 자식 노드에 해당하는게 없으면 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

    # 구조 보여주기
    def show(self, d, curr_node):  # d : 깊이
        # 깊이가 0 이라면 해당 node는 head
        if d == 0:
            curr_node = self.head

        # 정렬한 후 찾기
        for child in sorted(curr_node.children.keys()):
            print(' ' * d, child, sep="")
            # 재귀로 내려가면서 찾기
            self.show(d + 1, curr_node.children[child])


trie = Trie()

N = int(sys.stdin.readline())  # 디렉토리 경로 개수

for _ in range(N):
    # \ 로 구분하려면 \\ 써야함 왜?
    info = list(sys.stdin.readline().strip().split('\\'))   # 디렉토리 정보
    # print(info)
    trie.insert(info)

trie.show(0, None)