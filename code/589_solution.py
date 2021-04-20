    def preorder(self, root: 'Node') -> List[int]:
        tree_values = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            tree_values.append(node.val)
            stack.extend(node.children[::-1])
        return tree_values
