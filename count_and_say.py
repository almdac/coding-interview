# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        digits = [d for d in self.countAndSay(n-1)]
        i = amount = 1
        speach = ''
        while i < len(digits):
            current, previous = digits[i], digits[i-1]
            if previous == current:
                amount += 1
            else:
                speach.join(f'{amount}{previous}')
                amount = 0
            i += 1
        
        if len(digits) == 1:
            return f'1{digits[0]}'
        else:
            return speach