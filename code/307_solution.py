class NumArray(SegmentTree):
    def __init__(self, nums: List[int]):
        super().__init__(nums)

    def update(self, index: int, val: int) -> None:
        super().update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return super().query(left, right)
      
# Segment Tree implemented with tree nodes 
class TreeNode:
    def __init__(self, val=None, parent=None, left=None, right=None, start=None, end=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.start = start
        self.end = end
    
    def __repr__(self):
        print('val {} start {} end {}'.format(self.val, self.start, self.end))
        
class SegmentTree:
    def __init__(self, values):
        self.build_tree(values)
    
    def build_tree(self, values):
        nodes = [TreeNode(val=val, start=i, end=i) for i, val in enumerate(values)]
        self.leaves = nodes
        while len(nodes) != 1:
            parents = []
            for l, r in zip_longest(nodes[::2], nodes[1::2], fillvalue=None):
                val = l.val if not r else l.val + r.val
                end = l.end if not r else r.end
                parent = TreeNode(val, left=l, right=r, start=l.start, end=end)
                l.parent = parent
                if r: r.parent = parent
                parents.append(parent)
            nodes = parents
        self.root = nodes[0]
        
    def update(self, index, val):
        leaf = self.leaves[index]
        diff = val - leaf.val
        node = leaf
        while node:
            node.val += diff
            node = node.parent              
            
    def query(self, left, right):
        l = self.leaves[left]
        r = self.leaves[right]
        if l == r: return l.val
        
        total = l.val + r.val
        while l.parent != r.parent:
            if l == l.parent.left:
                total += l.parent.right.val
            if r == r.parent.right:
                total += r.parent.left.val
            l = l.parent
            r = r.parent
        return total        

# Segment Tree implemented using array.
class SegmentTree:
    def __init__(self, values):
        self.n = n = len(values)
        self.tree = values + values
        for i in range(n-1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
            
    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 0:
            if index % 2:
                l, r = index-1, index  
            else: 
                l, r = index, index + 1
            self.tree[index >> 1] = self.tree[l] + self.tree[r]
            index >>= 1
        
    def query(self, l, r):
        l += self.n
        r += self.n
        total = 0
        while l <= r:
            if l % 2: 
                total += self.tree[l]
                l += 1
            if r % 2 == 0:
                total += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return total

