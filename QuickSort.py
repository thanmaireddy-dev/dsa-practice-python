import random
def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
def quickSort(self, nums, start, end):
        if start >= end:
            return

        pivot_idx = random.randint(start, end)
        pivot = nums[pivot_idx]
        low = start
        mid = start
        high = end
        
        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == pivot:
                mid += 1
            else: # nums[mid] > pivot
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        self.quickSort(nums, start, low - 1)
        self.quickSort(nums, high + 1, end)

    