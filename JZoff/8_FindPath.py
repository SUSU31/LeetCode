from JZoff.temp import BinaryTree, TreeNode

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        self.expectNumber = expectNumber
        if root is None:
            return []
        self.re = []
        self.find(root, 0, [])
        return self.re
    def find(self, root, tempsum, temp_list):
        tempsum += root.val
        temp_list.append(root.val)
        if root.left is None and root.right is None:
            if tempsum == self.expectNumber:
                l1 = []
                l1.extend(temp_list)
                self.re.append(l1)

        if root.left is not None:
            self.find(root.left, tempsum, temp_list)
        if root.right is not None:
            self.find(root.right, tempsum, temp_list)

        tempsum -= root.val
        temp_list.pop()



if __name__ == '__main__':
        S = Solution()
        T1 = BinaryTree()

        a = [10,5,12,4,7]

        for t in a:
            T1.add(t)

        T1.pre_order_loop()

        print('-----------')
        re = S.FindPath(T1.root, 22)
        print(re)
        # for r in re:
        #     for k in r:
        #         print(k.val)
        #     print('-----------')