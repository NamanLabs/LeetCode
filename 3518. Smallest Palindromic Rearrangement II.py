class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
import math
class Solution:
    def smallestPalindrome(self,s:str,k:int)->str:
        counts=Counter(s)
        left_counts={}
        mid_char=""
        for char,count in counts.items():
            if count%2!=0:
                mid_char=char
            if count//2>0:
                left_counts[char]=count//2
        L=sum(left_counts.values())
        total_perms=math.factorial(L)
        for count in left_counts.values():
            total_perms//=math.factorial(count)
        if k>total_perms:
            return ""
        left_half=[]
        available_chars=sorted(left_counts.keys())
        for i in range(L):
            for char in available_chars:
                if left_counts[char]>0:
                    perms_with_char=total_perms*left_counts[char]//(L-i)
                    if k<=perms_with_char:
                        left_half.append(char)
                        left_counts[char]-=1
                        total_perms=perms_with_char
                        break
                    else:
                        k-=perms_with_char
        left_str="".join(left_half)
        return left_str+mid_char+left_str[::-1]
