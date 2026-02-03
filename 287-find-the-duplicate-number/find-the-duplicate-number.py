# Problem: Find the Duplicate Number
# Pattern: Floyd's Cycle Detection (Tortoise and Hare)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Key Idea: Treat array as a linked list with a cycle

class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]   # move 2 steps
            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
