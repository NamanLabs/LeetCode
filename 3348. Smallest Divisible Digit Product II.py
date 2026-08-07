class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Get prime factors of t
        def get_factors(n):
            cnt = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in cnt:
                while n % p == 0:
                    cnt[p] += 1
                    n //= p
            return cnt, n
            
        req, remainder = get_factors(t)
        
        # If t has prime factors other than 2, 3, 5, or 7, it's impossible
        if remainder > 1:
            return "-1"
            
        # Helper to pack required prime factors into minimum digits
        def get_min_digits(r2, r3, r5, r7):
            min_len = float('inf')
            best_digits = ""
            
            for c8 in range((r2 + 2) // 3 + 1):
                for c9 in range((r3 + 1) // 2 + 1):
                    rem2 = max(0, r2 - c8 * 3)
                    rem3 = max(0, r3 - c9 * 2)
                    
                    c6 = min(rem2, rem3)
                    rem2 -= c6
                    rem3 -= c6
                    
                    c4 = rem2 // 2
                    rem2 %= 2
                    
                    c2 = rem2
                    c3 = rem3
                    
                    cur_len = c8 + c9 + c6 + c4 + c2 + c3 + r5 + r7
                    
                    if cur_len <= min_len:
                        curr_digits = '8'*c8 + '9'*c9 + '6'*c6 + '4'*c4 + '3'*c3 + '2'*c2 + '5'*r5 + '7'*r7
                        sorted_curr = "".join(sorted(curr_digits))
                        
                        if cur_len < min_len:
                            min_len = cur_len
                            best_digits = sorted_curr
                        elif sorted_curr < best_digits:
                            best_digits = sorted_curr
                            
            return min_len, best_digits
        
        def get_digit_factors(d):
            factors = {2: 0, 3: 0, 5: 0, 7: 0}
            if d == 0: return factors
            for p in factors:
                temp = d
                while temp % p == 0:
                    factors[p] += 1
                    temp //= p
            return factors

        n = len(num)
        first_zero = num.find('0')
        max_valid_len = first_zero if first_zero != -1 else n
        
        # O(N) OPTIMIZATION: Precompute prefix factors
        prefix_factors = [{2: 0, 3: 0, 5: 0, 7: 0}]
        for i in range(max_valid_len):
            df = get_digit_factors(int(num[i]))
            prev = prefix_factors[-1]
            curr = {p: prev[p] + df[p] for p in prev}
            prefix_factors.append(curr)

        # Check if the original number is already fully valid
        if max_valid_len == n:
            curr = prefix_factors[n]
            if all(curr[p] >= req[p] for p in req):
                return num
                
        # Step 3: Traverse backwards to find the best place to increment
        # Start from max_valid_len, or n - 1 if there were no zeros
        start_i = min(n - 1, max_valid_len)
        
        for i in range(start_i, -1, -1):
            curr_factors = prefix_factors[i] # Instantly grab precomputed factors in O(1)
            
            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                df = get_digit_factors(d)
                needed = {p: max(0, req[p] - (curr_factors[p] + df[p])) for p in req}
                
                min_len, best_digits = get_min_digits(needed[2], needed[3], needed[5], needed[7])
                slots_left = n - 1 - i
                
                if min_len <= slots_left:
                    suffix = best_digits + '1' * (slots_left - min_len)
                    suffix = "".join(sorted(suffix))
                    return num[:i] + str(d) + suffix

        # Step 4: If we must increase the total length of the number
        min_len, best_digits = get_min_digits(req[2], req[3], req[5], req[7])
        suffix = best_digits + '1' * max(0, (n + 1) - min_len)
        return "".join(sorted(suffix))
