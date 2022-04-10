class DoublyListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev= prev


class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def createLinkedList(n):
            head = DoublyListNode(1)
            prev = head
            for x in range(2, n + 1):
                curr = DoublyListNode(x)
                prev.next = curr
                curr.prev = prev
                prev = curr
            head.prev = curr
            curr.next = head
            return head

        if n == 1:
            return 1

        head = createLinkedList(n)
        curr = head
        count = n
        while count > 1:
            step = 1
            while step < k:
                curr = curr.next
                step += 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr = curr.next
            count -= 1
        return curr.val


n = 5
k = 2

n = 6
k = 5

n = 6
k = 1

n = 1
k = 1

solution = Solution()
print(solution.findTheWinner(n, k))
