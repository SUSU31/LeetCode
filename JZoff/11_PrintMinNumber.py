class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers)==0:
            return ''
        if len(numbers)==1:
            return numbers[0]
        d1 = [numbers[0]]
        for i in range(1,len(numbers)):
            state = 1
            for j in range(len(d1) - 1, -1, -1):
                f = self.compare(numbers[i], d1[j])
                if f>0:
                    d1.insert(j + 1, numbers[i])
                    state = 0
                    break
            if state:
                d1.insert(0, numbers[i])
        str1 = ''
        for num in d1:
            str1 += str(num)
        return int(str1)

    def compare(self, str1, str2):
        str1 = str(str1)
        str2 = str(str2)
        c1 = 0
        c2 = 0
        if str1 == str2:
            return 0
        while True:
            if str1[c1] > str2[c2]:
                return 1
            if str1[c1] < str2[c2]:
                return -1
            if c1 == -1 and c2 == -1:
                break
            c1 = -1 if c1 == -1 or c1 == len(str1) - 1 else c1+1
            c2 = -1 if c2 == -1 or c2 == len(str2) - 1 else c2 + 1

        return 0

if __name__ == '__main__':
    S = Solution()
    print(S.PrintMinNumber([3,5,1,4,2]))
    # print(S.compare(4,5))
