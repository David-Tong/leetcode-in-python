# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # pre-process
        nums = set(nums)
        dummy = ListNode()
        dummy.next = head

        # process
        prev = dummy
        curr = head
        while curr:
            if curr.val in nums:
                pass
            else:
                prev.next = curr
                prev = prev.next
            curr = curr.next

        prev.next = curr
        ans = dummy.next
        return ans


"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

nums = [1,2,3]
"""

"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(1)
node6 = ListNode(2)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

nums = [1]
"""

"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node.next = node2
node2.next = node3
node3.next = node4

nums = [5]
"""

node = ListNode(2)
node2 = ListNode(10)
node3 = ListNode(9)

node.next = node2
node2.next = node3

nums = [9,2,5]

solution = Solution()
head = solution.modifiedList(nums, node)

head
