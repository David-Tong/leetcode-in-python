class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        sum = 0
        while fast:
            sum += fast.val
            if fast.val == 0:
                if slow != fast:
                    node = ListNode(sum)
                    slow.next = node
                    node.next = fast
                sum = 0
                slow = fast
            fast = fast.next

        dummy = ListNode(1)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.val == 0:
                slow.next = fast.next
            slow = fast
            fast = fast.next
        return dummy.next


node = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(0)
node4 = ListNode(3)
node5 = ListNode(0)
node6 = ListNode(2)
node7 = ListNode(2)
node8 = ListNode(0)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

solution = Solution()
node = solution.mergeNodes(node)

while node:
    print(node.val)
    node = node.next
