class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N = len(grid)

        def doConstruct(sx, sy, step):
            if step == 1:
                return Node(grid[sx][sy], 1, None, None, None, None)

            is_leaf = True
            for x in range(step):
                for y in range(step):
                    cx = sx + x
                    cy = sy + y
                    if grid[sx][sy] != grid[cx][cy]:
                        is_leaf = False
                        break
                if not is_leaf:
                    break

            if is_leaf:
                return Node(grid[sx][sy], 1, None, None, None, None)
            else:
                node = Node(0, 0, None, None, None, None)
                next_step = step // 2
                node.topLeft = doConstruct(sx, sy, next_step)
                node.topRight = doConstruct(sx, sy + next_step, next_step)
                node.bottomLeft = doConstruct(sx + next_step, sy, next_step)
                node.bottomRight = doConstruct(sx + next_step, sy + next_step, next_step)
                return node

        return doConstruct(0, 0, N)


grid = [[0,1],[1,0]]

solution = Solution()
print(solution.construct(grid))
