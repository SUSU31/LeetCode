class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglynumbers = [1]
        nextindex = 1
        while index >= nextindex:
            temp2 = []
            for i in range(0, len(uglynumbers)):
                if uglynumbers[i] *2 > uglynumbers[-1]:
                    temp2.append(uglynumbers[i] *2)
                if uglynumbers[i] *3 > uglynumbers[-1]:
                    temp2.append(uglynumbers[i] *3)
                if uglynumbers[i] *5 > uglynumbers[-1]:
                    temp2.append(uglynumbers[i] *5)
            t_min = min(temp2)
            uglynumbers.append(t_min)
            nextindex+=1
        return uglynumbers[index-1]

if __name__ == '__main__':
    S = Solution()
    print(S.GetUglyNumber_Solution(1))