# https://leetcode.com/explore/item/1661

class Solution:
    memo = [0]*31
    
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if self.memo[n] == 0:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            return self.memo[n]
        else:
            return self.memo[n]