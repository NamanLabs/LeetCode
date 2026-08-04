class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        operations = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                # We found a valid pair!
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                # Sum is too small, we need a larger number
                left += 1
            else:
                # Sum is too large, we need a smaller number
                right -= 1
                
        return operations
