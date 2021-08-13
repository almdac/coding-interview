# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        for i in range(1, len(nums)):
            subproblems = [lis[k] for k in range(i) if nums[k] < nums[i]]
            lis[i] = 1 + max(subproblems, default=0)
        return max(lis)
