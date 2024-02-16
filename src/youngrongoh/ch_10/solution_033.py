def solution(k, operations):
    s = custom_set(k)
    for o in operations:
        if o[0] == 'u':
            s.union(o[1], o[2])
    return s.count()

class custom_set:
    def __init__(self, k):
        self.tree = [x for x in range(k)]

    def find(self, x):
        if x == self.tree[x]:
            return x
        else:
            return self.find(self.tree[x])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x >= root_y:
            self.tree[root_y] = root_x
        else:
            self.tree[root_x] = root_y
    
    def count(self):
        c = 0
        for i in range(len(self.tree)):
            if i == self.tree[i]:
                c += 1
        return c