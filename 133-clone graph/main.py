class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        from collections import deque
        bfs = deque()
        visited = {}
        bfs.append(node)
        dup_node = Node(node.val)
        visited[node] = dup_node
        while bfs:
            curr = bfs.popleft()
            dup_curr = visited[curr]
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    dup_neighbor = Node(neighbor.val)
                    dup_curr.neighbors.append(dup_neighbor)
                    bfs.append(neighbor)
                    visited[neighbor] = dup_neighbor
                else:
                    dup_neighbor = visited[neighbor]
                    dup_curr.neighbors.append(dup_neighbor)
        return dup_node


node = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

#node.neighbors = [node2, node4]
node2.neighbors = [node, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node, node3]

solution = Solution()
dup_node = solution.cloneGraph(None)

print(dup_node)