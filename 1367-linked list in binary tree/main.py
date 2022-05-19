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
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        bfs = deque()
        visited = set()
        if root.val == head.val:
            bfs.append((root, head))
            visited.add((root, head))
        else:
            bfs.append((root, None))
            visited.add((root, None))
        while bfs:
            tree, linked = bfs.popleft()
            if tree and linked:
                if linked.next is None:
                    return True
                if tree.left:
                    if linked.next.val == tree.left.val:
                        if (tree.left, linked.next) not in visited:
                            bfs.append((tree.left, linked.next))
                            visited.add((tree.left, linked.next))
                    if (tree.left, None) not in visited:
                        bfs.append((tree.left, None))
                        visited.add((tree.left, None))
                if tree.right:
                    if linked.next.val == tree.right.val:
                        if (tree.right, linked.next) not in visited:
                            bfs.append((tree.right, linked.next))
                            visited.add((tree.right, linked.next))
                    if (tree.right, None) not in visited:
                        bfs.append((tree.right, None))
                        visited.add((tree.right, None))
            elif linked is None:
                if tree:
                    if tree.val == head.val:
                        if (tree, head) not in visited:
                            bfs.append((tree, head))
                            visited.add((tree, head))
                    else:
                        if tree.left:
                            if (tree.left, None) not in visited:
                                bfs.append((tree.left, None))
                                visited.add((tree.left, None))
                        if tree.right:
                            if (tree.right, None) not in visited:
                                bfs.append((tree.right, None))
                                visited.add((tree.right, None))
        return False


"""
node = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(2)
node4 = ListNode(6)
node5 = ListNode(8)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node11 = TreeNode(1)
node12 = TreeNode(4)
node13 = TreeNode(4)
node14 = TreeNode(2)
node15 = TreeNode(2)
node16 = TreeNode(1)
node17 = TreeNode(6)
node18 = TreeNode(8)
node19 = TreeNode(1)
node20 = TreeNode(3)

node11.left = node12
node11.right = node13
node12.right = node14
node13.left = node15
node14.left = node16
node15.left = node17
node15.right = node18
node18.left = node19
node18.right = node20
"""

"""
node = ListNode(1)
node2 = ListNode(10)

node.next = node2

node11 = TreeNode(1)
node12 = TreeNode(1)
node13 = TreeNode(10)
node14 = TreeNode(1)
node15 = TreeNode(9)

node11.right = node12
node12.left = node13
node12.right = node14
node13.left = node15
"""

node = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(1)

node.next = node2
node2.next = node3

node11 = TreeNode(2)
node12 = TreeNode(2)
node13 = TreeNode(2)
node14 = TreeNode(1)


node11.right = node12
node12.right = node13
node13.right = node14


solution = Solution()
print(solution.isSubPath(node, node11))
