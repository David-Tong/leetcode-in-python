class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        bfs = deque()
        bfs.append(root)

        end = False
        while bfs:
            curr = bfs.popleft()
            if curr:
                if end:
                    return False
                if curr.left:
                    bfs.append(curr.left)
                else:
                    bfs.append(None)
                if curr.right:
                    bfs.append(curr.right)
                else:
                    bfs.append(None)
            else:
                end = True
        return True


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
#node.right = node3
node2.left = node4
#node2.right = node5
#node3.right = node7

solution = Solution()
print(solution.isCompleteTree(node))
