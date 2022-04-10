class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        N = len(nodes)
        left = 0
        right = N - 1
        count = 0
        while count < N:
            if count % 2 == 0:
                if count == N - 1:
                    nodes[left].next = None
                else:
                    nodes[left].next = nodes[right]
                    left += 1
            else:
                if count == N - 1:
                    nodes[right].next = None
                else:
                    nodes[right].next = nodes[left]
                    right -= 1
            count += 1


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
solution.reorderList(node)

while node:
    print(node.val)
    node = node.next