# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # bfs
        dummy = TreeNode()
        from collections import deque
        bfs = deque()
        bfs.append((dummy, root))

        from collections import defaultdict
        while bfs:
            size = len(bfs)
            dicts = defaultdict(dict)
            for x in range(size):
                parent, current = bfs.popleft()
                if parent not in dicts:
                    dicts[parent] = dict()
                dicts[parent][current] = current.val
                if current.left:
                    bfs.append((current, current.left))
                if current.right:
                    bfs.append((current, current.right))

            total = 0
            for node in dicts:
                for child in dicts[node]:
                    total += dicts[node][child]

            for node in dicts:
                for child in dicts[node]:
                    child.val = total - sum(dicts[node].values())

        return root


node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(9)
node4 = TreeNode(1)
node5 = TreeNode(10)
node6 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

solution = Solution()
root = solution.replaceValueInTree(node)

root