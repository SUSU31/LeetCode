class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 0:
            return None
        temp_max = array[0]
        temp_sum = 0
        for num in array:
            if temp_sum + num <= num:
                temp_sum = num
            else:
                temp_sum += num
            if temp_sum >= temp_max:
                temp_max = temp_sum
        return temp_max


if __name__ == '__main__':
    S = Solution()
    print(S.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))
