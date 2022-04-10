class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        length = 0
        node = head
        while node:
            length += 1
            tail = node
            node = node.next

        step = length - k % length - 1
        node = head
        while step > 0:
            node = node.next
            step -= 1

        tail.next = head
        head = node.next
        node.next = None

        return head


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

#node.next = node2
node2.next = node3
#node3.next = node4
node4.next = node5

k = 2
k = 4

solution = Solution()
node = solution.rotateRight(node, k)

while node:
    print(node.val)
    node = node.next
