class Solution:
    def Power(self, base, exponent):
        if base == 0 and exponent == 0:
            return 0
        temp = 1
        exp = exponent
        if exponent < 0:
            exp = -exponent
        for i in range(0, exp):
            temp = temp*base
        if exponent < 0:
            temp = 1/temp

        return temp

if __name__ == '__main__':
    S=Solution()
    print(S.Power(2, -3))