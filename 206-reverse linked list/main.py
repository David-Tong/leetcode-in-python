class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def doReverseList(curr):
            if curr.next is None:
                self.head = curr
                return curr
            next = doReverseList(curr.next)
            next.next = curr
            return curr

        if head is None:
            return None
        doReverseList(head)
        head.next = None
        return self.head


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
node2.next = None
node3.next = node4
node4.next = node5

solution = Solution()
curr = solution.reverseList(node)

while curr:
    print(curr.val)
    curr = curr.next
