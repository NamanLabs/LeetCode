from collections import deque
from typing import List


class Solution:

  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    dq = deque()  # stores indices of elements in decreasing order of value
    res = []

    for i, num in enumerate(nums):
      # 1. Remove indices that are out of the current window bound
      if dq and dq[0] < i - k + 1:
        dq.popleft()

      # 2. Maintain monotonic decreasing order:
      # Remove smaller elements from the back as they are useless
      while dq and nums[dq[-1]] < num:
        dq.pop()

      dq.append(i)

      # 3. Add the maximum for the current window (at the front of the deque)
      if i >= k - 1:
        res.append(nums[dq[0]])

    return res
