from collections import Counter, defaultdict
from typing import List


class Solution:

  def isPossible(self, nums: List[int]) -> bool:
    count = Counter(nums)
    end = defaultdict(int)  # tracks sequences ending at number x

    for x in nums:
      # If x has already been used in an earlier group, skip it
      if count[x] == 0:
        continue

      count[x] -= 1

      # 1. Best choice: attach x to a sequence ending at x - 1
      if end[x - 1] > 0:
        end[x - 1] -= 1
        end[x] += 1

      # 2. Second best choice: start a new valid triplet [x, x+1, x+2]
      elif count[x + 1] > 0 and count[x + 2] > 0:
        count[x + 1] -= 1
        count[x + 2] -= 1
        end[x + 2] += 1

      # 3. Cannot attach and cannot form a new triplet -> impossible
      else:
        return False

    return True
