# Problem: Move Zeroes
# Pattern: Two Pointers / In-place
# Time Complexity: O(n)
# Space Complexity: O(1)
# Key Idea: Compact non-zero elements to the front

class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill the rest with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
