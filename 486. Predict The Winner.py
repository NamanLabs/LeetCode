class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        # i think we need to find possiblites for each player
        memo = {}
        
        def get_max_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            pick_left = nums[left] - get_max_diff(left + 1, right)
            pick_right = nums[right] - get_max_diff(left, right - 1)
            
            best_choice = max(pick_left, pick_right)
            memo[(left, right)] = best_choice
            
            return best_choice
            
        return get_max_diff(0, len(nums) - 1) >= 0
