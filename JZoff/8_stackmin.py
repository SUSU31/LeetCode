# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.elems = []
        self.mine = []
    def push(self, node):
        self.elems.append(node)
        if len(self.mine) == 0:
            self.mine.append(node)
        elif self.mine[-1] > node:
            self.mine.append(node)
        else:
            self.mine.append(self.mine[-1])
    def pop(self):
        if len(self.elems) == 0:
            return None
        pope = self.elems[-1]
        if len(self.elems) == 1:
            self.elems = []
            self.mine = []
        else:
            self.elems = self.elems[:-1]
            self.mine = self.mine[:-1]
        return pope
    def top(self):
        if len(self.elems) == 0:
            return None
        else:
            return self.elems[-1]
    def min(self):
        return self.mine[-1]


if __name__ == '__main__':
    S = Solution()
    S.push(2)
    S.push(3)
    S.push(1)
    print(S.min())
    print(S.top())
    print(S.min())
    print(S.pop())
    print(S.min())
    print(S.pop())
    print(S.min())

