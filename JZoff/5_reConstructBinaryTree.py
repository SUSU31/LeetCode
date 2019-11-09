class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0 or len(tin) == 0: return None
        root = TreeNode(pre[0])
        for i in range(0, len(tin)):
            if pre[0] == tin[i]:
                root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
                root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

def pre(L, root):
    if root is not None:
        L.append(root.val)
        L = pre(L, root.left)
        L = pre(L, root.right)
    return L

if __name__ == '__main__':
    S=Solution()
    t = S.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
    print(t.right.val)
    L=[]
    L=pre(L, t)
    print(L)
