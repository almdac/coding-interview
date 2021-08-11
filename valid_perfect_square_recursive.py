class Solution:
    def __init__(self, target: int = None, func: callable = None) -> None:
        self._target = target
        self._func = func

    def _bynary_search_increasing(self, left, right):
        mid = (left+right)//2
        evaluation = self._func(mid)
        if left > right:
            return False
        if evaluation == self._target:
            return True
        elif evaluation < self._target:
            return self._bynary_search_increasing(mid+1, right)
        else:
            return self._bynary_search_increasing(left, mid-1)

    def isPerfectSquare(self, num: int) -> bool:
        self._target = num
        self._func = lambda x: x*x
        return self._bynary_search_increasing(0, num)