# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        nums = set(nums)

        # process
        curr = head
        ans = 0
        start = False
        while curr:
            if curr.val in nums:
                if not start:
                    start = True
                    ans += 1
            else:
                if start:
                    start = False
            curr = curr.next
        return ans


"""
node = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)

node.next = node2
node2.next = node3
node3.next = node4

nums = [0,1,3]
"""

node = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

nums = [0,3,1,4]
nums = [0,2,4]

solution = Solution()
print(solution.numComponents(node, nums))
