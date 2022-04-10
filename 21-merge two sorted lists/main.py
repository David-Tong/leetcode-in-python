class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2

        prev = None
        head = None
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                if head is None:
                    head = curr1
                    prev = curr1
                else:
                    prev.next = curr1
                    prev = prev.next
                curr1 = curr1.next
            else:
                if head is None:
                    head = curr2
                    prev = curr2
                else:
                    prev.next = curr2
                    prev = prev.next
                curr2 = curr2.next

        if curr1 is not None:
            if prev is None:
                head = curr1
            else:
                prev.next = curr1

        if curr2 is not None:
            if prev is None:
                head = curr2
            else:
                prev.next = curr2

        return head


node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(4)
node11.next = node12
node12.next = node13

node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
node21.next = node22
node22.next = node23

solution = Solution()
curr = solution.mergeTwoLists(None, None)

while curr:
    print(curr.val)
    curr = curr.next
