class Solution:
    def f(self, s1, s2):
        out_s = []
        for ch1 in s1:
            for ch2 in s2:
                out_s.append(ch1+ch2)
        return out_s

    def letterCombinations(self, digits: str) -> list:
        str_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6':'mno',
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return ['']
        s1 = [ch for ch in str_map[digits[0]]]
        if len(digits) == 1:
            return s1
        digits = digits[1:]
        for ch in digits:
            s2 = [c for c in str_map[ch]]
            s1 = self.f(s1, s2)

        return s1

if __name__ == '__main__':
    # S = Solution()
    # s1 = S.letterCombinations("23456789")
    # print(s1)
    ans = []
    A = ['()']
    B = ['({)']
    ans.append("".join(A))
    ans.append("".join(B))
    print(ans)
