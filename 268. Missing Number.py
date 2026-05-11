# in this we subtract sum of all numbers from sum of all n+1 numbers to get the missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)