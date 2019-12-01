from JZoff.temp import ListNode, listnode

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        if pHead1.val > pHead2.val:
            p = pHead2
            p1 = pHead1
            p2 = pHead2.next
        else:
            p = pHead1
            p1 = pHead1.next
            p2 = pHead2

        nh = p

        while p1 is not None or p2 is not None:
            if p1 is None:
                p.next = p2
                break
            if p2 is None:
                p.next = p1
                break

            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        return nh

if __name__ == '__main__':
    S=Solution()
    nl = listnode([1,3,5])
    nl2 = listnode([2,4,6])
    k = S.Merge(nl, nl2)
    while k is not None:
        print(k.val)
        k = k.next
