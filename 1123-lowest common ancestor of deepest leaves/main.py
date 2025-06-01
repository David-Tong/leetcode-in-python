# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # step 1 - use bfs to find max depth
        from collections import deque
        bfs = deque()
        bfs.append(root)
        max_depth = -1
        while bfs:
            size = len(bfs)
            max_depth += 1
            for _ in range(size):
                curr = bfs.popleft()
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)

        # print(max_depth)

        # step 2 - use dfs to search lca for all nodes with max depth
        self.lca = None
        def search(node, level):
            if level == max_depth:
                self.lca = node
                return True
            left, right = False, False
            if node.left:
                left = search(node.left, level + 1)
            if node.right:
                right = search(node.right, level + 1)
            if left & right:
                self.lca = node
            return left | right

        search(root, 0)
        # print(self.lca.val)

        ans = self.lca
        return ans


"""
node = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9
"""

node = TreeNode(1)

solution = Solution()
print(solution.lcaDeepestLeaves(node))
