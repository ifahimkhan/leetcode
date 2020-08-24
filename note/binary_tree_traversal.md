---
title: Binary Tree Traversal
author: Ren Zhang
date: Aug-24-2020
---

# Binary Tree Traversal
![binary tree traversal](./assets/tree_traversals.png)

## DFS Traversals
1. Recurrsive implementation of the tree dfs traversals are pretty straightforwardly easy.
2. With a hashmap, the iterative implementation can be very easy, but it need extra O(n) space for the hash.
3. Otherwise, the iterative version of the three dfs traversals can be quite different.

```python
def inorder(node): 
    # inorder(left subtree) -> root -> inorder(right subtree)
    if node.left: inorder(node.left)
    print(node.val)
    if node.right: inorder(node.right)

def postorder(node):
    # postorder(left subtree) -> postorder(right subtree) -> root
    if node.left: postorder(node.left)
    if node.right: postorder(node.right)
    print(node.val)

def preorder(node):
    # root -> preorder(left subtree) -> preorder(right subtree)
    print(node.val)
    if node.left: preorder(node.left)
    if node.right: preorder(node.right)

def tree_dfs_iterative(root):
    stack = [root] if root else []
    visited = set()
    while stack:
        node = stack.pop()
        if not node: continue
        if node in visited:
            print(node.val)
        else:
            visited.add(node)
            # stack.extend([node.right, node, node.left])  # inorder
            # stack.extend([node, node.right, node.left])  # postorder
            stack.extend([node.right, node.left, node])  # preorder

def inorder_iterative(root):
    node, stack = root, []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right

def preorder_iterative(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node: continue
        print(node.val)
        stack.append(node.right)
        stack.append(node.left)

def postorder_iterative(root):
    # basically, we push two copies on to stack, first one for backtrack, second one for traversal
    stack = [root, root]
    while stack:
        node = stack.pop()
        if stack and stack[-1] is node:
            for child in [node.right, node.left]:
                if not child: continue
                stack.extend([child, child])
        else: print(node.val)
```

## BFS traversal
1. BFS traversal with queue is quite straightforward. 
2. Coding BFS recurssively is unneccessarily complicated, thus I am omitting it. 

```python
def tree_bfs_iterative(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node: continue
        print(node.val)
        queue.extend([node.left, node.right])
```
