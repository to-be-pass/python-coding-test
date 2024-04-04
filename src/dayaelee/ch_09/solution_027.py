class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while 1:
                if curr.val > key:
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

    def search(self, key):
        curr = self.root
        while curr and key != curr.val:
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        
        return curr
        
def solution(lst, search_lst):

    bst = BST()

    for key in lst:
        bst.insert(key)
    
    result = []

    for searchVal in search_lst:
        if bst.search(searchVal):
            result.append(True)
        else:
            result.append(False)

    return result
