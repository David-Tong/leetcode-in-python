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
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)
        else:
            return ""

        nodes = []
        while bfs:
            node = bfs.popleft()
            if node:
                nodes.append(node)
                bfs.append(node.left)
                bfs.append(node.right)
            else:
                nodes.append(None)

        idx = len(nodes) - 1
        while nodes[idx] is None:
            idx -= 1

        ans = ""
        for node in nodes[:idx+1]:
            if node is None:
                ans += "null,"
            else:
                ans += str(node.val) + ","
        return ans[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = []
        if data == "":
            return None
        data = data.split(",")
        for datum in data:
            if datum != "null":
                node = TreeNode(datum)
            else:
                node = None
            nodes.append(node)

        slow = 0
        fast = 1
        while fast < len(nodes):
            node = nodes[slow]
            if node:
                node.left = nodes[fast]
                if fast + 1 < len(nodes):
                    node.right = nodes[fast + 1]
                fast += 2
            slow += 1

        return nodes[0]

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
node4.left = node6
node4.right = node7

serializer = Codec()
deserializer = Codec()

data = serializer.serialize(node)
print(data)
node = deserializer.deserialize(data)

node