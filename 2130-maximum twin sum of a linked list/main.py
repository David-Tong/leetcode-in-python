# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        values = list()

        node = head
        while node:
            values.append(node.val)
            node = node.next

        L = len(values)
        ans = 0
        for x in range(L // 2):
            ans = max(ans, values[x] + values[L - 1 - x])
        return ans


"""
node = ListNode(5)
node2 = ListNode(4)
node3 = ListNode(2)
node4 = ListNode(1)
"""

"""
node = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(3)

node.next = node2
node2.next = node3
node3.next = node4
"""

node = ListNode(1)
node2 = ListNode(100000)

node.next = node2

solution = Solution()
print(solution.pairSum(node))
