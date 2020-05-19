---
title: Binary Search
author: Ren Zhang
date: May-18-2020
---

# Binary Search
## Remarks
+ The binary search algorithm solves the problem of finding a target within a sorted sequence.
+ The algorithm iteratively updating the lower and upper bound of the search space where the target is sure to reside. The update is done by checking the middle element of search space.
+ The algorithm runs in O(logN) time worst case.
+ We can apply binary search on the domain of a monotonic function. 
+ The given sequence as a whole may not be ordered, but if we know certain subsequence is ordered, we can apply binary search on the subsequence.


## Usage
1. To find a value in array: 
```python
def binary_search(arr, t):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (h + l) // 2  # use l + (h - l) // 2 for non python
        if arr[m] == t: return m
        elif arr[m] > t: h = m - 1
        else: l = m + 1
    return -1
```

In case the target value occurrs more than once, this binary search code will find one, but not guarantee to be either leftmost or rightmost. 

2. To find the left most occurrence of the value:
```python
def binary_search_left(arr, t):
    l, h = 0, len(arr) - 1
    while l < h:
        m = (h + l) // 2
        if arr[m] < t: l = m + 1
        else: h = m
    return l
```

In the case the target value does not exist in the array, the index returned by this code points to the first element that is larger than the target value. Thus it is the location where we can insert the target value while maintain the sorted order of the sequence. 

That is to say, if `binary_search_left(arr, t)` returns `i`, then `arr[:i] < t` and `arr[i:] >= t`. 

3. To find the right most occurrence of the value:
```python
def binary_search_right(arr, t):
    l, h = 0, len(arr) - 1
    while l < h:
        m = (h + l) // 2
        if arr[m] <= t: l = m + 1
        else: h = m
    return l - 1
```

In the case the target value does not exist in the array, the index returned by this code points to the last element that is smaller than the target value. Thus insert the target value at this location will violate the sorted order. 

That is to say, if `binary_search_right(arr, t)` returns `i`, then `arr[:i+1] <= t` and `arr[i+1:] > t`.