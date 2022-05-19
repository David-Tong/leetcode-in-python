class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        from collections import defaultdict
        self.dicts = defaultdict(int)

        from collections import deque
        bfs = deque()
        self.root = root
        root.val = 0
        bfs.append(root)
        while bfs:
            size = len(bfs)
            for x in range(size):
                node = bfs.popleft()
                self.dicts[node.val] += 1

                if node.left:
                    node.left.val = node.val * 2 + 1
                    bfs.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 2
                    bfs.append(node.right)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.dicts:
            return True
        else:
            return False


node = TreeNode(-1)
node2 = TreeNode(-1)
node3 = TreeNode(-1)
node4 = TreeNode(-1)
node5 = TreeNode(-1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

findElements = FindElements(node)
print(findElements.find(1))
print(findElements.find(3))
print(findElements.find(5))
