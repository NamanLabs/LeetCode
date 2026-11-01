class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
            
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            # Expand for odd length palindromes (centered on a character)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    start = l
                    max_len = curr_len
                l -= 1
                r += 1
                
            # Expand for even length palindromes (centered between characters)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    start = l
                    max_len = curr_len
                l -= 1
                r += 1
                
        return s[start:start + max_len]
