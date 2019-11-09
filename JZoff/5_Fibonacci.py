class Solution:
    def Fibonacci(self, n):
        Flist = [0, 1]
        for i in range(2, n+1):
            Flist.append(Flist[i-1]+Flist[i-2])
        return Flist[n]

if __name__ == '__main__':
    S=Solution()
    print(S.Fibonacci(4))