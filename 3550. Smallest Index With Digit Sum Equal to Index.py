class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            s = 0
            while val > 0:
                s += val % 10
                val //= 10
            if s == i:
                return i
        return -1
