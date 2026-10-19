class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        a = sorted(nums)
        arr = []
        for i in range(len(a)):
            if a[i] == target:
                arr.append(i)
        return arr
