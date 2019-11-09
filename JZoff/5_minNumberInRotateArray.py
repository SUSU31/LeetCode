class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0: return 0
        i, j = 0, len(rotateArray) - 1
        while i<j:
            m = (i+j) // 2
            if rotateArray[j] < rotateArray[m]:
                i = m+1
            else:
                j = m
        return rotateArray[i]

if __name__ == '__main__':
    S=Solution()
    print(S.minNumberInRotateArray([5,6,7,1,2,3]))
