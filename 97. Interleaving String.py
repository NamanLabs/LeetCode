class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Length check
        if len(s1) + len(s2) != len(s3):
            return False

        # Ensure s2 is the shorter or targeted string for O(len(s2)) space
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m, n = len(s1), len(s2)
        
        # dp[j] will store whether s1[:i] and s2[:j] can form s3[:i+j]
        dp = [False] * (n + 1)
        dp[0] = True

        # Base case for matching s2 with s3 (when s1 is empty)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill DP array line by line
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[n]
