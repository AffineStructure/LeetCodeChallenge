import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum, current_sum = -sys.maxsize - 1, 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum