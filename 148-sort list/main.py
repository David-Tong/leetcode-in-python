class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# merge sort solution
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def doSort(head, length):
            if length == 1:
                return head

            # get middle
            middle = length // 2
            node = head
            for x in range(middle):
                node = node.next
            head2 = node

            head = doSort(head, middle)
            head2 = doSort(head2, length - middle)
            return doMerge(head, head2, middle, length - middle)

        def doMerge(head, head2, length, length2):
            x, y = 0, 0
            node, node2 = head, head2
            new_head = None
            curr = None
            if node.val < node2.val:
                new_head = node
                node = node.next
                x += 1
            else:
                new_head = node2
                node2 = node2.next
                y += 1
            curr = new_head

            while x < length and y < length2:
                if node.val < node2.val:
                    curr.next = node
                    node = node.next
                    x += 1
                else:
                    curr.next = node2
                    node2 = node2.next
                    y += 1
                curr = curr.next

            if x < length:
                curr.next = node
            else:
                curr.next = node2

            while x < length:
                curr = curr.next
                x += 1

            while y < length2:
                curr = curr.next
                y += 1

            curr.next = None
            return new_head

        # get list length
        if not head:
            return None

        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        return doSort(head, length)


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


solution = Solution()
node = solution.sortList(node)

while node:
    print(node.val)
    node = node.next
