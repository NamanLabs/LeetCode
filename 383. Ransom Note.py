from collections import Counter


class Solution:

  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Check if ransomNote requires more letters than magazine has
    return not (Counter(ransomNote) - Counter(magazine))
