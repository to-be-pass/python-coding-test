def solution(lst, search_lst):

    class Node:
        # 노드 생성자
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    # 이진 트리
    class BST:
        # 생성자
        # 첨에 트리는 루트 자리만 주어짐 
        def __init__(self):
            self.root = None

        # 넣기
        def insert(self, key):
            if not self.root:
                self.root = Node(key) # 이런식으로도 객체 생성함
            else:
                curr = self.root
                while 1:
                    if curr.key > key:
                        if curr.left:
                            curr = curr.left
                        else:
                            curr.left = Node(key)
                            break
                    else:
                        if curr.right:
                            curr = curr.right
                        else:
                            curr.right = Node(key)
                            break

        # 찾기 
        def search(self, k):
            curr = self.root
            while curr and curr.val != k:
                if k < curr.val:
                    curr = self.left # 이게 어딜 가리키는거? 
                else:
                    curr = self.right
            return curr
        
            

    bst = BST ()


    result = []

    for i in lst:
        bst.insert(i)
    
    for j in search_lst:
        if bst.search(j) == True:
            result.append(True)
        else:
            result.append(False)

    print(result)

    return result
