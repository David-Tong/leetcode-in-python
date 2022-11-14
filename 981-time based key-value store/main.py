class TimeEntity(object):

    def __init__(self):
        from collections import defaultdict
        self.timestamps = list()
        self.values = defaultdict(str)

    def set(self, value, timestamp):
        self.timestamps.append(timestamp)
        self.values[timestamp] = value

    def get_largest_timestamp_prev(self, timestamp):
        from bisect import bisect_right
        idx = bisect_right(self.timestamps, timestamp)
        return self.values[self.timestamps[idx - 1]] if idx > 0 else ""


class TimeMap(object):

    def __init__(self):
        from collections import defaultdict
        self.entities = defaultdict(TimeEntity)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.entities[key].set(value, timestamp)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        return self.entities[key].get_largest_timestamp_prev(timestamp)


timemap = TimeMap()
print(timemap.get("foo", 1))
timemap.set("foo", "bar", 1)
print(timemap.get("foo", 1))
print(timemap.get("foo", 3))
timemap.set("foo", "bar2", 4)
print(timemap.get("foo", 4))
print(timemap.get("foo", 5))
