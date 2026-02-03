# Problem: Contains Duplicate
# Pattern: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Use a set to track visited elements

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
