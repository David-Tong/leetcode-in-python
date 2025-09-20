class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        from collections import defaultdict
        self.children = defaultdict(list)
        self.locks = defaultdict(int)
        for idx, p in enumerate(parent):
            if p != -1:
                self.children[p].append(idx)
            self.locks[idx] = 0
        #print(self.children)
        #print(self.locks)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locks[num] == 0:
            self.locks[num] = user
            return True
        else:
            return False

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locks[num] == user:
            self.locks[num] = 0
            return True
        else:
            return False

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        # condition 1 : The node is unlocked
        if self.locks[num] == 0:
            # condition 2 : It has at least one locked descendant (by any user)
            descendant_locked = False
            to_unlock = list()
            from collections import deque
            bfs = deque()
            for node in self.children[num]:
                bfs.append(node)
            while bfs:
                curr = bfs.popleft()
                if self.locks[curr] != 0:
                    descendant_locked = True
                    to_unlock.append(curr)
                for node in self.children[curr]:
                    bfs.append(node)

            if descendant_locked:
                # condition 3 : It does not have any locked ancestors.
                parent_unlocked = True
                curr = self.parent[num]
                while curr != -1:
                    if self.locks[curr] != 0:
                        parent_unlocked = False
                        break
                    curr = self.parent[curr]
                if parent_unlocked:
                    # lock the node
                    self.locks[num] = user
                    # unlock all locked descendants
                    for node in to_unlock:
                        self.locks[node] = 0
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

"""
parent = [-1,0,0,1,1,2,2]
lt = LockingTree(parent)
print(lt.lock(2,2))
print(lt.unlock(2,3))
print(lt.unlock(2,2))
print(lt.lock(4,5))
print(lt.upgrade(0,1))
print(lt.lock(0,1))
"""

parent = [-1,0,3,4,7,4,3,0,1,8]
lt = LockingTree(parent)
print(lt.upgrade(7, 27))
print(lt.upgrade(8, 43))
print(lt.upgrade(1, 42))
print(lt.unlock(8, 43))
print(lt.upgrade(8, 8))
print(lt.unlock(2, 33))
print(lt.unlock(3, 14))
print(lt.upgrade(8, 5))
print(lt.upgrade(2, 30))
print(lt.upgrade(2, 1))
print(lt.unlock(8,21))
print(lt.upgrade(4,11))
print(lt.lock(8,25))
print(lt.upgrade(9,44))
print(lt.unlock(6,12))
print(lt.lock(8,4))
print(lt.lock(5,50))
print(lt.upgrade(1,15))
print(lt.lock(4,21))
print(lt.upgrade(9,32))