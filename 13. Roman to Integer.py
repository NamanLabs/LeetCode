class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman symbol to its integer value
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the string in reverse order
        for char in reversed(s):
            current_value = roman_map[char]
            
            # If current value is less than the previous one, subtract it
            if current_value < prev_value:
                total -= current_value
            # Otherwise, add it
            else:
                total += current_value
                
            # Update prev_value for the next iteration
            prev_value = current_value
            
        return total
