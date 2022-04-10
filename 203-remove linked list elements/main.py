class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                curr = curr.next
            else:
                prev.next = curr
                prev = prev.next
                curr = curr.next
        prev.next = curr

        return dummy.next


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node = ListNode(7)
node2 = ListNode(7)
node3 = ListNode(7)
node4 = ListNode(7)

node.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
curr = solution.removeElements(None, 7)

while curr:
    print(curr.val)
    curr = curr.next
