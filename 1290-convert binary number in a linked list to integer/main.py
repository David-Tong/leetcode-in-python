class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        N = count

        count = 0
        ans = 0
        while curr:
            ans += curr.val * 2 ** (N - count)
            count +=1
            curr = curr.next
        return ans

