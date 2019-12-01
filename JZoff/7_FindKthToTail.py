from JZoff.temp import ListNode, listnode

class Solution:
    def FindKthToTail(self, head, k):
        temp_list = []
        h = head
        while h is not None:
            temp_list.append(h)
            h = h.next
        if len(temp_list) >= k:
            temp = temp_list[-k]
        else:
            temp = None
        if k == 0:
            temp = None
        return temp

if __name__ == '__main__':
    S=Solution()
    nl = listnode([1, 12, 3,4 ,5])
    print(S.FindKthToTail(nl, 2))
