from JZoff.temp import TreeNode, BinaryTree


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return
        # if root.left is None or root.right is None:
        #     return
        temp_n = root.left
        root.left = root.right
        root.right = temp_n
        self.Mirror(root.left)
        self.Mirror(root.right)
        return

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
        # T2.pre_order_loop()
        S.Mirror(T1.root)
        T1.pre_order_loop()

