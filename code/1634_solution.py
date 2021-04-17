class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        curr = sentinel = PolyNode()
        
        while poly1 and poly2:
            if poly1.power > poly2.power:
                curr.next = poly1
                curr = curr.next
                poly1 = poly1.next
            elif poly2.power > poly1.power:
                curr.next = poly2
                curr = curr.next
                poly2 = poly2.next
            else:
                coef = poly1.coefficient + poly2.coefficient
                if coef != 0:
                    curr.next = PolyNode(coef, poly1.power)
                    curr = curr.next
                poly1 = poly1.next
                poly2 = poly2.next       
        curr.next = None
        
        if poly1: curr.next = poly1
        if poly2: curr.next = poly2
        
        return sentinel.next
