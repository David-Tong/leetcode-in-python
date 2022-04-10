class MyHashMap(object):

    def __init__(self):
        self.dicts = [None] * (10 ** 6 + 1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.dicts[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.dicts[key]
        if value is not None:
            return value
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.dicts[key] = None


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 0)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
