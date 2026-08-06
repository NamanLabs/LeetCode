class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            digit_product = 1
            while temp > 0:
                digit_product *= temp % 10
                temp //= 10
            if digit_product % t == 0:
                return n    
            n += 1
