class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            mod_val = word_weight % 26
            mapped_char = chr(ord('z') - mod_val)
            
            result.append(mapped_char)
            
        return "".join(result)
