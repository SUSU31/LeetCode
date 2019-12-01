from JZoff.temp import TreeNode, BinaryTree

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot2 is None:
            return False
        if pRoot1 is None:
            return False
        if abs(pRoot1.val - pRoot2.val) < 1e-8:
            result = self.TreeI(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def TreeI(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False

        if not abs(pRoot1.val-pRoot2.val) < 1e-8:
            return False

        L = self.TreeI(pRoot1.left, pRoot2.left)
        R = self.TreeI(pRoot1.right, pRoot2.right)
        return L and R

if __name__ == '__main__':
        S = Solution()
        T1 = BinaryTree()
        T2 = BinaryTree()
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3]
        for t in a:
            T1.add(t)
        for t in b:
            T2.add(t)
        T1.pre_order_loop()
        T2.pre_order_loop()

        print(S.HasSubtree(T1.root, T2.root))
