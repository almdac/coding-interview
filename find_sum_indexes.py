# Given an array arr of size n, and a number x, find 2 indexes i, j such that when i != j,
# arr[i] + arr[j] == x in O(n) time

class Solution:
    def find_sum_indexes(self, arr: list[int], x: int) -> tuple[int, int]:
        hash = {}
        for i, n in enumerate(arr):
            if n in hash:
                return (hash[n], i)
            else:
                hash[x-n] = i
        return None