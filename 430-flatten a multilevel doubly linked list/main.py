# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def doFlatten(head):
            node = head
            while node:
                prev = node
                if node.child:
                    rear = doFlatten(node.child)
                    succ = node.next
                    if succ:
                        succ.prev = rear
                    rear.next = succ
                    node.next = node.child
                    node.child.prev = node
                    #node.child = None
                    node = succ
                else:
                    node = node.next
            if prev.child:
                prev = rear
            return prev

        if head:
            doFlatten(head)

        node = head
        while node:
            node.child = None
            node = node.next

        return head


"""
node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node3.child = node7
node7.next = node8
node8.next = node9
node9.next = node10
node8.child = node11
node11.next = node12

node2.prev = node
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5
node8.prev = node7
node9.prev = node8
node10.prev = node9
node12.prev = node11
"""

"""
node = Node(1)
node2 = Node(2)
node3 = Node(3)

node.next = node2
node.child = node3
"""

"""
node = None
"""

"""
node = Node(1)
"""

node = Node(1)
node2 = Node(2)
node3 = Node(3)

node.child = node2
node2.child = node3

solution = Solution()
head = solution.flatten(node)

head
