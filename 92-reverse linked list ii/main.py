class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head

        nodes = [dummy]
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes.append(None)

        for x in range(right, left, -1):
            nodes[x].next = nodes[x-1]

        nodes[left - 1].next = nodes[right]
        nodes[left].next = nodes[right + 1]

        return dummy.next


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

left = 2
right = 5

solution = Solution()
node = solution.reverseBetween(node, left, right)

while node:
    print(node.val)
    node = node.next
