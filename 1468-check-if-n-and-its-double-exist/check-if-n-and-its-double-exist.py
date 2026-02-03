# Problem: Check If N and Its Double Exist
# Pattern: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Key Idea: Check 2*x and x/2 while iterating

class Solution:
    def checkIfExist(self, arr):
        seen = set()

        for x in arr:
            # Check if double exists
            if 2 * x in seen:
                return True

            # Check if half exists (only if x is even)
            if x % 2 == 0 and x // 2 in seen:
                return True

            seen.add(x)

        return False
