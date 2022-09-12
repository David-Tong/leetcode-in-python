class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # get linked list length
        node = head
        L = 0
        while node:
            L += 1
            node = node.next

        if L < 2:
            return True

        # get the first half start
        H = L // 2
        node = head
        idx = 0
        while idx < H - 1:
            idx += 1
            node = node.next

        first = node
        if L % 2 == 0:
            second = node.next
        else:
            second = node.next.next

        # revert the first half
        prev = None
        curr = head
        idx = 0
        while idx < H:
            idx += 1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # start to validate palindrome
        while first and second:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
        return True


"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node.next = node2
node2.next = node3
node3.next = node4
"""

"""
node = ListNode(1)
node2 = ListNode(2)

node.next = node2
"""

"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
"""

node = ListNode(1)

solution = Solution()
print(solution.isPalindrome(node))
