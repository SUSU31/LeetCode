from JZoff.temp import TreeNode,BinaryTree
from logzero import logger

class Solution:
    def Convert(self, pRootOfTree):
        self.lastnode = None
        if pRootOfTree is not None:
            self.convertnode(pRootOfTree)
        while self.lastnode is not None and self.lastnode.left is not None:
            self.lastnode = self.lastnode.left
        return self.lastnode

    def convertnode(self, cur_root):
        if cur_root is None:
            return
        pnode = cur_root
        if pnode.left is not None:
            self.convertnode(pnode.left)
        pnode.left = self.lastnode
        if self.lastnode is not None:
            self.lastnode.right = pnode
        self.lastnode = pnode
        if pnode.right is not None:
            self.convertnode(pnode.right)
        return


if __name__ == '__main__':
    T1 = BinaryTree()
    a = [1, 2, 3, 4, 5]
    for t in a:
        T1.add(t)
    T1.pre_order_loop()
    S = Solution()
    t = S.Convert(T1.root)
    print('----------')
    while t is not None:
        print(t.val)
        t = t.right
