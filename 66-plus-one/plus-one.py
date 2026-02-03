# Problem: Plus One
# Pattern: Array / Carry Simulation
# Time Complexity: O(n)
# Space Complexity: O(1) (in-place, except when adding new digit)
# Key Idea: Simulate addition from right to left

class Solution:
    def plusOne(self, digits):
        n = len(digits)

        # Start from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # If all digits were 9
        return [1] + digits
