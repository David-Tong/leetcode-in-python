class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        steps = length - n - 1
        if steps < 0:
            if head.next:
                return head.next
            else:
                return None
        else:
            curr = head
            count = 0
            while count < steps:
                curr = curr.next
                count += 1
            curr.next = curr.next.next

        return head


solution = Solution()

node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

#node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

curr = solution.removeNthFromEnd(node, 1)
while curr:
    print(curr.val)
    curr = curr.next
