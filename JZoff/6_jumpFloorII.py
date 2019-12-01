class Solution:
    def jumpFloorII(self, number):
        nums = [0, 1, 2]
        for i in range(3, number+1):
            temp = 0
            for j in range(1, i):
                temp += nums[i-j]
            nums.append(temp+1)

        return nums[number]


if __name__ == '__main__':
    S=Solution()
    print(S.jumpFloorII(4))

