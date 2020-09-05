class Solution:
    def solution_two_pass(self, root1, root2):
        def inorder_traversal(node, order):
            if node:
                order = inorder_traversal(node.left, order)
                order.append(node.val)
                order = inorder_traversal(node.right, order)
            return order
        
        # inoder on both seperately
        order1 = inorder_traversal(root1, deque())
        order2 = inorder_traversal(root2, deque())
        order = []
        # merge two sorted list
        while order1 or order2:
            if not order1:  
                order.append(order2.popleft())
            elif not order2:  
                order.append(order1.popleft())
            else:
                order.append(order1.popleft() if order1[0] < order2[0] else order2.popleft())        
        return order

    def solution_one_pass(self, root1, root2):
        stack1, stack2, order = [], [], []
        
        def to_left_leaf(node, stack):
            while node:
                stack.append(node)
                node = node.left
            return node, stack
        
        def extact_next_inorder(stack):
            node = stack.pop()
            order.append(node.val)
            node = node.right
            return node, stack
            
        while any([root1, root2, stack1, stack2]):
            root1, stack1 = to_left_leaf(root1, stack1)
            root2, stack2 = to_left_leaf(root2, stack2)
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                root1, stack1 = extact_next_inorder(stack1)
            else:
                root2, stack2 = extact_next_inorder(stack2)
                    
        return order

    
    getAllElements = solution_one_pass
