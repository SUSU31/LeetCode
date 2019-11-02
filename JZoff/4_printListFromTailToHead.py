# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        arraylist = []
        while listNode is not None:
            arraylist.insert(0, listNode.val)
            listNode = listNode.next
        return arraylist

def listnode(strnum):
    h = ListNode(strnum[0])
    p = h
    for i in range(1, len(strnum)):
        num = str(strnum[i])
        p.next = ListNode(num)
        p = p.next
    return h

if __name__ == '__main__':
    S=Solution()
    print(S.printListFromTailToHead(listnode([1,2,3,4])))
