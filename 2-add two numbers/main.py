class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        carry = 0
        while l1 and l2:
            addup = l1.val + l2.val + carry
            val = addup % 10
            carry = addup // 10
            node = ListNode(val)
            prev.next = node
            prev = node
            l1 = l1.next
            l2 = l2.next

        while l1:
            addup = l1.val + carry
            val = addup % 10
            carry = addup // 10
            node = ListNode(val)
            prev.next = node
            prev = node
            l1 = l1.next

        while l2:
            addup = l2.val + carry
            val = addup % 10
            carry = addup // 10
            node = ListNode(val)
            prev.next = node
            prev = node
            l2 = l2.next

        if carry > 0:
            node = ListNode(carry)
            prev.next = node
            prev = node

        return dummy.next


node11= ListNode(2)
node12 = ListNode(4)
node13 = ListNode(9)
node11.next = node12
node12.next = node13

node21 = ListNode(5)
node22 = ListNode(6)
node23 = ListNode(4)
node21.next = node22
#node22.next = node23

solution = Solution()
node = solution.addTwoNumbers(node11, node21)

while node:
    print(node.val)
    node = node.next