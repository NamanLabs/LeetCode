class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            # Extend the range while elements are consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            # Format based on whether the range contains one or multiple numbers
            if start == nums[i]:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i]}")

            i += 1

        return ranges
