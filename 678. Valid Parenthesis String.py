class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Minimum possible open brackets '('
        high = 0  # Maximum possible open brackets '('
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
            
            # Agar high < 0 ho gaya, matlab ')' zyada ho gaye jinhe match nahi kiya ja sakta
            if high < 0:
                return False
            
            # low 0 se kam nahi ho sakta (open brackets negative nahi ho sakte)
            if low < 0:
                low = 0
                
        # String valid hai agar minimum open brackets balance 0 ho sake
        return low == 0
