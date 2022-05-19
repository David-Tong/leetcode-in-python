class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        bfs = deque()
        bfs.append(root)
        ans = 0
        while bfs:
            ans = 0
            size = len(bfs)
            for x in range(size):
                node = bfs.popleft()
                ans += node.val
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node6.right = node8

solution = Solution()
print(solution.deepestLeavesSum(node))
