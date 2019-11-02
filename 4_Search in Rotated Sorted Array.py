class Solution:
    # def search(self, nums: list, target: int) -> int:
    def search(self, nums: list, target: int) -> int:
        if not nums: return -1
        i, j = 0, len(nums)-1
        while i<j:
            m = (i+j) // 2
            if nums[m]< nums[j]:
                j = m
            else:
                i = m+1

        p = i
        if target == nums[0]: return 0
        if not p == 0 and target > nums[0]:
            i, j = 0, p - 1
        else:
            i, j = p, len(nums) - 1
        while i<=j:

            m = (i+j) // 2
            if nums[m]>target:
                j = m-1
            elif nums[m]<target:
                i=m+1
            else:
                return m
        return -1

if __name__ == '__main__':
    S=Solution()
    print(S.search([1,3], 3))

