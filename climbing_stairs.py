class Solution:
    memo = [0]*46

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0: return 1
        if self.memo[n] == 0: 
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]