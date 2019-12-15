class Solution:
    def IsPopOrder(self, pushV, popV):
        pushV = list(pushV)
        popV = list(popV)
        if len(popV) == 1:
            if popV[1] == pushV[1]:
                return True
            else:
                return False
        for i in range(1, len(popV)):
            idx = pushV.index(popV[i-1])
            pushV.remove(popV[i-1])
            idx2 = pushV.index(popV[i])
            if idx2 < idx - 1:
                return False
        return True


if __name__ == '__main__':
    S = Solution()
    print(S.IsPopOrder([1,2,3,4,5],[4,3,5,1,2]))