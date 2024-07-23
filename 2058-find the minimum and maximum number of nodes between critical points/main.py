# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # pre-process
        if not head.next.next:
            return -1, -1

        fast = head.next.next
        middle = head.next
        slow = head

        # process
        idx = 1
        mini = float("inf")
        criticals = list()
        while fast:
            if slow.val < middle.val > fast.val:
                if criticals:
                    mini = min(mini, idx - criticals[-1])
                criticals.append(idx)
            elif slow.val > middle.val < fast.val:
                if criticals:
                    mini = min(mini, idx - criticals[-1])
                criticals.append(idx)

            idx += 1
            fast = fast.next
            middle = middle.next
            slow = slow.next

        if len(criticals) > 1:
            maxi = criticals[-1] - criticals[0]
            return mini, maxi
        else:
            return -1, -1


"""
node = ListNode(3)
node2 = ListNode(1)

node.next = node2
"""

"""
node = ListNode(5)
node2 = ListNode(3)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(1)
node7 = ListNode(2)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
"""

"""
node = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(2)
node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(2)
node7 = ListNode(2)
node8 = ListNode(2)
node9 = ListNode(7)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
"""

"""
node = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(3)
node4 = ListNode(2)

node.next = node2
node2.next = node3
node3.next = node4
"""

node = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)

node.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
print(solution.nodesBetweenCriticalPoints(node))
