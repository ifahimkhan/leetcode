class MyHashMap:
    def __init__(self, num_buckets=10000):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def _hash(self, key):
        return key % self.num_buckets

    def _find(self, key):
        bucket = self.buckets[self._hash(key)]
        for idx, (k, v) in enumerate(bucket):
            if k == key: return bucket, idx, v
        return bucket, -1, None

    def put(self, key: int, value: int) -> None:
        bucket, idx, v = self._find(key)
        if idx == -1: bucket.append([key, value])
        else: bucket[idx][1] = value
        

    def get(self, key: int) -> int:
        bucket, idx, v = self._find(key)
        return v if idx != -1 else -1        

    def remove(self, key: int) -> None:
        bucket, idx, v = self._find(key)
        if idx != -1: 
            bucket[idx] = bucket[-1]
            bucket.pop()
 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
