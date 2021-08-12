from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = max_global = nums[0]
        for n in nums[1:]:
            max_curr = max(n, max_curr+n)
            if max_curr > max_global:
                max_global = max_curr
        return max_global       