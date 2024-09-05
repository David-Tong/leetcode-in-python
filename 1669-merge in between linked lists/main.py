# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # get start and end nodes in list one
        idx = 0
        node = list1
        prev_a = None
        next_b = None
        while node:
            if idx == a - 1:
                prev_a = node
            elif idx == b + 1:
                next_b = node
                break
            idx += 1
            node = node.next

        # get head and rear nodes in list two
        node = list2
        while node.next:
            node = node.next
        head = list2
        rear = node

        # concat
        if not prev_a or not next_b:
            raise Exception()
        prev_a.next = head
        rear.next = next_b

        return list1


node11 = ListNode(10)
node12 = ListNode(1)
node13 = ListNode(13)
node14 = ListNode(6)
node15 = ListNode(9)
node16 = ListNode(5)

node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node15
node15.next = node16

node21 = ListNode(1000000)
node22 = ListNode(1000001)
node23 = ListNode(1000002)

node21.next = node22
node22.next = node23

a = 3
b = 4

solution = Solution()
node = solution.mergeInBetween(node11, a, b, node21)

while node:
    print(node.val)
    node = node.next
