#         m = (l + r) // 2
#         root
#           V
# [-10, -3, 0, 5, 9]
#  |___ ___|  |_ _| 
#      V        V
# left subtree right subtree

# left = recurrsive(l, m - 1)
# node = construct(trav.val)
# trav = trav->next
# right = recurrsive(m + 1, r)

class Solution:
    def sortedListToBST(self, head):
        def count_nodes(node):
            n = 0
            while node:
                node = node.next
                n += 1
            return n
                
        n = count_nodes(head)
        self.trav = head
        
        def make_tree(l, r):
            if l > r: return None 
            m = (l + r) // 2
            left = make_tree(l, m - 1)
            node = TreeNode(self.trav.val)
            self.trav = self.trav.next
            node.left = left
            node.right = make_tree(m + 1, r)
            return node
            
        return make_tree(0, n - 1)
