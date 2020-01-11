import copy
class Solution:

    def InversePairs(self, data):
        if len(data) == 0:
            return 0
        self.copy = copy.copy(data)
        self.data = copy.copy(data)
        return self.inversecount(0, len(data)-1) % 1000000007

    def inversecount(self, start, end):
        if end == start:
            self.copy[start] = self.data[start]
            return 0
        lens = (end-start)//2
        left = self.inversecount(start, start+lens)
        right = self.inversecount(start + lens + 1, end)
        i = start+lens
        j = end
        idx = end
        count = 0
        temp = copy.copy(self.data)
        while i>=start and j>=start+lens+1:
            if temp[i] > temp[j]:
                self.copy[idx]=temp[i]
                count+=j-lens-start
                idx -= 1
                i -= 1
            else:
                self.copy[idx] = temp[j]
                idx -= 1
                j -= 1
        while i>=start:
            self.copy[idx] = temp[i]
            idx -= 1
            i -= 1

        while j>=start+lens+1:
            self.copy[idx] = temp[j]
            idx -= 1
            j -= 1
        self.data[start:end+1] = copy.copy(self.copy[start:end+1])
        return count+left+right

if __name__ == '__main__':
    S = Solution()
    print(S.InversePairs([1,2,3,4,5,6,7,0]))

