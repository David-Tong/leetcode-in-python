# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # pre-process
        vals = list()
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        idx = 0
        count = 0
        stack = list()
        processed = list()
        while idx < len(vals):
            if len(stack) == count:
                if count % 2 == 0:
                    processed.extend(stack[::-1])
                else:
                    processed.extend(stack)
                stack = list()
                count += 1
            stack.append(vals[idx])
            idx += 1
        if len(stack) % 2 == 0:
            processed.extend(stack[::-1])
        else:
            processed.extend(stack)
        # print(processed)

        # process
        node = head
        idx = 0
        while node:
            node.val = processed[idx]
            node = node.next
            idx += 1
        return head


node = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(9)
node6 = ListNode(1)
node7 = ListNode(7)
node8 = ListNode(3)
node9 = ListNode(8)
node10 = ListNode(4)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

solution = Solution()
print(solution.reverseEvenLengthGroups(node))
