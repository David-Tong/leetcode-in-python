class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        def doSwap(nodes):
            if len(nodes) == 0:
                return None
            elif len(nodes) == 1:
                nodes[0].next = None
                return nodes[0]
            elif len(nodes) == 2:
                nodes[0].next = None
                nodes[1].next = nodes[0]
                return nodes[1]
            else:
                next = doSwap(nodes[2:])
                nodes[0].next = next
                nodes[1].next = nodes[0]
                return nodes[1]

        node = doSwap(nodes)
        return node


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

#node.next = node2
#node2.next = node3
#node3.next = node4
#node4.next = node5

solution = Solution()
node = solution.swapPairs(None)

while node:
    print(node.val)
    node = node.next
