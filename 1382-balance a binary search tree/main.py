# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # in-order traverse
        def leftMost(node):
            while node:
                stack.append(node)
                node = node.left

        nums = list()
        stack = list()
        if root:
            leftMost(root)

        while stack:
            node = stack.pop()
            nums.append(node.val)
            if node.right:
                leftMost(node.right)

        # construct BST
        L = len(nums)
        if L <= 1:
            return root

        from collections import deque
        bfs = deque()
        idx = 0
        root = TreeNode()
        bfs.append(root)

        while bfs:
            for _ in range(len(bfs)):
                node = bfs.popleft()
                idx += 1
                if idx < L:
                    node.left = TreeNode()
                    bfs.append(node.left)
                    idx += 1
                else:
                    break
                if idx < L:
                    node.right = TreeNode()
                    bfs.append(node.right)
                else:
                    break

        # setup BST
        idx = 0
        stack = list()
        if root:
            leftMost(root)

        while stack:
            node = stack.pop()
            node.val = nums[idx]
            idx += 1
            if node.right:
                leftMost(node.right)

        return root


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.right = node2
node2.right = node3
node3.right = node4
"""

node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node.left = node2
node.right = node3

solution = Solution()
ans = solution.balanceBST(node)

ans
