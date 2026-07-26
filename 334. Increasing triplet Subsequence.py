class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('INF')
        second = float('INF')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n 
            else:
                return True
        return False
