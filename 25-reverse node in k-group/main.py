class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        def doReverse(nodes, k):
            if len(nodes) == 0:
                return None
            elif len(nodes) < k:
                return nodes[0]
            else:
                idx = k - 1
                while idx > 0:
                    nodes[idx].next = nodes[idx - 1]
                    idx -= 1
                nodes[0].next = doReverse(nodes[k:], k)
                return nodes[k-1]

        return doReverse(nodes, k)

"""
node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
"""

nums = [60,58,61,88,89,21,23,79,74,9,47,33,63,71,96,14,0,60,98,72,85,4,19,22,77,9,8,62,27,55,50,39,14,63,28,3,36,51,34,11,12,82,96,75,5,92,41,5,5,92,29,90,96,0,64,26,9,25,40,88,80,90,28,94,5,56,49,41,59,36,52,71,18,0,98,75,45,39,32,50,31,61,92,80,13,57,6,74,82,46,63,62,88,91,9,93,99,10,86,58,46,91,81,16,91,31,91,36,70,23,86,54,36,79,86,1,88,44,76,70,42,39,84,82,30,93,27,81,4,13,91,50,4,72,19,96]

prev = None
for num in nums:
    node = ListNode(num)
    if prev:
        prev.next = node
    else:
        head = node
    prev = node

#k = 2
k = 3

solution = Solution()
node = solution.reverseKGroup(head, k)

while node:
    print(node.val)
    node = node.next
