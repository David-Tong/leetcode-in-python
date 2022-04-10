class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        else:
            if head.next.next is None:
                return head

        first = head
        second = head.next

        even = head
        odd = head.next
        last_even = None
        while even and odd:
            even.next = odd.next
            even = even.next
            if even:
                last_even = even
                odd.next = even.next
                odd = odd.next
        last_even.next = second
        return head


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node.next = node2
#node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

solution = Solution()
curr = solution.oddEvenList(node)

while curr:
    print(curr.val)
    curr = curr.next