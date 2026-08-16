class Solution:
    def isPalindrome(self, x: int) -> bool:
        right = len(str(x))-1 
        left = 0
        s = str(x)
        while left <= right :
            if s[left] == s[right]:
                left += 1 
                right -= 1
            else :
                return False
        return True
