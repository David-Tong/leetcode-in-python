class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodes = {}
        dummy = Node(0)
        prev = dummy
        orig = head
        while orig:
            curr = Node(orig.val)
            prev.next = curr
            prev = curr
            nodes[orig] = curr
            orig = orig.next

        orig = head
        while orig:
            if orig.random:
                nodes[orig].random = nodes[orig.random]
            else:
                nodes[orig].random = None
            orig = orig.next

        return dummy.next


node = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node
node3.random = node5
node4.random = node3
node5.random = node

solution = Solution()
node = solution.copyRandomList(node)

while node:
    print(node.val)
    if node.random:
        print(node.random.val)
    else:
        print("None")
    node = node.next
