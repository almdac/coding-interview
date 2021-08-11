# https://leetcode.com/problems/first-bad-version/ 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Find x such that not isBadVersion(x-1) and isBadVersion(x)
        left, right = 1, n
        while left <= right:
            mid = (left+right)//2
            audit = isBadVersion(mid)
            if mid == 1 and audit:
                return mid
            if not isBadVersion(mid-1) and audit:
                return mid
            if audit:
                right = mid-1
            else:
                left = mid+1