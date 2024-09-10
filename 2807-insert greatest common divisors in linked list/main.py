# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def lcd(a, b):
            a, b = max(a, b), min(a, b)
            while b:
                a, b = b, a % b
            return a

        # process
        slow = head
        fast = head.next
        while fast:
            node = ListNode(lcd(slow.val, fast.val))
            slow.next = node
            node.next = fast
            slow = fast
            fast = fast.next
        return head


node = ListNode(18)
node2 = ListNode(6)
node3 = ListNode(10)
node4 = ListNode(3)

node.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
head = solution.insertGreatestCommonDivisors(node)

head
