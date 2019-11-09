class Solution:
    def jumpFloor(self, number):
        Flist = [1, 2]
        for i in range(2, number):
            Flist.append(Flist[i - 1] + Flist[i - 2])
        return Flist[number-1]


if __name__ == '__main__':
    S=Solution()
    print(S.jumpFloor(4))