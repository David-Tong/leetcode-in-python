class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        from collections import deque
        bfs = deque()
        bfs.append(root)
        ans = []
        while bfs:
            L = len(bfs)
            ans.append(bfs[L - 1].val)
            for x in range(L):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)
node5 = TreeNode(4)

#node.left = node2
node.right = node3
node2.right = node4
#node3.right = node5

solution = Solution()
print(solution.rightSideView(node))
