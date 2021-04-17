class DDL:
    def __init__(self, val, /, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt

class FrontMiddleBackQueue:
    def __init__(self):
        self._init()
        self.n = 0
        
    def _init(self, val=None):
        node_or_val = None if val is None else DDL(val)
        self.front = node_or_val
        self.back = node_or_val
        self.middle = node_or_val

    def debug_print(self):
        print('front', self.front.val, 'middle', self.middle.val, 'back', self.back.val)
        if self.front:
            node = self.front
            while node:
                print(node.val, end = ' ')
                node = node.nxt
        print('')
        
    def pushFront(self, val: int) -> None:
        self.n += 1
        if not self.front: 
            self._init(val)
        else:
            old_front = self.front
            new_front = DDL(val, nxt=old_front)
            old_front.pre = new_front
            if self.n % 2 == 0: 
                self.middle = self.middle.pre
        self.debug_print()

    def popFront(self) -> int:
        if self.front is None: return -1
        self.n -= 1
        val = self.front.val
        if self.n:
            self.front = self.front.nxt
            self.front.pre = None
            if self.n % 2 == 1: self.middle = self.middle.nxt
        else:
            self._clear()
        # self.debug_print()
        return val
        
                
    def pushMiddle(self, val: int) -> None:        
        self.n += 1
        if not self.middle:
            self.front = self.middle = self.back = DDL(val)
        else:
            new_middle = DDL(val)
            old_middle = self.middle
            if self.n % 2 == 1:
                new_middle.nxt = old_middle.nxt
                new_middle.pre = old_middle
                old_middle.nxt = new_middle
            else:
                new_middle.pre = old_middle.pre
                old_middle.pre.nxt = new_middle
                new_middle.nxt = old_middle
                old_middle.pre = new_middle
            self.middle = new_middle
        # self.debug_print()

    def popMiddle(self) -> int:
        if not self.middle: return -1
        self.n -= 1
        val = self.middle.val
        # print('val', val)
        if self.n == 0:
            self.front = self.middle = self.back = DDL(val)
        elif self.n == 1:
            # print(self.back.val)
            self.front = self.middle = self.back
            self.back.pre = None
        else:
            self.middle.pre.nxt = self.middle.nxt
            if self.n % 2 == 0:
                self.middle = self.middle.pre
            else:
                self.middle = self.middle.nxt            
        # print(self.middle.val)
        # self.debug_print()
        return val    
    
        
    def pushBack(self, val: int) -> None:
        self.n += 1
        if not self.back:
            self.front = self.middle = self.back = DDL(val)
        else:
            old_back = self.back
            new_back = DDL(val, pre=old_back)
            old_back.nxt = new_back
            if self.n % 2 == 1: self.middle = self.middle.nxt
        self.back = new_back
        # self.debug_print()

    def popBack(self) -> int:
        if self.back is None: return -1
        self.n -= 1
        val = self.back.val
        self.back = self.back.pre
        if self.back:
            self.back.nxt = None
            if self.n % 2 == 0: self.middle = self.middle.pre
        else:
            self.front = self.back = self.middle = None
        # self.debug_print()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
