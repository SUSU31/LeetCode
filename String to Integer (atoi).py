class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip(' ')
        if len(str) == 0:
            return 0
        sign = 1
        t = 0
        if str[0] == '+':
            sign = 1
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]
        for char in str:
            if 47 < ord(char) < 58:
                t = t * 10 + int(char)
            else:
                break
        t = sign * t
        if t < -pow(2, 31):
            t = -pow(2, 31)
        if t > pow(2, 31) - 1:
            t = pow(2, 31) - 1
        return t

if __name__ == '__main__':
    S = Solution()
    t = S.myAtoi('  -4193 with words')
    print(t)