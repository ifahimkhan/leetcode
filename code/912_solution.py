class Solution:
    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            s = i
            for j in range(i + 1, n):
                if nums[j] < nums[s]: 
                    s = j
            nums[i], nums[s] = nums[s], nums[i]
        return nums

    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            swapped = False
            for j in range(n - i):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    swapped = True
            if not swapped: break
        return nums

    def insertion_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    def merge_sort(self, nums):
        temp = nums.copy()

        def merge(low, mid, high):
            for i in range(low, high + 1):
                temp[i] = nums[i]

            i, j = low, mid + 1
            for k in range(low, high + 1):
                if i > mid:
                    nums[k] = temp[j]
                    j += 1
                elif j > high:
                    nums[k] = temp[i]
                    i += 1
                elif temp[j] < temp[i]:
                    nums[k] = temp[j]
                    j += 1
                else:
                    nums[k] = temp[i]
                    i += 1

        n = len(nums)
        step_size = 1
        while step_size < n:
            for low in range(0, n, 2 * step_size):
                mid = low + step_size - 1
                high = min(n - 1, low + 2 * step_size - 1)
                merge(low, mid, high)
            step_size *= 2    
        return nums
    
    
    def quick_sort(self, nums):
        import random

        def partition(l, h):
            if l >= h: return
            p = random.randint(l, h)
            nums[l], nums[p] = nums[p], nums[l]
            pivot = nums[l]
            i, j = l, h
            while i < j:
                while i < h and nums[i] <= pivot: i += 1
                while j > l and nums[j] >= pivot: j -= 1
                if j > i and nums[i] > nums[j]: nums[i], nums[j] = nums[j], nums[i]
            nums[j], nums[l] = nums[l], nums[j]
            return j

        def sort(l, h):
            if h > l:
                j = partition(l, h)
                sort(l, j - 1)
                sort(j + 1, h)

        sort(0, len(nums) - 1)
        return nums
    
    sortArray = merge_sort # quick_sort # bubble_sort # selection_sort
