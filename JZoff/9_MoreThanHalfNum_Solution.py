class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dict = {}
        for num in numbers:
            if not num in dict:
                dict[num] = 1
            else:
                dict[num] += 1
            if dict[num] > len(numbers)/2:
                return num
        return 0

if __name__ == '__main__':
    S = Solution()
    print(S.MoreThanHalfNum_Solution([1,1,5,2,3,1,1]))