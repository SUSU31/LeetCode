# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):

        if len(array) == 0: return False
        # write code here
        h, w = len(array), len(array[0])
        i, j = h-1, 0
        while i>=0 and j < w:
            if target > array[i][j]:
                j += 1
            elif target < array[i][j]:
                i -= 1
            else:
                return True
        return False

import numpy as np
if __name__ == '__main__':
    a = np.array([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
    S=Solution()
    print(S.Find(11, a))