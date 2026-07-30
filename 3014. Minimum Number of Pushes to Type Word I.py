class Solution:
    def minimumPushes(self, word: str) -> int:
        # agar 8 word ka hai toh count 8 varna below 8 hai toh count of words is the return value 
        # else agar 8 sai bada hai toh 
        # baaki characters sabke 2 mai fill karne honge toh will click it 2 times 
        n = len(word)
        total_pushes = 0
        for i in range(n):
            pushes_needed = (i // 8) + 1
            total_pushes += pushes_needed
            
        return total_pushes
