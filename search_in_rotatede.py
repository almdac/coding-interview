# Cracking The Coding Interview (10.3)

import math

class Solution:
    def _find_pivot(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] > nums[(mid+1)%n]:
                return (mid+1)%n
            if nums[mid] < nums[(mid-1)%n]:
                return mid
            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return 0

    def search_in_rotated(self, target: int, nums: list[int]) -> int:
        pivot, n = self._find_pivot(nums), len(nums)
        left= pivot
        right = (left-1)%n
        i = 1
        while left != right:
            fraction = math.ceil(n/(2**i))
            mid = (left+fraction)%n
            if nums[mid] < target:
                left = (mid+1)%n
            elif nums[mid] > target:
                right = mid
            else:
                return mid
            i += 1
        if nums[left] == target:
            return left
        return -1