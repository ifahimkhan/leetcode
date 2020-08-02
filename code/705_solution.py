class MyHashSet:
    def __init__(self, num_buckets=10000):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def _hash(self, val):
        return val % self.num_buckets

    def _find(self, val):
        key = self._hash(val)
        bucket = self.buckets[key]
        for i, v in enumerate(bucket):
            if v == val: return bucket, i
        return bucket, -1

    def add(self, val):
        bucket, idx = self._find(val)
        if idx == -1: bucket.append(val)

    def remove(self, val):
        bucket, idx = self._find(val)
        if idx != -1: bucket.pop(idx)

    def contains(self, val):
        return self._find(val)[1] != -1
