# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # pre-process
        dummy = ListNode(0, head)

        node = head
        number = ""
        L = 0
        while node:
            number += str(node.val)
            node = node.next
            L += 1
        number = str(int(number) * 2)

        # process
        if len(number) > L:
            addition = number[:len(number) - L]
            prev = dummy
            for digit in addition:
                node = ListNode(digit)
                prev.next = node
                prev = node
            node.next = head

        node = head
        for digit in number[len(number) - L:]:
            node.val = digit
            node = node.next
        return dummy.next


"""
node = ListNode(1)
node2 = ListNode(8)
node3 = ListNode(9)

node.next = node2
node2.next = node3
"""

node = ListNode(9)
node2 = ListNode(9)
node3 = ListNode(9)

node.next = node2
node2.next = node3


solution = Solution()
node = solution.doubleIt(node)

number = ""
while node:
    number += node.val
    node = node.next
print(number)