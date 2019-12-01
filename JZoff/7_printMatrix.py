class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        slist = []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        while l < r and t < b:

            for i in range(l, r):
                slist.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                slist.append(matrix[i][r-1])
            r -= 1
            if b > t:
                for i in range(r-1, l-1, -1):
                    slist.append(matrix[b-1][i])
                b -= 1
            if l < r:
                for i in range(b-1, t-1, -1):
                    slist.append(matrix[i][l])
                l += 1
        return slist

if __name__ == '__main__':
    s = [[1,2,3,4]]  # ,[5,6,7,8],[9,10,11,12],[13,14,15,16]
    S = Solution()
    print(S.printMatrix(s))