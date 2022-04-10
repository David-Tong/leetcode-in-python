class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        count = 0
        middle = length // 2
        curr = head
        while count < middle:
            curr = curr.next
            count += 1

        return curr


solution = Solution()

node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

curr = solution.middleNode(node)
while curr:
    print(curr.val)
    curr = curr.next


