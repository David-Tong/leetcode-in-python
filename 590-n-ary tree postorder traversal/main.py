# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # shortcut
        if not root:
            return list()

        # pre-process
        stack = list()
        seenOnce = set()
        stack.append(root)

        # process
        ans = list()
        while stack:
            curr = stack[-1]
            if curr not in seenOnce:
                if curr.children:
                    for child in curr.children[::-1]:
                        stack.append(child)
                seenOnce.add(curr)
            else:
                node = stack.pop()
                ans.append(node.val)
        return ans


node = Node(1)
node2 = Node(3)
node3 = Node(2)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node.children = list()
node.children.append(node2)
node.children.append(node3)
node.children.append(node4)
node2.children = list()
node2.children.append(node5)
node2.children.append(node6)

solution = Solution()
print(solution.postorder(node))
