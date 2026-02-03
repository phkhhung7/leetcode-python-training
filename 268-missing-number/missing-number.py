# Problem: Missing Number
# Pattern: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Store numbers in a set and find the missing one

class Solution:
    def missingNumber(self, nums):
        s = set(nums)
        n = len(nums)

        for i in range(n + 1):
            if i not in s:
                return i
