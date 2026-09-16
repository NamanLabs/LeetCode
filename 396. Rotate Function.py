class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # Calculate F(0)
        current_F = sum(i * val for i, val in enumerate(nums))
        max_F = current_F
        
        # Calculate F(k) iteratively using the state transition formula
        for k in range(1, n):
            current_F = current_F + total_sum - n * nums[n - k]
            if current_F > max_F:
                max_F = current_F
                
        return max_F
