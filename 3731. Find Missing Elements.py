class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = []
        for i in range(len(nums) - 1):
            current_num = nums[i]
            next_num = nums[i + 1]
            if next_num - current_num > 1:
                for missing in range(current_num + 1, next_num):
                    memo.append(missing)
        return memo
