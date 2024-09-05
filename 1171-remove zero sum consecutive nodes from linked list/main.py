# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        nodes = list()
        presums = list()

        # process
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        presum = 0
        while node:
            presum += node.val
            if presum not in presums:
                nodes.append(node)
                presums.append(presum)
                dicts[presum] = len(nodes) - 1
            else:
                nodes = nodes[:dicts[presum] + 1]
                presums = presums[:dicts[presum] + 1]
            node = node.next

        # post-process
        for x in range(len(nodes)):
            if x == len(nodes) - 1:
                nodes[x].next = None
            else:
                nodes[x].next = nodes[x + 1]

        return dummy.next


"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(-3)
node4 = ListNode(3)
node5 = ListNode(1)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
"""

"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(-3)
node5 = ListNode(4)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
"""

node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(-3)
node5 = ListNode(-2)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
node = solution.removeZeroSumSublists(node)

while node:
    print(node.val)
    node = node.next
