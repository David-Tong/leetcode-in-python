# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = list()
        def leftMost(stack, node):
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left

        stack = list()
        leftMost(stack, root)
        while stack:
            node = stack.pop()
            leftMost(stack, node.right)
        return "".join(str(ans))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        if len(data) > 0:
            root = TreeNode(data[0])
        else:
            return

        def insert(node, val):
            if val < node.val:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            elif val > node.val:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)

        for num in data[1:]:
            insert(root, num)

        return root


# Your Codec object will be instantiated and called as such:
node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node.left = node2
node.right = node3

ser = Codec()
deser = Codec()
tree = ser.serialize(None)
print(tree)
ans = deser.deserialize(tree)
print(ans)
