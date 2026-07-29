class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_str = ""
        i = 0
        length = len(chars)
        while i < length:
            char = chars[i]
            count = 0
            while i < length and chars[i] == char:
                count += 1
                i += 1
            compressed_str += char
            if count > 1:
                compressed_str += str(count)
        for j in range(len(compressed_str)):
            chars[j] = compressed_str[j]
        return len(compressed_str)
