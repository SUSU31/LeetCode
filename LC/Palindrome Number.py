class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    S = Solution()
    t = S.isPalindrome(0)
    print(t)
