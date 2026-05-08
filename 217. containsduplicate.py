# we will make an if loop pass and check whether it is present or not if present we will update check count +1 and if not present it will remain 0 and go through whole array
#we did by using set and comparing the length of set and list if they are equal then there is no duplicate and if they are not equal then there is duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True