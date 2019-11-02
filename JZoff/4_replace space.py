# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.replace(' ', '%20')
        return s




if __name__ == '__main__':
    S=Solution()
    print(S.replaceSpace('a apple hah'))