class Solution:
    def rectCover(self, number):
        Flist = [0, 1, 2]
        for i in range(3, number+1):
            Flist.append(Flist[i - 1] + Flist[i - 2])
        return Flist[number]

if __name__ == '__main__':
    S=Solution()
    print(S.rectCover(5))
