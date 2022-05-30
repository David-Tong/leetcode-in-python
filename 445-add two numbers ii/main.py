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
        def doAdd(num1, num2):
            M = len(num1)
            N = len(num2)
            num = list()

            idx1 = 0
            idx2 = 0
            carry = 0
            while idx1 < M and idx2 < N:
                total = num1[idx1] + num2[idx2] + carry
                num.append(total % 10)
                carry = total // 10
                idx1 += 1
                idx2 += 1

            while idx1 < M:
                total = num1[idx1] + carry
                num.append(total % 10)
                carry = total // 10
                idx1 += 1

            while idx2 < N:
                total = num2[idx2] + carry
                num.append(total % 10)
                carry = total // 10
                idx2 += 1

            if carry > 0:
                num.append(carry)

            return num

        num1 = list()
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        num1 = num1[::-1]

        num2 = list()
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num2 = num2[::-1]

        num = doAdd(num1, num2)
        num = num[::-1]

        prev = ListNode(num[0])
        head = prev
        for digit in num[1:]:
            node = ListNode(digit)
            prev.next = node
            prev = node

        return head


node11 = ListNode(7)
node12 = ListNode(2)
node13 = ListNode(4)
node14 = ListNode(3)

node11.next = node12
node12.next = node13
node13.next = node14

node21 = ListNode(5)
node22 = ListNode(6)
node23 = ListNode(4)

node21.next = node22
node22.next = node23

solution = Solution()
head = solution.addTwoNumbers(node11, node21)

while head:
    print(head.val)
    head = head.next