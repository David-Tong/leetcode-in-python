# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # get L
        L = 0
        node = head
        while node:
            L += 1
            node = node.next

        # get parts
        Q = L // k
        R = L % k

        parts = [0] * k
        for x in range(k):
            parts[x] = Q
        for x in range(R):
            parts[x] += 1

        # do parts
        node = head
        ans = [None] * k
        for x in range(k):
            if parts[x] == 0:
                break
            for y in range(parts[x]):
                if y == 0:
                    ans[x] = node
                prev = node
                node = node.next
                if y == parts[x] - 1:
                    prev.next = None
        return ans


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node.next = node2
node2.next = node3

k = 5

solution = Solution()
print(solution.splitListToParts(node, k))
