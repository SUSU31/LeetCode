class Solution:
    def isValid(self, s: str) -> bool:
        A = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                A.append(c)
            elif len(A) == 0:
                return False
            elif c == ')':
                if not A.pop() == '(':
                    return False
            elif c == ']':
                if not A.pop() == '[':
                    return False
            elif c == '}':
                if not A.pop() == '{':
                    return False
        if len(A) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    S = Solution()
    print(S.isValid('(){()}[]'))




