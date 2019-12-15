from JZoff.temp import BinaryTree, TreeNode

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        else:
            return self.VerifySquenceOfBST1(sequence)

    def VerifySquenceOfBST1(self, sequence):
        if len(sequence) == 0:
            return True
        root = sequence[-1]
        f = 0
        k = -1
        for i in range(len(sequence)-1):
            if sequence[i] > root:
                f = 1
                k = i
            if f == 1 and sequence[i] < root:
                return False
        if k == 0:
            left = []
            right = sequence[:-1]
        elif k == -1:
            left = sequence[:-1]
            right = []
        else:
            left = sequence[:k]
            right = sequence[k:-1]

        return self.VerifySquenceOfBST1(left) and self.VerifySquenceOfBST1(right)


if __name__ == '__main__':
    S = Solution()
    print(S.VerifySquenceOfBST([7,4,6,5]))