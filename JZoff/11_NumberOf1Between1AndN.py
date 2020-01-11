class Solution:
    def NumberOf1Between1AndN_Solution(self, n):

        return self.NomOf1(str(n))

    def NomOf1(self, str_n):
        if len(str_n) == 1:
            if str_n == '0':
                return 0
            else:
                return 1
        firstnum = 0
        if int(str_n[0]) == 1:
            firstnum = int(str_n[1:]) + 1
        elif int(str_n[0]) > 1:
            firstnum = pow(10, len(str_n)-1)

        othernum = pow(10, len(str_n)-2) * (len(str_n)-1) * int(str_n[0])

        next_str = '0'
        for i in range(1, len(str_n)):
            if not str_n[i] == '0':
                next_str = str_n[i:]
                break
        recnum = self.NomOf1(next_str)

        return firstnum + othernum + recnum

if __name__ == '__main__':
    S = Solution()
    print(S.NumberOf1Between1AndN_Solution(55))
