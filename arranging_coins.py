class Solution:
    def ap(self, n):
        return ((1+n)/2)*n
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, self.ap(n)
        while left <= right:
            mid = (left+right)//2
            if self.ap(mid) < n:
                left = mid+1
            else:
                right = mid-1
        if self.ap(left) > n:
            return int(left-1)
        else:
            return int(left)