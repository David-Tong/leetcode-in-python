# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # pre-process
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y = 0, -1
        steps = [n, m - 1, n - 1, m - 2]
        matrix = [[-1] * n for _ in range(m)]

        # process
        node = head
        while node:
            for idx, (dx, dy) in enumerate(DIRECTIONS):
                for _ in range(steps[idx]):
                    x, y = x + dx, y + dy
                    matrix[x][y] = node.val
                    node = node.next
                    if not node:
                        return matrix
                if steps[idx] - 2 >= 0:
                    steps[idx] -= 2
                else:
                    steps[idx] = 0
        return matrix


"""
m = 3
n = 5

node = ListNode(3)
node2 = ListNode(0)
node3 = ListNode(2)
node4 = ListNode(6)
node5 = ListNode(8)
node6 = ListNode(1)
node7 = ListNode(7)
node8 = ListNode(9)
node9 = ListNode(4)
node10 = ListNode(2)
node11 = ListNode(5)
node12 = ListNode(5)
node13 = ListNode(0)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13
"""

m = 1
n = 4

node = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)

node.next = node2
node2.next = node3


solution = Solution()
print(solution.spiralMatrix(m, n, node))
