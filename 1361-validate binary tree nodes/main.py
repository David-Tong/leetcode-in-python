class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        # check ingrees
        ingrees = [0] * n
        for child in leftChild:
            if child >= 0:
                ingrees[child] += 1
        for child in rightChild:
            if child >= 0:
                ingrees[child] += 1

        zeros = 0
        zero = -1
        for idx, ingree in enumerate(ingrees):
            if ingree > 1:
                return False
            elif ingree == 0:
                zeros += 1
                zero = idx

        if zeros > 1:
            return False

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(zero)

        visited = [False] * n
        visited[zero] = True

        count = 0
        while bfs:
            node = bfs.popleft()
            count += 1
            if leftChild[node] != -1:
                if not visited[leftChild[node]]:
                    visited[leftChild[node]] = True
                    bfs.append(leftChild[node])
                else:
                    return False
            if rightChild[node] != -1:
                if not visited[rightChild[node]]:
                    visited[rightChild[node]] = True
                    bfs.append(rightChild[node])
                else:
                    return False

        return True if count == n else False


n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,3,-1,-1]

n = 2
leftChild = [1,0]
rightChild = [-1,-1]

n = 2
leftChild = [-1, -1]
rightChild = [-1, -1]

n = 5
leftChild = [2,2,-1,1,3]
rightChild = [2,2,1,2,1]

n = 4
leftChild = [3,-1,1,-1]
rightChild = [-1,-1,0,-1]

n = 4
leftChild = [1,0,3,-1]
rightChild = [-1,-1,-1,-1]

solution = Solution()
print(solution.validateBinaryTreeNodes(n, leftChild, rightChild))
