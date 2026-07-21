class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #check agar count of 0 if  count of 0 is >= n than true else false but adjaceny wala dekhna hai 
        count = 1  
        total_safely_planted = 0
        for plot in flowerbed:
            if plot == 0:
                count += 1
            else:
                total_safely_planted += (count - 1) // 2
                count = 0
        count += 1
        total_safely_planted += (count - 1) // 2
        return total_safely_planted >= n
