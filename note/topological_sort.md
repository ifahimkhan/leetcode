---
title: Topological Sort  
author: Ren Zhang
date: July-5-2020
---  

# Topological Sort  
![topsort](./assets/topsort.png)

## Remarks  
+ Topological sort gives a topological order of the nodes in a [directed acyclic graph(DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph).
+ A topological ordering implies: for each directed edge `u -> v`, `u` must comes before `v` in the ordering.
+ It is a useful preprocessing on the graph, we can implement search for shortest/longest path easily based on this ordering. 
+ It also gives sort of a notion of levels/diameter of the connected components in the graph. 

## Implementation  

+ One implementation of topological sort is to do DFS and put the postorder on to an array.
+ The reverse of the postorder traversal is the topological order.
+ We can also incorporate cycle detection into the DFS topological sort implementation. We can stop early when we found a cycle.  

```python
def topsort(nodes, edges):
    n = len(nodes)
    visited = set()
    path = set() # for cycle detection
    top_order = deque([])

    def dfs(node):
        ''' Perform dfs traversal, Return True if cycle is found. '''
        if node in visited: return False
        if node in path: return True
        path.add(node)
        
        for neighbor in edges[node]:
            if dfs(neighbor): return True
        visited.add(node)
        path.discard(node)
        top_order.appendleft(node)  # put postorder on to array
        return False

    for node in nodes:
        if dfs(node): return []
        
    return top_order

nodes = set(range(7))
edges = {
    0: [2, 5, 1],
    1: [4, 6],
    2: [3],
    3: [4],
    4: [6],
    5: [2,3],
    6: []
}
print(topsort(nodes, edges))
```

+ Another implementation for topological sort is BFS based, aka the Khan's algorith.
+ The BFS topological sort would require more graph preprocessing, we will also need the in degrees(or in edges) for each node. 
+ We can still detect cycle with BFS topological sort. But only after the procedure is done. When there are cycles in the graph, the ordering will be incomplete. Because, the in_degrees for the nodes in the cycle won't be 0. 
+ With BFS topological sort, we can also test the uniqueness of the topological ordering. If the topological ordering is unique, the queue can only hold one node at any given time. 

```python
def topsort(queue, out_edges, in_degrees):
    ordering = []
    while queue:
        node = queue.popleft()
        ordering.append(node)
        for next_ in out_edges[node]:
            in_degrees[next_] -= 1
            if not in_degrees[next_]:
                queue.append(next_)

    return ordering

in_degrees = {0:0, 1:1, 2:2, 3:2, 4:2, 5:1, 6:2}
queue = deque([node for node in in_degrees if not in_degrees[node]])
print(topsort(queue, edges, in_degrees))
```