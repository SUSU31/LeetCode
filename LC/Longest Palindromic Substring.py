import numpy as np


class Solution:
    def longestPalindrome(self, s: str) -> str:
       if len(s) == 0:
           return ''
       ms = s[0]
       for i in range(0, len(s)):
           for j in range(len(s), i, -1):
               if len(ms) >= j-i+1:
                   break
               if s[i:j] == s[i:j][::-1]:
                   ms = s[i:j]
       return ms


if __name__ == '__main__':
    S = Solution()
    s1 = S.longestPalindrome('ccc')
    print(s1)
