from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [i for i,j in Counter(nums).items() if j == 1][0]