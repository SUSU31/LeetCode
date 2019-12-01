class Solution:
    def reOrderArray(self, array):
        temp1 = []
        temp2 = []
        for i in array:
            if i%2 == 0:
                temp2.append(i)
            else:
                temp1.append(i)
        temp = temp1 + temp2
        return temp

if __name__ == '__main__':
    S=Solution()
    print(S.reOrderArray([1, 12, 3,4 ,5]))