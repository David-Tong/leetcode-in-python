class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getListLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length_a = getListLength(headA)
        length_b = getListLength(headB)

        node_a = headA
        node_b = headB
        if length_a > length_b:
            gap = length_a - length_b
            while gap > 0:
                node_a = node_a.next
                gap -= 1
        else:
            gap = length_b - length_a
            while gap > 0:
                node_b = node_b.next
                gap -= 1

        while node_a and node_b:
            if node_a == node_b:
                return node_a
            node_a = node_a.next
            node_b = node_b.next

        return None


node11 = ListNode("a1")
node12 = ListNode("a2")
node31 = ListNode("c1")
node32 = ListNode("c2")
node33 = ListNode("c3")
node21 = ListNode("b1")
node22 = ListNode("b2")
node23 = ListNode("b3")

node11.next = node12
#node12.next = node31
node31.next = node32
node32.next = node33
node21.next = node22
node22.next = node23
#node23.next = node31

solution = Solution()
node = solution.getIntersectionNode(node11, node21)

print(node.val)