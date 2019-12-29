class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(haystack) == 0:
            return -1
        idx = -1
        for i in range(0,len(haystack)):
            if needle[0] == haystack[i]:
                idx = i
                for j in range(0, len(needle)):
                    if i+j > len(haystack)-1:
                        idx = -1
                        break
                    if not needle[j] == haystack[i+j]:
                        idx = -1
                        break
            if not idx == -1:
                break

        return idx


if __name__ == '__main__':
    S= Solution()
    print(S.strStr("a", 'a'))