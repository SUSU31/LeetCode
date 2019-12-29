class Solution:
    def nextPermutation(self, nums: list) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        flag2 = 0
        temp = []
        for i in range(len(nums)-1, 0, -1):
            temp.append(nums[i])
            if nums[i] > nums[i-1]:
                flag = 1
                for j in range(i, len(nums)):
                    if nums[i-1] >= nums[j]:
                        temp[len(nums)-j] = nums[i-1]
                        nums[i - 1] = nums[j-1]
                        nums[i:] = temp
                        flag2 = 1
                        break
                if flag2 == 0:
                    temp[0] = nums[i-1]
                    nums[i - 1] = nums[-1]
                    nums[i:] = temp
                break

        if flag == 0:
            nums[-1] = nums[0]
            nums[:-1] = temp

        return nums


if __name__ == '__main__':
    S=Solution()
    print(S.nextPermutation([3,2,1]))

