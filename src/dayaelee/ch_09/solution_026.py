def pre(nodes, idx):
    if idx < len(nodes):
        ret = str(nodes[idx]) + " "
        ret += pre(nodes, idx * 2 + 1)
        ret += pre(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def inorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def postorder(nodes, idx):
    if idx < len(nodes):
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
def preorder(nodes, cnt) :
    if len(nodes) > cnt:
        #print(nodes[cnt])
        result = str(nodes[cnt]) + " "
        result += preorder(nodes, (cnt * 2) + 1)
        result += preorder(nodes, (cnt * 2 ) + 2)
        return result
    else:
        return ""

def inorder(nodes, cnt) :
    if len(nodes) > cnt:
        result = inorder(nodes, (cnt * 2) + 1)
        result += str(nodes[cnt]) + " "
        result += inorder(nodes, (cnt *2) + 2)
        return result
    else:
        return "" 

def postorder(nodes, cnt) :
    if len(nodes) > cnt:
        result = postorder(nodes, (cnt * 2) + 1)
        result += postorder(nodes, (cnt * 2 ) + 2)
        result += str(nodes[cnt]) + " "
        return result
    else:
        return ""

def solution(nodes):
    print('hi')
    return [
        pre(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1],
    ]
    # 전위, 중위, 후위 순회 결과 계산
    # 노드 리스트와 루트 노드의 인덱스를 매개변수로 각각 호출
    
    return [preorder(nodes, 0)[:-1], inorder(nodes, 0)[:-1], postorder(nodes, 0)[:-1] ]


    
