---
title: Linked List
author: Ren Zhang
date: May-25-2020
---  

# Linked List  
![linked list image](./assets/LinkedList.png)
## Remarks  
+ Linked List is a sequence of node objects where each node store pointers to (1) some other node in the sequence, (2) the data this node is associated with. 
+ Linked List can be used as the underline data structure for many common abstract data types like lists, stacks, queues, etc. 

| operation        | time |
| ---------------- | ---: |
| push at front    | O(1) |
| pop at front     | O(1) |
| push at back     | O(1) |
| pop at back      | O(N) |
| access via index | O(N) |
| insert in middle | O(N) |
| delete in middle | O(N) |
| swap two nodes   | O(N) |

## Common operations on singly linked list.
1. Node class for singly linked list.
```python
class ListNode(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __repr__(self):
        return ' ' .join([super().__repr__()[:-1], 'of', str(self.item), ' >'])

nodes = list(map(ListNode, ['Head', 'Shoulders', 'Knees', 'Toes']))
for prev, next_ in zip(nodes, nodes[1:]):
    prev.next = next_

head = nodes[0]
tail = nodes[-1]
del nodes
```  

2. Traversal the linked list.
```python
def traversal(head, verbose=0):
    trav = head
    n = 0
    while trav:
        if verbose: print(trav.item)
        if not trav.next: tail = trav
        trav = trav.next
        n += 1
    return tail, n

# def traversal(head, k):
# def traversal(head, val):

assert traversal(head) == (tail, 4)
```   

3. Push and pop node at front.
```python
def push_front(head, node):
    node.next = head
    return node

def pop_front(head):
    return head.next

node = ListNode('Hat')
head = push_front(head, node)    
assert head == node and traversal(head)[1] == 5

head = pop_front(head)
assert head == node.next and traversal(head)[1] == 4
```

4. Push and pop node at back. 
```python
def push_back(tail, node):  
    tail.next = node
    return node

def pop_back(head, tail):  
    trav = head
    while trav.next is not tail: trav = trav.next
    trav.next = None
    tail = trav
    return tail

node = ListNode('Shoes')
tail = push_back(tail, node)
assert tail == node and traversal(head)[1] == 5

tail = pop_back(head, tail)
assert traversal(head)[1] == 4 and tail.next == None
```

5. Insert and delete nodes in the middle.
```python
def get(head, i):
    trav = head
    prev = None
    while trav and i:
        i -= 1
        prev = trav
        trav = trav.next
    return prev, trav

def insert(head, i, node):
    prev, next_ = get(head, i)
    prev.next = node
    node.next = next_

def erase(head, i):
    prev, curr = get(head, i)
    prev.next = curr.next    

node = ListNode('Belly Button')
insert(head, 2, node)
assert get(head, 2)[1] == node and traversal(head)[1] == 5

erase(head, 2)
assert get(head, 2)[1] == node.next and traversal(head)[1] == 4
```

6. Swap nodes
```python
def swap(head, i, j):
    i, j = sorted([i, j])
    prev_i, node_i = get(head, i)
    prev_j, node_j = get(node_i, j-i)
    if prev_i: prev_i.next = node_j
    prev_j.next = node_i
    temp = node_i.next
    node_i.next = node_j.next 
    node_j.next = temp
    return head if prev_i else node_j

old_head = head
head = swap(head, 1, 0)
head = swap(head, 2, 3)
head = swap(head, 3, 2)
head = swap(head, 0, 1)
assert head == old_head
```

7. Reverse Linked List
```python
def reverse(head):
    prev = None
    trav = head
    while trav:
        # trav.next, prev, trav = prev, trav, trav.next
        next_ = trav.next
        trav.next = prev
        prev = trav
        trav = next_
    return prev
```

## Common Problems
1. Two Pointers 
   1. left, right - Palindrome
   2. slow, fast - cycle, last k 
2. Multiple Lists
   1. Merge, Intersection
3. Search and Sorting
4. Implement Stack/Queue/Deque etc.
5. Doubly Linked List + Hash Table