# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listnode(strnum):
    h = ListNode(strnum[0])
    p = h
    for i in range(1, len(strnum)):
        num = str(strnum[i])
        p.next = ListNode(num)
        p = p.next
    return h


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head is None:
            if head.next is None:
                n_head = head
                return n_head
            else:
                n_head = head.next
        else:
            return None
        p = head
        q = n_head
        r = n_head.next
        n_head.next = p
        p.next = None
        while not r is None:
            q = r.next
            if not q is None:
                p.next = q
                p = r
                r = q.next
                q.next = p
                p.next = None
            else:
                p.next = r
                r = None
        return n_head


if __name__ == '__main__':
    S=Solution()
    s = listnode('1234567890')
    # p = s
    # while not p is None:
    #     print(p.val)
    #     p = p.next

    t = S.swapPairs(s)
    p = t
    while not p is None:
        print(p.val)
        p = p.next
