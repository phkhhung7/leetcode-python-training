# Problem: Single Number
# Pattern: Bit Manipulation (XOR)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Key Idea: a ^ a = 0, a ^ 0 = a

class Solution:
    def singleNumber(self, nums):
        result = 0

        for n in nums:
            result ^= n

        return result
