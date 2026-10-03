class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with base index -1
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Stack is empty, store current index as new boundary
                    stack.append(i)
                else:
                    # Calculate current valid substring length
                    max_len = max(max_len, i - stack[-1])

        return max_len
