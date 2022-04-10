class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from queue import PriorityQueue
        q = PriorityQueue()

        points = [0] * len(lists)

        index = 0
        while index < len(lists):
            if lists[index]:
                q.put((lists[index].val, index))
            points[index] = lists[index]
            index += 1

        if q.empty():
            return None
        mini, index = q.get()
        head = points[index]
        nxt = head.next
        if nxt:
            q.put((nxt.val, index))
            print(nxt.val, index)
        points[index] = nxt

        prev = head
        while not q.empty():
            mini, index = q.get()
            curr = points[index]
            if curr:
                nxt = curr.next
                if nxt:
                    q.put((curr.next.val, index))
                    print(curr.next.val, index)
                points[index] = curr.next
            prev.next = curr
            prev = curr

        return head


node11 = ListNode(1)
node12 = ListNode(4)
node13 = ListNode(5)
node11.next = node12
node12.next = node13

node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
node21.next = node22
node22.next = node23

node31 = ListNode(2)
node32 = ListNode(6)
node31.next = node32

lists = [node11, node21, node31]
lists = [node11, None]
solution = Solution()
curr = solution.mergeKLists(lists)

res = []
while curr:
    res.append(curr.val)
    curr = curr.next

print(res)
