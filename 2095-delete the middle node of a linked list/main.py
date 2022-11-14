class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # corner cases
        if head.next is None:
            return None
        elif head.next.next is None:
            head.next = None
            return head

        # process
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        run = True
        while run:
            for x in range(2):
                fast = fast.next
                if fast is None:
                    run = False
                    break
            if run:
                slow = slow.next

        slow.next = slow.next.next
        return head


node = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(7)
node5 = ListNode(1)
node6 = ListNode(2)
node7 = ListNode(6)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

solution = Solution()
head = solution.deleteMiddle(node)

head