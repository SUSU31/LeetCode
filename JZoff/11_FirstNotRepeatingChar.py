class Solution:
    def FirstNotRepeatingChar(self, s):
        first = []
        firstidx = []
        sec = []
        for i in range(0,len(s)):
            if not s[i] in first:
                first.append(s[i])
                firstidx.append(i)
            elif not s[i] in sec:
                sec.append(s[i])
        for i in range(0, len(first)):
            if not first[i] in sec:
                return firstidx[i]
        return -1

if __name__ == '__main__':
    S = Solution()
    print(S.FirstNotRepeatingChar('google'))