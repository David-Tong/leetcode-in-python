class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        slow = head
        fast = head.next

        count = 0
        while fast:
            if slow.val == fast.val:
                fast = fast.next
                count += 1
            else:
                if count >= 1:
                    count = 0
                    prev.next = fast
                else:
                    prev = slow
                slow = fast
                fast = fast.next
        if count >= 1:
            count = 0
            prev.next = fast
        return dummy.next


node = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(5)

node.next = node2
#node2.next = node3
node3.next = node4
node4.next = node5
#node5.next = node6
#node6.next = node7

solution = Solution()
node = solution.deleteDuplicates(node)

while node:
    print(node.val)
    node = node.next
