class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        p1 = 0
        p2 = len(nums) - 1
        while p1<=p2:
            mid = (p1+p2) // 2
            if nums[mid] > target:
                p2 = mid - 1
            elif nums[mid] < target:
                p1 = mid + 1
            else:
                break
        if p1<=p2:
            k1, k2 = mid, mid
            for i in range(mid, -1, -1):
                if nums[i] == target:
                    k1 = i
                else:
                    break
            for i in range(mid, len(nums)):
                if nums[i] == target:
                    k2 = i
                else:
                    break
            re = [k1, k2]
        else:
            re = [-1, -1]
        return re



if __name__ == '__main__':
    S= Solution()
    print(S.searchRange([1], 1))