class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        def buildBST(nodes, left, right):
            if left < right:
                middle = (left + right) // 2
                root = TreeNode(nodes[middle].val)
                root.left = buildBST(nodes, left, middle - 1)
                root.right = buildBST(nodes, middle + 1, right)
                return root
            elif left == right:
                return TreeNode(nodes[left].val)

        return buildBST(nodes, 0, len(nodes) - 1)


node = ListNode(-10)
node2 = ListNode(-3)
node3 = ListNode(0)
node4 = ListNode(5)
node5 = ListNode(9)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
root = solution.sortedListToBST(None)


def leftMost(node, stack):
    while node:
        stack.append(node)
        node = node.left

stack = []
leftMost(root, stack)
while stack:
    node = stack.pop()
    print(node.val)
    leftMost(node.right, stack)



