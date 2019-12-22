# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def creat_list(labels, randoms):
    H = RandomListNode(labels[0])
    p = H
    for i in range(1, len(labels)):
        n = RandomListNode(labels[i])
        p.next = n
        p = p.next
    p = H
    for rand in randoms:
        if rand == -1:
            p.random = None
        else:
            t_p = H
            while t_p is not None:
                if t_p.label == rand:
                    break
                t_p = t_p.next
            p.random = t_p
        p = p.next


    return H

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        p = pHead
        while p is not None:
            n = RandomListNode(p.label)
            n.next = p.next
            p.next = n
            p = n.next
        p = pHead
        while p is not None:
            n = p.next
            if p.random is not None:
                n.random = p.random.next
            else:
                n.random = None
            p = n.next
        nH = pHead.next
        p = nH
        while p is not None:
            if p.next is not None:
                p.next = p.next.next
            else:
                p.next = None
            p = p.next
        return nH


if __name__ == '__main__':
    H = creat_list([1,2,3,4], [3, 4, 2, -1])
    p = H
    while p is not None:
        print(p.label)
        p = p.next
    print('----')
    p = H
    while p is not None:
        print(p.label)
        p = p.random
    S = Solution()
    H = S.Clone(H)
    print('++++++++++')
    p = H
    while p is not None:
        print(p.label)
        p = p.next
    print('----')
    p = H
    while p is not None:
        print(p.label)
        p = p.random
    S = Solution()
    nH = S.Clone(H)