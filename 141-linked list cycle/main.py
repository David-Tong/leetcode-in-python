class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
            else:
                return False
            if slow == fast:
                return True
        return False


node = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node.next = None
node2.next = node2
node3.next = node4
node4.next = node2

solution = Solution()
print(solution.hasCycle(None))