class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        successor = current.next
        while True:
            current.val = successor.val
            if successor.next:
                current = successor
                successor = successor.next
            else:
                current.next = None
                break


node = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.deleteNode(node2)

node2