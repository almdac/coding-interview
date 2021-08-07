# https://leetcode.com/explore/item/3253

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left, right, head = m-1, n-1, m+n-1
        while right >= 0 and left >= 0:
            if nums2[right] > nums1[left]:
                nums1[head] = nums2[right]
                right -= 1
            else:
                nums1[head] = nums1[left]
                left -= 1
            head -= 1
        if right >= 0:
            nums1[:head+1] = nums2[:right+1]
        else:
            nums1[:head+1] = nums1[:left+1]