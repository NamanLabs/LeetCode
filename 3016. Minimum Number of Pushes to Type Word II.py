class Solution:
    def minimumPushes(self, word: str) -> int:
        # I THINK ISME LETTER KI FREQUENCY COUNT KARKE PHIR ALLOT KARNA CHAHIYE FIRST 8 MOST FREQUENT KO PHELI POSITION THEN THE 9 TH LEAST ON 2ND POSITION AND SO ON AND 
        counts = Counter(word)
        freqs = sorted(counts.values(), reverse=True)
        total_pushes = 0
        
        for i, freq in enumerate(freqs):
            pushes_needed = (i // 8) + 1
            total_pushes += freq * pushes_needed
            
        return total_pushes
