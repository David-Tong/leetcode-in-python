# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        # pre-process
        from collections import defaultdict
        nodes = defaultdict(list)
        children = set()

        for description in descriptions:
            node, child, left = description
            nodes[node].append((child, left))
            children.add(child)

        root = None
        for node in nodes:
            if node not in children:
                root = TreeNode(node)
                break

        def doCreate(parent):
            for child, left in nodes[parent.val]:
                node = TreeNode(child)
                if left:
                    parent.left = node
                else:
                    parent.right = node
                doCreate(node)

        # process
        doCreate(root)
        return root


descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
descriptions = [[1,2,1],[2,3,0],[3,4,1]]

solution = Solution()
root = solution.createBinaryTree(descriptions)

root
