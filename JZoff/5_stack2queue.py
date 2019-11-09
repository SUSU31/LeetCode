class Solution:
    def __init__(self):
        self.eles = []
    def push(self, node):
        # write code here
        self.eles.append(node)
    def pop(self):
        # return xx
        t = self.eles[0]
        self.eles = self.eles[1:]
        return t

if __name__ == '__main__':
    S=Solution()
    S.push(1)
    S.push(2)
    print(S.pop())
    S.push(3)
    print(S.pop())
    print(S.pop())