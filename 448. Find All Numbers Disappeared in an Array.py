# we are creating set because set will not have duplicate values and we are creating set of range of 1 to n+1 because we want to find the missing numbers in the array and we are subtracting the set of nums from the set of range to get the missing numbers in the array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       return list(set(range(1, len(nums) + 1)) - set(nums))