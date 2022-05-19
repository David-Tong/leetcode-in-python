class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def doInsert(dummy, index, length):
            # do insert
            prev = dummy
            node = dummy.next
            idx = index
            while idx > 0:
                prev = node
                node = node.next
                idx -= 1
            curr = node

            prev2 = dummy
            node2 = dummy.next
            idx = 0
            while node2 and idx < index and node2.val < curr.val:
                prev2 = node2
                node2 = node2.next
                idx += 1

            if node2 and idx < index:
                prev2.next = curr
                prev.next = curr.next
                curr.next = node2

        # get length of list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # short cut
        if length == 1:
            return head

        # create dummy node
        dummy = ListNode(-6000)
        dummy.next = head

        # sort
        for x in range(1, length):
            doInsert(dummy, x, length)
        return dummy.next

"""
node = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)

node.next = node2
node2.next = node3
node3.next = node4
"""

node = ListNode(-1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)
node6 = ListNode(10)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

solution = Solution()
node = solution.insertionSortList(node)

while node:
    print(node.val)
    node = node.next
