# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # process
        node = head
        stack = list()
        from collections import defaultdict
        dicts = defaultdict(int)
        idx = 0
        while node:
            while stack and stack[-1][1] < node.val:
                old_idx, _ = stack.pop()
                dicts[old_idx] = node.val
            stack.append((idx, node.val))
            idx += 1
            node = node.next

        # post-process
        ans = [0] * idx
        for idx in dicts:
            ans[idx] = dicts[idx]
        return ans


"""
node = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(5)

node.next = node2
node2.next = node3
"""

node = ListNode(2)
node2 = ListNode(7)
node3 = ListNode(4)
node4 = ListNode(3)
node5 = ListNode(5)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
print(solution.nextLargerNodes(node))
