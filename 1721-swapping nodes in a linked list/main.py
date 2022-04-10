class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        curr = head
        idx = 0
        while curr:
            curr = curr.next
            idx += 1

        rev_k = idx - k + 1
        if k == rev_k:
            return head

        prev_k = dummy
        node_k = None
        next_k = None
        prev_rev_k = dummy
        node_rev_k = None
        next_rev_k = None
        curr = head
        idx = 1
        while curr:
            if idx == k - 1:
                prev_k = curr
            elif idx == k:
                node_k = curr
            elif idx == k + 1:
                next_k = curr

            if idx == rev_k - 1:
                prev_rev_k = curr
            elif idx == rev_k:
                node_rev_k = curr
            elif idx == rev_k + 1:
                next_rev_k = curr

            curr = curr.next
            idx += 1

        if abs(k - rev_k) == 1:
            if k < rev_k:
                prev_k.next = node_rev_k
                node_rev_k.next = node_k
                node_k.next = next_rev_k
            else:
                prev_rev_k.next = node_k
                node_k.next = node_rev_k
                node_rev_k.next = next_k
        else:
            prev_k.next = node_rev_k
            node_rev_k.next = next_k
            prev_rev_k.next = node_k
            node_k.next = next_rev_k

        return dummy.next


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
#node2.next = node3
#node3.next = node4
#node4.next = node5

k = 2
k = 1
#k = 5

solution = Solution()
node = solution.swapNodes(node, k)

while node:
    print(node.val)
    node = node.next
