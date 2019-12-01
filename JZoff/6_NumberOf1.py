class Solution:
    def NumberOf1(self, n):
        nbin = bin(n & int("1"*32, 2))
        print(nbin)
        num = 0
        if nbin[0] == '-':
            nbin = nbin.replace('-0b', '')
            for i in range(len(nbin)-1, -1, -1):
                if nbin[i] == '1':
                    break
            t = i
            for i in range(0, t):
                if nbin[i] == '0':
                    num+=1
            num+=2
        else:
            nbin = nbin.replace('0b', '')
            for i in range(0, len(nbin)):
                if nbin[i] == '1':
                    num+=1
        return num


if __name__ == '__main__':
    S=Solution()
    print(S.NumberOf1(-1))