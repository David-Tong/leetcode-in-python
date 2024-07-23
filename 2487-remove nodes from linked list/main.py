# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # monotonic stack
        stack = list()

        node = head
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next

        L = len(stack)
        for x in range(L - 1):
            stack[x].next = stack[x + 1]
        stack[L - 1].next = None
        head = stack[0]
        return head


node = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(13)
node4 = ListNode(3)
node5 = ListNode(8)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
head = solution.removeNodes(node)

node = head
while node:
    print(node.val)
    node = node.next
