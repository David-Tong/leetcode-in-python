class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head
        self.length = 0
        curr = self.head
        while curr:
            self.length += 1
            curr = curr.next

    def getRandom(self):
        """
        :rtype: int
        """
        import random
        step = random.randint(0, self.length - 1)
        index = 0
        curr = self.head
        while index < step:
            curr = curr.next
            index += 1
        return curr.val


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node.next = node2
node2.next = node3

solution = Solution(node)
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
