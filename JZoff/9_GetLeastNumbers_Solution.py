class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        templist = []
        for ts in tinput:
            if not ts in templist:
                templist.append(ts)
        templist.sort()
        return templist[0:k]

if __name__ == '__main__':
    S = Solution()
    print(S.GetLeastNumbers_Solution([1,1,5,2,3,1,1], 3))