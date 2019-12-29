class Solution:
    def intToRoman(self, num: int) -> str:
        map = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        d_num=[1000, 500, 100, 50, 10, 5]
        p = [0] * len(d_num)

        flags = ['']*len(d_num)
        for i in range(len(d_num)):
            p[i] = num//d_num[i]
            num -= p[i]*d_num[i]
            if i == 0 and not num // 900 == 0:
                flags[i] = 'CM'
                num -= 900
            elif i == 1 and not num // 400 == 0:
                flags[i] = 'CD'
                num -= 400
            elif i == 2 and not num // 90 == 0:
                flags[i] = 'XC'
                num -= 90
            elif i == 3 and not num // 40 == 0:
                flags[i] = 'XL'
                num -= 40
            elif i == 4 and not num // 9 == 0:
                flags[i] = 'IX'
                num -= 9
            elif i == 5 and not num // 4 == 0:
                flags[i] = 'IV'
                num -= 4

        str1 = ''
        for i in range(len(d_num)):
            str1 += map[d_num[i]]*p[i] + flags[i]
        str1 += map[1]*num
        return str1


if __name__ == '__main__':
    S = Solution()
    s1 = S.intToRoman(1994)
    print(s1)


