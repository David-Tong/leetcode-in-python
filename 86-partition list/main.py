class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        curr = head
        less_than = ListNode()
        greater_than = ListNode()
        less_than_head = less_than
        greater_than_head = greater_than
        while curr:
            if curr.val < x:
                less_than.next = curr
                less_than = less_than.next
            else:
                greater_than.next = curr
                greater_than = greater_than.next
            curr = curr.next

        less_than.next = greater_than_head.next
        greater_than.next = None
        return less_than_head.next


node = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

#node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

x = 100

solution = Solution()
node = solution.partition(node, x)

while node:
    print(node.val)
    node = node.next
