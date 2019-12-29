class Solution:
    def maxArea(self, height) -> int:
        maxarea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            maxarea = max(maxarea, min(height[l],height[r])*(r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxarea


if __name__ == '__main__':
    S = Solution()
    h = [1,8,6,2,5,4,8,3,7]
    m = S.maxArea(h)
    print(m)

