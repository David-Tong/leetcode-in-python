class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val == prev.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = prev.next
                curr = curr.next

        prev.next = curr
        return head


node = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(3)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

solution = Solution()
curr = solution.deleteDuplicates(node)

while curr:
    print(curr.val)
    curr = curr.next