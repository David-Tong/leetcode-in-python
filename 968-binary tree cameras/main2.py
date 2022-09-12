class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def placeCamera(node):
            if node is None:
                status = dict()
                status["withCamera"] = 1000
                status["noCameraWatchByParent"] = 0
                status["noCameraWatchByChildren"] = 0
                return status

            left = placeCamera(node.left)
            right = placeCamera(node.right)

            # withCamera
            withCamera = min(
                left["noCameraWatchByParent"] + right["noCameraWatchByParent"],
                left["withCamera"] + right["noCameraWatchByParent"],
                left["noCameraWatchByParent"] + right["withCamera"]
            ) + 1

            # noCameraWatchByParent
            noCameraWatchByParent = min(
                left["withCamera"] + right["withCamera"],
                left["withCamera"] + right["noCameraWatchByChildren"],
                left["noCameraWatchByChildren"] + right["withCamera"],
                left["noCameraWatchByChildren"] + right["noCameraWatchByChildren"]
            )

            # noCameraWatchByChildren
            noCameraWatchByChildren = min(
                left["withCamera"] + right["withCamera"],
                left["withCamera"] + right["noCameraWatchByChildren"],
                left["noCameraWatchByChildren"] + right["withCamera"]
            )

            status = dict()
            status["withCamera"] = withCamera
            status["noCameraWatchByParent"] = noCameraWatchByParent
            status["noCameraWatchByChildren"] = noCameraWatchByChildren
            return status

        status = placeCamera(root)
        return min(status["withCamera"], status["noCameraWatchByChildren"])


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.right = node2
node2.right = node3
node3.right = node4


solution = Solution()
print(solution.minCameraCover(node))
