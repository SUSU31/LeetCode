from JZoff.temp import BinaryTree, TreeNode

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        t_list = []
        p_list = []
        if root is None:
            return []
        t_list.append(root)

        while not len(t_list) == 0:
            node = t_list[0]
            p_list.append(node.val)
            if not node.left is None:
                t_list.append(node.left)
            if not node.right is None:
                t_list.append(node.right)
            t_list.pop(0)
        return p_list


if __name__ == '__main__':
        S = Solution()
        T1 = BinaryTree()

        a = [1, 2, 3, 4, 5]

        for t in a:
            T1.add(t)

        T1.pre_order_loop()


        print(S.PrintFromTopToBottom(T1.root))
