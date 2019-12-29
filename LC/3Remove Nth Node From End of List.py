# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = []
        s = head
        while not s is None:
            temp.append(s.val)
            s = s.next
        if n == len(temp):
            if len(temp) == 0 or len(temp) == 1:
                return None
            else:
                out_h = ListNode(temp[1])
        else:
            out_h = ListNode(temp[0])
        t_n = out_h
        if not n == len(temp):
            for i in range(1, len(temp)):
                if not i == len(temp) - n:
                    t_n.next = ListNode(temp[i])
                    t_n = t_n.next
        elif not len(temp) == 2:
            for i in range(2, len(temp)):
                if not i == len(temp) - n:
                    t_n.next = ListNode(temp[i])
                    t_n = t_n.next

        return out_h

if __name__ == '__main__':
    t = ListNode(1)
    k = t
    t.next = ListNode(2)
    t = t.next
    t.next = ListNode(3)
    t = t.next
    t.next = ListNode(4)
    t = t.next
    # t.next = ListNode(5)
    # t = t.next
    S = Solution()
    s1 = S.removeNthFromEnd(k, 4)
    while not s1 is None:
        print(s1.val)
        s1 = s1.next