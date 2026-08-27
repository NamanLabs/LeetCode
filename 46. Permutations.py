# SOLUTION 1 
from itertools import permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return [list(p) for p in permutations(nums)]

# SOLUTION 2 
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start: int):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                # Swap the current element with the element at index i
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse for the next index
                backtrack(start + 1)
                # Backtrack / restore the original state
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
