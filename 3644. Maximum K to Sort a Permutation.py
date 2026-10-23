class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, num in enumerate(nums):
            if num != i:
                if k == -1:
                    k = num
                else:
                    k &= num
        
        return 0 if k == -1 else k
