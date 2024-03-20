def solution(lst, search_lst):
    tree = BST()
    for value in lst:
        tree.insert(value)
    
    answer = []
    for value in search_lst:
        answer.append(tree.search(value))
    return answer


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        curr = self.root
        while curr:
            if curr.value > value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(value)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(value)
                    break
        
    def search(self, value):
        curr = self.root
        while curr:
            if curr.value == value:
                return True
            if curr.value > value:
                curr = curr.left
            else:
                curr = curr.right
        return False
